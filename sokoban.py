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
  
    mapa=[]
    

    personaje_fila= 2
    personaje_columna= 1
    
    def leerMapa(self):
        self.mapa=[
        [3,3,3,3,3,3],
        [3,1,1,1,1,3],
        [3,0,1,4,1,3],
        [3,1,1,1,1,3],
        [3,3,3,3,3,3],
    ]


        
    def imprimirMapa(self):
        for fila in self.mapa:
            print(fila)
            
    def moverDerecha(self):
        print("Mover Derecha")
          # 0 personaje.espacio
        if (self.mapa[self.personaje_fila][self.personaje_columna]== 0 and self.mapa[self.personaje_fila][self.personaje_columna + 1]== 1):
            self.mapa[self.personaje_fila][self.personaje_columna]= 1
            self.mapa[self.personaje_fila][self.personaje_columna + 1]= 0
            self.personaje_columna += 1
            print("# personaje.espacio derecha")
    # 1. personaje, meta
        elif (self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 4):
            self.mapa[self.personaje_fila][self.personaje_columna] = 1
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 5
            self.personaje_columna += 1 
            print("personaje,meta derecha") #actuliza el movimiento del personaje
    #
    def moverIzquierda(self):
        print("Mover izquierda")
    
    def moverArriba(self):
        print("Mover arriba")
    
    def moverAbajo(self):
        print("Mover abajo")
    
    def jugar(self):
        instrucciones="a-izquierda\nd-derecha\nw-arriba\ns-abajo"
        print(instrucciones)
        self.leerMapa()
        while True:
            self.imprimirMapa()
            movimiento = input("Mover Hacia: ")
            if movimiento == "d":
                self.moverDerecha()
            elif movimiento == "a":
                self.moverIzquierda()
            elif movimiento == "w":
                self.moverArriba()
            elif movimiento == "s":
                self.moverAbajo()
            elif movimiento == "q":
              print("salir del juego")
              break
                
juego = Sokoban()
juego.jugar()
