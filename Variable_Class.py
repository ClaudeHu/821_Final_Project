"""Creating a Variable class."""


class Variable:
    """Variable class."""

    def __init__(self, name: str, values: list):
        """Initialize."""
        self.name = name
        self.values = values

    def set_type(self, var_type: str):
        """Setter for variable type."""
        if var_type not in ["Binary", "Categorical", "Discrete", "Continuous"]:
            raise ValueError(
                "Invalid type. Please put 'Binary', 'Categorical', 'Discrete',\
                     or 'Continuous'."
            )
        self._var_type = var_type

    @property
    def get_type(self):
        """Variable type."""
        return self._var_type

    def set_x_or_y(self, x_or_y_type: str):
        """Setter for variable classification."""
        if x_or_y_type not in ["x", "y"]:
            raise ValueError("Invalid input. Please put 'x' or 'y'.")
        self._x_or_y = x_or_y_type

    @property
    def get_x_or_y(self):
        """Variable classification as x or y."""
        return self._x_or_y
