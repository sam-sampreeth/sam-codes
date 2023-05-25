import numpy as nump
import matplotlib.pyplot as plt

freq = int(input("Enter frequency - "))
peakVol = int(input("Enter peak voltage - "))
resistance = int(input("Enter resistance - "))

period = 1 / freq
numSamples = 1000
time = nump.linspace(0, period, numSamples)
omega = 2 * 3.14 * freq
peakCur = peakVol / resistance

voltage = peakVol * nump.sin(omega * time)
current = peakCur * nump.sin(omega * time)
power = voltage * current

avg_power = max(power)
print(avg_power)

plt.plot(time, voltage, label="Voltage (V)")
plt.plot(time, current, label="Current (A)")
plt.axhline(y=avg_power, label="Average Power (Pavg)", color="r")
plt.xlabel("Time(s)")
plt.ylabel("Value")
plt.title("Voltage, Current, and Power in a Purely Resistive Circuit")
plt.legend()
plt.grid(1)
plt.show()
