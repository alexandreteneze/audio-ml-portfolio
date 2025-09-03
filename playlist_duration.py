songs = []
num_songs = int(input("Entrez le nombre de chansons : "))
for i in range(num_songs):
    name = input(f"Nom de la chanson {i+1} : ")
    minutes = int(input("Minutes : "))
    seconds = int(input("Secondes : "))
    songs.append(minutes * 60 + seconds)
print(f"Duree totale : {sum(songs) // 60} min {sum(songs) % 60} sec")