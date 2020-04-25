"""
Unit and regression test for the mars package.
"""

# Import package, test suite, and other packages as needed
import mars
import pytest
import sys


def test_mars_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "mars" in sys.modules


def test_floats():

    assert 2 + 2 == 4
    assert pytest.approx(2.123 + 4.332 + 1e-15, abs=1.0e-14) == 6.455


@pytest.mark.xfail
def test_floats_xfail():
    assert pytest.approx(2.123 + 4.332 + 1e-5, abs=1.0e-7) == 6.455


def test_exception():

    val = []
    with pytest.raises(TypeError):
        val += 1.234


@pytest.mark.parametrize("a,b,ans", [(2, 2, 4), (3.0, 4.0, 7)])
def test_add(a, b, ans):

    assert (a + b) == ans
