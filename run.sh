#!/bin/bash
# Startup script for Flask Superheroes API

echo "Starting Flask Superheroes API..."
echo "================================="
echo

# Activate virtual environment and run the app
source .venv/bin/activate
python app.py
