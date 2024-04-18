import random
import itertools
import ordpy as ord


dimension = 3
interval  = 1
length_serie = 100


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


def generate_transition_matriz(line_colums):
    matriz = []
    for i in range(line_colums):
       matriz.append([0]*line_colums)
    
    return matriz

serie = gerar_serie(length_serie)
permutation = permutation(serie,dimension= dimension, tau= interval)
dict_result = generate_dict_distributions(permutation,dimension)

print()
print(f'permutation: {permutation}')
print()
print(f'dict_result: {dict_result}')
print(generate_transition_matriz(3))