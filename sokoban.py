class Sokoban:
  """
  0_personaje
  1_espacio
  2_caja
  3_pared
  4_metas
  5-persoaje_meta
  6_caja_meta
  """
  
  mapa=[
    [3,3,3,3,3],
    [3,1,1,1,1,3],
    [3,1,1,0,1,3],
    [3,1,1,1,1,3],
    [3,3,3,3,3,3],
  ]

juego=Sokoban()
print(juego.mapa)
personaje_fila= 3 #fila en la que se encuentrael personaje
personaje_columna= 9 #columna en la que se encuentra el persoaje 
#variable que hubica la posicion del personaje en el mapa
def imprimirMapa(self):#imprime el mapa
for fila in self.mapa: #recorde la fila por el mapa