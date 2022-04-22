"""Creating a Variable class."""


class Variable:
    """Variable class."""

    def __init__(self, name: str, values: list):
        """Initialize."""
        self.name = name
        self.values = values

    @property
    def get_type(self):
        """Variable type."""
        return self._type

    # @type.setter
    def set_type(self, var_type: str):
        """Setter for variable type."""
        self._type = var_type

    @property
    def get_x_or_y(self):
        """Variable classification as x or y."""
        return self._x_or_y

    # @x_or_y.setter
    def set_x_or_y(self, x_or_y_type: str):
        """Setter for variable classification."""
        self._x_or_y = x_or_y_type
