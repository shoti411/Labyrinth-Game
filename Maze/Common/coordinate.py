class Coordinate:
    """
    Coordinate represents an X,Y location in the Maze Game. 
    X, Y must be either -1, -1 or both positive ints. 
    -1, -1 represents the location of an extra Tile.
    """
    
    def __init__(self, x, y):
        self.__check_coordinate(x, y)
        self.__x = x
        self.__y = y

    def __check_coordinate(x,y):
        if ((x == -1 and y != -1) or (x != -1 and y == -1)):
            raise ValueError('A Coordinate must have both X and Y as -1 or they must both be positive.')
        if ((x != -1 and y != -1) and (x < 0 or y < 0)):
            raise ValueError('A Coordinate must have both X and Y as -1 or they must both be positive.')
        if (not isinstance(x, int)) or (not isinstance(y, int)):
            raise ValueError('A Coordiante require X and Y to be integers.')

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y
    