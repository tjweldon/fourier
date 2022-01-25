from src.calculus import Curve, RealFunction, Interval


class Period(Interval):
    def characteristic_equivalent(self, x: float) -> float:
        return (x - self.lower) % float(self) + self.lower


class PeriodicCurve(Curve):
    def __init__(self, function: RealFunction, period: Interval):
        super().__init__(function)
        self._period = Period(period)

    def at(self, x: float) -> float:
        return super().at(self._period.characteristic_equivalent(x))