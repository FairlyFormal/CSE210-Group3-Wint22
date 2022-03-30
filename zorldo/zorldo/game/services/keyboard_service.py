import pyray
from game.shared.point import Point
from game.casting.snake import Snake



class KeyboardService:
    """Detects player input. 
    
    The responsibility of a KeyboardService is to indicate whether or not a key is up or down.

    Attributes:
        _keys (Dict[string, int]): The letter to key mapping.
    """

    

    def __init__(self):
        """Constructs a new KeyboardService."""
        self._keys = {}
        
        self._keys['w'] = pyray.KEY_W
        self._keys['a'] = pyray.KEY_A
        self._keys['s'] = pyray.KEY_S
        self._keys['d'] = pyray.KEY_D

        self._keys['i'] = pyray.KEY_I
        self._keys['j'] = pyray.KEY_J
        self._keys['k'] = pyray.KEY_K
        self._keys['l'] = pyray.KEY_L

    def is_key_up(self, key):
        """Checks if the given key is currently up.
        
        Args:
            key (string): The given key (w, a, s, d or i, j, k, l)
        """
        pyray_key = self._keys[key.lower()]
        return pyray.is_key_up(pyray_key)

    def is_key_down(self, key):
        """Checks if the given key is currently down.
        
        Args:
            key (string): The given key (w, a, s, d or i, j, k, l)
        """
        pyray_key = self._keys[key.lower()]
        return pyray.is_key_down(pyray_key)

    def get_direction(self, x, y):
        """Gets the selected direction based on the currently pressed keys.

        Returns:
            Point: The selected direction.
        """
        
        dx = 0
        dy = 0


        if pyray.is_key_down(pyray.KEY_A):
            dx = -1
        
        
        if pyray.is_key_down(pyray.KEY_D):
            dx = 1
        
        if pyray.is_key_down(pyray.KEY_W):
            dy = -1
        
        if pyray.is_key_down(pyray.KEY_S):
            dy = 1

        direction = Point(dx, dy)
        direction = direction.scale(self._cell_size)
        
        return direction