#!/bin/bash
# Simple script to start the local server

# Check if Python 3 is available
if command -v python3 &> /dev/null; then
    python3 server.py
elif command -v python &> /dev/null; then
    python server.py
else
    echo "❌ Python is not installed. Please install Python 3 to run the server."
    exit 1
fi

