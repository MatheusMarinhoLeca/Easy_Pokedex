# Easy Pokédex
Easy Pokédex is a convenient tool that allows you to access detailed information about Pokémon without having to capture them.

## Features
- **Search Pokémon by Name or ID**: Easily search for any Pokémon by entering its name or ID in the search bar.
- **Random Pokémon Generator**: Generate and display a random Pokémon with just one click.
- **Detailed Pokémon Information**: View comprehensive details about each Pokémon, including:
  - Abilities
  - Types
  - Height and Weight
  - Base Experience
  - Stats such as HP, Attack, Defense, and Speed
- **Dynamic Type Coloring**: The background color changes dynamically based on the primary type of the Pokémon.
- **Pokémon Images**: Display high-quality Pokémon images in the application window.
- **Pokémon Sidebar**: A sidebar feature will allow users to browse a complete list of all Pokémon, making it easier to explore the available options.

## Configuration
#### Prerequisites
- Python 3.10
- Pip (Python package manager)
- Virtual environment (recommended for isolated Python environments)

### Setup Instructions

#### **Run Locally**
1. **Clone the repository**:  
   ```bash
   git clone https://github.com/MatheusMarinhoLeca/Easy_Pokedex.git
   ```

2. **Create a virtual environment**:  
   In the project’s root directory, create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:  
   Install the required dependencies using `pip`:
   ```bash
   pip install .
   ```

4. **Run the application**:  
   To run the application locally, use:
   ```bash
   easy-pokedex
   ```
#### **Run with Docker**

1. **Run with Docker Compose**:
   For a simplified and consistent setup, use the provided `docker-compose.yml` file:
   ```bash
   DISPLAY=<your_display_variable> X11_SOCKET=<your_x11_socket_path> docker-compose up
   ```

### **Notes for Different Platforms**
  - **macOS**: Install and run [XQuartz](https://www.xquartz.org/), enable "Allow connections from network clients" in Preferences, and run `xhost + 127.0.0.1`. Set `DISPLAY` to `host.docker.internal:0` and ensure `/tmp/.X11-unix` exists.
  - **Linux**: Set `DISPLAY` to `:0` and ensure the X11 server is running. Verify that `/tmp/.X11-unix` is accessible.
  - **Windows**: Install and run an X11 server like [VcXsrv](https://vcxsrv.com). Set `DISPLAY` to `host.docker.internal:0.0` and create `C:/tmp/.X11-unix`.
    
## Feedback
If you have any feedback, feel free to reach out to me at matheus.demoraisleca@ucalgary.ca

## Authors
- [@MatheusMarinhoLeca](https://github.com/MatheusMarinhoLeca)

## Contributing
Contributions are welcome! Please check the [CONTRIBUTING.md](CONTRIBUTING.md) file for guidelines on how to contribute to this project.

## License
This project is copyright Matheus Marinho de Morais Leça. It is licensed under the MIT license. See the following file for the complete license:
[MIT License](LICENSE).

Pokémon and Pokémon character names are trademarks of Nintendo.
