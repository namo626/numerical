import Data.List

-- We have a list of pairs of points to interpolate: (x1,y1), (x2,y2), ...
-- we can create a newton polynomial from those points, store it, and use it
-- to evaluate at any x
type Point = (Double, Double)

sample :: [Point]
sample = [(2,6), (3,3), (8,12), (10,15)]

-- problem [6]
hw :: [Point]
hw = zip [-1, 0, 1, 2, 3] [5, 1, 0, 2, 7]

-- problem [7]
function :: Double -> Double
function x = 1 / (1 + x^2)

p2 :: Polynomial
p2 = mkNewton $ zip [-2, 0, 2] [1/5, 1, 1/5]

p4 :: Polynomial
p4 = mkNewton $ zip xs (map function xs)
  where xs = [-2,-1,0,1,2]


-- representation for newton polynomial
data Polynomial = Polynomial
  { coeffs     :: [Double]   -- list of divided differences
  , dataPoints :: [Point]  -- list of given data points
  }

mkNewton :: [Point] -> Polynomial
mkNewton ps = Polynomial
  { coeffs     = divDifSeq ps
  , dataPoints = ps
  }

eval :: Polynomial -> Double -> Double
eval pl = interp (dataPoints pl) (coeffs pl)

-------------------------------------------------------------

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
