import unittest
from Armes import Weapon
from Armes import Lance_missiles_antisurface
from Armes import Lance_missiles_anti_air
from Armes import Lance_torpilles

class TestWeapons(unittest.TestCase):

    def test_fire_at(self):
        weapon = Weapon(ammo=10, range=100)
        weapon.fire_at(50, 60, 70)  
        self.assertEqual(weapon.ammo, 9)

        # Test when ammo is zero
        with self.assertRaises(Exception) as context:
            weapon.fire_at(50, 60, 70)
        self.assertTrue('NoAmmunitionError' in str(context.exception))

class TestLanceMissilesAntiSurface(unittest.TestCase):

    def test_fire_at(self):
        missile = Lance_missiles_antisurface(ammo=50, range=100)
        missile.fire_at(150, 150, 150)  # This should print "OutOfRangeError"
        self.assertEqual(missile.ammo, 49)

        missile.fire_at(50, 50, 0)  # This should print "Firing at coordinates (50, 50, 0)"
        self.assertEqual(missile.ammo, 48)

        # Test when ammo is zero
        with self.assertRaises(Exception) as context:
            missile.ammo = 0
            missile.fire_at(50, 50, 0)
        self.assertTrue('NoAmmunitionError' in str(context.exception))

class TestLanceMissilesAntiAir(unittest.TestCase):

    def test_fire_at(self):
        missile = Lance_missiles_anti_air(ammo=40, range=20)
        missile.fire_at(30, 30, -5)  # This should print "Firing at coordinates (30, 30, -5)"
        self.assertEqual(missile.ammo, 39)

        # Test when ammo is zero
        with self.assertRaises(Exception) as context:
            missile.ammo = 0
            missile.fire_at(30, 30, -5)
        self.assertTrue('NoAmmunitionError' in str(context.exception))

class TestLanceTorpilles(unittest.TestCase):

    def test_fire_at(self):
        torpedo = Lance_torpilles(ammo=24, range=40)
        torpedo.fire_at(50, 50, 50)  # This should print "OutOfRangeError"
        self.assertEqual(torpedo.ammo, 23)

        torpedo.fire_at(50, 50, -5)  # This should print "Firing at coordinates (50, 50, -5)"
        self.assertEqual(torpedo.ammo, 22)

        # Test when ammo is zero
        with self.assertRaises(Exception) as context:
            torpedo.ammo = 0
            torpedo.fire_at(50, 50, -5)
        self.assertTrue('NoAmmunitionError' in str(context.exception))