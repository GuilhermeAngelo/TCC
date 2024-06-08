import itertools
import ordpy as ord
import pandas as pd


dimension = 3
interval  = 1
length_serie = 1000


def read_csv(archive_name: str, column: int) -> list:
    serie = pd.read_csv(filepath_or_buffer=archive_name)
    length_serie = len(serie)
    result = []
    for i in range(length_serie):
        lin = serie.iloc[i].to_list()
        result += [lin[column]]
    return result


def pattern_permutation(dimension: int) -> str:
    pattern = ''
    for i in range (dimension):
        pattern += str(i+1)
    return pattern


def permutation(serie: list, dimension: int, tau: int) -> list:
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
 

def view_matriz(matriz, dimension):
    perms = sorted(generate_all_permutations(dimension))
    line_coluns = len(matriz)

    print()
    print('    ',*perms, end=" ",sep="  ")
    print('\n')
    for i in range(line_coluns): 
        print(perms[i] , *matriz[i], sep=dimension*" ")
    
    return ""