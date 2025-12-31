# ISS Crew LED Monitor

A simple Raspberry Pi project that shows how many people are currently on the International Space Station using an LED bar graph.

## What It Does
- Pulls live data from a public ISS API
- Reads the current number of astronauts in space
- Lights up LEDs to represent that number
- Updates once per minute

## Hardware Required
- Raspberry Pi
- LED Bar Graph (or individual LEDs)
- Resistors
- Jumper wires

## Software Required
- Python 3
- gpiozero
- requests

### Install dependencies:
bash
pip install gpiozero requests

### Run script
python iss_led_monitor.py

