from typing import Union, List, Tuple
from lib.functions import Approximations
from utils.combustibles import Combustible

class Coefficients:
    def __init__(self, combustible_info: List[str, Tuple], T: float) -> None:
        self.combustible = Combustible(**combustible_info)
        self.t_gh = T
        return None
    
    @property
    def b_m(self):
        b_m = round(float((0.767 * self.combustible.get_air_steo() + self.combustible.KN) / self.combustible.tot_steo), 4)
        return b_m

    @property
    def b_N(self):
        return round(float())