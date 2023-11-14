from pakudex import Pakudex

# pakudex = Pakudex(capacity=5)
# species = "psygoose"
# pakudex.add_pakuri(species)


# never use the pakuri class in this program

def main():

    menuOption = -1
    capacity = -5

    # Initial Menu Output
    print("Welcome to Pakudex: Tracker Extraordinaire!")    # Menu Welcome

    while True:
        try:
            capacity = int(input("Enter max capacity of the Pakudex: "))    # Input validation for capacity
        except ValueError:
            print("Please enter a valid size.")
            continue
        else:
            if capacity < 0 or capacity > 20:
                print("Please enter a valid size.")
                continue
            else:
                break

    pakudex = Pakudex(capacity)
    print(f"The Pakudex can hold {pakudex.capacity} species of Pakuri.")

    while menuOption != 6:
        print("Pakudex Main Menu\n" + "-"*17)
        print("1. List Pakuri\n2. Show Pakuri\n3. Add Pakuri\n4. Evolve Pakuri\n5. Sort Pakuri\n6. Exit")
        menuOption = int(input("What would you like to do? "))

        if menuOption == 1:
            if pakudex.size == 0:
                print("No Pakuri in Pakudex yet!")
            else:
                print("Pakuri In Pakudex:")
                for i, j in enumerate(pakudex.get_species_array()):     # FIXME WORKING!!!
                    print(i+1, end="")
                    print(f". {j}")
                print("")

        elif menuOption == 2:
            speciesName = input("Enter the name of the species to display: ")   # FIXME WORKING!!!
            if pakudex.get_stats(speciesName) is None:
                print("Error: No such Pakuri!\n")
            else:
                print(f"Species: {speciesName}")
                print(f"Attack: ", pakudex.get_stats(speciesName)[0])
                print(f"Defense: ", pakudex.get_stats(speciesName)[1])
                print(f"Speed: ", pakudex.get_stats(speciesName)[2])
                print("")

        elif menuOption == 3:
            name = input("Enter the name of the species to add: ")     # FIXME WORKING!!!
            yesNo, code = pakudex.add_pakuri(name)
            if yesNo is False and code == "duplicate":
                print("Error: Pakudex already contains this species!")
            elif yesNo is False and code == "full":
                print("Error: Pakudex is full!")
            elif yesNo is True and code == "working":
                print(f"Pakuri species {name} successfully added!\n")

        elif menuOption == 4:   # todo ADD STUFF
            species = input("Enter the name of the species to evolve: ")
            yesOrNo = pakudex.evolve_species(species)
            if yesOrNo is True:
                print(f"{species} has evolved!")
            elif yesOrNo is False:
                print("Error: No such Pakuri!")

        elif menuOption == 5:   # todo ADD STUFF
            pass
        elif menuOption == 6:
            break
        else:
            print("Invalid Menu Option!")

    print("Thanks for using Pakudex! Bye!")

if __name__ == "__main__":
    main()

