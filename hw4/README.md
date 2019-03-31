Author: Chayanon Wichitrnithed
OS: Arch Linux 4.19.30-1-lts
Compiler: GHC 8.6.4


Composite Trapezoidal Rule
=====================

Load the file into GHCi:

    $ ghci CompositeTrapezoidal.hs

To integrate a function, use "integrate" with inputs: function to integrate, lower bound, upper bound, and number of subintervals. For example, to integrate e^(-x^2) from x = 0 to x = 1 using 128 subintervals, type

    *Main> integrate (\x -> exp (-x^2)) 0 1 128
    0.74682039...

To quit, type

    *Main> :q


Bisection Method and Newton's Method
=====================

Load the file into GHCi:

    $ ghci RootFinding.hs

To use bisection for the polynomial given in the problem, specify the number of iterations, lower bound, and upper bound. For example, to display 20 iterations with a = 1 and b = 2, type

    *Main> mapM_ print $ take 20 $ bisection p 1 2


To use Newton's method for part (a) in problem 6, specify the number of iterations and the initial guess. For example, with 15 iterations with x0 = -2, we use

    *Main> display sampleA 15 (-2)

For part (b), we use sampleB:

    *Main> display sampleB 7 0
