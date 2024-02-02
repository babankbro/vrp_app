import sys
sys.path.append("./utility")
sys.path.append("./problem")

from data_lookup import *
from algorithm_factory import *
from vrp import *
import numpy as np
from pymoo.optimize import minimize
import matplotlib.pyplot as plt

lookup = create_data_lookup("./dataset/input_vrp.csv")
print(lookup['DM'].shape)
print(lookup['DM'])

n_customers = len(lookup['DM']) - 1
demands = lookup['DEMAND']
visit_times = lookup['VISITED TIME']
vehicle_capacity = 100
max_travel_time = 10*60
distance_matrix = lookup['DM']
problem = VRPProblem(n_customers, demands, visit_times, vehicle_capacity, 
                 max_travel_time, distance_matrix)

#xs = np.random.random(n_customers)
factory = AlgorithmFactory()
algorithm = factory.get_algorithm(name = "DE")


print(algorithm)
res = minimize(problem,
               algorithm,
               ("n_gen", 10),
               seed=1,
               verbose=1)

xs = res.X
td, routes = problem.decode_routes(xs)
print(f"Total Distance: {td}")
for route in routes:
    print(route)

xs =  lookup['LNG']
ys =  lookup['LAT']
plt.scatter(xs, ys, color='blue')
plt.scatter(xs[:1], ys[:1], color='red')


for route in routes:
    route = route['route']
    route.insert(0, 0)
    route.append(0)
    plt.plot(xs[route], ys[route], color='black')

plt.show()