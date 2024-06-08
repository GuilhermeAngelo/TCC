import itertools
import math

import numpy as np
import ordpy as ord

from ordinal.ordinal import (generate_dict_distributions,
                             generate_matriz_trasition, pattern_permutation,
                             read_csv, view_matriz)


class OrdinalSequence:


    def __init__(self, archive_name:str, dimension:int, tau: int, column:int = 0) -> None:
        self.archive_name = archive_name
        self.dimension = dimension
        self.tau = tau
        self.data = read_csv(self.archive_name, column)
        self.length_serie = len(self.data)
        self.n = self.length_serie - (self.dimension - 1)*self.tau
        self.pattern = pattern_permutation(self.dimension)
        self.permutations = self.permutation()
        self.all_patterns = self.generate_all_permutations()
    
    def generate_all_permutations(self):
        return [''.join(permutation) for permutation in itertools.permutations(self.pattern)]


    def to_string(self, permuted_serie: list) -> list:
        result = []
        for i in range(self.n):
            string_arr = ""
            for j in range(self.dimension):
                string_arr += str(permuted_serie[i][j] + 1)
            result.append(string_arr)
        return result


    def permutation(self) -> list:
        permuted_serie = ord.ordinal_sequence(data=self.data, dx= self.dimension, taux= self.tau)
        return self.to_string(permuted_serie)

    def uniform_probability(self):
        return 1/math.factorial(self.dimension)

    def generate_uniform_distribution_probability(self):
        uniform_distribution = {}
        probabilitity = self.uniform_probability()

        for pattern in self.all_patterns:
            uniform_distribution[pattern] = probabilitity

        return uniform_distribution
    
    def distritution_probability(self) -> dict:
        distributions_patterns = generate_dict_distributions(self.permutations, self.dimension)
        dict_distributuion_probability = {}

        for pattern in self.all_patterns:
            dict_distributuion_probability[pattern] = (distributions_patterns.get(pattern)/self.n)

        return dict_distributuion_probability
    
    def entropy_max(self) -> float:
        return np.log10(math.factorial(self.dimension))
    

    def get_shannon (self, distribution: dict):
        entropy = 0

        for pattern in self.all_patterns: 
            entropy += (distribution.get(pattern)*np.log10(distribution.get(pattern)))

        return -1*entropy
    

    def sum_discts(self, distribution: dict, u_distribution: dict) -> dict:
        sum_dict = {}

        for pattern in self.all_patterns:
            sum_dict[pattern] = (distribution[pattern] + u_distribution[pattern]) / 2

        return sum_dict
    

    def permutation_entropy(self, distribution = None , sum_uniform = False, auto = True, normalize = False) -> float:

        if auto == True:
            distribution_p = self.distritution_probability()

            if sum_uniform == False:
                if normalize:
                    return self.normalized_permutation_entropy(self.get_shannon(distribution_p))
                else:
                    return self.get_shannon(distribution_p)
            
            else:
                distribution_u = self.generate_uniform_distribution_probability()
                sum_distributions = self.sum_discts(distribution_p, distribution_u)
                
                if normalize:
                    return self.normalized_permutation_entropy(self.get_shannon(sum_distributions))
                else:
                    return self.get_shannon(sum_distributions)
        else:
            if distribution != None:
                distribution = distribution_p
                
                if sum_uniform == False:
                    if normalize:
                        return self.normalized_permutation_entropy(self.get_shannon(distribution))
                    else:
                        return self.get_shannon(distribution) 
                
                else:
                    distribution_u = self.generate_uniform_distribution_probability()
                    sum_distributions = self.sum_discts(distribution_p, distribution_u)

                    if normalize:
                        return self.normalized_permutation_entropy(self.get_shannon(sum_distributions))
                    else:
                        return self.get_shannon(sum_distributions)           
                
            else:
                print('informe a distribuição de probabilidade que deseja realizar a permutação entrópica')
    
    def uniform_permutation_entropy(self) -> float:
        u_distribution = self.generate_uniform_distribution_probability()

        return self.get_shannon(u_distribution)

    
    def jensen_shannon_divergense(self):
        
        divergense = self.permutation_entropy(sum_uniform = True) - (self.permutation_entropy()/2 + self.uniform_permutation_entropy()/2)
        
        return divergense


    def normalized_permutation_entropy(self, permutation_entropy) -> float:
        entropy_norm = permutation_entropy/self.entropy_max()

        return entropy_norm


    def inverse_of_maximum_value_JS(self):
        fact_d = math.factorial(self.dimension)
        Q_0 = (((fact_d + 1)/fact_d)*(np.log(fact_d + 1)) -2*np.log(2*fact_d) + (np.log(fact_d)))**1

        return -2*Q_0
    
    
    def desequilibrium_QJS(self):

        return self.inverse_of_maximum_value_JS()*self.jensen_shannon_divergense()

if __name__ == "__main__":
    for i in range(1):
        objec = OrdinalSequence(archive_name='dados_random.csv', dimension=3, tau=1, column=i)

        dp = f'\nDistribuição de Prob: \n{objec.distritution_probability()}\n\nDistribuição de Prob unifome: \n{objec.generate_uniform_distribution_probability()}\n\npermutação entropica:\n{objec.permutation_entropy()}\n\nQ0:\n{objec.inverse_of_maximum_value_JS()}\n\nQjs: {objec.desequilibrium_QJS()}\n\n'        

        print(dp)