import math

class Coordinate:
    """
    Coordinate represents an X, Y location in the Maze Game. 
    X, Y must be either -1, -1 or both positive ints. 
    -1, -1 represents a location off the board.
    0, 0 represents the top-most left-most position.
    """
    
    def __init__(self, x, y):
        self.__check_coordinate(x, y)
        self.__x = x
        self.__y = y

    def __check_coordinate(self,x,y):
        if (not isinstance(x, int)) or (not isinstance(y, int)):
            raise ValueError('A Coordiante require X and Y to be integers.')
        if ((x == -1 and y != -1) or (x != -1 and y == -1)):
            raise ValueError('A Coordinate must have both X and Y as -1 or they must both be positive.')
        if ((x != -1 and y != -1) and (x < 0 or y < 0)):
            raise ValueError('A Coordinate must have both X and Y as -1 or they must both be positive.')
        

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def get_euclid_distance(self, coordinate):
        """
        Calculate the Euclidean distance between this Coordinate and a given Coordinate

        :param: coordinate <Coordinate>

        :return: <int>
        """

        if not isinstance(coordinate, Coordinate):
            raise ValueError('coordinate must be type Coordinate')

        if self.getX() == -1 or coordinate.getX() == -1:
            raise ValueError('Cannot get the distance from a Coordinate off the board.')
        return math.sqrt((self.getX()-coordinate.getX())**2 + (self.getY()-coordinate.getY())**2)
    
    def __eq__(self, other):
        if isinstance(other, Coordinate):
            return self.getX() == other.getX() and self.getY() == other.getY()

        return False

    def __lt__(self, other):
        if not isinstance(other, Coordinate):
            raise ValueError(f'Cannot compare between {other} and Coordinate.')

        if self.getX() < other.getX():
            return True
        elif self.getY() < other.getY():
            return True
        return False

    def __str__(self):
        return f"({self.getX()},{self.getY()})"
