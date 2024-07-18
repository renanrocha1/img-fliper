from enum import Enum
from PIL.Image import Transpose

class Direction(str, Enum):
    UP = 'flip_y'
    LEFT = 'flip_x'
    DOWN = 'rotate_l'
    RIGHT = 'rotate_r'

    def get_transpose(self):
        if self == Direction.UP:
            return Transpose.FLIP_TOP_BOTTOM
        return Transpose.FLIP_LEFT_RIGHT
    
    def get_rotation(self):
        if self == Direction.DOWN:
            return 90
        return -90