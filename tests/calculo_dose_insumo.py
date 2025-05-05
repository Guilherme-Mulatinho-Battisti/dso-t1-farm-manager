from insumo import Semente, Fertilizante, Defensivo
from cultura import Cultura
from calculo_dose import CalculoDose

# Sementes
sem1 = Semente(nome='Certificada RR', valor=100, cultura='Soja', tecnologia='Não Transgenica')
sem2 = Semente(nome='VT Pro 2', valor=120, cultura='Milho', tecnologia='Transgenica')

# Fertilizantes
fert1 = Fertilizante(nome='NPK', valor=1000, fonte='Quimico')
fert2 = Fertilizante(nome='composto_organico', valor=400, fonte='Organico')

# Defensivos
def1 = Defensivo(nome='Abamex', valor=500, funcao='Herbicida')
def2 = Defensivo(nome='Star', valor=700, funcao='Inseticida')
def3 = Defensivo(nome='Engeo', valor=600, funcao='Fungicida')
def4 = Defensivo(nome='Deca', valor=600, funcao='Acaricida')

# Cultura
cultura1 = Cultura(nome='Milho', quant_semente=2, dose_fertilizante=30, dose_defensivo=50, temp_crescimento=10, num_aplicacao=2)
cultura2 = Cultura(nome='Soja', quant_semente=0.8, dose_fertilizante=40, dose_defensivo=30, temp_crescimento=8, num_aplicacao=1)

# Calculo de dose

plant1 = CalculoDose(insumo=fert1, cultura=cultura1, area=1000)

print(plant1.calcular_dose_fert())
print(plant1.calcular_dose_defe())
print(plant1.calcular_dose_semente())
