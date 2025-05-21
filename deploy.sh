#!/bin/bash

SESSION="lift-your-weights"

# Kill any existing session with the same name
tmux has-session -t $SESSION 2>/dev/null
if [ $? -eq 0 ]; then
    echo "Killing existing tmux session: $SESSION"
    tmux kill-session -t $SESSION
fi

# Start new detached session
echo "Starting new tmux session: $SESSION"
tmux new-session -d -s $SESSION

# Start frontend in another window
tmux new-window -t $SESSION -n 'telegram'
tmux send-keys -t $SESSION:2 'python main.py' C-m

echo "Deployment started in tmux session: $SESSION"

