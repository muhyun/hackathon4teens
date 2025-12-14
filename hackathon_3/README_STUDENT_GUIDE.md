
# 🧪 Middle School Student Guide
## Real-Time Lab Monitoring with micro:bit

### Goal
Build a system that measures lab conditions (temperature, air quality) using sensors,
sends data with micro:bit, and displays it live on a web dashboard.

### Learning Goals
- Understand sensors and data
- Learn basic Python and micro:bit programming
- Read and explain graphs
- Work like scientists and engineers

---
## Project Flow
Sensor → micro:bit → Raspberry Pi → Web Dashboard

- Sensor: Converting environment into numbers
- micro:bit: Sending numbers to Raspberry Pi
- Raspberry Pi: Collecting numbers and displaying them

#### Example Sensor Data

- Temperature (°C) / Humidity (%)
- Gas concentration (0–1023)
- Light intensity
- Sound level
- Motion/PIR detection

#### Role of Raspberry Pi

- Receive sensor data
- [optional] Store data (JSON/CSV)
- Run a real-time Flask web server
- Serve dashboard UI
- Implement alert logic when thresholds are exceeded

---
## Steps
1. Connect sensors to micro:bit (VCC, GND, Signal)
    - VCC: Voltage/Power pin. Often labeled as 3V or 3V3
    - GND: Ground pin
    - SIG: the sensor's data/signal pins. P0 or P1
2. Upload MicroPython code to micro:bit
    - Check if the sensor data is printed out in Terminal
3. Run Flask server on Raspberry Pi
4. View real-time dashboard in browser
    - Lastest time
    - Lastest sensing data
    - Sensing plot
5. Perform experiments and analyze graphs

---
## Safety Rules
- No water near electronics
- Do not inhale gas sensors
- Ask teacher before experiments

---
## Experiment examples
- Temperature vs number of people
- Ventilation before/after opening windows
- Air changes using alcohol spray (teacher supervised)

---
You are now a young researcher 🚀

## Project tips

### how to install required python packages

```bash
pip install flask pyserial
```

### how to run Flask app

```bash
python app.py
```