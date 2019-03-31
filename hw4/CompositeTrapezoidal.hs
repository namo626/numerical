import Data.List (foldl')

integrate :: (Double -> Double) -> Double -> Double -> Int -> Double
integrate f a b n = h*(sum' xs) + (h/2)*(f a + f b)
  where
    h = (b-a) / fromIntegral n
    xs = tail $ take (n) $ map f xs'
    xs' = a : map (+h) xs'


sum' = foldl' (+) 0

funcA :: Double -> Double
funcA x = exp (-x^2)

funcB :: Double -> Double
funcB x = 1 / (2 + cos x)
