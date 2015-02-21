# rice_problem
Funny interview question given by a coworker @[ltbesh](https://github.com/ltbesh)

## The problem:

Given a chessboard with in each square a certain amount of rice grains. Find the path from the first square (top-left) to the last square (bottom-right) that gives you the most quantity of rice grains. The algorithm must be `O(nm)` in space and time (`nm` = the size of the chessboard).


## Hints:

At first I thought of bruteforcing, using graph theory, etc. But it took too much time and too much space. The hint is in the fact that it takes `O(nm)` (so you only need a fixed number of matrices of the same size, and you only need to iterate a fixed number of times).

You should think about *how* to iterate over the matrix.

## Solution:

The solution is given in the `solution` branch
