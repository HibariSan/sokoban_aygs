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
    personaje_columna= 4
    
    def leerMapa(self):
        self.mapa=[
        [3,3,3,3,3,3],
        [3,1,1,1,1,3],
        [3,4,2,4,0,1,3],
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
            self.personaje_columna += 1 #actuliza el movimiento del personaje
            print("personaje,meta derecha") 
    # 2. personaje,caja,espacio
        elif(self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 2 and self.mapa[self.personaje_fila][self.personaje_columna + 2] == 1):
            self.mapa[self.personaje_fila][self.personaje_columna] = 1
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 0
            self.mapa[self.personaje_fila][self.personaje_columna + 2] = 2
            self.personaje_columna += 1
            print("personaje,caja,espacio derecha")
    # 3. personaje,caja,meta
        elif(self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 2 and self.mapa[self.personaje_fila][self.personaje_columna + 2] == 4):
            self.mapa[self.personaje_fila][self.personaje_columna] = 1
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 0
            self.mapa[self.personaje_fila][self.personaje_columna + 2] = 6
            self.personaje_columna += 1
            print("personaje,caja,espacio derecha")
    # 4. personaje,caja_meta,espacio
        elif(self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 6 and self.mapa[self.personaje_fila][self.personaje_columna + 2] == 1):
            self.mapa[self.personaje_fila][self.personaje_columna] = 1
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 5
            self.mapa[self.personaje_fila][self.personaje_columna + 2] = 2
            self.personaje_columna += 1
            print("personaje,caja_meta,espacio derecha")
    # 5. personaje,caja_meta,meta
        elif(self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 0 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 4):
            self.mapa[self.personaje_fila][self.personaje_columna] = 1
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 6 
            self.mapa[self.personaje_fila][self.persoanje_columna + 2] = 5
            self.personaje_columna += 1
            print("personaje,caja_meta,meta derecha")
    # 6. personaje_meta,espacio
        elif(self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 2 and self.mapa[self.personaje_fila][self.personaje_columna + 2] == 1):
            self.mapa[self.personaje_fila][self.personaje_columna] = 5
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 1
            self.mapa[self.personaje_fila][self.persoanje_columna + 2] = 4
            self.personaje_columna += 1
            print("personaje_meta,espacio derecha")
    # 7. personaje_meta,meta
        elif(self.mapa[self.personaje_fila][self.personaje_columna] == 0 and  self.mapa[self.personaje_fila][self.personaje_columna + 1] == 2 and self.mapa[self.personaje_fila][self.personaje_columna + 2] == 1):
            self.mapa[self.personaje_fila][self.personaje_columna] = 5
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 4
            self.mapa[self.personaje_fila][self.personaje_columna + 2] = 4
            self.personaje_columna += 1
            print("personaje_meta,espacio derecha")
    # 8. personaje_meta,caja,espacio
        elif(self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 2 and self.mapa[self.personaje_fila][self.personaje_columna + 2] == 1):
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 0
            self.mapa[self.personaje_fila][self.personaje_columna + 2] = 2
            self.personaje_columna += 1
            print("personaje_meta,caja,espacio derecha")
    # 9. personaje_meta,caja,meta
        elif(self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 2 and self.mapa[self.personaje_fila][self.personaje_columna + 2] == 4):
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 0
            self.mapa[self.personaje_fila][self.personaje_columna + 2] = 6
            self.personaje_columna += 1
            print("personaje_meta,caja,meta derecha")
    # 10. personaje_meta,caja_meta,espacio 
        elif(self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 6 and self.mapa[self.personaje_fila][self.personaje_columna + 2] == 1):
            self.mapa[self.personaje_fila][self.personaje_columna] = 6
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 1
            self.mapa[self.personaje_fila][self.personaje_columna + 2] = 5
            self.personaje_columna += 1
            print("personaje_meta,caja_meta,espacio derecha")
    # 11. personaje_meta,caja_meta,meta
        elif(self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 6 and self.mapa[self.personaje_fila][self.personaje_columna + 2] == 4):
            self.mapa[self.personaje_fila][self.personaje_columna] = 6
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 4
            self.mapa[self.personaje_fila][self.personaje_columna + 2] = 5
            self.personaje_columna += 1
            print("personaje_meta,caja_meta,meta derecha")
            
    def moverIzquierda(self):
        print("Mover izquierda")
    # 12. persona,espacio
        if (self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 1):
            self.mapa[self.personaje_fila][self.personaje_columna] = 1
            self.mapa[self.personaje_fila][self.personaje_columna - 1] = 0
            self.personaje_columna -= 1 #actuliza el movimiento del personaje
            print("personaje,meta izquierda")
    # 13. personaje,meta
        elif(self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 4): 
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            self.mapa[self.personaje_fila][self.personaje_columna - 1] = 0
            self.personaje_columna -= 1
            print("personjae,meta izquierda")
    # 14. personaje,caja,espacio
        elif(self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 2 and self.mapa[self.personaje_fila][self.personaje_columna - 2] == 1):
            self.mapa[self.personaje_fila][self.personaje_columna] = 1
            self.mapa[self.personaje_fila][self.personaje_columna] = 0
            self.mapa[self.personaje_fila][self.personaje_columna] = 2
            self.personaje_columna -= 1
            print("personaje,caja,espacio izquierda")
    # 15. personaje,caja,meta
        elif(self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 2 and self.mapa[self.personaje_fila][self.personaje_columna - 2] == 4):
            self.mapa[self.personaje_fila][self.personaje_columna] = 1
            self.mapa[self.personaje_fila][self.personaje_columna] = 0
            self.mapa[self.personaje_fila][self.personaje_columna] = 6
            self.personaje_columna -= 1
            print("personaje,caja,meta izquierda")
    # 16. personaje,caja_meta,espacio
        elif(self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 6 and self.mapa[self.personaje_fila][self.personaje_columna - 2] == 1):
            self.mapa[self.personaje_fila][self.personaje_columna] = 1
            self.mapa[self.personaje_fila][self.personaje_columna] = 5
            self.mapa[self.personaje_fila][self.personaje_columna] = 2
            self.personaje_columna -= 1
            print("personaje,caj_meta,espacio izquierda")
    # 17. personaje_meta,meta
        elif(self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 5 and self.mapa[self.personaje_fila][self.personaje_columna - 2] == 4):
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            self.mapa[self.personaje_fila][self.personaje_columna] = 5
            self.personaje_columna -= 1
            print("personaje_meta,meta izquierda")
    # 18. personaje_meta,caja,espacio
        elif(self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 2 and self.mapa[self.personaje_fila][self.personaje_columna - 2] == 1):
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            self.mapa[self.personaje_fila][self.personaje_columna] = 0
            self.mapa[self.personaje_fila][self.personaje_columna] = 2
            self.personaje_columna -= 1
            print("personaje_meta,caja,espacio izquierda")
    # 19. persona_meta,caja,meta
        elif(self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 2 and self.mapa[self.personaje_fila][self.personaje_columna - 2] == 4):
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            self.mapa[self.personaje_fila][self.personaje_columna] = 0
            self.mapa[self.personaje_fila][self.personaje_columna] = 6
            print("personaje_meta,caja,meta izquierda")
    # 20. personaje_meta,caja_meta,espacio
        elif(self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 6 and self.mapa[self.personaje_fila][self.personaje_columna - 2] == 1): 
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            self.mapa[self.personaje_fila][self.personaje_columna] = 5
            self.mapa[self.personaje_fila][self.personaje_columna] = 2
            self.personaje_columna -= 1
            print("personaje_meta,caja_meta izquierda")
    # 21. personaje_meta,caja_meta,meta
        elif(self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 6 and self.mapa[self.personaje_fila][self.personaje_columna - 2] == 4):
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            self.mapa[self.personaje_fila][self.personaje_columna] = 5
            self.mapa[self.personaje_fila][self.personaje_columna] = 6
            print("personaje_meta,caja_meta,meta izquierda")
    def moverArriba(self):
        print("Mover arriba")
    # 22. espacio,personaje    
        if(self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_columna][self.personaje_fila - 1] == 1):
            self.mapa[self.personaje_columna][self.personaje_fila] = 1
            self.mapa[self.personaje_columna][self.personaje_fila - 2] =0
            self.personaje_columna -= 1
            print("espacio,personaje arriba")
    # 23. meta,personaje
        elif(self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 1):
            self.mapa[self.personaje_columna][self.personaje_fila] = 4
            self.mapa[self.personaje_columna][self.personaje_fila - 2] = 0
            self.personaje_columna -= 1
            print("meta,personaje arriba")
    # 24. espacio,caja,personaje
        elif(self.mapa[self.personaje_columna][self.personaje_fila] == 2 and self.mapa[self.personaje_columna][self.personaje_fila - 1] == 0 and self.mapa[self.personaje_fila][self.personaje_columna -2 ] == 1):
            self.mapa[self.personaje_columna][self.personaje_fila] = 1
            self.mapa[self.personaje_columna][self.personaje_fila] = 2
            self.mapa[self.personaje_columna][self.personaje_fila - 2] = 0
            self.personaje_columna -= 1
            print("espacio,caja,personaje arriba")
    # 25. meta,caja,personaje
        elif(self.mapa[self.personaje_columna][self.personaje_fila] == 6 and self.mapa[self.personaje_columna][self.personaje_fila - 1] == 0 and self.mapa[self.personaje_columna][self.personaje_fila - 2] == 1):
            self.mapa[self.personaje_columna][self.personaje_fila] = 4
            self.mapa[self.personaje_columna][self.personaje_fila] = 2
            self.mapa[self.personaje_columna][self.personaje_fila] = 0
            self.personaje_columna -= 1
            print("meta,caja,personaje arriba")
    # 26. espacio,caja_meta,personaje        
        elif(self.mapa[self.personaje_columna][self.personaje_fila] == 2 and self.mapa[self.personaje_columna][self.personaje_fila - 1] == 5 and self.mapa[self.personaje_columna][self.personaje_filaq - 2] == 1): 
            self.mapa[self.personaje_columna][self.personaje_fila] = 1
            self.mapa[self.personaje_columna][self.personaje_fila] = 6
            self.mapa[self.personaje_columna][self.personaje_fila] = 0
            self.personaje_columna -= 1
            print("espacio,caja_meta,personaje arriba")
    # 27. meta,caja_meta,personaje
        elif(self.mapa[self.personaje_columna][self.personaje_fila] == 6 and self.mapa[self.personaje_columna][self.personaje_fila - 1] == 5 and self.mapa[self.personaje_columna][self.personaje_fila - 2] == 1):
            self.mapa[self.personaje_columna][self.personaje_fila] = 4
            self.mapa[self.personaje_columna][self.personaje_fila] = 6
            self.mapa[self.personaje_columna][self.personaje_fila] = 0
            self.personaje_columna -= 1
            print("meta,caja_meta,personaje arriba")
    # 28. espacio,personaje_meta
        elif(self.mapa[self.personaje_columna][self.personaje_fila] == 0 and self.mapa[self.personaje_columna][self.personaje_fila- 1] == 4):
            self.mapa[self.personaje_columna][self.personaje_fila] =1
            self.mapa[self.personaje_columna][self.personaje_fila] = 5
            self.personaje_columna -= 1
            print("espacio,personaje_meta arriba")
    # 29. meta,personaje_meta 
        elif(self.mapa[self.personaje_columna][self.personaje_fila] == 5 and self.mapa[self.personaje_columna][self.personaje_fila - 1] == 4):
            self.mapa[self.personaje_columna][self.personaje_fila] = 4
            self.mapa[self.personaje_columna][self.personaje_fila] = 5
            self.personaje_columna -= 1
            print("meta,personaje_meta arriba")
    # 30. espacio,caja,personaje_meta
        elif(self.mapa[self.personaje_columna][self.personaje_fila] == 2 and self.mapa[self.personaje_columna][self.personaje_fila - 1] == 0 and self.mapa[self.personaje_columna][self.personaje_fila - 2] == 4):
            self.mapa[self.personaje_columna][self.personaje_fila] = 1
            self.mapa[self.personaje_columna][self.personaje_fila] = 2
            self.mapa[self.personaje_columna][self.personaje_fila] = 5
            self.personaje_columna -= 1
            print("espacio,caja,personaje_meta arriba")
    # 31. meta,caja,personaje_meta 
        elif(self.mapa[self.personaje_columna][self.personaje_fila] == 6 and self.mapa[self.personaje_columna][self.personaje_fila - 1] == 0 and self.mapa[self.personaje_columna][self.personaje_fila - 2] == 4):
            self.mapa[self.personaje_columna][self.personaje_fila] == 4
            self.mapa[self.personaje_columna][self.personaje_fila] == 2
            self.mapa[self.personaje_columna][self.personaje_fila] == 5
            self.personaje_columna -= 1
            print("meta,caja,personaje_meta arriba")
    # 32. espacio,caja_meta,personaje_meta
        elif(self.mapa[self.personaje_columna][self.personaje_fila] == 2 and self.mapa[self.personaje_columna][self.personaje_fila - 1] == 5 and self.mapa[self.personaje_columna][self.personaje_fila - 2] == 4):
            self.mapa[self.personaje_columna][self.personaje_fila] = 1
            self.mapa[self.personaje_columna][self.personaje_fila] = 6
            self.mapa[self.personaje_columna][self.personaje_fila] = 5
            self.personaje_columna -= 1
            print("espacio,caja_meta,personaje_meta arriba")
    # 33. meta,caja_meta,personaje_meta
        elif(self.mapa[self.personaje_columna][self.personaje_fila] == 6 and self.mapa[self.personaje_columna][self.personaje_fila - 1] == 5 and self.mapa[self.personaje_columna][self.personaje_fila - 2] == 4):
            self.mapa[self.personaje_columna][self.personaje_fila] = 4
            self.mapa[self.personaje_columna][self.personaje_fila] = 6
            self.mapa[self.personaje_columna][self.personaje_fila] = 5
            self.personaje_columna -= 1
            print("meta,caja_meta,personaje_meta")
    # 34.         
            
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
