#!/bin/bash

echo "🌐 Initializing Persistent HTTPS Tunnel..."
pkg install openssh -y > /dev/null 2>&1

while true; do
    echo ""
    echo "🚀 Launching Native HTTPS Tunnel..."
    echo "--------------------------------------------------------"
    echo "Copy your live HTTPS link (.lhr.life) below:"
    echo "--------------------------------------------------------"
    
    # SSH with KeepAlive to prevent idle timeouts
    ssh -o ServerAliveInterval=15 \
        -o ServerAliveCountMax=3 \
        -o StrictHostKeyChecking=no \
        -R 80:localhost:8080 nokey@localhost.run

    echo ""
    echo "⚠️ Connection dropped. Reconnecting in 3 seconds..."
    sleep 3
done
