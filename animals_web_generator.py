import json


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


def generate_animals_string(animals_data):
    """ Generates a string containing all animal information """
    output = ''
    for animal in animals_data:
        # Add name
        output += f"Name: {animal['name']}\n"
        
        # Add diet if it exists
        if 'characteristics' in animal and 'diet' in animal['characteristics']:
            output += f"Diet: {animal['characteristics']['diet']}\n"
        
        # Add first location if it exists
        if 'locations' in animal and len(animal['locations']) > 0:
            output += f"Location: {animal['locations'][0]}\n"
        
        # Add type if it exists
        if 'characteristics' in animal and 'type' in animal['characteristics']:
            output += f"Type: {animal['characteristics']['type']}\n"
        
        output += "\n"  # Empty line for separation
    
    return output


def generate_html(template_path, animals_data, output_path):
    """ Generates HTML file by replacing placeholder with animal data """
    # Read the HTML template
    with open(template_path, "r") as template_file:
        html_content = template_file.read()
    
    # Generate animals string
    animals_string = generate_animals_string(animals_data)
    
    # Replace the placeholder with animals data
    html_content = html_content.replace("__REPLACE_ANIMALS_INFO__", animals_string)
    
    # Write the new HTML content to output file
    with open(output_path, "w") as output_file:
        output_file.write(html_content)
    
    print(f"HTML file generated successfully: {output_path}")


def print_animal_info(animals_data):
    """ Prints information for each animal (keeping for backward compatibility) """
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
    """ Main function to read animal data and generate HTML """
    animals_data = load_data('animals_data.json')
    generate_html('animals_template.html', animals_data, 'animals.html')


if __name__ == "__main__":
    main()
