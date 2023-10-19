import unittest
from Armes import Weapon, Lance_torpilles, Lance_missiles_anti_air, Lance_missiles_antisurface


class TestWeapons(unittest.TestCase):

    def test_fire_at(self):
        weapon = Weapon(ammo=10, range=100)
        weapon.fire_at(50, 60, 70)  
        self.assertEqual(weapon.ammo, 9)

        # ammo is zero
        with self.assertRaises(Exception) as context:
            weapon.fire_at(50, 60, 70)
        self.assertTrue('NoAmmunitionError' in str(context.exception))

class TestLanceMissilesAntiSurface(unittest.TestCase):

    def test_fire_at(self):
        missile = Lance_missiles_antisurface(ammo=50, range=100)
        missile.fire_at(150, 150, 150)  # "OutOfRangeError"
        self.assertEqual(missile.ammo, 49)

        missile.fire_at(50, 50, 0)  # In range
        self.assertEqual(missile.ammo, 48)

        # ammo is zero
        with self.assertRaises(Exception) as context:
            missile.ammo = 0
            missile.fire_at(50, 50, 0)
        self.assertTrue('NoAmmunitionError' in str(context.exception))

class TestLanceMissilesAntiAir(unittest.TestCase):

    def test_fire_at(self):
        missile = Lance_missiles_anti_air(ammo=40, range=20)
        missile.fire_at(30, 30, -5)  # In range
        self.assertEqual(missile.ammo, 39)

        # ammo is zero
        with self.assertRaises(Exception) as context:
            missile.ammo = 0
            missile.fire_at(30, 30, -5)
        self.assertTrue('NoAmmunitionError' in str(context.exception))

class TestLanceTorpilles(unittest.TestCase):

    def test_fire_at(self):
        torpedo = Lance_torpilles(ammo=24, range=40)
        torpedo.fire_at(50, 50, 50)  #  "OutOfRangeError"
        self.assertEqual(torpedo.ammo, 23)

        torpedo.fire_at(50, 50, -5)  # In range
        self.assertEqual(torpedo.ammo, 22)

        # ammo is zero
        with self.assertRaises(Exception) as context:
            torpedo.ammo = 0
            torpedo.fire_at(50, 50, -5)
        self.assertTrue('NoAmmunitionError' in str(context.exception))