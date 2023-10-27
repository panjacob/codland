data = [4, 0, 5, 0, 3, 0, 0, 5]
non_zero_index = 0 # Miejsce dla liczby niezerowej

for i, item in enumerate(data): # enumeate zwraca iterator jak i wartość z listy
    if item != 0:
        data.pop(i)  # Usuwa z liczbę z danego miejsca
        data.insert(non_zero_index, item) # Wstawia liczbę w miejsce dla kolejnej liczby niezerowej i przesuwa resztę
        non_zero_index += 1 # Kolejne miejsce dla liczby niezerowej jest o jeden w prawo (czyli o jeden więcej)

print(data)
