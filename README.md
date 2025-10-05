# My Zootopia 🦁

A Python web generator that creates a beautiful HTML page displaying information about various animals in a styled card format.

## Description

My Zootopia is a simple yet elegant web generator that takes animal data from a JSON file and transforms it into a visually appealing HTML webpage. Each animal is displayed as a card showing key characteristics like diet, location, and type.

## Features

- 🐾 **Animal Cards**: Beautiful card-based layout for animal information
- 📊 **JSON Data Source**: Easy-to-update animal information in JSON format
- 🎨 **Styled HTML Output**: Pre-styled HTML template with modern CSS
- 🛡️ **Error Handling**: Comprehensive error handling for file operations
- 📱 **Responsive Design**: Clean, modern styling that works across devices

## Project Structure

```
My-Zootopia/
├── animals_data.json          # Animal information database
├── animals_template.html      # HTML template with styling
├── animals_web_generator.py   # Main Python script
├── animals.html              # Generated output (created when you run the script)
└── __pycache__/              # Python cache files
```

## Requirements

- Python 3.x
- No additional dependencies required (uses only standard library)

## Usage

1. **Run the generator:**
   ```bash
   python animals_web_generator.py
   ```

2. **View the output:**
   Open `animals.html` in your web browser to see the generated animal cards.

3. **Customize the data:**
   Edit `animals_data.json` to add, remove, or modify animal information.

4. **Modify the template:**
   Update `animals_template.html` to change the styling or layout.

## Animal Data Format

Each animal in `animals_data.json` should follow this structure:

```json
{
  "name": "Animal Name",
  "characteristics": {
    "diet": "Omnivore/Carnivore/Herbivore",
    "type": "Animal type"
  },
  "locations": ["Location1", "Location2"]
}
```

## Generated Output

The script generates an HTML file with:
- Animal name as the card title
- Diet information
- Primary location
- Animal type
- Responsive card-based layout with modern styling

## Error Handling

The application includes comprehensive error handling for:
- Missing or unreadable files
- Invalid JSON format
- File permission issues
- Empty data files

## Development

### Code Structure

- `load_data()`: Loads and validates JSON data with error handling
- `serialize_animal()`: Converts animal data to HTML card format
- `generate_animals_string()`: Processes all animals into HTML
- `generate_html()`: Creates final HTML file from template
- `main()`: Orchestrates the entire generation process

### Adding New Features

1. Modify the JSON structure in `animals_data.json`
2. Update the `serialize_animal()` function to handle new fields
3. Adjust the CSS in `animals_template.html` as needed

## License

This project is open source and available under the [MIT License](LICENSE).

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

---
