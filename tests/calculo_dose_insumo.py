from model.insumo import Semente, Fertilizante, Defensivo, Implemento
from model.cultura import Cultura


# Sementes
sem1 = Semente(nome='Certificada RR', id=101, valor=100, cultura='Soja', tecnologia='Não Transgenica')
sem2 = Semente(nome='VT Pro 2', id=102, valor=120, cultura='Milho', tecnologia='Transgenica')

# Fertilizantes
fert1 = Fertilizante(nome='NPK', id=201, valor=1000, fonte='Quimico')
fert2 = Fertilizante(nome='composto_organico', id=202,  valor=400, fonte='Organico')

# Defensivos
def1 = Defensivo(nome='Abamex', id=301, valor=500, funcao='Herbicida')
def2 = Defensivo(nome='Star', id=302, valor=700, funcao='Inseticida')
def3 = Defensivo(nome='Engeo', id=303, valor=600, funcao='Fungicida')
def4 = Defensivo(nome='Deca', id=304, valor=600, funcao='Acaricida')

# Implementos
impl1 = Implemento(nome='Arado', id=401, valor=1500, tipo='Mecanico')
impl2 = Implemento(nome='Grade', id=402, valor=1200, tipo='Manual')

# Cultura
cultura1 = Cultura(nome='Milho', id=1, dose_semente=2, dose_fertilizante=30, dose_defensivo=50, temp_crescimento=10, num_aplicacao=2)
cultura2 = Cultura(nome='Soja', id=2, dose_semente=0.8, dose_fertilizante=40, dose_defensivo=30, temp_crescimento=8, num_aplicacao=1)

