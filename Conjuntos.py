####################################### Conjuntos #######################################
# Estrutura de dados Set!

linguaens = {"Java", "Python", "Java"}
print(linguaens)

#############Acessando valores - Set não tem índice, necessário transformar em lsita para acessor por índice.

numeros = {1, 2, 3, 4, 3, 2}
numeros = list(numeros)
print(numeros[0])

conjunto_a = {1, 2, 3}
conjunto_b = {3, 4, 5}

conjunto_a.union(conjunto_b)
conjunto_a.intersection(conjunto_b)
conjunto_b.difference(conjunto_a)
conjunto_a.symmetric_difference(conjunto_b)

####{}.issubset - Subconjunto

conjunto_c = {1, 2, 3}
conjunto_d = {4, 1, 2, 5, 6, 3}

conjunto_c.issubset(conjunto_d)  # True, o conjunto C está contido no conjunto D. C é subconjunto de D.
conjunto_d.issubset(conjunto_c)  # False, o conjunto D não está contido no conjunto C. D não é subconjunto de C.

conjunto_c.issuperset(conjunto_a) # False
conjunto_d.issuperset(conjunto_c) # True


conjunto_e = {1, 2, 3, 4, 5}
conjunto_f = {6, 7, 8, 9}
conjunto_g = {1, 0}

conjunto_e.isdisjoint(conjunto_f) # True, os elementos do conjunto E não estão no conjunto F
conjunto_e.isdisjoint(conjunto_g) # False, os elementos do conjunto E estão contidos no conjunto G.


