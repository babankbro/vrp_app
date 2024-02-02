import numpy as np
from pymoo.core.problem import ElementwiseProblem

class VRPProblem(ElementwiseProblem):
    
    def __init__(self, n_customers, demands, visit_times, vehicle_capacity, 
                 max_travel_time, distance_matrix):
        #print("n_customers", n_customers)
        #super().__init__(n_var=n_customers, n_obj=1, xl=0, xu=1)
        
        self.demands = demands
        self.visit_times = visit_times
        self.vehicle_capacity = vehicle_capacity
        self.max_travel_time = max_travel_time
        self.distance_matrix = distance_matrix
        super().__init__(n_var=n_customers, n_obj=1, n_constr=0,  xl=0, xu=1)

    def _evaluate(self, xs, out, *args, **kwargs):
        #print(xs.shape)
        
        total_distance, routes = self.decode_routes(xs)
        out["hash"] = hash(str(xs))
        out["F"] = total_distance

    def decode_routes(self, x):
        permutation = np.argsort(x) + 1
        #print("permutation",permutation)
        demands = self.demands
        vehicle_capacity = self.vehicle_capacity
        max_travel_time_per_route = self.max_travel_time
        visit_times = self.visit_times
        distance_matrix = self.distance_matrix
        route_infos = []
        routes = []
        current_route = []
        remaining_capacity = vehicle_capacity
        total_travel_time = 0
        depot = 0
        last_point = depot
        total_distance = 0
        route_distance = 0
        for customer in permutation:
            demand = demands[customer]
            additional_travel_time = visit_times[customer]
            travel_time = distance_matrix[last_point][customer]
            go_back_time = distance_matrix[customer][depot]
            #print("customer", customer)
            #print(demand, remaining_capacity)
            if (demand <= remaining_capacity and 
                total_travel_time + travel_time + additional_travel_time + go_back_time<= max_travel_time_per_route):
                current_route.append(customer)
                remaining_capacity -= demand
                total_travel_time += additional_travel_time + travel_time 
                last_point = customer
                route_distance += travel_time
            else:
                route_distance += go_back_time
                total_travel_time += go_back_time
                total_distance += route_distance
                route_infos.append( {'route': current_route, 
                                     "distance":route_distance, 'time': total_travel_time}  )
                #routes.append(current_route)
                last_point = depot
                current_route = [customer]
                remaining_capacity = vehicle_capacity - demand
                travel_time = distance_matrix[last_point][customer]
                total_travel_time = additional_travel_time  + travel_time
                route_distance = travel_time
                

        if current_route:
            route_distance += go_back_time
            total_travel_time += go_back_time
            total_distance += route_distance
            route_infos.append( {'route': current_route, 
                                 "distance":route_distance, 'time': total_travel_time})
        
        return total_distance, route_infos
              