from typing import List
from lib.functions import Approximations as ap
from lib.combustibles import Combustible


class Coefficients:
    """
    A class that holds, given a combustible, it's important constants to determine the specific heat of flue gas.
    """
    def __init__(self, combustible_info: List, T: float, n: float) -> None:
        self.combustible = Combustible(combustible_info[0], combustible_info[1])
        self.t_gh = T
        self.a_cp = 1
        self.n = n
        self.air = self.combustible.air_steo * self.n
        self.flue_gas = self.air + (1 - self.combustible.Kash)

    @property
    def cp_CO2(self):
        return round(ap.cp_CO2(self.t_gh), 4)

    @property
    def a_m(self):
        a_m = float(3.667 * self.combustible.KC / self.combustible.tot_steo)
        return round(a_m, 4)

    @property
    def a_C(self):
        return round(self.a_m / self.a_cp, 4)

    @property
    def b_m(self):
        b_m = float((0.767 * self.combustible.air_steo + self.combustible.KN) / self.combustible.tot_steo)
        return round(b_m, 4)

    @property
    def b_cp(self):
        return round(ap.b_cp(self.t_gh), 4)

    @property
    def b_N(self):
        return round(self.b_m / self.b_cp, 4)

    @property
    def c_cp(self):
        return ap.c_cp(self.t_gh)

    @property
    def c_m(self):
        c_m = (8.938 * self.combustible.KH + self.combustible.KM) / self.combustible.tot_steo
        return c_m

    @property
    def c_H(self):
        return round(self.c_m / self.c_cp, 4)

    @property
    def d_m(self):
        d_m = 2 * self.combustible.KS / self.combustible.tot_steo
        return round(d_m, 4)

    @property
    def d_cp(self):
        d_cp = ap.d_cp(self.t_gh)
        return round(d_cp, 4)

    @property
    def d_S(self):
        return round(self.d_m / self.d_cp, 4)

    @property
    def f_m(self):
        return round(self.combustible.air_steo * (self.n - 1) / self.flue_gas, 4)

    @property
    def cp_A(self):
        return round(ap.c_pa(self.t_gh), 4)

    @property
    def f_A(self):
        return round(self.f_m * self.cp_A)

    def __str__(self):
        return f"""cp_CO2 = {self.cp_CO2}
a_N = {self.a_C}
b_N = {self.b_N}
c_H = {self.c_H}
d_S = {self.d_S}

m_tot_steo = {self.combustible.tot_steo}
m_flue_Gas = {self.flue_gas}

f_A = {self.f_A}
"""

    def get_cp_flue_gas(self):
        cp_gh = self.cp_CO2/(self.a_C + self.b_N + self.c_H + self.d_S) * self.combustible.tot_steo / self.flue_gas + self.f_A
        return round(cp_gh, 4)

