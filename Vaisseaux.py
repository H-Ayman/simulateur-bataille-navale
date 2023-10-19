from Armes import Lance_missiles_anti_air, Lance_missiles_antisurface, Lance_torpilles

class Vessel():

    def _init_(self, coordinates, max_hits, weapon):
        self.coordinates= coordinates
        self.max_hits= max_hits
        self.weapon =weapon
    

    def go_to(self,x:int,y:int,z:int):
        self.coordinates=(x,y,z)
    
    def get_coordinates(self):
        return self.coordinates
    
    def fire_at(self,x:int,y:int,z:int):
        if self.ammo > 0:
            print(f"Firing at coordinates ({x}, {y}, {z})")
            self.ammo -= 1
        else:
            print("NoAmmunitionError")


class Cruiser(Vessel):
    def _init_(self, coordinates, max_hits, weapon):
        self.coordinates=coordinates
        self.max_hits=6
        self.weapon= Lance_missiles_anti_air
    
    def go_to(self,x:int,y:int,z:int):

        if z==0:
            self.coordinates=(x,y,z)
        else:
            return 'deplacement impossible'
    
    def get_coordinates(self):
        return super().get_coordinates()
    
    def fire_at(self, x: int, y: int, z: int):
        return self.weapon.fire_at(x, y, z)

class Submarine(Vessel):
    def _init_(self, coordinates, max_hits, weapon):
        self.coordinates=coordinates
        self.max_hits=2
        self.weapon= Lance_torpilles
    
    def go_to(self,x:int,y:int,z:int):

        if z==0 or z==-1:
            self.coordinates=(x,y,z)
        else:
            return 'deplacement impossible'
    
    def get_coordinates(self):
        return super().get_coordinates()
    
    def fire_at(self, x: int, y: int, z: int):
        return self.weapon.fire_at(x, y, z)

class Frigate(Vessel):
    def _init_(self, coordinates, max_hits, weapon):
        self.coordinates=coordinates
        self.max_hits=5
        self.weapon= Lance_missiles_antisurface
    
    def go_to(self,x:int,y:int,z:int):

        if z==0:
            self.coordinates=(x,y,z)
        else:
            return 'deplacement impossible'
    
    def get_coordinates(self):
        return super().get_coordinates()
    
    def fire_at(self, x: int, y: int, z: int):
        return self.weapon.fire_at(x, y, z)

class Destroyer(Vessel):
    def _init_(self, coordinates, max_hits, weapon):
        self.coordinates=coordinates
        self.max_hits=4
        self.weapon= Lance_torpilles
    
    def go_to(self,x:int,y:int,z:int):

        if z==0:
            self.coordinates=(x,y,z)
        else:
            return 'deplacement impossible'
    
    def get_coordinates(self):
        return super().get_coordinates()
    
    def fire_at(self, x: int, y: int, z: int):
        return self.weapon.fire_at(x, y, z)

class Aircraft(Vessel):
    def _init_(self, coordinates, max_hits, weapon):
        self.coordinates=coordinates
        self.max_hits=1
        self.weapon= Lance_missiles_antisurface
    
    def go_to(self,x:int,y:int,z:int):

        if z==1:
            self.coordinates=(x,y,z)
        else:
            return 'deplacement impossible'
    
    def get_coordinates(self):
        return super().get_coordinates()
    
    def fire_at(self, x: int, y: int, z: int):
        return self.weapon.fire_at(x, y, z)