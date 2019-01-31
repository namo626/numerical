import Data.List


------------------------------------------------------------------------------------------------
{- BETA TO DECIMAL CONVERSION -}

-- convert a beta-base number (given in terms of integer and fractional parts) to decimal
beta2Dec :: Int -> ([Int], [Int]) -> Double
beta2Dec beta (intPart, fracPart) = (fromIntegral $ foldl' f 0 intPart) + foldr g 0 (0:fracPart)
  where
    f b a | a > (beta-1) = error "Digit exceeds base"
          | otherwise = a + beta*b

    g a b | a > (beta-1) = error "Digit exceeds base"
          | otherwise = a' + (1.0/beta')*b
          where a' = fromIntegral a
                beta' = fromIntegral beta



------------------------------------------------------------------------------------------------
{- DECIMAL TO BINARY CONVERSION AND SOME AUXILIARY FUNCTIONS -}

-- convert a positiver INTEGER to its beta-base representation
int2Beta :: Int -> Int -> [Int]
int2Beta _    0 = [0]
int2Beta beta n = iter n []
  where iter m rems
          | m == 0    = rems
          | otherwise = iter quotient (remainder:rems)
          where (quotient, remainder) = quotRem m beta


-- the fractional part of a floating point binary can be finite or repeating
data FracBinary = Finite [Int]
                | Repeating [Int]
                deriving Show

-- convert a positive decimal to a binary (expressed as integer and fractional part)
dec2Bin :: Double -> ([Int], FracBinary)
dec2Bin 0 = ([0], Finite [0])
dec2Bin x = (int2Beta 2 int, frac2Bin frac)
  where
    (int, frac) = splitDec x


-- auxiliary function; convert a decimal with only fractional part to a binary (also with only fractional part)
frac2Bin :: Double -> FracBinary
frac2Bin y = iter y [] []
  where
    iter z result seen
      | eqFloat z 0       = Finite (reverse result)
      | isElem seen (z*2) = Repeating (reverse result)
      | otherwise         = iter fracPart (intPart:result) ((z*2):seen)
      where
        (intPart, fracPart) = splitDec (z*2)


-- split a number into integer part and fractional part
splitDec :: Double -> (Int, Double)
splitDec x = (floor x, x - fromIntegral (floor x))

-- compare floating point numbers
eqFloat :: Double -> Double -> Bool
eqFloat x y = abs (x-y) < 0.00001

-- is the number in the given list?
isElem :: [Double] -> Double -> Bool
isElem ls x = any (eqFloat x) ls
