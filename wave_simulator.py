import math

freq1 = 440  # A4 note
freq2 = 660  # E5 note
sample_rate = 44100  # Standard audio rate
duration = 0.5  # 0.5 seconds

time_points = [t / sample_rate for t in range(int(duration * sample_rate))]
wave = [math.sin(2 * math.pi * freq1 * t) + math.sin(2 * math.pi * freq2 * t) for t in time_points]

print(f"Frequences : {freq1} Hz + {freq2} Hz")
print("Premiers 5 echantillons :", wave[:5])

with open("wave_data.txt", "w", encoding="utf-8") as f:
    for sample in wave:
        f.write(f"{sample:.6f}\n")
print("Donnees enregistrees dans 'wave_data.txt'")