"""2. Fie 𝑓:{1,2, … ,1500} × {−1,0, , … ,2500} → ℝ, 𝑓(𝑥, 𝑦) = 𝑦 ∗ (𝑠𝑖𝑛(𝑥 − 2))^2
funcţia obiectiv a
unei probleme de maxim. Fiecărui fenotip (𝑥, 𝑦) ∈ {1,2, … ,1500} × {−1,0, , … ,2500} îi
corespunde un genotip şir binar obţinut prin reprezentarea în bază 2 a fiecărei componente a
fenotipului.
a. Scrieţi o funcţie Python pentru generarea aleatoare a unei populaţii, pop, cu dimensiunea dim;
calitatea fiecărui individ este memorată la sfârşitul fiecărei reprezentări cromozomiale;
b. Pentru o probabilitate de recombinare dată, pc, scrieţi o funcţie de recombinare utilizând
operatorul de încrucişare multi-punct pentru 3 puncte de încrucişare care, pe baza populaţiei pop
obţine o nouă populaţie, popc. Populaţia rezultată are tot dim indivizi (este utilizată şi
recombinarea asexuată şi calitatea fiecărui individ este memorată la sfârşitul fiecărei reprezentări
cromozomiale).
"""
import numpy as np
def fitness(x, y):
    """Calculeaza calitatea unui individ"""
    return y * np.sin(x - 2)**2

def genereaza_popi(dim):
    """Genereaza o populatie de dim indivizi, fiecare reprezentat printr-un sir de 16 biti, pentru a acoperi tot
    intervalul de valori. Calitatea fiecarui individ este memorata la sfarsitul fiecarei reprezentari cromozomiale.
    Cum fiecare individ are o reprezentare pe 16 biti, un rand din matricea pop are 33 de elemente. Primele 16
    pozitii desemneaza reprezentarea binara a lui x, urmatoarele 16 pozitii reprezinta reprezentarea binara a lui y,
    iar ultima pozitie memoreaza calitatea individului. Calitatea va fi de tip float, deoarece functia fitness
    returneaza un numar real. Trebuie sa schimbam afisarea matricei, astfel incat sa fie afisate doar cu o zecimală."""
    pop = np.zeros((dim, 33), dtype=int)
    x = np.random.randint(1, 1501, size=dim)
    y = np.random.randint(-1, 2501, size=dim)
    for i in range(dim):
        pop[i, :16] = np.array(list(np.binary_repr(x[i], width=16)), dtype=int)
        pop[i, 16:32] = np.array(list(np.binary_repr(y[i], width=16)), dtype=int)
        pop[i, 32] = fitness(x[i], y[i])
    return pop

def recombinare(pop, pc):
    """Functia de recombinare multi-punct pentru 3 puncte de incrucisare. Pentru fiecare individ, se genereaza
    un numar aleatoriu intre 0 si 1. Daca numarul este mai mic decat probabilitatea de recombinare, atunci
    individul va fi supus recombinarii. Daca nu, individul va fi copiat in noua populatie. Pentru recombinare,
    se va folosi operatorul de incrucisare multi-punct pentru 3 puncte de incrucisare. Se va genera un vector
    cu 3 valori aleatoare, care vor fi pozitiile punctelor de incrucisare. Se va copia din individul parinte
    in individul copil, incepand cu pozitia 0 si pana la pozitia primului punct de incrucisare. Apoi se va
    copia din individul parinte in individul copil, incepand cu pozitia urmatoare celui de-al doilea punct de
    incrucisare si pana la pozitia urmatoare celui de-al treilea punct de incrucisare. In final, se va copia din
    individul parinte in individul copil, incepand cu pozitia urmatoare celui de-al treilea punct de incrucisare
    si pana la pozitia finala. Calitatea fiecarui individ va fi calculata si va fi memorata la sfarsitul fiecarei
    reprezentari cromozomiale. Populatia rezultata are dim indivizi."""
    popc = np.zeros((pop.shape[0], 33), dtype=int)
    for i in range(0, pop.shape[0], 2):
        if np.random.rand() < pc:
            p1 = np.random.choice([j for j in range(16)])
            p2 = np.random.choice([j for j in range(16)])
            while p2 == p1:
                p2 = np.random.choice([j for j in range(16)])
            p3 = np.random.choice([j for j in range(16)])
            while p3 == p1 or p3 == p2:
                p3 = np.random.choice([j for j in range(16)])
            puncte = [p1, p2, p3]
            puncte.sort()
            popc[i, :puncte[0]] = pop[i, :puncte[0]]
            popc[i, puncte[0]:puncte[1]] = pop[i+1, puncte[0]:puncte[1]]
            popc[i, puncte[1]:puncte[2]] = pop[i, puncte[1]:puncte[2]]
            popc[i, puncte[2]:] = pop[i+1, puncte[2]:]
            popc[i, 32] = fitness(int("".join(map(str, popc[i, :16])), 2), int("".join(map(str, popc[i, 16:32])), 2))
        else:
            popc[i, :] = pop[i, :]
            popc[i+1, :] = pop[i+1, :]
    return popc

def main():
    """Functia main"""
    dim = 4
    pc = 0.7
    pop = genereaza_popi(dim)
    print(f"Populatia initiala, formata din {dim} indivizi.\n\n",pop)
    popc = recombinare(pop, pc)
    print(f"\nPopulatia dupa recombinare cu probabilitate de {pc}, formata tot din {dim} indivizi.\n\n", popc)