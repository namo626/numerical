import Data.List

newton :: (Double -> Double) -- function whose root we want to find
       -> (Double -> Double) -- derivative of the above function
       -> Double             -- initial point
       -> [Double]             -- resulting point

newton f f' x0 = x0 : newton f f' x1
  where
    v0 = f x0
    x1 = x0 - v0 / (f' x0)

-- selectNewton ::  Double -> Double -> [(Double, Double)] -> [(Double, Double)]
-- selectNewton delta epsilon xs =
--   map (\(a,b,c) -> (a,b)) $ takeWhile (\(x, v, d) -> (d >= delta)) xs'

--   where
--     xs' = zipWith (\(x1,v1) (x0,v0) -> (x0,v0, abs (x1-x0))) (tail xs) xs

display :: (Double -> [Double]) -> Int -> Double -> IO ()
display ns amount x0 = mapM_ print$ take amount $ ns x0


sampleA = newton funcA funcA'
sampleB = newton funcB funcB'

func' :: Double -> Double
func' x = exp x - 1/(1+x^2)

funcA, funcA', funcB, funcB' :: Double -> Double
funcA x = exp x - 3*x^2
funcA' x = exp x - 6*x

funcB x = x - 1 - 0.3*cos x
funcB' x = 1 + 0.3*sin x


bisection :: (Double -> Double) -> Double -> Double -> [(Double, Double, Double, Double)]
bisection f a b
  | fm * fa <= 0 = (a, b, m, fm) : bisection f a m
  | otherwise = (a, b, m, fm) : bisection f m b
  where
    fa = f a
    fm = f m
    m = 0.5 * (a + b)

p :: Double -> Double
p x = 2*x^3 - 3*x - 4
