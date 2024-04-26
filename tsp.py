"""
calculate the distances between each city (x ,y) and storing in a distance matrix
rows represent the city we are coming from
cols represent the city we are going to
"""
def calculate_distances(cities):
  n = len(cities)
  distances = [[0 for _ in range(n)] for _ in range(n)]
  for i in range(n):
    for j in range(n):
      from_c = cities[i]
      to_c = cities[j]
      xf, yf = from_c[0], from_c[1]
      xt, yt = to_c[0], to_c[1]
      distance = ( (xf-xt)**2 + (yf-yt)**2 )**(.5)
      distances[i][j] = distance
  return distances

"""
default city function
"""
def get_cities():
  cities = [
      (0, 0),
      (-1, 1),
      (1, 1),
      (0, -1),
      (5, 5),
  ]
  return cities


"""
given a city finds the shortest possible route and its distance that 
goes through all other cities once and returns back to the original city

cc:int - current city
fc:int - first city
available_cities:[int] - list of valid possible cities to travel to from the current city
distances:[float][float] - a matrix storing distances between cities
curr_dist:float - sum of the distances between all cities on the current path (how far you've traveled so far)
path:[int] - the path that you have traveled so far
"""
def tsp_helper(cc, fc, available_cities, distances, curr_dist, path):
  cp_path = path[:]
  cp_path.append(cc)
  shortest_distance = None
  for ac in available_cities:
    cp_ac = available_cities[:]
    cp_ac.remove(ac)
    new_dist = curr_dist + distances[cc][ac]
    distance, best_path = tsp_helper(ac, fc, cp_ac, distances, new_dist, cp_path)
    if shortest_distance == None or distance < shortest_distance:
      shortest_distance = distance
  if not available_cities:
    shortest_distance = curr_dist + distances[cc][fc]
    best_path = cp_path
  return shortest_distance, best_path


"""
traveling salesman problem start off method
"""
def tsp(cities, distances):
  shortest_path = None
  shortest_dist = None
  for city in cities:
    cp_ac = cities[:]
    cp_ac.remove(city)
    distance, path = tsp_helper(city, city, cp_ac, distances, 0, [])
    if shortest_path is None or distance < shortest_dist:
      path.append(city)
      shortest_path = path
      shortest_dist = distance
  return shortest_dist, shortest_path


"""
given a prints the cities in the order specified by path
path being the path found by the algorithm
"""
def print_points(cities, path):
  for i in range(len(cities)):
    idx = path[i]
    print(cities[idx], "->", end=" ")
  print(cities[path[-1]])


def main():
  cities = get_cities()
  distances = calculate_distances(cities)
  shortest_dist, shortest_path = tsp(list(range(len(cities))), distances)
  print("distance", shortest_dist)
  print_points(cities, shortest_path)


main()

"""
tsp:
    shortest_distance = None
    visited cities
    for each c:
        if c in visited: coninue
        dist = start to me + me -> you + your shortest route
        if dist < shortest distance: update SD
    # at this point you have the shortest route through you
    return shortest distance, path to end

final point: return the shortest distance from that point to the starting point
start point: loop over all starting points in a master function
"""