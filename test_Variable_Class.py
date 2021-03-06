"""Variable class test file."""

import pytest
from Variable_Class import Variable


def test_variable():
    """Test variable class."""
    var_test = Variable("Age", [1, 2])
    assert var_test.name == "Age"
    assert var_test.values == [1, 2]
    var_test.set_x_or_y("x")
    assert var_test.get_x_or_y == "x"
    var_test.set_type("Continuous")
    assert var_test.get_type == "Continuous"
    with pytest.raises(ValueError):
        var_test.set_x_or_y("X")
        var_test.set_x_or_y("Y")
        var_test.set_x_or_y("aaaaa")
        var_test.set_type("continuous")
        var_test.set_type("discrete")
        var_test.set_type("wronginput")
