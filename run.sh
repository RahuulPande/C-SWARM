#!/bin/bash

# Cognizant Talent Edge CRM Toolkit Launcher
echo "🚀 Starting Cognizant Talent Edge CRM Toolkit..."

# Add local bin to PATH
export PATH="$HOME/.local/bin:$PATH"

# Check if streamlit is available
if ! command -v streamlit &> /dev/null; then
    echo "❌ Streamlit not found. Installing dependencies..."
    pip install --break-system-packages -r requirements.txt
fi

# Start the Streamlit application
echo "🌟 Launching application on http://localhost:8501"
streamlit run app.py --server.address=0.0.0.0 --server.port=8501