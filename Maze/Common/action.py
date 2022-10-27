class Action:
    """
    Action represents the two types of actions a player can take during a turn. Pass or Move
    """
    def get_degree(self):
        raise NotImplemented('get_degree not implemented.')

    def get_direction(self):
        raise NotImplemented('get_direction not implemented.')

    def get_index(self):
        raise NotImplemented('get_index not implemented.')

    def get_isrow(self):
        raise NotImplemented('get_isrow not implemented.')

    def get_coordinate(self):
        raise NotImplemented('get_coordinate not implemented')

    def get_move(self):
        raise NotImplemented('get_move not implemented')

    def is_pass(self):
        raise NotImplemented('is_pass not implemented.')

    def does_undo(self, action):
        """
        Checks if this Action will undo the given Action

        :param: action <Action>

        :return: <boolean>
        """

        raise NotImplemented('is_action not implemented')

class Pass:
    """
    Represents a Pass Action in which a Player passes their turn.
    """

    def is_pass(self):
        return True

    def does_undo(self, action):
        return False

class Move:
    """
    Represents a Move Action for a Player.

    A Move Action is represented as a degree, direction, index, isrow, and coordinate.
    degrees represents the degrees to rotate the extra Tile by.
    direction represents the direction to shift the row or column by. Either -1 (left or up) or 1 (right or down)
    index represents the row or column index to shift
    isrow is boolean for if the index is for a row
    coordinate is the Coordinate to move to
    """

    def __init__(self, degrees, direction, index, isrow, coordinate):
        self.__degrees = degrees
        self.__direction = direction
        self.__index = index
        self.__isrow = isrow
        self.__coordinate = coordinate

    def get_degree(self):
        return self.__degrees

    def get_direction(self):
        return self.__direction

    def get_index(self):
        return self.__index

    def get_isrow(self):
        return self.__isrow

    def get_coordinate(self):
        return self.__coordinate

    def get_move(self):
        return self.__degrees, self.__direction, self.__index, self.__isrow, self.__coordinate 

    def is_pass(self):
        return False

    def does_undo(self, action):
        if not isinstance(action, Move):
            return False
        
        if self.get_isrow() != action.get_isrow():
            return False

        return self.get_index() == action.get_index() and self.get_direction() == -1*action.get_direction() 


    


