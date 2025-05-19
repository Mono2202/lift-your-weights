#!/bin/bash

pkill -f "python main.py lift-your-weights"
nohup python main.py lift-your-weights > output.log 2>&1 &

