import random
import turtle
import math
import copy

def student_details():
    
    student_id = 18040210
    student_username = 'ss19aee'

    return student_id, student_username

def generate_map(x_range, y_range, locations):

    generated_map = []
    for x in range(locations):
        x_rand = random.randint(-x_range, x_range)
        y_rand = random.randint(-y_range, y_range)
        locations = [x_rand, y_rand]
        generated_map.append(locations)

    return generated_map

def print_map(speed, color, thickness, selected_map):
    print("printing map")

    turtle.speed(speed)
    turtle.color(color)
    turtle.pensize(thickness)
    turtle.goto(selected_map[0])

    for x in range(len(selected_map)):
        turtle.goto(selected_map[x])

    
def calculate_distance(starting_x, starting_y, destination_x, destination_y):
    distance = math.hypot(destination_x - starting_x, destination_y - starting_y)  # calculates Euclidean distance (straight-line) distance between two points
    return distance

def calculate_path(selected_map):

    distance = 0
    for x in range(len(selected_map)):
        cal_distance = calculate_distance(selected_map[x-1][0], selected_map[x-1][1], selected_map[x][0], selected_map[x-1][1])
        distance = distance + cal_distance

    return distance

#################################################################################################

def nearest_neighbour_algorithm(selected_map):

    temp_map = copy.deepcopy(selected_map)

    optermised_map = []

    optermised_map.append(temp_map.pop(0))

    # you need to create an empty list for your optimised map 
    for x in range(len(temp_map)):
        location_check = {

            "coordinates": temp_map[0],
            "distance_calc": calculate_distance(optermised_map[len(optermised_map)-1][0],optermised_map[len(optermised_map)-1][1], temp_map[0][0],temp_map[0][1])

            }

        
    for m in range(len(temp_map)):
        dist_new = calculate_distance(optermised_map[len(optermised_map)-1][0],optermised_map[len(optermised_map)-1][1], temp_map[m][0],temp_map[m][1])

        if dist_new < location_check["distance_calc"]:
            location_check["distance_calc"] = dist_new
            location_check["coordinates"] = temp_map[m]


    optermised_map.append(location_check["coordinates"])
    temp_map.remove(location_check["coordinates"])


    return optermised_map

#################################################################################################

def genetic_algorithm(selected_map, population, iterations, mutation_rate, elite_threshold):

    gene_pool = create_population(population, selected_map)
    
    best_solution = iterator(iterations, mutation_rate, gene_pool, elite_threshold)

    return best_solution

def create_population(population, selected_map):

    gene_pool = []

    for y in range(population):
        gene_pool.append(copy.deepcopy(selected_map))
        random.shuffle(gene_pool[y])

    return gene_pool

def fitness_function(gene_pool, best_solution):

    ranking = []
    best_score = calculate_path(best_solution)
    for x in gene_pool:
        score = calculate_path(x)
        if score < best_score:
            best_solution = x
        ranking.append(score)

    sorted_gene_pool = [x for _,x in sorted(zip(ranking,gene_pool))]

    
    return sorted_gene_pool, best_solution

def iterator(gene_pool, iterations, mutation_rate, elite_threshold):

    best_solution = []
    temp_gene_pool = []

    for i in range(iterations):
        sorted_pool, new_best_solution = fitness_function(gene_pool, best_solution)

        new_gene_pool = mating_function(sorted_pool, new_best_solution, mutation_rate, elite_threshold)

        temp_gene_pool.extend(new_gene_pool)


    for x in range(len(temp_gene_pool)):
        temp_gene_pool[x] = {
            "single_gene": temp_gene_pool[x],
            "calculate_distance": calculate_path(temp_gene_pool[x])
        }


    temp_gene_pool = sorted(temp_gene_pool, key=lambda i : i['calculate_distance'])

    best_solution = temp_gene_pool[0]["single_gene"]

    return best_solution

def mating_function(gene_pool, best_solution, mutation_rate, elite_threshold):

    new_gene_pool = []
    for i in gene_pool:
        parent_1 = copy.deepcopy(gene_pool[random.randint(0, int(len(gene_pool)*elite_threshold))])
        parent_2 = copy.deepcopy(i)
        child = breed(parent_1, parent_2)
        child = mutate(child, mutation_rate)
        new_gene_pool.append(child)
    
    return new_gene_pool

def breed(parent_1, parent_2):

    cut_point = []

    cut_point.extend([random.randint(0,len(parent_2)),random.randint(0, len(parent_2))])

    child = []
    dna_1 =[]
    dna_2 =[]


    for n in range(cut_point[0], cut_point[1]):
        dna_1.append(parent_1[n])
    dna_2 = [item for item in parent_2 if item not in dna_1]

    child = dna_1 + dna_2

    return child

def mutate(child, mutation_rate):

    for switch in range(len(child)):
        if(random.random()<mutation_rate):
            switch_with = random.randint(0,len(child)-1)
            gene_1 = child[switch]
            gene_2 = child[switch_with]
            child[switch] = gene_2
            child[switch_with] = gene_1

    mutated_child = child

    return mutated_child
