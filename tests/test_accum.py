import pytest
from stuff import accum
from stuff.accum import Accumulator

##########~~~ Fixtures ~~~######################

# @pytest.fixture
# def accum():
#     return Accumulator()

###########~~~ Tests ~~~~#######################
@pytest.mark.accumulator
def test_accumulator_init(accum):
    assert accum.count == 0

@pytest.mark.accumulator
def test_accumulator_add_one(accum):
    accum.add()
    assert accum.count == 1

@pytest.mark.accumulator
def test_accumulator_add_three(accum):
    accum.add(3)
    assert accum.count == 3

@pytest.mark.accumulator
def test_accumulator_add_twice(accum):
    accum.add()
    accum.add()
    assert accum.count == 2

@pytest.mark.accumulator
def test_accumulator_cannot_set_count_directly(accum):
    with pytest.raises(AttributeError, match="can't set attribute") as e:
      accum.count = 10

# #asserts that accum internal count starts from 0
# def test_accumulator_init():
#     accum = Accumulator()
#     assert accum.count == 0

# #verifies that add method adds 1 to the internal count
# def test_accumulator_add_one():
#     accum = Accumulator()
#     accum.add()
#     assert accum.count == 1

# #verifies that add method adds 3 to the internal count
# def test_accumulator_add_three():
#     accum = Accumulator()
#     accum.add(3)
#     assert accum.count == 3

# #verifies that add method adds the amount twice
# def test_accumulator_add_twice():
#     accum = Accumulator()
#     accum.add()
#     accum.add()
#     assert accum.count == 2

# #Verifies that count cannot be set directly as it's a read only property.
# def test_accumulator_cannot_set_count_directly():
#     accum = Accumulator()
#     with pytest.raises(AttributeError, match="can't set attribute") as e:
#       accum.count = 10

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~ Arrange - Act - Assert (Pattern for writing tests using pytest) ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~