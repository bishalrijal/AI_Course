import time
import numpy as np
from problems import NQueen
from uninformed_search_algo import (
    breadth_first_search,
    depth_first_search,
    depth_limit_search,
    uniform_cost_search,
)


if __name__ == '__main__':
    size = int(input('Enter size: '))
    t = time.time()
    solution = uniform_cost_search(NQueen(np.zeros((size, size))))
    if solution:
        solution.display()
    else:
        print('No solution')
    print('Time taken: ', time.time() - t, 'sec')
