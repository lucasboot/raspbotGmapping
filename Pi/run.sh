#!/bin/bash 

python LaserScan.py &
python velocities &
python obstavoid.py
