from pakuri import Pakuri

class Pakudex:

    def __init__(self, capacity=20):
        self.capacity = capacity    # initial value is 20
        self.pakuris = []*capacity    # store a list of pakuri objects
        self.size = 0   # keep track of the # of concrete pakuri objects in self.pakuri

    def get_size(self):
        return self.size

    def get_capacity(self):
        return self.capacity

    def get_species_array(self):
        res = []
        for pak in self.pakuris:        # loop through self.pakuris to look at each pakuri object
            res.append(Pakuri.get_species(pak))     # append pakuri.species to the res
        return res

    def get_stats(self, species):
        for paku in self.pakuris:   # loop through self.pakuri to look at each pakuri object
            if Pakuri.get_species(paku) == species:  # compare pakuri.species == species
                return [int(Pakuri(species).get_attack()), int(Pakuri(species).get_defense()), int(Pakuri(species).get_speed())]
                # if true, return [pakuri.attack, pakuri.defense, pakuri.speed]  ^^^
        return None

    def sort_pakuri(self):
        self.pakuris = self.pakuris.sort()  # Sorts the pakuri objects in the pakudex according to Python ordering of species NAMES

    def add_pakuri(self, species):
        # loop through self.pakuri to look at each pakuri object
        # compare pakuri.species == species
        if species in self.get_species_array():  # 1. Check duplicates => return False
            return False, "duplicate"
        if self.size == self.capacity:  # 2. When the list is full => return False
            return False, "full"
        else:
            self.pakuris.append(Pakuri(species))    # add a new pakuri object into the list (if other 2 conditions above are not met)
            self.size += 1  # increment self.size
            return True, "working"    # return True

    def evolve_species(self, species):
        if species in self.get_species_array():
            for paku in self.pakuris:
                if Pakuri.get_species(paku) == species:
                    Pakuri(species).evolve()
        else:
            return False
        return True


