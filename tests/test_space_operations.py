"""Testing the new space.

This should run as part of the CI/CD pipeline.
"""

import pytest

from cadcad.spaces import EmptySpace, Integer, Real

# from cadcad.errors import InstanceError
from cadcad.spaces import space

@space
class Space_1:
    d_1: Integer
    d_2: Integer

@space
class Space_2:
    d_3: Integer
    d_4: Integer
    

def test_cartesian_product():
    # Test Commutative Properties
    Space_3 = Space_1 * Space_2
    Space_4 = Space_2 * Space_1
    assert Space_3.unroll_schema() == Space_4.unroll_schema()


def test_merge_product():
    # Test Commutative Properties
    Space_3 = Space_1 + Space_2
    Space_4 = Space_2 + Space_1
    assert Space_3.unroll_schema() == Space_4.unroll_schema()

    
def test_repeated_merge_product():
    N = 5
    Space_1_N = Space_1 ** N
    assert len(Space_1_N.dimensions()) == N
