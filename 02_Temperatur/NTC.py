from machine import ADC
import math

class NTC:
    # A, B, C is the Steinhart-Hart coefficients for the Thermistor (specific for the thermistor)
    # Vref = is the voltage given the voltage divider
    # Rref = is the value of the resistor in the voltage divider
    def __init__(self, pin, A = 1.624e-3, B = 1.235e-4, C = 9.124e-7, Vref = 3.3, Rref = 10e3):
        self.A = A
        self.B = B
        self.C = C
        self.ADC = ADC(pin)
        self.Vref = Vref
        self.Rref = Rref

    # Returns the current temperature from the configured pin
    def readT(self):
        # Read voltage over Rtemp from AD-converter
        adc0 = self.ADC.read_u16()
        # Convert uint16 -> value between 0 and Vref
        Vout = (self.Vref/65535)*adc0
        
        # Calculate Resistance of Thermistor on Pin
        Rt = (Vout * self.Rref) / (self.Vref - Vout)
        
        # Use Steinhart–Hart equation to calculate Termperature
        # https://en.wikipedia.org/wiki/Steinhart%E2%80%93Hart_equation
        TempK = 1 / (self.A + (self.B * math.log(Rt)) + self.C * math.pow(math.log(Rt), 3))
        
        # Convert Temperature in Kelvin to Temperature in Celsius
        TempC = TempK - 273.15
    
        return TempC
