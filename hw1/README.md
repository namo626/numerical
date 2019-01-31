Author: Chayanon Wichitrnithed
Operating System: Arch Linux 4.19.14-1-lts
Language Used: Haskell
Compiler: ghc 8.6.3


Running the code
=====================

Once the Glasgow Haskell Compiler (GHC) has been installed, load the file into the
REPL in the command line:

    $ ghci Conversion.hs

Once inside the interactive session, use the conversion functions "beta2Dec" and "dec2Bin".
For example, to convert 11.1 in binary to decimal, write the integer and fractional part as lists:

    *Main> beta2Dec 2 ([1,1], [1])
    3.5

To convert 6.25 from decimal to binary, write

    *Main> dec2Bin 6.25
    ([1,1,0], Finite [0,1])

and we see that 6.25 is 110.01 (having non-repeating decimals) in binary.


Finally, to quit the session, write

    *Main> :q
