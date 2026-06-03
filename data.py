# ======================================================
# PROYECTO NEVERA IoT - PUENTE PYTHON
# ======================================================

import serial
import time
from supabase import create_client

url = "https://equlpatbwgevghaihlpj.supabase.co"

key = "sb_publishable_5BLE9i3yGJ8R9iQw4b9Ncg_6QNhJgen"

supabase = create_client(url, key)

arduino = None
try:
    arduino = serial.Serial('COM3', 9600)
    print("Arduino conectado")
except:

    print("Arduino no conectado")

time.sleep(2)

print("Enviando datos a Supabase...\n")

while True:

    if arduino:

        try:

            data = arduino.readline().decode().strip()

            if data:

                temperatura = float(data)

                humedad = 0

                print(f"🌡 Temp real: {temperatura}")

                supabase.table("sensores").insert({

                    "temperatura": temperatura,
                    "humedad": humedad,

                }).execute()

        except Exception as e:

            print("Error:", e)
    else:
        print("Esperando Arduino...")
    time.sleep(2)