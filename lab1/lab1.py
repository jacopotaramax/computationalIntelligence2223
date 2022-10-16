import random
import logging

def problem(N, seed=None):
    random.seed(seed)
    return [
        list(set(random.randint(0, N - 1) for n in range(random.randint(N // 5, N // 2))))
        for n in range(random.randint(N, N * 5))
    ]

def greedy(N,l):
    goal = set(range(N))
    covered = set()
    solution = list()
    all_lists = sorted(l, key=lambda l: len(l))
    while goal != covered:
        x = all_lists.pop(0)
        if not set(x) < covered:
            solution.append(x)
            covered |= set(x)
    
    #print("Gready solution : ", solution)
    logging.info(
        f"Greedy solution for N={N}: w={sum(len(_) for _ in solution)} (bloat={(sum(len(_) for _ in solution)-N)/N*100:.0f}%)"
    )
    logging.debug(f"{solution}")



def set_cover(N, sets):
    goal = set(range(0, N))
    covered = set()
    
    subsets = [set(x) for x in sets]
    
    elements = set(e for s in subsets for e in s)
    if elements != goal:
        return None
    
    cover = []  
    while covered != elements:
        subset = max(subsets, key=lambda s: len(s-covered) / (len(s.intersection(covered))+1))
        cover.append(subset)
        covered |= subset
    
    logging.info(
        f"Cover solution for N={N}: w={sum(len(_) for _ in cover)} (bloat={(sum(len(_) for _ in cover)-N)/N*100:.0f}%)"
    )
    logging.debug(f"{cover}")


if __name__=="__main__":
    logging.getLogger().setLevel(logging.INFO)
    for N in [5, 10, 20, 100, 500, 1000]:
        l = problem(N,42)
        greedy(N,l)
        set_cover(N,l)
        print('')