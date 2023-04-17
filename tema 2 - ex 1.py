"""1. Fie 𝑓: 𝒫(𝑛) → ℕ 𝑝𝜖𝒫(𝑛), 𝑓(𝑝) = |{(𝑖,𝑗)⁄𝑖 < 𝑗, 𝑝(𝑖) = 𝑗 ş𝑖 𝑝(𝑗) = 𝑖 }| funcţia obiectiv a unei
probleme de maxim, unde 𝒫(𝑛) desemnează mulţimea permutărilor de n elemente.
a. Scrieţi o funcţie Python pentru generarea aleatoare a unei populaţii, pop, cu dimensiunea dim;
calitatea fiecărui individ este memorată la sfârşitul fiecărei reprezentări cromozomiale;
b. Pentru o probabilitate de mutaţie dată, pm, scrieţi o funcţie de mutaţie utilizând operatorul de
mutaţie prin inserare care, pe baza populaţiei pop obţine o nouă populaţie, popm. Populaţia
rezultată are tot dim indivizi.
"""

import numpy as np

def fitness(p):
    """Calculates the fitness of a permutation p"""
    n = len(p)
    return sum([1 for i in range(n) for j in range(i+1, n) if p[i] == j and p[j] == i])

def generate_population(dim, n):
    """Generates a random population of permutations of n elements"""
    pop = np.zeros((dim, n+1), dtype=int)
    for i in range(dim):
        pop[i, :n] = np.random.permutation(n)
        pop[i, n] = fitness(pop[i, :n])
    return pop

def mutation(pop, pm):
    """Mutation operator"""
    dim, n = pop.shape
    popm = np.zeros((dim, n), dtype=int)
    for i in range(dim):
        if np.random.rand() < pm:
            # mutation
            j = np.random.randint(n-1)
            popm[i, :] = np.concatenate((pop[i, :j], pop[i, j+1:], pop[i, j:j+1]))
        else:
            # no mutation
            popm[i, :] = pop[i, :]
    return popm

def main():
    """Main function"""
    dim = 10
    n = 5
    pm = 0.1
    pop = generate_population(dim, n)
    print(f"Populatia initiala, cu {dim} indivizi, permutari de ordin {n}\n\n",pop)
    popm = mutation(pop, pm)
    print(f"\n\nPopulatia rezultat, cu {pm} probabilitate de mutatie, tot cu {dim} indivizi, permutari de ordin "
          f"{n}\n\n",popm)