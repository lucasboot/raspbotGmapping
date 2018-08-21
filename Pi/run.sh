#!/bin/bash 
python LaserScan.py &
python encoderdireito.py &
python encoderesquerdo.py &
python obstavoid.py &
python velocities.py
