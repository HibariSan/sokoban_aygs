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