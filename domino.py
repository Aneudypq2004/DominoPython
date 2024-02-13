# Este módulo podría contener la lógica principal del juego,
# incluyendo la inicialización del juego,
# el manejo de turnos, y la lógica para jugar fichas.
import random


class FichaDomino:
    def __init__(self, izquierda, derecha):
        self.izquierda = izquierda
        self.derecha = derecha
    def __str__(self):
        return f'[{self.izquierda}|{self.derecha}]'



class Domino():
    
    def __init__(self, amountPlayer):

        self.amountPlayer = amountPlayer
        self.jugadores = [[] for _ in range (amountPlayer)]
        self.fichas = self.crearCombinaciones()
        self.repartirFichas()
        self.jugadorActual = 0

    def crearCombinaciones(self):

        fichas = []

        for izquierda in range(7):

            for derecha in range(izquierda, 7):
                fichas.append(FichaDomino(izquierda, derecha))

        random.shuffle(fichas)

        return fichas

    def repartirFichas(self):
        
        amountPlayer = len(self.jugadores)
        
        fichasPorJugador = 7;
        
        for _ in range(fichasPorJugador):
            for jugador in self.jugadores:
                jugador.append(self.fichas.pop())


    def imprimirFichas(self):
        
        for i, jugador in enumerate(self.jugadores, start = 1):
            print(f"Jugador {i}:{', '.join(map(str, jugador))}")

    def jugadaValida(self, ficha, lado):
        return ficha.izquierda == lado or ficha.derecha == lado

    def jugarFicha(self, indiceFicha, lado):
        
        ficha = self.jugadores[self.jugadorActual][indiceFicha]
        
        if self.jugadaValida(ficha, lado):
            self.jugadores[self.jugadorActual].pop(indiceFicha)
            return True
        return False

    def siguienteTurno(self):
        self.jugadorActual = (self.jugadorActual + 1) % self.amountPlayer





