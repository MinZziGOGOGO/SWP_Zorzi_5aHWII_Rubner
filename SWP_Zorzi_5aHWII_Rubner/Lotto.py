import random
import matplotlib.pyplot as plt

def lotto_ziehung():
    lotto_zahlen = [i+1 for i in range(45)]
    ziehung = list()

    for i in range(6):
        random_number = lotto_zahlen[random.randint(0, 44)]
        ziehung.append(random_number)
        lotto_zahlen[random_number - 1], lotto_zahlen[-1 - i] = lotto_zahlen[-1 - i], lotto_zahlen[random_number - 1]
    return ziehung

def  lottoziehung_statistik():
    my_dictionary = {i: 0 for i in range(45)}
    for i in range(1000):
        jetzige_zahlen = lotto_ziehung()
        for j in jetzige_zahlen:
            my_dictionary[j - 1] += 1

    keys = [key + 1 for key in my_dictionary.keys()]  # Numbers from 1 to 45
    values = my_dictionary.values()
    plt.figure(figsize=(10, 6))
    plt.bar(keys, values, color='skyblue')
    plt.xlabel('Lotto Numbers')
    plt.ylabel('Frequency')
    plt.title('Frequency of Lotto Numbers Drawn')
    plt.xticks(keys)
    return plt.show()

lottoziehung_statistik()


