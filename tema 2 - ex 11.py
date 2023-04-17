"""11. Fie 𝑓:{1,2,…,500}→ℝ,𝑓(𝑥)=(𝑠𝑖𝑛(𝑥−2))2−𝑥∙𝑐𝑜𝑠(2∙𝑥) funcţia obiectiv a unei probleme de maxim. Fiecărui fenotip 𝑥∈{1,2,…,500} îi corespunde un genotip şir binar obţinut prin reprezentarea standard în bază 2 a lui x.
a. Scrieţi o funcţie Python pentru generarea aleatoare a unei populaţii, pop, cu dimensiunea dim; calitatea fiecărui individ este memorată la sfârşitul fiecărei reprezentări cromozomiale;
b. Scrieţi o funcţie Python care, pentru populaţia generată pop obţine o populaţie de părinţi prin aplicarea selecţiei de tip turneu cu k indivizi (k parametru de intrare)."""

import numpy as np

def fitness(x):
    return (np.sin(x - 2) ** 2) - x * np.cos(2 * x)

def generate_population(dim):
    pop = np.zeros((dim, 10), dtype=int)
    num = np.random.randint(1, 501, dim)
    for i in range(dim):
        pop[i, :9] = [int(x) for x in bin(num[i])[2:].zfill(9)]
        pop[i, 9] = fitness(num[i])
    return pop

def tournament_selection(pop, k):
    parinti = np.zeros((len(pop), 10), dtype=int)
    for i in range(len(pop)):
        idx = np.random.randint(0, len(pop), k)
        parinti[i] = pop[idx[np.argmax(pop[idx, 9])]]
    return parinti

def main():
    dim = 10
    k = 3
    pop = generate_population(dim)
    print(f"Populatia initiala, cu {dim} indivizi:\n",pop)
    parinti = tournament_selection(pop, k)
    print(f"Populatia parintilor, cu {dim} indivizi si {k} participanti la turnir\n\n", parinti)