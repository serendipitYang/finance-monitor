#!/bin/bash
# Prevent Mac from sleeping when on AC power
# Run with: sudo pmset -c sleep 0

# Check current power settings
echo "Current power settings:"
pmset -g | grep -E "(sleep|displaysleep|hibernatemode)"

# Recommended settings for headless server:
# sudo pmset -c sleep 0        # Never sleep when plugged in
# sudo pmset -c displaysleep 5  # Display sleeps after 5 min (saves energy)
# sudo pmset -c hibernatemode 0 # Disable hibernation for faster wake
