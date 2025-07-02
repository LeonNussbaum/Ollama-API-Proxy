#!bash/sh
source ollama-proxy/bin/activate
uvicorn proxy:app --host 0.0.0.0 --port 11435
