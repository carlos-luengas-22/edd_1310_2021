from backtracking import LaberintoADt
import time

pasillos_inicial = ((2,1),(2,2),(2,3),(2,4),(3,2),(4,2))
lab = LaberintoADt( 6 , 6 pasillos_inicial, (5,2) , (2,5))
lab.buscar_entrada()

lab.to_string()
#Imprimimos Pila
lab.imprimir_camino()

while not lab.es_salida(laberinto.get_pos_actual()[0] , laberinto.get_pos_actual()[1]):
    print("probar")
    lab.resolver_laberito()
    lab.imprimir_camino()
    time.sleep(1.0)
