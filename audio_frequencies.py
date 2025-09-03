import librosa
import numpy as np

audio_path = "C:\\Users\\user\\Desktop\\MATCHERING TRACKS\\TEST 02\\TEST 03\\woop2_master_16bit.wav"
try:
    audio, sr = librosa.load(audio_path)
    duration = len(audio) / sr
    print(f"Fréquence d'échantillonnage : {sr} Hz")
    print(f"Durée de l'audio : {duration:.2f} secondes")
    # Basic frequency analysis
    fft_data = np.abs(np.fft.fft(audio))
    freqs = np.fft.fftfreq(len(fft_data)) * sr
    peak_freq = freqs[np.argmax(fft_data[:len(fft_data)//2])]
    print(f"Fréquence dominante approximative : {abs(peak_freq):.2f} Hz")
except FileNotFoundError:
    print("Erreur : Fichier 'woop2_master_16bit.wav' non trouvé. Vérifiez le chemin.")
except Exception as e:
    print(f"Erreur : {e}")