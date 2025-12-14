
from flask import Flask, render_template, jsonify
import serial, threading

SERIAL_PORT = "/dev/tty.usbmodem"  # Change for Windows (COM3)
BAUDRATE = 115200

latest = {"time": "-", "value": 0}

app = Flask(__name__)

def serial_reader():
    global latest
    ser = serial.Serial(SERIAL_PORT, BAUDRATE, timeout=1)
    while True:
        line = ser.readline().decode().strip()
        if "," in line:
            t, v = line.split(",")
            latest = {"time": t, "value": float(v)}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/data")
def api():
    return jsonify(latest)

if __name__ == "__main__":
    threading.Thread(target=serial_reader, daemon=True).start()
    app.run(debug=True)
