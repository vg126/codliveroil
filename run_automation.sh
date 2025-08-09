#!/bin/bash
# Quick launcher script for the automated face refinement system

echo "🚀 Launching Automated Face Refinement System..."
echo "📁 Working directory: $(pwd)"
echo "🕐 Start time: $(date)"
echo ""

# Ensure data directory exists
mkdir -p data

# Run the automated system
python3 automated_face_refinement.py

echo ""
echo "🏁 System execution complete at: $(date)"
echo "📊 Check the data/ folder for CSV results"
echo "🖼️ Check the terminal output for image URLs"