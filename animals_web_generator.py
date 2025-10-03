import json
import sys
import os


def load_data(file_path):
    """
    Loads data from a JSON file with comprehensive error handling.
    
    Args:
        file_path (str): Path to the JSON file to load
        
    Returns:
        dict/list: Parsed JSON data
        
    Raises:
        SystemExit: If file cannot be loaded or parsed
    """
    try:
        # Check if file exists
        if not os.path.exists(file_path):
            print(f"Error: File '{file_path}' not found.")
            sys.exit(1)
            
        # Check if file is readable
        if not os.access(file_path, os.R_OK):
            print(f"Error: File '{file_path}' is not readable.")
            sys.exit(1)
            
        # Attempt to open and parse the JSON file
        with open(file_path, "r", encoding="utf-8") as handle:
            data = json.load(handle)
            
        # Validate that we have data
        if not data:
            print(f"Warning: File '{file_path}' is empty or contains no data.")
            
        return data
        
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON format in '{file_path}': {e}")
        sys.exit(1)
    except IOError as e:
        print(f"Error: Could not read file '{file_path}': {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error loading '{file_path}': {e}")
        sys.exit(1)


def serialize_animal(animal_obj):
    """
    Serializes a single animal object into HTML card format.
    
    Args:
        animal_obj (dict): Dictionary containing animal information
        
    Returns:
        str: HTML string for a single animal card
    """
    output = ''
    
    # Start list item with card class
    output += '<li class="cards__item">\n'
    
    # Add card title with animal name
    output += f'  <div class="card__title">{animal_obj["name"]}</div>\n'
    
    # Start card text paragraph
    output += '  <p class="card__text">\n'
    
    # Add diet if it exists
    if 'characteristics' in animal_obj and 'diet' in animal_obj['characteristics']:
        output += f'      <strong>Diet:</strong> {animal_obj["characteristics"]["diet"]}<br/>\n'
    
    # Add first location if it exists
    if 'locations' in animal_obj and len(animal_obj['locations']) > 0:
        output += f'      <strong>Location:</strong> {animal_obj["locations"][0]}<br/>\n'
    
    # Add type if it exists
    if 'characteristics' in animal_obj and 'type' in animal_obj['characteristics']:
        output += f'      <strong>Type:</strong> {animal_obj["characteristics"]["type"]}<br/>\n'
    
    # Close card text paragraph
    output += '  </p>\n'
    
    # Close list item
    output += '</li>\n'
    
    return output


def generate_animals_string(animals_data):
    """
    Generates HTML string containing all animal information as styled card items.
    
    Args:
        animals_data (list): List of animal dictionaries
        
    Returns:
        str: Complete HTML string for all animal cards
    """
    output = ''
    for animal_obj in animals_data:
        output += serialize_animal(animal_obj)
    
    return output


def generate_html(template_path, animals_data, output_path):
    """
    Generates HTML file by replacing placeholder with animal data.
    
    Args:
        template_path (str): Path to the HTML template file
        animals_data (list): List of animal dictionaries
        output_path (str): Path where the generated HTML will be saved
    """
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


def main():
    """
    Main function to read animal data and generate HTML webpage.
    
    Loads animal data from JSON file and generates a styled HTML page
    using the provided template.
    """
    animals_data = load_data('animals_data.json')
    generate_html('animals_template.html', animals_data, 'animals.html')


if __name__ == "__main__":
    main()
