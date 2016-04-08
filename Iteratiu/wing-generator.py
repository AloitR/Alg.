#!/usr/bin/python

import sys

from random import choice, shuffle, sample
from string import uppercase

wing_types = map( lambda x : x + '-Wing', ['A', 'B', 'E', 'V', 'X', 'Y'] )
solution = 0

def ship_gen(size):
    free_pos = sample( range( size ), size >> 1 )
    position = 0
    global solution
    solution = min( free_pos )
    while position <= size:
        if position not in free_pos:
            yield (choice(wing_types), str(position))
        position += 1

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit('Usage: ' + sys.argv[0] + ' <list_size>')

    list_size = int(sys.argv[1])

    out_list = [ i for i in ship_gen(list_size * 2) ]

    out_list = out_list[:list_size]

    shuffle( out_list )

    print '%s' % '\n'.join(map(lambda x: ' '.join(x), out_list))
    print >> sys.stderr, 'Solution: ' + str(solution)
