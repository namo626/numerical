module Lib where

import Data.List

beta2Dec :: Int -> ([Int], [Int]) -> Double
beta2Dec beta (intPart, fracPart) = (fromIntegral $ foldl' f 0 intPart) + foldr g 0 (0:fracPart)
  where
    f b a | a > (beta-1) = error "Digit exceeds base"
          | otherwise = a + beta*b

    g a b | a > (beta-1) = error "Digit exceeds base"
          | otherwise = a' + (1.0/beta')*b
          where a' = fromIntegral a
                beta' = fromIntegral beta

bin2Dec :: ([Int], [Int]) -> Double
bin2Dec = beta2Dec 2

dec2Beta :: Int -> Int -> [Int]
dec2Beta _    0 = [0]
dec2Beta beta n = iter n []
  where iter m rems
          | m == 0    = rems
          | otherwise = iter quotient (remainder:rems)
          where (quotient, remainder) = quotRem m beta

dec2Bin :: Double -> ([Int], [Int])
dec2Bin 0 = ([0], [0])
dec2Bin x = (dec2Beta 2 int, frac2Bin frac)
  where
    (int, frac) = splitDec x

frac2Bin :: Double -> [Int]
frac2Bin y
  | y < tolerance = []
  | otherwise     = intPart : frac2Bin fracPart
  where
    (intPart, fracPart) = splitDec (y * 2)
    tolerance           = 0.0000001

splitDec :: Double -> (Int, Double)
splitDec x = (floor x, x - fromIntegral (floor x))
