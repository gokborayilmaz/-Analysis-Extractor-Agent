# 21-Day Agent Series: Day 1 AGENT : release_announcement_writer_agent

Welcome to the **21-Day Agent Series**, where each day brings a new, cutting-edge agent!  
Today marks **Day 1**, featuring the `release_announcement_writer_agent`. This agent specializes in generating polished, platform-specific release announcements tailored for LinkedIn, Reddit, Discord, and Twitter.

---

## Overview

The `release_announcement_writer_agent` is a FastAPI-powered application that analyzes GitHub release pages and generates announcements in Markdown format for multiple platforms. This agent focuses on:

- **LinkedIn**: Corporate-style posts
- **Reddit**: Technical content
- **Discord**: Community-friendly messages
- **Twitter**: Fun, emoji-rich updates

With a built-in web-based UI, this agent simplifies the process of crafting professional and engaging announcements.

---

## Features

- **GitHub Release Analysis**: Fetches and processes data from GitHub release pages.
- **Platform-Specific Announcements**: Creates tailored content for various platforms.
- **Markdown Rendering**: Renders announcements in a readable HTML format.
- **Copy Feature**: Each platform's announcement can be copied to the clipboard with a single click.

---

## Installation

### Prerequisites
- Python 3.9 or higher
- Git
- Virtual environment (recommended)

### Steps
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the root directory and configure it as follows:
   ```env
   AZURE_OPENAI_ENDPOINT=<your_azure_openai_endpoint>
   AZURE_OPENAI_API_VERSION=<your_azure_openai_api_version>
   AZURE_OPENAI_API_KEY=<your_azure_openai_api_key>
   ```

---

## Running the Application

1. Start the FastAPI server:
   ```bash
   uvicorn upsonicai:app --reload
   ```

2. Open the UI in your browser:
   ```
   http://127.0.0.1:8000/
   ```

3. Use the form to input:
   - **GitHub Release URL**
   - **Company URL**
   - **Product Aim**

4. Click "Generate" to see platform-specific announcements rendered in the UI. Each platform's content will be displayed in separate boxes with a "Copy" button for easy sharing.

---

## API Documentation

Interactive API docs are available at:
- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---



---

## Acknowledgments

Special thanks to the Upsonic framework for making agent management seamless.
