class Weapon:
    def __init__(self, ammo, range):
        self.ammo = ammo
        self.range = range
    
    def fire_at(self,x:int,y:int,z:int):
        if self.ammo > 0:
            print(f"Firing at coordinates ({x}, {y}, {z})")
            self.ammo -= 1
        else:
            print("NoAmmunitionError")




class Lance_missiles_antisurface(Weapon):
    def _init_(self,ammo,range):
        self.ammo= 50
        self.range = 100

    def fire_at(self,x:int,y:int,z:int):
        if self.ammo==0:
            print("NoAmmunitionError")
        elif x>self.range and y>self.range and z!=0:
            print('OutOfRangeError')
            self.ammo-=1
        else:
            print(f"Firing at coordinates ({x}, {y}, {z})")
            self.ammo -= 1


class Lance_missiles_anti_air(Weapon):
    def _init_(self,ammo,range):
        self.ammo= 40
        self.range = 20

    def fire_at(self,x:int,y:int,z:int):
        if self.ammo==0:
            print("NoAmmunitionError")
        elif x>self.range and y>self.range and z<=0:
            print('OutOfRangeError')
            self.ammo-=1
        else:
            print(f"Firing at coordinates ({x}, {y}, {z})")
            self.ammo -= 1


class Lance_torpilles(Weapon):
    def _init_(self,ammo,range):
        self.ammo= 24
        self.range = 40

    def fire_at(self,x:int,y:int,z:int):
        if self.ammo==0:
            print("NoAmmunitionError")
        elif x>self.range and y>self.range and z>=0:
            print('OutOfRangeError')
            self.ammo-=1
        else:
            print(f"Firing at coordinates ({x}, {y}, {z})")
            self.ammo -= 1