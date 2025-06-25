class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        l=[]
        Kelvin = celsius + 273.15
        Fahrenheit = celsius * 1.80 + 32.00
        l.append(Kelvin)
        l.append(Fahrenheit)
        return l

