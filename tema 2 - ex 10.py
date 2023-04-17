"""
10. Fie 𝑓:{1,2,…,350}→ℝ,𝑓(𝑥)=𝑥2 funcţia obiectiv a unei probleme de maxim. Fiecărui fenotip 𝑥∈{1,2,…,350} îi corespunde un genotip şir binar obţinut prin codificarea Gray.
a. Scrieţi o funcţie Python pentru generarea aleatoare a unei populaţii, pop, cu dimensiunea dim;
b. Aplicaţi funcţia de generare implementată mai sus pentru obţinerea a două populaţii, pop1, pop2. Scrieţi o funcţie Python care obţine o nouă populaţie prin aplicarea unei proceduri de tip GENITOR (cu înlocuirea a 2 indivizi) celor două populaţii, unde pop2 este considerată populaţia progeniturilor lui pop1. Populaţia rezultată are tot dim indivizi.
"""

import numpy as np

def fitness(x):
    """Calculează fitness-ul unui individ"""
    return x ** 2

def binary_to_gray(x):
    """Codifică un număr binar în codul Gray"""
    x = int(x, 2)
    return bin(x ^ (x >> 1))[2:]

def generate_population(dim):
    """Generează o populaţie aleatoare de dim indivizi"""
    pop = np.zeros((dim, 10), dtype=int)
    x = np.random.randint(1, 351, dim)
    for i in range(dim):
        pop[i, :9] = np.array(list(binary_to_gray(bin(x[i])[2:]).zfill(9)))
        pop[i, 9] = fitness(x[i])
    return pop

def genitor(pop1, pop2):
    """Procedura de tip GENITOR"""
    dim, n = pop1.shape
    poz1, poz2 = np.random.randint(0, dim, 2)
    pop1 = pop1[pop1[:, -1].argsort()]
    pop1[0, :] = pop2[poz1, :]
    pop1[1, :] = pop2[poz2, :]
    return pop1, poz1, poz2

def main():
    """Funcţia principală"""
    dim = 10
    pop1 = generate_population(dim)
    print(f"Populatia initiala, cu {dim} indivizi\n\n", pop1)
    pop2 = generate_population(dim)
    print(f"\n\nPopulatia progeniturilor, cu {dim} indivizi\n\n", pop2)
    pop, poz1, poz2 = genitor(pop1, pop2)
    print(f"\n\nPopulatia rezultat, tot cu {dim} indivizi, unde primii 2 cei mai slabi cromozomi au fost "
          f"schimbati cu cromozomii {poz1} si {poz2} din pop2.\n\n", pop)