try:
    frequencies = [float(input(f"Entrez la fréquence {i+1} (Hz) : ")) for i in range(5)]
    print(f"Moyenne des fréquences : {sum(frequencies)/len(frequencies):.2f} Hz")
except ValueError:
    print("Erreur: Entrez des nombres valides.")