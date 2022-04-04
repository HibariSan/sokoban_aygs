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
personaje_fila= 0
personaje_columna= 0
def imprimirMapa(self):
  for fila in self.mapa:
    print(fila)
def moverDerecha(self):
  print("Mover Derecha")
  # 5. personaje, espacio
  if (sel.mapa[sel.persoaje_fila][self.persoaje_columna] == self.persoaje
and self.mapa[self.personaje_fila][self.persoaje_columna + 1] ==self.espacio):


    self