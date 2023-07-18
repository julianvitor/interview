# -*- coding: utf-8 -*-
# This code was written and tested in the standard implementation of Python 3.11.3. Execution on alternative implementations like pypy has not been tested.

# Intermediate points are not necessary for the polygon. 
# Lines only need two points: endpoint and start point if they are vectors, or point A and B if they are not.
# Removing intermediate points simplifies the polygon. [(1,1),(1,2),(1,3),(1,4),(2,4),(3,4),(4,4)] --> [(1,1),(1,4),(4,4)].
# Points can be aligned on the X or Y axis.


def remove_intermediate_points(list):
    if len(list) <= 2:# Empty lists or lists containing a single element do not require simplification.
        return list

    # Creates a new list with the first point.
    new_list = [list[0]]

    # Iterates through the list of points starting from the second element (element 0 is the initial point).
    for i in range(1, len(list) - 1):
        # Checks if the current point is aligned with the adjacent points, if is not, adds it.
        if not is_aligned(list[i-1], list[i], list[i+1]):
            new_list.append(list[i]) 

    # Adds the last point to the new list.
    new_list.append(list[-1])

    return new_list

def is_aligned(ponto_anterior, ponto_referencia, ponto_posterior):
    # Checks if the points are aligned.
    return (ponto_referencia[0] - ponto_anterior[0]) * (ponto_posterior[1] - ponto_referencia[1]) == (ponto_posterior[0] - ponto_referencia[0]) * (ponto_referencia[1] - ponto_anterior[1])

list_points = [(1,1),(1,2),(1,3),(1,4),(2,4),(3,4),(4,4),(5,4)]
new_list_points = remove_intermediate_points(list_points)

print("original list", list_points)
print("optimized list", new_list_points)




























# MIT License

# Copyright (c) 2023 Julian Carreiro

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
