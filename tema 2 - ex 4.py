"""4. Fie 𝑓:[−1,1] × [0,1] × [−2,1] → ℝ, 𝑓(𝑥1, 𝑥2, 𝑥3) = 1 + 𝑠𝑖𝑛(2𝑥1 − 𝑥3) + 𝑐𝑜𝑠(𝑥2) funcţia
obiectiv a unei probleme de maxim. Un genotip este un vector 𝑥 = (𝑥1, 𝑥2, 𝑥3)𝑇, 𝑥 ∈ [−1,1] × [0,1] × [−2,1]

a. Scrieţi o funcţie Python pentru generarea aleatoare a unei populaţii, pop, cu dimensiunea dim;
indivizii populaţiei sunt însoţiţi de funcţia merit (sunt vectori cu 4 componente).
b. Pentru o probabilitate de recombinare dată, pc, scrieţi o funcţie de recombinare utilizând
operatorul de recombinare aritmetică totală care, pe baza populaţiei pop obţine o nouă populaţie,
popc. Populaţia rezultată are tot dim indivizi (este utilizată şi recombinarea asexuată şi calitatea
fiecărui individ este memorată la sfârşitul fiecărei reprezentări cromozomiale).
"""

import numpy as np


def fitness(x):
    """Calculează fitness-ul unui individ"""
    return 1 + np.sin(2 * x[0] - x[2]) + np.cos(x[1])


def generate_population(dim):
    """Generează o populaţie aleatoare de dim indivizi"""
    pop = np.zeros((dim, 4))
    for i in range(dim):
        pop[i][0] = np.random.uniform(-1, 1)
        pop[i][1] = np.random.uniform(0, 1)
        pop[i][2] = np.random.uniform(-2, 1)
        pop[i, 3] = fitness(pop[i, :3])
    return pop


def crossover(pop, pc, alpha=0.5):
    """Operator de recombinare aritmetică totală
    """
    dim, n = pop.shape
    popc = np.zeros((dim, n))
    for i in range(0, dim, 2):
        if np.random.rand() < pc:
            # crossover
            popc[i, :3] = alpha * pop[i, :3] + (1 - alpha) * pop[i + 1, :3]
            popc[i + 1, :3] = alpha * pop[i + 1, :3] + (1 - alpha) * pop[i, :3]
            popc[i, 3] = fitness(popc[i, :3])
            popc[i + 1, 3] = fitness(popc[i + 1, :3])
        else:
            popc[i, :] = pop[i, :]
            popc[i + 1, :] = pop[i + 1, :]
    return popc


def main():
    dim = 10
    pc = 0.7
    alpha = 0.4
    pop = generate_population(dim)
    print(f"Populatia initiala, cu {dim} indivizi:\n", pop)
    popc = crossover(pop, pc, alpha)
    print(f"\nPopulatia finala, cu {dim} indivizi, probabilitate de recombinare de {pc} si coeficient de "
          f"recombinare {alpha}\n\n", popc)
