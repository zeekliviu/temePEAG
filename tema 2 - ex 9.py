"""9. Fie 𝑓:{1,2,…,2500}→ℝ,𝑓(𝑥)=(𝑠𝑖𝑛(𝑥−2))2 funcţia obiectiv a unei probleme de maxim. Fiecărui fenotip 𝑥∈{1,2,…,2500} îi corespunde un genotip şir binar obţinut prin reprezentarea standard în bază 2 a lui x.
a. Scrieţi o funcţie Python pentru generarea aleatoare a unei populaţii, pop, cu dimensiunea dim; calitatea fiecărui individ este memorată la sfârşitul fiecărei reprezentări cromozomiale;
b. Scrieţi o funcţie Python care, pentru populaţia generată pop obţine o populaţie de părinţi prin aplicarea selecţiei de tip ruletă cu distribuţia de probabilitate FPS cu sigma-scalare."""

import numpy as np


def fitness(x):
    """Calculeaza fitness-ul unui individ x"""
    return np.sin(x - 2) ** 2


def generate_population(dim):
    """Generează o populaţie aleatoare de dim indivizi"""
    pop = np.zeros((dim, 13), dtype=float)
    for i in range(dim):
        pop[i, :12] = np.random.randint(0, 2, 12)
        integer = int("".join(map(str, pop[i, :12])).replace('.', ''), 2)
        pop[i, 12] = fitness(integer)
    return pop


def fps(qual):
    """Calculează probabilitatea de selecţie a unui individ, în funcţie de calitatea sa, fara sigma-scalare"""
    fps = np.zeros(len(qual))
    suma = np.sum(qual)
    for i in range(len(qual)):
        fps[i] = qual[i] / suma
    qfps = fps.copy()
    for i in range(1, len(qual)):
        qfps[i] = qfps[i - 1] + fps[i]
    return qfps


def sigmafps(qual):
    """Calculează probabilitatea de selecţie a unui individ, în funcţie de calitatea sa, cu sigma-scalare"""
    medie = np.mean(qual)
    deviatie = np.std(qual)
    new_qual = [max(0, qual[i] - medie + 2 * deviatie) for i in range(len(qual))]
    if np.sum(new_qual) == 0:
        return fps(qual)
    return fps(new_qual)


def roulette(pop):
    """Aplică selecţia de tip ruletă cu distribuţia de probabilitate FPS cu sigma-scalare"""
    pop_initiala = np.asarray(pop)
    parinti = pop_initiala.copy()
    fitnessuri = pop_initiala[:, parinti.shape[1] - 1]
    qfps = sigmafps(fitnessuri)
    for i in range(len(pop_initiala)):
        r = np.random.uniform(0, 1)
        pozitie = np.where(qfps >= r)[0][0]
        parinti[i, :] = pop_initiala[pozitie, :]
        parinti[i, parinti.shape[1] - 1] = fitness(int("".join(map(str, parinti[i, :12])).replace('.', ''), 2))
    return parinti


def main():
    """Funcţia principală"""
    dim = 10
    pop = generate_population(dim)
    print(f"Populatia initiala, cu {dim} indivizi\n\n", pop)
    popp = roulette(pop)
    print(f"\n\nPopulatia rezultat, cu {dim} indivizi\n\n", popp)

