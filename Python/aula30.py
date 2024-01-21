"""
Constante = "Variables" que no mudan
Muchas de las condiciones en if (malos)
    <- Conteo de complejidad (malo)
ES RECOMENDADO DEJAR EN MAYUSCULAS LAS VARIABLES CONSTANTES
PARA DEJAR EN CLARO QUE NO ES NECESARIO MUDAR
    
"""

velocidad = 61 # velocidad actual del auto
local_carro = 101 # local en que el auto esta en la carretera

RADAR_1 = 60 # velocidad maxima del radar 1
LOCAL_1 = 100 # local donde el radar 1 esta
RADAR_RANGE = 1 # distancia de lectura de radar

velocidad_auto_passo_radar_1 = velocidad > RADAR_1
auto_multado_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE)


if velocidad_auto_passo_radar_1:
    print('Velocidad del auto paso del radar1')

if  auto_multado_radar_1 and velocidad_auto_passo_radar_1:
    print('auto multado por el radar 1')