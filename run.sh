#!/bin/bash

# Load Environment Keys
if [ -f "config.env" ]; then
    source config.env
fi

# Execute Pipeline Options
if [ "$1" == "--daemon" ]; then
    echo "Starting Rebel AI Master Suite in continuous background loop..."
    nohup bash -c 'while true; do python main.py; python build_store.py; python broadcast.py; sleep 3600; done' > daemon_execution.log 2>&1 &
    echo "Daemon active! Monitor logs with: tail -f daemon_execution.log"
else
    python main.py
    python build_store.py
    python broadcast.py
fi
