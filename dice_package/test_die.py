from .dice import RollableDie

def test_geometry():
        die = RollableDie()
        assert die.sides==6

def test_roll():
    die = RollableDie()
    options=list(range(1,die.sides+1))
    roll = die.roll()
    assert roll in options
