import math as m


class Approximations:
    @classmethod
    def cp_CO2(cls, T:float) -> float:
        return round(float(0.1874 * (1.000061**T) * T ** 0.2665), 4)

    @classmethod
    def c_cp(cls, T: float) -> float:
        return round(float(0.5657 - 0.00000668 * T - 10465 / (T**2)), 4)
    
    @classmethod
    def c_pa(cls, T: float) -> float:
        return round(float(0.7124 * 1.00011**T * T**0.051), 4)

    @classmethod
    def d_cp(cls, T: float) -> float:
        return round(float(m.exp(2.679 - 151.16 / T - 0.289 * m.log(T, m.exp(1)))), 4)
    
    @classmethod
    def b_cp(cls, T: float) -> float:
        return round(float(0.9094 + 0.000169 * T - 11135 / (T**2)), 4)
