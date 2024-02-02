
from pymoo.algorithms.soo.nonconvex.brkga import BRKGA
from pymoo.algorithms.soo.nonconvex.ga import GA
from pymoo.operators.sampling.lhs import LHS
from pymoo.algorithms.soo.nonconvex.de import DE
from pymoo.core.duplicate import ElementwiseDuplicateElimination

class MyElementwiseDuplicateElimination(ElementwiseDuplicateElimination):
    def is_equal(self, a, b):
        return a.get("hash") == b.get("hash")


class AlgorithmFactory:
    
    def get_algorithm(self, name="GA", paramters={"NP": 50}):
        if name == "GA":
            algorithm = BRKGA(
                n_elites=paramters['NP'],
                n_offsprings=paramters['NP']*2,
                n_mutants=paramters['NP'],
                bias=0.7,
                eliminate_duplicates=MyElementwiseDuplicateElimination())
            
            algorithm = GA(
                pop_size=100,
                eliminate_duplicates=True)
            
            return algorithm
        elif  name=="DE":
            algorithm = DE(
                pop_size=paramters['NP'],
                sampling=LHS(),
                variant="DE/rand/1/bin",
                CR=0.3,
                dither="vector",
                jitter=False
            )
            return algorithm
        print("Don't have this algorithm!")
        return None