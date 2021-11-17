from __future__ import annotations

import operator
from typing import Optional, Callable, Generator

import functools

RealFunction = Callable[[float], float]


class Interval(tuple):
    @property
    def upper(self) -> Optional[float]:
        return max(*self)

    @property
    def lower(self) -> Optional[float]:
        return min(*self)

    @property
    def midpoint(self) -> Optional[float]:
        return {
            (False, False): (self.upper - self.lower)/2 + self.lower,
            (True, True): 0
        }.get(
            (self.upper is None, self.lower is None),
            None
        )

    def __contains__(self, item: float) -> bool:
        return self.lower < item < self.upper

    def __float__(self) -> float:
        return float(self.upper - self.lower)

    @classmethod
    def from_min_and_delta(cls, minimum: float, delta: float) -> Interval:
        return cls((minimum, minimum + delta))


class Rectangle:
    def __init__(self, interval: Interval, height: float):
        self._interval = interval
        self._height = height

    @property
    def area(self) -> float:
        return float(float(self._interval) * self._height)

    @property
    def midpoint(self) -> float:
        return self._interval.midpoint

    def __repr__(self):
        return f"Interval: {self._interval}, Height: {self._height}"

    def __float__(self) -> float:
        return self.area

    def __add__(self, other) -> float:
        return float(self) + float(other)


class NumericIntegral:
    def __init__(self, interval: Interval, curve: RealFunction, delta_x: float):
        self._interval = interval
        self._curve = curve
        self._delta_x = delta_x if delta_x < len(interval) else len(interval)

    @property
    def domain_decomposition(self) -> Generator[Interval]:
        current_max = self._interval.lower
        while current_max < self._interval.upper:
            yield Interval.from_min_and_delta(current_max, self._delta_x)
            current_max = min(current_max + self._delta_x, self._interval.upper)

    @property
    def rectangles(self) -> Generator[Rectangle]:
        for i, interval in enumerate(self.domain_decomposition):
            height = self._curve(interval.midpoint)
            yield Rectangle(interval, height)

    def __float__(self) -> float:
        return float(functools.reduce(operator.add, (float(rect) for rect in self.rectangles)))
