#!/bin/zsh
# Script to activate Python virtual environment and start a shell

# Set error handling
set -e

SCRIPT_DIR="${0:A:h}"
REPO_DIR="$(cd "$SCRIPT_DIR/../../../.." && pwd -P)"
TARGET_DIR="${AUTOMATIZACIONES_DIR:-$REPO_DIR}"
VENV_PATH="${PYTHON_VIRTUAL_ENV:-${VIRTUAL_ENV:-$TARGET_DIR/venv_arm64}}"

# Change to the automation directory
echo "Changing to automation directory..."
cd "$TARGET_DIR" || {
    echo "Error: Failed to change directory"
    exit 1
}

# Check if virtual environment exists
if [[ ! -d "$VENV_PATH" ]]; then
    echo "Error: Virtual environment directory not found: $VENV_PATH"
    echo "Please create the virtual environment first."
    exit 1
fi

if [[ ! -f "$VENV_PATH/bin/activate" ]]; then
    echo "Error: Activation script not found in $VENV_PATH/bin/activate"
    echo "The virtual environment may be corrupted."
    exit 1
fi

# Activate virtual environment
echo "Activating virtual environment..."
source "$VENV_PATH/bin/activate" || {
    echo "Error: Failed to activate virtual environment"
    exit 1
}

echo "Virtual environment activated successfully!"
echo "Starting new shell session..."

# Start a new shell session with the activated environment
exec zsh
