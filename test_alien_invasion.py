import pytest
from alien_invasion import AlienInvasion
import math

@pytest.fixture
def ai():
    ai = AlienInvasion()
    return ai

def test_ship_movement_right(ai):
    # Example test: Ship moves right
    base = ai.ship.rect.centerx
    ai.ship.moving_right = True
    ai.ship.update()
    # Assuming speed is 1.5
    assert ai.ship.rect.centerx == round(base + ai.settings.ship_speed)


def test_ship_movement_left(ai):
    # Example test: Ship moves left
    base = ai.ship.rect.centerx
    ai.ship.moving_left = True
    ai.ship.update()
    # Assuming speed is 1.5
    assert ai.ship.rect.centerx == base - math.floor(ai.settings.ship_speed)

def test_ship_movement_up(ai):
    # Example test: Ship moves up
    base = ai.ship.rect.centery
    ai.ship.moving_up = True
    ai.ship.update()
    # Assuming speed is 1.5
    assert ai.ship.rect.centery == base - math.floor(ai.settings.ship_speed)

def test_ship_movement_down(ai):
    # Example test: Ship moves down
    base = ai.ship.rect.centery
    ai.ship.moving_down = True
    ai.ship.moving_up = True
    ai.ship.update()
    # Assuming speed is 1.5
    assert ai.ship.rect.centery == base -1


