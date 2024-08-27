from game.piece import Piece

class Queen(Piece):
    def __str__(self):
        if self.__color__ == "WHITE":
            return "♕"
        else:
            return "♛"
    
    def get_move_king(self, board, from_row, from_col):
        movimientos = []
        direcciones = [
            (-1, -1), (-1, 0), (-1, 1),  
            (0, -1),          (0, 1),    
            (1, -1), (1, 0), (1, 1)
        ]
        for direccion in direcciones:
            to_row = from_row + direccion[0]
            to_col = from_col + direccion[1]
            if to_row < 1 or to_row > 8 or to_col < 1 or to_col > 8:
                continue
            else:
                if board.get_piece(to_row, to_col) == None:
                    movimientos.append((to_row, to_col))
        return movimientos
    
    def posibles_moves(self, from_row, from_col):
        Queen = self.__board__.get_piece(from_row, from_col)
        if Queen == None:
            return []
    
        else: 
            return Queen.get_move_Queen(self.__board__, from_row, from_col)
        
        

        