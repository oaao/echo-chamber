import itertools
import json
import pprint

from candidates import CANDIDATES

combinations = list(itertools.combinations(CANDIDATES, 2))

if __name__ == '__main__':

    with open('current.json', 'w') as f:
        json.dump(combinations, f, indent=2)

    pprint.pprint(combinations, indent=4)
