#!/bin/bash
echo "========================================================"
echo "⚡ STARTING REBEL AI AUTONOMOUS HIGH-TURNOVER DAEMON"
echo "========================================================"

while true; do
    TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
    echo "[$TIMESTAMP] [INFO] Starting automated sync cycle..." | tee -a daemon_execution.log
    
    bash sync_and_deploy.sh 2>&1 | tee -a daemon_execution.log
    
    echo "[$TIMESTAMP] [INFO] Sync cycle complete. Sleeping for 1 hour..." | tee -a daemon_execution.log
    echo "--------------------------------------------------------"
    sleep 3600
done
