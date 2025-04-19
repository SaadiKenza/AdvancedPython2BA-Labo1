import pytest
import utils

def test_fact():
    assert utils.fact(0)==1
    assert utils.fact(5)==120
    assert utils.fact(-5)==ValueError

def test_roots():
    assert utils.roots(1,0,1)==(1j,-1j)


# def test_integrate():
#     # À compléter...
#     pass
