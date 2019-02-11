Author: Chayanon Wichitrnithed
Operating System: Arch Linux 4.19.14-1-lts
Language Used: Haskell
Compiler: ghc 8.6.3


Running the code
=====================

Once the Glasgow Haskell Compiler (GHC) has been installed, load the file into the
REPL in the command line:

    $ ghci Polynomial.hs

To create a Newton polynomial with a list of (x,y) data points, use:

    *Main> let newton = mkNewton [(-1,5), (0,1), (1,0), (2,2), (3,7)]

Then to evaluate this polynomial, for instance at x = -1, use:

    *Main> eval newton (-1)


Finally, to quit the session, write

    *Main> :q
