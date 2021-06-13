class Combustible:
    def __init__(self, name: str, properties: list) -> None:
        self.name = name.upper()
        self.KC, self.KH , self.KO, self.KN, self.KS, self.KM, self.Kash = [round(Ki / 100, 4) for Ki in properties]
    
    def __str__(self):
        print(f"{self.name.title()} has the following chemical composition in %")
        return f"""
    Carbon.............{round(self.KC * 100, 2)}%
    Hydrogen...........{round(self.KH * 100, 2)}%
    Oxygen.............{round(self.KO * 100, 2)}%
    Nitrogen...........{round(self.KN * 100, 2)}%
    Sulphur............{round(self.KS * 100, 2)}%
    Moisture...........{round(self.KM * 100, 2)}%
    Ashes..............{round(self.Kash * 100, 2)}%
    
It requires {self.air_steo} kg air/kg fuel."""

    @property
    def air_steo(self) -> float:
        return round((2.9978 * self.KH - 0.3747 * self.KO + 0.3747 * self.KS + self.KC) * 11.445, 4)
    
    @property
    def tot_steo(self) -> float:
        return round((self.air_steo + 1 - self.Kash), 7)
    


