import math

def half_life(decayRate):
    k = decayRate / 100  # Conversion from % to decimal
    return math.log(0.5) / -k

decayRate = 0.12
halfLifeYears = half_life(decayRate)

print(f"The half-life of carbon-14 is {halfLifeYears:.2f} years.")