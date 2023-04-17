"""3. Fie 𝑓:[−1,1] × [0,0.2] × [0,1] × [0,5] → ℝ, 𝑓(𝑥1, 𝑥2, 𝑥3, 𝑥4) = 1 + 𝑠𝑖𝑛(2𝑥1 − 𝑥3) + (𝑥2 ∗𝑥4)^(1/3) funcţia
obiectiv a unei probleme de maxim. Un genotip este un vector 𝑥 =(𝑥1, 𝑥2, 𝑥3, 𝑥4)𝑇, 𝑥 ∈ [−1,1] × [0,0.2] × [0,1] × [0,5]

a. Scrieţi o funcţie Python pentru generarea aleatoare a unei populaţii, pop, cu dimensiunea dim;
b. Pentru o probabilitate de mutaţie dată, pm, scrieţi o funcţie mutaţie de tip fluaj cu pragul 𝑡 =0.6 (𝜎 =𝑡/3) care,
pe baza populaţiei pop obţine o nouă populaţie, cu indivizii eventual mutanţi ai lui pop."""

import numpy as np


def fitness(x):
    """Calculates the fitness of a vector x"""
    return 1 + np.sin(2 * x[0] - x[2]) + (x[1] * x[3]) ** (1 / 3)


def generate_population(dim):
    """Genereaza o populatie aleatoare de dimensiune dim."""
    pop = np.zeros((dim, 5))
    for i in range(dim):
        pop[i, 0] = np.random.uniform(-1, 1)
        pop[i, 1] = np.random.uniform(0, 0.2)
        pop[i, 2] = np.random.uniform(0, 1)
        pop[i, 3] = np.random.uniform(0, 5)
        pop[i, 4] = fitness(pop[i, :4])
    return pop


def mutation(pop, pm):
    """Mutation operator"""
    dim, n = pop.shape
    popm = np.zeros((dim, n), dtype=float)
    for i in range(dim):
        if np.random.rand() < pm:
            sign = np.random.randint(0, 2)
            if sign == 0:
                sign = -0.6
            else:
                sign = 0.6
            j = np.random.randint(0, 4)
            popm[i, j] = pop[i, j] + sign
            if j == 0:
                if popm[i, j] < -1:
                    popm[i, j] = -1
                if popm[i, j] > 1:
                    popm[i, j] = 1
            elif j == 1:
                if popm[i, j] < 0:
                    popm[i, j] = 0
                if popm[i, j] > 0.2:
                    popm[i, j] = 0.2
            elif j == 2:
                if popm[i, j] < 0:
                    popm[i, j] = 0
                if popm[i, j] > 1:
                    popm[i, j] = 1
            elif j == 3:
                if popm[i, j] < 0:
                    popm[i, j] = 0
                if popm[i, j] > 5:
                    popm[i, j] = 5
            popm[i, 4] = fitness(popm[i, :4])
        else:
            popm[i, :] = pop[i, :]
    return popm


def main():
    """Main function"""
    dim = 10
    pm = 0.1
    pop = generate_population(dim)
    print(f"Populatia initiala, cu {dim} indivizi\n\n", pop)
    popm = mutation(pop, pm)
    print(f"\n\nPopulatia rezultat, cu {pm} probabilitate de mutatie, tot cu {dim} indivizi\n\n", popm)
