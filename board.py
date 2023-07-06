

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
        
        self.order = list(digitstr)
        n = 0
        
        for r in range(len(self.tiles)):
            for c in range(len(self.tiles[0])):
                self.tiles[r][c] = self.order[0+n]
                n += 1
                if '0' in self.tiles[r][c]:
                    self.blank_r = r
                    self.blank_c = c



                    
    def __repr__(self):
        """
        Returns a string representation of the Board object, displaying the board
        as a 3x3 grid with underscores for empty cells (blank tiles).
        """
        s = ''
        
        for r in range(len(self.tiles)):
            for c in range(len(self.tiles[0])):
                if self.tiles[r][c] == '0':
                    s += '_'
                else:
                    s += self.tiles[r][c]

                s += ' '
            s += '\n'
        return s


    ### Add your other method definitions below. ###
    
    def move_blank(self, direction):
        """
        Moves the blank tile (empty cell) in the specified direction if the move
        is valid. Updates the blank tile's position accordingly.
        """
        new_blank_r = self.blank_r
        new_blank_c = self.blank_c
    
        if direction == 'up':
            new_blank_r -= 1
        elif direction == 'down':
            new_blank_r += 1
        elif direction == 'left':
            new_blank_c -= 1
        elif direction == 'right':
            new_blank_c += 1
        else:
            return False
    
        #bounds
        if new_blank_r < 0 or new_blank_r > 2 or \
            new_blank_c < 0 or new_blank_c > 2:
            return False
    
        #swap blank to the new position
        self.tiles[self.blank_r][self.blank_c] = self.tiles[new_blank_r][new_blank_c]
        self.tiles[new_blank_r][new_blank_c] = '0'
    
        #new blank cell coordinates
        self.blank_r = new_blank_r
        self.blank_c = new_blank_c
    
        return True
    
    def digit_string(self):
        """
        Returns a single string containing all the digits in the Board object's
        tiles, in row-major order (left to right, top to bottom).
        """
        digit_str = ''
        for r in range(len(self.tiles)):
            for c in range(len(self.tiles[0])):
                digit_str += self.tiles[r][c]
        return digit_str
    
    def copy(self):
        """
        Returns a single string containing all the digits in the Board object's
        tiles, in row-major order (left to right, top to bottom).
        """
        digit_str = self.digit_string()
        return Board(digit_str)
    
    def num_misplaced(self):
        """
        Calculates the number of misplaced tiles in the Board object, excluding the
        blank tile.
        """
        wrong_tiles = 0
        for r in range(len(self.tiles)):
            for c in range(len(self.tiles[0])):
                if self.tiles[r][c] != '0' and self.tiles[r][c] != GOAL_TILES[r][c]:
                    wrong_tiles += 1
        return wrong_tiles
    
    def manhattan_distance(self):
        """
        Calculates the Manhattan distance from the current configuration
        of the board to the goal configuration.
        """
        distance = 0
        for i in range(3):
            for j in range(3):
                tile = self.tiles[i][j]
                if tile != '0':
                    # the correct position for the tile
                    correct_i = int(tile) // 3
                    correct_j = int(tile) % 3
                    # add the distance for this tile
                    distance += abs(i - correct_i) + abs(j - correct_j)
        return distance



    
    def __eq__(self, other):
        """
        Compares two Board objects to see if they have the same configuration of tiles.
        Returns True if the other object has the same tile configuration,
        False otherwise.
        """
        if type(self) == type(other):
            return self.tiles == other.tiles
        return False

        

    



    









