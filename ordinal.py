import random
import itertools
import ordpy as ord


dimension = 3
interval  = 1
length_serie = 10


def gerar_serie(length_serie):
    serie = []
    for i in range(length_serie):
        serie.append(random.randint(1,1000))
    return serie


def pattern_permutation(dimension):
    pattern = ''
    for i in range (dimension):
        pattern += str(i+1)
    return pattern


def permutation(serie,dimension,tau):
    n = length_serie - (dimension - 1)*tau
    permuted_serie = ord.ordinal_sequence(data=serie, dx= dimension, taux= tau)

    return to_string(permuted_serie,n,dimension)


def to_string(permuted_serie, length_serie, dimension):
    result = []
    for i in range(length_serie):
        string_arr = ""
        for j in range(dimension):
            string_arr += str(permuted_serie[i][j] + 1)
        result.append(string_arr)
    return result


def generate_all_permutations(dimension):
    return [''.join(permutation) for permutation in itertools.permutations(pattern_permutation(dimension))]


def generate_dict_distributions(permuted_serie,dimension):
    perms = generate_all_permutations(dimension)
    dict_resultant = dict(zip(perms, [0]*len(perms)))

    for perm in permuted_serie:
        dict_resultant[perm] = dict_resultant[perm] + 1

    return dict_resultant


def generate_matriz(dimension):
    perms = generate_all_permutations(dimension)
    length_all_permutations = len(perms)
    matriz = []
    for i in range(length_all_permutations):
       matriz.append([0]*length_all_permutations)
    
    return (matriz,perms)

def generate_matriz_trasition(dimension,permuted_serie):
    tupla = generate_matriz(dimension)
    matriz = tupla[0]
    perms = sorted(tupla[1])
    length_serie = len(permuted_serie)

    for i in range(length_serie - 1):
            matriz[perms.index(permuted_serie[i])][perms.index(permuted_serie[i+1])] += 1

    return matriz
 

serie = gerar_serie(length_serie)
permutation = permutation(serie,dimension= dimension, tau= interval)
dict_result = generate_dict_distributions(permutation,dimension)

print()
print(f'permutation: {permutation}')
print()
print(f'dict_result: {dict_result}')
print()
print(f'todas as permutações: {sorted(generate_all_permutations(dimension))}')

print(generate_matriz_trasition(dimension,permutation))