import serial
import time
from datetime import datetime


# Configura a porta serial
ser = serial.Serial(
    port='COM8',
    baudrate=115200,
    timeout=1
)

print("Lendo dados da COM8...")

term1, term2, term3 = [],  [], []

try:
    while True:
        if ser.in_waiting > 0:
            linha1 = ser.readline().decode('utf-8', errors='ignore').strip()
            linha2 = ser.readline().decode('utf-8', errors='ignore').strip()
            linha3 = ser.readline().decode('utf-8', errors='ignore').strip()
            _ = ser.readline().decode('utf-8', errors='ignore').strip()

            term1.append(f"{datetime.now().strftime("%H-%M-%S-%f")}: {linha1}")
            term2.append(f"{datetime.now().strftime("%H-%M-%S-%f")}: {linha2}")
            term3.append(f"{datetime.now().strftime("%H-%M-%S-%f")}: {linha3}")

            print(f"{linha1}|\t{linha2}|\t{linha3}")

except KeyboardInterrupt:
    print("\nLeitura interrompida.")

finally:
    ser.close()
    print("Porta serial fechada.")

with (
    open(f"term1_{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.txt", "w") as saida1,
    open(f"term2_{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.txt", "w") as saida2,
    open(f"term3_{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.txt", "w") as saida3
):
    saida1.write("\n".join(term1))
    saida2.write("\n".join(term2))
    saida3.write("\n".join(term3))