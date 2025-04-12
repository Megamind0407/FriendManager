#!/usr/bin/env bash

# Navigate to frontend and build it
cd ../frontend
npm install
npm run build

# Go to backend and install Python dependencies
cd ../backend
pip install -r requirements.txt
