"""7. Fie 𝑓:𝒫(𝑛)→ℕ 𝑝𝜖𝒫(𝑛),𝑓(𝑝)=|{(𝑖,𝑗)𝑖<𝑗,𝑝(𝑖)=𝑗 ş𝑖 𝑝(𝑗)=𝑖 ⁄}| funcţia obiectiv a unei probleme de maxim, unde 𝒫(𝑛) desemnează mulţimea permutărilor de n elemente.
a. Scrieţi o funcţie Python pentru generarea aleatoare a unei populaţii, pop, cu dimensiunea dim; calitatea fiecărui individ este memorată la sfârşitul fiecărei reprezentări cromozomiale;
b. Pentru o probabilitate de mutaţie dată, pm, scrieţi o funcţie de mutaţie utilizând operatorul de mutaţie prin amestec care, pe baza populaţiei pop obţine o nouă populaţie, popm. Populaţia rezultată are tot dim indivizi."""

import numpy as np


def fitness(p):
    """Calculeaza fitness-ul unei permutari p"""
    n = len(p)
    return sum([1 for i in range(n) for j in range(i + 1, n) if p[i] == j and p[j] == i])


def generate_population(dim, n):
    """Genereaza o populatie aleatoare de permutari de n elemente"""
    pop = np.zeros((dim, n + 1), dtype=int)
    for i in range(dim):
        pop[i, :n] = np.random.permutation(n)
        pop[i, n] = fitness(pop[i, :n])
    return pop


def mutation(pop, pm):
    """Operator de mutatie prin amestecare"""
    dim, n = pop.shape
    popm = np.zeros((dim, n), dtype=int)
    for i in range(dim):
        if np.random.rand() < pm:
            popm[i, :] = np.random.permutation(max(pop[i, :n]))
        else:
            popm[i, :] = pop[i, :]
    return popm


def main():
    """Functia principala"""
    dim = 10
    n = 5
    pm = 0.1
    pop = generate_population(dim, n)
    print(f"Populatia initiala, cu {dim} indivizi, permutari de ordin {n} \n\n", pop)
    popm = mutation(pop, pm)
    print(
        f"\n\nPopulatia rezultat, cu {pm} probabilitate de mutatie, tot cu {dim} indivizi, permutari de ordin {n}\n\n",
        popm)
