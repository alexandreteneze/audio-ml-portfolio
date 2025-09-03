import librosa
import numpy as np

audio_path = "C:\\Users\\user\\Desktop\\MATCHERING TRACKS\\TEST 02\\TEST 03\\woop2_master_16bit.wav"
try:
    audio, sr = librosa.load(audio_path)
    metadata = {
        "sample_rate_hz": sr,
        "duration_seconds": len(audio) / sr,
        "mean_amplitude": np.mean(np.abs(audio))
    }
    print("Metadonnees audio :")
    for key, value in metadata.items():
        print(f"{key}: {value:.2f}")
except FileNotFoundError:
    print("Erreur : Fichier non trouve.")
except Exception as e:
    print(f"Erreur : {e}")