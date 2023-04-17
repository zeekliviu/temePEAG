"""5. Fie funcţia 𝑓(𝑥)=Σ𝑥𝑖7𝑖=1,𝑥=(𝑥1,…,𝑥7)∈{0,1}7 care trebuie maximizată (un genotip este un vector binar cu 7 componente).
a. Scrieţi o funcţie Python pentru generarea aleatoare a unei populaţii, pop, cu dimensiunea dim; calitatea fiecărui individ este memorată la sfârşitul fiecărei reprezentări cromozomiale;
b. Pentru o probabilitate de recombinare dată, pc, scrieţi o funcţie de recombinare utilizând operatorul de încrucişare multi-punct pentru 2 puncte de încrucişare care, pe baza populaţiei pop obţine o nouă populaţie, popc. Populaţia rezultată are tot dim indivizi (este utilizată şi recombinarea asexuată şi calitatea fiecărui individ este memorată la sfârşitul fiecărei reprezentări cromozomiale)"""

import numpy as np

def fitness(x):
    """Calculează fitness-ul unui individ"""
    return sum(x)

def generate_population(dim):
    """Generează o populaţie aleatoare de dim indivizi"""
    pop = np.zeros((dim, 8), dtype=int)
    for i in range(dim):
        pop[i, :7] = np.random.randint(0, 2, 7)
        pop[i, 7] = fitness(pop[i, :7])
    return pop

def crossover(pop, pc):
    """Operator de recombinare multi-punct"""
    dim, n = pop.shape
    popc = np.zeros((dim, n), dtype=int)
    for i in range(0, dim, 2):
        if np.random.rand() < pc:
            # crossover
            p1 = np.random.randint(1, 7)
            p2 = np.random.randint(1, 7)
            if p1 > p2:
                p1, p2 = p2, p1
            popc[i, :p1] = pop[i, :p1]
            popc[i, p1:p2] = pop[i + 1, p1:p2]
            popc[i, p2:] = pop[i, p2:]
            popc[i + 1, :p1] = pop[i + 1, :p1]
            popc[i + 1, p1:p2] = pop[i, p1:p2]
            popc[i + 1, p2:] = pop[i + 1, p2:]
            popc[i, 7] = fitness(popc[i, :7])
            popc[i + 1, 7] = fitness(popc[i + 1, :7])
        else:
            popc[i, :] = pop[i, :]
            popc[i + 1, :] = pop[i + 1, :]
    return popc

def main():
    dim = 10
    pc = 0.7
    pop = generate_population(dim)
    print(f"Populatia initiala, cu {dim} indivizi:\n", pop)
    popc = crossover(pop, pc)
    print(f"\nPopulatia dupa recombinare cu probabilitate de {pc}, formata tot din {dim} indivizi.\n\n", popc)