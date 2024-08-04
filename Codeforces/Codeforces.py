##datos una persona
#38.946474 Latitud
#-77.437568 Longitud
##datos de la otra persona
#39.918620 latitud
# 116.443983 longitud
import math
radio=6371
#hace falta la peticion de datos

def formula_incognitas(longitud,latitud):
    x=radio*math.cos(latitud)*math.cos(longitud)
    y=radio*math.cos(latitud)*math.sin(longitud)
    z=radio*math.sin(latitud)
    return x,y,z

x1,y1,z1=formula_incognitas(38.946474,-77.437568)
x2,y2,z2=formula_incognitas(39.918620,116.443983)



def formula_distancia():
    distancia=math.sqrt((x2-x1)**2+(y2-y1)**2+(z2-z1)**2)
    return distancia
print(formula_distancia())




