import json


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


def print_animal_info(animals_data):
    """ Prints information for each animal """
    for animal in animals_data:
        # Print name
        print(f"Name: {animal['name']}")
        
        # Print diet if it exists
        if 'characteristics' in animal and 'diet' in animal['characteristics']:
            print(f"Diet: {animal['characteristics']['diet']}")
        
        # Print first location if it exists
        if 'locations' in animal and len(animal['locations']) > 0:
            print(f"Location: {animal['locations'][0]}")
        
        # Print type if it exists
        if 'characteristics' in animal and 'type' in animal['characteristics']:
            print(f"Type: {animal['characteristics']['type']}")
        
        print()  # Empty line for separation


def main():
    """ Main function to read and print animal data """
    animals_data = load_data('animals_data.json')
    print_animal_info(animals_data)


if __name__ == "__main__":
    main()
