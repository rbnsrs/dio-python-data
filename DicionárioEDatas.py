############################## Dicionarios ##############################
# Dicionário é um conjunto não ordenado de paras chave valor.

############################### Datas ###############################

from datetime import date, datetime, timedelta

data = date(2023, 7, 10)
print(data)

print(date.today())
data_hora = datetime(2023, 7, 10)
print(data_hora)
print("$$$$$$$$$$$$")
print(datetime.today())

################### Time Delta ###################
tipo_carro = 'G' # P M G
tempo_pequeno = 30
tempo_medio = 34
tempo_grande = 60

data_atual = datetime.now()  # Traz o objeto com timezone correto.

if tipo_carro == 'P':
    data_estimada = data_atual + timedelta(minutes=tempo_pequeno)
    print(f'O carro chegou: {data_atual} e ficará pronto às {data_estimada}')
elif tipo_carro == 'M':
    data_estimada = data_atual + timedelta(minutes=tempo_medio)
    print(f'O carro chegou: {data_atual} e ficará pronto às {data_estimada}')
else:
    data_estimada = data_atual + timedelta(minutes=tempo_grande)
    print(f'O carro chegou: {data_atual} e ficará pronto às {data_estimada}')

###################################################################
print("##############################################")
print(date.today() - timedelta(days=1))
resultado = datetime(2023, 7, 25, 10, 19, 20) - timedelta(hours=1)
print(resultado.time())

print(datetime.now().date)

############################ #Formatando data e horas #######################################
# Para realizar essa formação importamos a biblioteca datetime; importação realizada no início do texto.


data_hora_atual = datetime.now()
date_hora_str = "2024-07-03 10:20"

mascara_ptbr = "%d/%m/%Y %H:%M"
mascara_en = "%Y-%m-%d %H:%M"


print(data_hora_atual.strftime(mascara_ptbr))

data_convertida = datetime.strptime(date_hora_str, mascara_en)
print(data_convertida)
print(type(data_convertida))

######################### Time Zone #################################
from datetime import datetime, timezone
import pytz

d = datetime.now(pytz.timezone('Europe/Oslo'))
d2 = datetime.now(pytz.timezone('America/Sao_Paulo'))
print(d)
print(d2)

######################### Time Zone - Sem Pytz #################################

data_oslo = datetime.now(timezone(timedelta(hours=2)))
data_sp = datetime.now(timezone(timedelta(hours=-3)))
print(data_oslo)
print(data_sp)