# 4_board.py

class Board:
    
    def _init_(self):
        self.board = []

    def display(self):
        print("Estado actual del tablero:")
        for row in self.board:
            print(row)

    def place_tile(self, tile):
        if not self.board:
            self.board.append([tile])
        else:
            first_value, last_value = tile

            # Intenta colocar en el extremo izquierdo
            if first_value == self.board[0][0]:
                self.board.insert(0, [last_value, first_value])
            # Intenta colocar en el extremo derecho
            elif last_value == self.board[-1][-1]:
                self.board.append([first_value, last_value])
            else:
                print("No se puede colocar la ficha en el tablero.")

# Ejemplo de uso
if _name_ == "_main_":
    # Crear un tablero
    domino_board = Board()

    # Mostrar el tablero vacío
    domino_board.display()

    # Colocar fichas en el tablero
    domino_board.place_tile((1, 2))
    domino_board.display()

    domino_board.place_tile((2, 3))
    domino_board.display()

    domino_board.place_tile((4, 3))
    domino_board.display()