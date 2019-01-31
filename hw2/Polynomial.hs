import Data.List

-- (xi, f(xi))
type Point = (Double, Double)

sample :: [Point]
sample = [(2,6), (3,3), (8,12), (10,15)]

-- divided difference
divDif :: [Point] -> Double
divDif []       = error "No data points"
divDif [(x, y)] = y
divDif zs       = (1/diff) * (forward - backward)
  where
    forward  = divDif $ tail zs
    backward = divDif $ init zs
    diff     = (fst $ last zs) - (fst $ head zs)

divDifSeq :: [Point] -> [Double]
divDifSeq = map divDif . tail . inits

interp :: [Point] -> [Double] -> Double -> Double
interp [] _ _  = 0
interp _ [] _  = 0
interp ps ds x = iter ds (init $ map fst ps)
  where
    iter [d'] [] = d'
    iter (d':ds') (p':ps') = d' + (x-p') * (iter ds' ps')
