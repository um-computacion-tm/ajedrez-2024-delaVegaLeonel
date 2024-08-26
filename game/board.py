from game.piece import Rook 
from game.rook import Rook

class Board:
    def self(Board):
        ...

class Board:
    def __init__(self):
        self.__positions__ = []
        for _ in range(8):
            col = []
            for _ in range(8):
                col.append(None)
            self.__positions__.append(col)
        self.__positions__[0][0] = Rook("BLACK") # Black
        self.__positions__[0][7] = Rook("BLACK") # Black
        self.__positions__[7][7] = Rook("WHITE") # White
        self.__positions__[7][0] = Rook("WHITE") # White

    def __str__(self):
        board_str = ""
        for row in self.__positions__:
            for cell in row:
                if cell is not None:
                    board_str += str(cell)
                else:
                    board_str += " "
            board_str += "\n"
        return board_str
    
    def get_piece(self, row, col):
        return self.__positions__[row][col]
    
    def display_board(self):
        for row in self.__positions__:
            for piece in row:
                if piece is None:
                    print('.', end=' ')
                else:
                    if piece.color == "BLACK":
                        print('B', end=' ')
                    else:
                        print('W', end=' ')
            print()  # Nueva línea después de cada fila

