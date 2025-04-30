class CalculoDose:

    def __init__(self, insumo:, cultura, area):
        self.insumo = insumo
        self.cultura = cultura
        self.area = area

# TODO calculo dosse generico

    def calcular_dose_fert(self):
        if self.insumo.fonte == 'Quimico':
            return float((self.insumo.valor * self.cultura.dose_fertilizante) * 0.7) # Reais por dose
        else:
            return self.insumo.valor * self.cultura.dose_fertilizante  # Reais por dose

    def calcular_dose_defe(self):
        
        return float(self.insumo.valor * self.cultura.dose_defensivo)  # Reais por dose

    def calcular_dose_semente(self):
        return float(self.insumo.valor * self.cultura.quant_semente)
