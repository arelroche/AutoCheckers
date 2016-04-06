def player_input(self):
    '''
    read player input and process
    
    If no piece at location: set_bitmap value to 'None'
    Else create new Piece and
         color = 'DARK'
         is_king  = ?
    '''
    
    while True:
    
        self.new_row = raw_input("Row Number: ")
        self.new_col = raw_input("Column Number: ")
        self.new_command = raw_input("Command: ")
        #self.board.set_bitmap(new_row, new_col, new_command)
        
        '''
        Need code to retrieve existing piece and not create new piece
        '''
    
        if new_command == 'PICK':
            
            # Insert PICK execution here
            
            print "Enter place location" 
            final_row = raw_input("Row Number: ")
            final_col = raw_input("Column Number: ")
            self.new_command = 'PLACE'
            
            # Insert PLACE execution
            
            is_new_king = raw_input("Is this a new king? ")
            if is_new_king == 'YES':
                print "King"    #debug command
                #Modify piece.is_king 
            
            
        elif new_command == 'CAPTURE':
            
            # Insert CAPTURE execution here
            # Remove captured piece from dark_pieces list 
            
        else:
            print "Invalid command!"
            
            
        user_resp = raw_input("Are you done? ")
        if user_resp == 'YES':
            break