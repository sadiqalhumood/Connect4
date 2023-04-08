#
# board.py (Final project)
#
# A Board class for the Eight Puzzle
#
# name: Sayed AlGharbi
# email: AlGharbi@bu.edu
#
# If you worked with a partner, put their contact info below:
# partner's name: Sadiq Alhumood
# partner's email: sadiq@bu.edu
#

# a 2-D list that corresponds to the tiles in the goal state
GOAL_TILES = [['0', '1', '2'],
              ['3', '4', '5'],
              ['6', '7', '8']]

class Board:
    """ A class for objects that represent an Eight Puzzle board.
    """
    def __init__(self, digitstr):
        """ a constructor for a Board object whose configuration
            is specified by the input digitstr
            input: digitstr is a permutation of the digits 0-9
        """
        # check that digitstr is 9-character string
        # containing all digits from 0-9
        assert(len(digitstr) == 9)
        for x in range(9):
            assert(str(x) in digitstr)

        self.tiles = [[''] * 3 for x in range(3)]
        self.blank_r = -1
        self.blank_c = -1

        # Put your code for the rest of __init__ below.
        # Do *NOT* remove our code above.
        for r in range(len(self.tiles)):
            for c in range(len(self.tiles[0])):
                self.tiles[r][c] = digitstr[3*r + c]
                if self.tiles[r][c] == '0':
                   self.blank_r = r
                   self.blank_c = c
                    
                    
            


    ### Add your other method definitions below. ###
    def __repr__(self):
        """returns a string representation of a Board object"""
        s = ''
        for r in range(len(self.tiles)):
            for c in range(len(self.tiles[0])):
                if self.tiles[r][c] == '0':
                    s+= '_ '
                else:
                    s += self.tiles[r][c] + ' '
                if c == 2:
                    s += '\n'
        return s 
        
    def  move_blank(self, direction):
        """ takes as input a string direction that specifies the
        direction in which the blank should move, and that attempts 
        to modify the contents of the called Board object accordingly"""
        if direction == 'up' and\
            self.blank_r > 0:
                self.tiles[self.blank_r][self.blank_c] = self.tiles[self.blank_r-1][self.blank_c]
                self.tiles[self.blank_r-1][self.blank_c] = '0'
                self.blank_r -= 1
                return True 
        elif direction == 'down' and\
            self.blank_r < 2:
                 self.tiles[self.blank_r][self.blank_c] = self.tiles[self.blank_r+1][self.blank_c]
                 self.tiles[self.blank_r+1][self.blank_c] = '0'
                 self.blank_r += 1
                 return True 
        elif direction == 'right' and\
            self.blank_c < 2:
                 self.tiles[self.blank_r][self.blank_c] = self.tiles[self.blank_r][self.blank_c+1]
                 self.tiles[self.blank_r][self.blank_c+1] = '0'
                 self.blank_c += 1
                 return True 
        elif direction == 'left' and\
            self.blank_c > 0:
                 self.tiles[self.blank_r][self.blank_c] = self.tiles[self.blank_r][self.blank_c-1]
                 self.tiles[self.blank_r][self.blank_c-1] = '0'
                 self.blank_c -= 1
                 return True 
                 
        return False
        
    def digit_string(self):
        """returns a string of digits that corresponds to the current 
        contents of the called Board object’s tiles attribute"""
        s = ''
        for r in range(len(self.tiles)):
            for c in range(len(self.tiles[0])):
               s += self.tiles[r][c] 
        return s 
    
    def copy(self):
        """returns a newly-constructed Board object that is a deep copy of the called object """
        x = Board(self.digit_string())
        return x 
    
    def num_misplaced(self):
        """returns the number of tiles in the called Board object that are not where they should be in the goal state"""
        count = 0
        for r in range(len(self.tiles)):
            for c in range(len(self.tiles[0])):
                if GOAL_TILES[r][c] != self.tiles[r][c]:
                    count += 1
        return count -1
    
    def __eq__(self, other):
        """return True if the called object (self) and the 
        argument (other) have the same values for the tiles 
        attribute, and False otherwise"""
        if self.tiles == other.tiles:
            return True
        return False

    def num_misplaced_1(self):
        """returns the number of tiles in the called Board object that are not where they should be in the goal state"""
        count = 0
        for r in range(len(self.tiles)):
            for c in range(len(self.tiles[0])):
                if GOAL_TILES[r][c] != self.tiles[r][c]:
                    count += 1
        #if '6' in self.tiles[2] and '7' in self.tiles[2] and '8' in self.tiles[2]:
            #count -=1
        #if '3' in self.tiles[1] and '4' in self.tiles[1] and '5' in self.tiles[1]:
            #count -=1
        #if '1' in self.tiles[0] and '2' in self.tiles[0]:
            #count -=1
            
        #make this function count the amount of places num is misplaced for example:
            #8 7 _ 
            #3 4 5 
            #6 2 1
        # should have 12 because 1 is misplaced by 2 rows and one column and so on
        return count -1
        
        
        
        
        
        