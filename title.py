class Tile:
    def _init_(self, left, right):
        self.left = left
        self.right = right

    def _repr_(self):
        return f"Tile({self.left}, {self.right})"

tile1 = Tile(3, 5)
tile2 = Tile(2, 2)

print(tile1)  # Esto imprimirá: Tile(3, 5)
print(tile2)  # Esto imprimirá: Tile(2, 2)