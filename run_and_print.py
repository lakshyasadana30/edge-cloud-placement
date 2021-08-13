import time
from typing import Dict

from algorithms import *
from utils import *


def run_problem(problem: ServerPlacer, n, k):
    assert hasattr(problem, "place_server")
    problem.place_server(n, k)
    return problem.objective_latency(), problem.objective_workload()


def run_with_parameters(problems: Dict[str, ServerPlacer], n, k):
    results = {}
    results['MIP'] = run_problem(problems['MIP'], n, k)
    results['Top-K'] = run_problem(problems['Top-K'], n, k)

    sum_a = 0
    sum_b = 0
    for t in range(10):
        res = run_problem(problems['K-means'], n, k)
        sum_a += res[0]
        sum_b += res[1]
        time.sleep(1)
    results['K-means'] = (sum_a / 10, sum_b / 10,)

    sum_a = 0
    sum_b = 0
    for t in range(10):
        res = run_problem(problems['Random'], n, k)
        sum_a += res[0]
        sum_b += res[1]
    results['Random'] = (sum_a / 10, sum_b / 10,)

    return results


def run(data: DataUtils):
    problems = {}
    problems['MIP'] = MIQPServerPlacer(data.base_stations, data.distances)
    problems['K-means'] = KMeansServerPlacer(data.base_stations, data.distances)
    problems['Top-K'] = TopKServerPlacer(data.base_stations, data.distances)
    problems['Random'] = RandomServerPlacer(data.base_stations, data.distances)
    with open('data/results.txt', 'w') as file:
        # First picture
        # for n in range(300, 3300, 300):
        for n in range(30, 33, 30):
             k = int(n / 10)
             print("N={0}, K={1}".format(n, k), file=file)
             results = run_with_parameters(problems, n, k)
             for key, value in results.items():
                print(key, "Average distance (km)={0}, Load standard deviation={1}".format(value[0], value[1]), file=file)
                file.flush()

        print("======================================================", file=file)

        # Second picture
        n = 30
        for k in range(15, 23, 15):
            print("N={0}, K={1}".format(n, k), file=file)
            results = run_with_parameters(problems, n, k)
            for key, value in results.items():
                print(key, "Average distance (km)={0}, Load standard deviation={1}".format(value[0], value[1]), file=file)
                file.flush()

        file.close()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    data = DataUtils('baseN.csv', 'userN.csv')
    run(data)
