from fastapi import FastAPI, Query
from fastapi.responses import HTMLResponse
from dotenv import load_dotenv
from upsonic import Agent, Task, ObjectResponse
from upsonic.client.tools import BrowserUse

# Load environment variables
load_dotenv()

app = FastAPI(title="Investing.com Hourly Technical Analysis Agent")

# Initialize the AI agent
investing_agent = Agent("Investing Analysis Agent - Hourly", model="azure/gpt-4o", reflection=True)

# Define response format for stock analysis
class StockSignal(ObjectResponse):
    stock: str
    buy: int
    sell: int

class StockSignalList(ObjectResponse):
    stocks: list[StockSignal]

@app.get("/", response_class=HTMLResponse)
async def root():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Investing.com Hourly Analysis</title>
        <script src="https://cdn.tailwindcss.com"></script>
    </head>
    <body class="bg-gray-100 flex justify-center items-center h-screen">
        <div class="bg-white p-8 rounded-lg shadow-lg w-[40rem]">
            <h1 class="text-2xl font-bold text-center mb-4">📊 Investing.com Hourly Technical Analysis</h1>
            <input id="stocks" type="text" placeholder="Enter stock symbols (comma-separated)" class="w-full p-2 border rounded mb-4">
            <button onclick="trackStocks()" class="bg-blue-500 text-white px-4 py-2 rounded w-full">Analyze Stocks</button>
            <div id="result" class="mt-4 text-sm text-gray-800 bg-gray-50 p-4 rounded overflow-y-auto h-64"></div>
        </div>
        <script>
            async function trackStocks() {
                const stocks = document.getElementById("stocks").value;
                if (!stocks) {
                    alert("Please enter at least one stock symbol.");
                    return;
                }
                const response = await fetch(`http://127.0.0.1:8000/track_stocks?stocks=${encodeURIComponent(stocks)}`);
                const data = await response.json();
                
                document.getElementById("result").innerText = JSON.stringify(data, null, 2);
            }
        </script>
    </body>
    </html>
    """

@app.get("/track_stocks")
async def track_stocks(stocks: str = Query(..., title="Stock symbols (comma-separated)")):
    """Tracks stock analysis from Investing.com."""
    try:
        stock_symbols = [s.strip().upper() for s in stocks.split(",")]
        results = []
        
        for stock in stock_symbols:
            investing_task = Task(
                f"Search 'Investing.com {stock} technical analysis' on Google, open the first link, and extract Buy/Sell counts.",
                tools=[BrowserUse],
                response_format=StockSignal
            )
            
            investing_agent.do(investing_task)
            
            if investing_task.response:
                results.append(investing_task.response)
        
        return {"stocks": results}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
