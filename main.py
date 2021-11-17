import math
from src.integration import NumericIntegral, Interval


def main():
    def curve(x: float) -> float: return math.sin(x)

    interval = Interval((0, 2*math.pi))
    integrals = [NumericIntegral(interval, curve, 1/denominator) for denominator in range(1, 10000, 100)]

    return integrals


if __name__ == '__main__':
    _integrals = main()
    for _integral in _integrals:
        print(float(_integral))

