import math
from src.calculus import Interval, Curve
from src.periodic_functions import Period, PeriodicCurve


def integral_sanity_check():
    interval = Interval((0, 2 * math.pi))
    precision = lambda denominator: float(interval) / denominator
    denominators = (1.5 ** n for n in range(1, 20))
    integrals = [
        Curve(math.sin).integrate(interval, precision=precision(denominator)) for denominator in denominators
    ]
    return integrals


def indefinite_integral_sanity_check():
    integral_curve = Curve(lambda x: math.cos(x)).integral_curve(1 / 100)

    deltas = [(f"{n}*π/2", integral_curve(n * math.pi / 2), math.sin(n * math.pi / 2)) for n in (1, 2, 3, 4)]

    return deltas


def differential_sanity_check():
    denominator = 1000
    num_samples = 4
    x_points = [i / num_samples for i in range(1, num_samples + 1)]
    curve = Curve(lambda x: (x ** 3) / 3)
    gradient_curve = curve.differentiate(1 / denominator)

    gradients = [(x ** 2, gradient_curve(x)) for x in x_points]

    return gradients


def fundamental_theorem_sanity_check():
    denominator = 100
    num_samples = 4
    x_points = [i / num_samples for i in range(1, num_samples + 1)]
    curve = Curve(lambda x: (x ** 3) / 3)
    gradient_curve = curve.differentiate(1 / denominator)
    approx_curve = gradient_curve.integral_curve(1 / denominator)

    gradients = [(curve(x), gradient_curve(x), approx_curve(x)) for x in x_points]

    return gradients


def get_periodic():
    period = Period((0.5, 1.5))
    curve = PeriodicCurve(lambda x: x**2, period)

    return curve


def vertical_curve_printer(curve: Curve, domain: Interval, sample_count: int = 20):
    samples = [(n * float(domain)) / sample_count + domain.lower for n in range(sample_count)]
    max_width = 50
    scale_factor = max_width / max(*samples)
    for x in samples:
        position = round(scale_factor * curve.at(x))
        line = [
            f"{x}".rjust(20),
            ("|" if position > 0 else ""),
            " " * max(position - 2, 0),
            "⊗"
        ]
        print("".join(line))


def main():
    return fundamental_theorem_sanity_check()



if __name__ == '__main__':
    # _integrals = main()
    # for _integral in _integrals:
    #     print(_integral)
    vertical_curve_printer(get_periodic(), Interval((0, 3)), 50)
