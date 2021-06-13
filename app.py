from lib.coefficients import Coefficients
from utils.menu import main_menu


while True:
    combustible = main_menu()
    if combustible:
        coefficients = Coefficients(*combustible)
        print(f"Mean specific heat of {coefficients.combustible.name.title()} at {coefficients.t_gh + 273.15}°C is:\n"
          f"{coefficients.get_cp_flue_gas()} kJ/kgK.")



