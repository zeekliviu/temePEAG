"""6. Fie 𝑓:{1,2,…,350}→ℝ,𝑓(𝑥)=𝑥2 funcţia obiectiv a unei probleme de maxim. Fiecărui fenotip 𝑥∈{1,2,…,350} îi corespunde un genotip şir binar obţinut prin codificarea Gray.
a. Scrieţi o funcţie Python pentru generarea aleatoare a unei populaţii, pop, cu dimensiunea dim;
b. Pentru o probabilitate de recombinare dată, pc, scrieţi o funcţie de recombinare utilizând operatorul de încrucişare uni-punct care, pe baza populaţiei pop obţine o nouă populaţie, popc. Populaţia rezultată are tot dim indivizi (este utilizată şi recombinarea asexuată)."""

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

def crossover(pop, pc):
    """Operator de recombinare uni-punct"""
    dim, n = pop.shape
    popc = np.zeros((dim, n), dtype=int)
    for i in range(0, dim, 2):
        if np.random.rand() < pc:
            p = np.random.randint(1, 9)
            popc[i, :p] = pop[i, :p]
            popc[i, p:] = pop[i + 1, p:]
            popc[i + 1, :p] = pop[i + 1, :p]
            popc[i + 1, p:] = pop[i, p:]
            popc[i, 9] = fitness(int("".join(map(str, popc[i, :9])), 2))
            popc[i + 1, 9] = fitness(int("".join(map(str, popc[i + 1, :9])), 2))
        else:
            popc[i, :] = pop[i, :]
            popc[i + 1, :] = pop[i + 1, :]
    return popc

def main():
    """Funcţia principală"""
    dim = 10
    pc = 0.7
    pop = generate_population(dim)
    print(f"Populatia initiala, cu {dim} indivizi\n\n", pop)
    popc = crossover(pop, pc)
    print(f"\n\nPopulatia rezultat, cu {pc} probabilitate de recombinare, tot cu {dim} indivizi\n\n", popc)