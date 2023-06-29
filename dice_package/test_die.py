from .dice import RollableDie

def test_geometry():
        die = RollableDie()
        assert die.sides==6
