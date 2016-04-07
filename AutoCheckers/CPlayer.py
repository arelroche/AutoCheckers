'''
Created by Arel Roche
Feb 27. 2016

'''

#This module contains the code to process player moves 
import numpy as np

from CPiece import CPiece
from CBoard import CBoard

class CPlayer(object) :
    '''
    Class for Player
    '''
    
    def __init__ (self,board):
        '''
        Constructor
        '''
        self.board = board 
                  
    
    
    def handoff(self):
              
        
        # reply = ''
        # while reply != 'y':
        #     reply = raw_input("Have you completed your turn? (y/n): ")          
        self.board_from_vision()
        
        
    def board_from_vision(self):
        
        board_temp = np.genfromtxt('board.txt', dtype=str)
        #print(board_temp)
        del self.board.light_pieces[:]
        del self.board.dark_pieces[:]
        
        for t_row in range(10):
            for t_col in range(10):              
                
                if ((t_row % 2 == 0) != (t_col % 2 == 0)) :
                    if board_temp[t_row][t_col] == 'X':
                        new_piece = CPiece(self.board, t_row, t_col,'DARK')
                        self.board.dark_pieces.append(new_piece)
                        self.board.set_bitmap(t_row, t_col, new_piece)
                    
                    elif board_temp[t_row][t_col] == '#':
                        new_piece = CPiece(self.board, t_row, t_col,'DARK')
                        new_piece.promote()                    
                        self.board.dark_pieces.append(new_piece)
                        self.board.set_bitmap(t_row, t_col, new_piece) 
                        
                    elif board_temp[t_row][t_col] == 'O':
                        new_piece = CPiece(self.board, t_row, t_col,'LIGHT')
                        self.board.light_pieces.append(new_piece) 
                        self.board.set_bitmap(t_row, t_col, new_piece)
                     
                    elif board_temp[t_row][t_col] == '$':
                        new_piece = CPiece(self.board, t_row, t_col,'LIGHT')
                        new_piece.promote()                    
                        self.board.light_pieces.append(new_piece)
                        self.board.set_bitmap(t_row, t_col, new_piece) 
                        
                    elif board_temp[t_row][t_col] == '.':
                            self.board.set_bitmap(t_row, t_col, None)
                    
                    else :
                        print "Invalid Input!"
                        
                else:
                    pass
                
                        
        #self.print_lists()
        #print "Board in Memory"
        #self.print_board_values()
                    
                            
    def print_lists(self):
        for piece in self.board.light_pieces:
            print(piece)
        for piece in self.board.dark_pieces:
            print(piece)
            
    def print_board_values(self):
        for row in range(10) :
            for col in range(10) :
                if ((row % 2 == 0) != (col % 2 == 0)) :
                    print(self.board.bitmap[int(5 * row + col / 2)])
        