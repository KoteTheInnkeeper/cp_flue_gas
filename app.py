from lib.coefficients import Coefficients

lignite_coal = ["Lignite coal", [51.12, 3.89, 14.65, 0.61, 1.87, 14.36, 13.5]]
natural_gas = ["Natural gas", [19.7454, 77.2545, 2, 1, 0, 0, 0]]
fuel_oil = ["Fuel Oil", [87.26, 10.49, 0.64, 0.58, 0.84, 0, 0.04]]

lignite_coefficients = Coefficients(lignite_coal, 1000, 1)
natural_coefficients = Coefficients(natural_gas, 1000, 1)
fuel_oil_coefficients = Coefficients(fuel_oil, 1000, 1)

cp_lignite = lignite_coefficients.get_cp_flue_gas()
cp_natural = natural_coefficients.get_cp_flue_gas()
cp_fuel_oil = fuel_oil_coefficients.get_cp_flue_gas()


print(f"Specific heat of {lignite_coefficients.combustible.name.title()} flue gas: {cp_lignite} kJ/kgK")
print(f"Specific heat of {natural_coefficients.combustible.name.title()} flue gas: {cp_natural} kJ/kgK")
print(f"Specific heat of {fuel_oil_coefficients.combustible.name.title()} flue gas: {cp_fuel_oil} kJ/kgK")
