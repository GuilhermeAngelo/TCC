import itertools
import ordpy as ord
from ordinal.ordinal import pattern_permutation, read_csv,view_matriz,generate_matriz_trasition, generate_dict_distributions


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
    

    def distritution_probability(self) -> dict:
        distributions_patterns = generate_dict_distributions(self.permutations, self.dimension)
        all_patterns = self.generate_all_permutations()
        dict_distributuion_probability = {}

        for pattern in all_patterns:
            dict_distributuion_probability[pattern] = (distributions_patterns.get(pattern)/self.n)

        return dict_distributuion_probability

if __name__ == "__main__":
    for i in range(1):
        objec = OrdinalSequence(archive_name='dados_random.csv', dimension=3, tau=1, column=i)
        dp = objec.distritution_probability()  
        print(dp)