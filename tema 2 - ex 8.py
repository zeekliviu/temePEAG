"""8. Fie 𝑓:𝒫(𝑛)→ℕ funcţia obiectiv definită pentru problema celor n regine astfel: 𝑝𝜖𝒫(𝑛),𝑓(𝑝)=𝑛×𝑛−12−|{(𝑖,𝑗)𝑖<𝑗,|𝑝(𝑖)−𝑝(𝑗)|=|𝑖−𝑗|⁄}|, unde 𝒫(𝑛) desemnează mulţimea permutărilor de n elemente.
a. Scrieţi o funcţie Python pentru generarea aleatoare a unei populaţii, pop, cu dimensiunea dim; calitatea fiecărui individ este memorată la sfârşitul fiecărei reprezentări cromozomiale;
b. Aplicaţi funcţia de generare implementată mai sus pentru obţinerea a două populaţii, pop1, pop2 cu câte dim indivizi. Scrieţi o funcţie Python care obţine o nouă populaţie prin aplicarea unei proceduri de tip elitist celor două populaţii, unde pop2 este considerată populaţia progeniturilor lui pop1. Populaţia rezultată are tot dim indivizi."""

import numpy as np

def fitness(p):
    """Calculeaza calitatea unei permutari p"""
    n = len(p)
    return n*(n-1)/2 - sum([abs(i-j) for i in range(n) for j in range(i+1, n) if abs(p[i]-p[j]) == abs(i-j)])

def generate_population(dim, n):
    """Genereaza o populatie aleatoare de permutari de n elemente"""
    pop = np.zeros((dim, n+1), dtype=int)
    for i in range(dim):
        pop[i, :n] = np.random.permutation(n)
        pop[i, n] = fitness(pop[i, :n])
    return pop

def elitist(pop1, pop2):
    """Procedura elitista"""
    dim, n = pop1.shape
    pop = np.zeros((dim, n), dtype=int)
    for i in range(dim):
        if pop1[i, n-1] > pop2[i, n-1]:
            pop[i, :] = pop1[i, :]
        else:
            pop[i, :] = pop2[i, :]
    return pop

def main():
    """Functia principala"""
    dim = 10
    n = 5
    pop1 = generate_population(dim, n)
    print(f"Populatia initiala 1, cu {dim} indivizi, permutari de ordin {n} \n\n", pop1)
    pop2 = generate_population(dim, n)
    print(f"\n\nPopulatia initiala 1, cu {dim} indivizi, permutari de ordin {n} \n\n", pop2)
    pop = elitist(pop1, pop2)
    print(f"\n\nPopulatia rezultat, cu {dim} indivizi, permutari de ordin {n}\n\n", pop)