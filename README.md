# Ollama-API-Proxy
A proxy for Ollama to easily disable thinking output for Home Assistant integrations.

## Features

- Proxies `/api/chat` requests to Ollama AI server, automatically setting `think=false` to disable thinking output.
- Streams responses back to the client.
- Supports fetching tags via `/api/tags`.
- Simple health check endpoint `/`.

## Requirements

- Python 3.9+
- FastAPI, httpx, uvicorn

## Setup

1. Install dependencies:

   ```bash
   pip install fastapi httpx uvicorn 


2. Configure the Ollama host URL in your code (`OLLAMA_HOST`).

3. Run the proxy server:

   ```bash
   uvicorn proxy:app --host 0.0.0.0 --port 11435


## Usage

* `POST /api/chat`: Forward chat requests to Ollama with thinking output disabled.
* `GET /api/tags`: Retrieve available tags.
* `GET /`: Health check.
