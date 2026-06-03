# ======================================================
#SIMULACIÓN (ACTIVA AHORA)
# ======================================================

import time
import random
from supabase import create_client


url = "https://equlpatbwgevghaihlpj.supabase.co"
key = "sb_publishable_5BLE9i3yGJ8R9iQw4b9Ncg_6QNhJgen"

supabase = create_client(url, key)

print(" Sistema IoT iniciado...")
print(" Simulación activa + envío a Supabase\n")

while True:

    temperatura = round(random.uniform(2, 8), 2)
    humedad = round(random.uniform(40, 70), 2)

    print(f"🌡 Temp: {temperatura} | 💧 Humedad: {humedad} |")

    try:
        supabase.table("sensores").insert({
            "temperatura": temperatura,
            "humedad": humedad,
        }).execute()

        print("✅ Enviado a Supabase\n")

    except Exception as e:
        print("❌ Error:", e)

    time.sleep(2)