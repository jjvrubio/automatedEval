#!/bin/zsh
# Script to activate Python virtual environment and start a shell

# Set error handling
set -e

# Change to the automation directory
echo "Changing to automation directory..."
cd /Users/juanjo/Documents/Personal/JJVR/automatizaciones || {
    echo "Error: Failed to change directory"
    exit 1
}

# Check if virtual environment exists
if [[ ! -d "venv_arm64" ]]; then
    echo "Error: Virtual environment directory 'venv_arm64' not found!"
    echo "Please create the virtual environment first."
    exit 1
fi

if [[ ! -f "venv_arm64/bin/activate" ]]; then
    echo "Error: Activation script not found in venv_arm64/bin/activate"
    echo "The virtual environment may be corrupted."
    exit 1
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv_arm64/bin/activate || {
    echo "Error: Failed to activate virtual environment"
    exit 1
}

echo "Virtual environment activated successfully!"
echo "Starting new shell session..."

# Start a new shell session with the activated environment
exec zsh
