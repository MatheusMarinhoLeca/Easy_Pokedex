"""
Copyright Matheus Marinho de Morais Leça, 2024
Licensed under MIT license.
See LICENSE for more information. 
"""

# Imports
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random
import json
from typing import Any
from functools import cache

# Defining color palette
primary_color = "white"
secondary_color = "#aba4f2"
tertiary_color = "#8b95f2"
background_color = "#d4b7ed"

def get_type_color(pokemon_type: str):
    """
    Returns the background color associated with a given Pokémon type.

    Args:
        pokemon_type (str): The type of Pokémon (e.g., 'fire', 'water').

    Returns:
        str: The corresponding color code in hexadecimal format for the given Pokémon type.
        If the type is not found, it returns '#FFFFFF' (white) by default.
    """
    type_colors = {
        "normal": "#E5E5D7",
        "fire": "#FBC6A4",
        "water": "#A9D4F5",
        "electric": "#FAE696",
        "grass": "#C4E7A1",
        "ice": "#D3F2F0",
        "fighting": "#E8A3A0",
        "poison": "#D9A4D9",
        "ground": "#F0E2B8",
        "flying": "#D7CFF5",
        "psychic": "#F9B3C4",
        "bug": "#DDE4A1",
        "rock": "#E4D5A1",
        "ghost": "#C7B5E3",
        "dragon": "#BCA9F9",
        "dark": "#D4C6B8",
        "steel": "#D8D8E9",
        "fairy": "#F7CCE2"
    }
    return type_colors.get(pokemon_type.lower(), "#FFFFFF")  # Default to white if type not found

def create_window():
    """
    Creates and configures the main window of the Easy Pokédex application.
    
    This includes setting up the welcome frame, search bar, buttons for searching and loading
    random Pokémon, and main display frame for showing Pokémon images and information.

    Returns:
        None
    """
    window = tk.Tk()
    window.title("Easy Pokédex")
    window.geometry("1280x720")
    window.config(bg=background_color)
    
    # Setting window icon
    try:
        img = tk.Image("photo", file="./images/pokedex.png")
        window.tk.call('wm', 'iconphoto', window._w, img)
    except Exception as e:
        print(f"Could not load icon: {e}")


    # Sidebar for Pokémon list
    sidebar = tk.Frame(window, width=300, bg=secondary_color)
    sidebar.pack(side="left", fill="y")

    sidebar_label = tk.Label(sidebar, text="Pokémon List", font=("Arial", 16), bg=secondary_color, fg=primary_color)
    sidebar_label.pack(pady=10)

    # Scrollbar and Listbox
    listbox_frame = tk.Frame(sidebar, bg=secondary_color)
    listbox_frame.pack(fill="both", expand=True, padx=10, pady=10)

    scrollbar = tk.Scrollbar(listbox_frame)
    scrollbar.pack(side="right", fill="y")

    listbox = tk.Listbox(listbox_frame, font=("Arial", 14), bg=primary_color, fg=secondary_color, yscrollcommand=scrollbar.set)
    listbox.pack(side="left", fill="both", expand=True)

    # Configure scrollbar to work with the listbox
    scrollbar.config(command=listbox.yview)

    for pokemon in load_all_pokemon_data():
        listbox.insert(tk.END, pokemon['name'].capitalize())

    # Function to load Pokémon from the sidebar
    def on_pokemon_select(event):
        selected_pokemon = listbox.get(listbox.curselection())
        load_pokemon(selected_pokemon, frame, pokemon_info_label, image_label)

    listbox.bind("<<ListboxSelect>>", on_pokemon_select)

    # Welcome Frame where is displayed the welcome message along with the search bar and buttons
    welcome_frame = tk.Frame(window, width=400, height=220, bg=tertiary_color)
    welcome_frame.pack(pady=30)
    welcome_frame.pack_propagate(0)  # Prevent the frame from resizing to fit its content

    label = tk.Label(welcome_frame, text="Welcome to Easy Pokédex\n\nEnter Pokémon Name or ID:", font=("Arial", 18), bg=tertiary_color, fg=primary_color)
    label.place(relx=0.5, rely=0.2, anchor='center')

    pokemon_entry = tk.Entry(welcome_frame, font=("Arial", 14), fg=secondary_color, bg=primary_color, bd=0, highlightthickness=0)
    pokemon_entry.place(relx=0.5, rely=0.5, anchor='center')

    search_button = tk.Button(welcome_frame, text="Search Pokémon", command=lambda: load_pokemon(pokemon_entry.get(), frame, pokemon_info_label, image_label), fg=secondary_color, bd=0, highlightbackground=tertiary_color)
    search_button.place(relx=0.5, rely=0.7, anchor='center')

    load_button = tk.Button(welcome_frame, text="Get Random Pokémon", command=lambda: load_pokemon(return_random_pokemon_id(), frame, pokemon_info_label, image_label), fg=secondary_color, bd=0, highlightbackground=tertiary_color)
    load_button.place(relx=0.5, rely=0.85, anchor='center')

    # Main frame for displaying Pokémon image and info
    frame = tk.Frame(window, width=700, height=650, bg=tertiary_color)
    frame.pack()
    frame.pack_propagate(0) 
    frame.pack_forget()  # Hide initially

    # Sub-frame for organizing image and info inside the main frame
    content_frame = tk.Frame(frame, bg=tertiary_color)
    content_frame.place(relx=0.5, rely=0.5, anchor='center')

    image_label = tk.Label(content_frame, width=200, height=200, bg=tertiary_color)
    image_label.pack(pady=10)

    pokemon_info_label = tk.Label(content_frame, text="", font=("Arial", 18), bg=tertiary_color, fg=primary_color)
    pokemon_info_label.pack(pady=10)

    window.mainloop()

@cache
def load_all_pokemon_data() -> list[dict[str, Any]]:
    """
    Loads all Pokémon data from the JSON file.

    Returns:
        list[dict[str, Any]]: A list of dictionaries containing the Pokémon data.

    Note:
        The data is cached to avoid reading the file multiple times.
    """
    with open('data/pokemon_data.json', 'r') as file:
        return json.load(file)

def load_pokemon_data(name_or_id: str):
    """
    Loads the Pokémon data from the JSON file based on the name or ID.

    Args:
        name_or_id (str): The name or ID of the Pokémon.

    Returns:
        dict: A dictionary containing the Pokémon's data.
    
    Raises:
        ValueError: If the Pokémon is not found.
    """
    try:
        # Load Pokémon data from JSON file
        pokemon_data = load_all_pokemon_data()

        # Find the Pokémon by name or ID
        for poke in pokemon_data:
            if poke['name'].lower() == name_or_id.lower() or str(poke['id']) == name_or_id:
                return poke

        raise ValueError("Pokémon not found")
    except Exception as e:
        raise Exception(f"Error loading Pokémon data: {e}")


def update_pokemon_info(pokemon: dict, frame: tk.Frame, info_label: tk.Label, image_label: tk.Label):
    """
    Updates the GUI with the Pokémon's image and stats.

    Args:
        pokemon (dict): The Pokémon's data.
        frame (tk.Frame): The frame in which the Pokémon data will be displayed.
        info_label (tk.Label): The label where Pokémon stats and abilities will be shown.
        image_label (tk.Label): The label where the Pokémon image will be displayed.

    Returns:
        None
    """
    try:
        # Load and resize the Pokémon image
        image = Image.open(pokemon['image_path'])
        image = image.resize((200, 200), Image.LANCZOS)
        img = ImageTk.PhotoImage(image)

        # Set the background color based on the Pokémon type
        pokemon_type = pokemon['type'][0].lower()
        image_label.config(image=img, bg=get_type_color(pokemon_type))
        image_label.image = img

        # Pokémon information
        abilities = ', '.join([str(ability[0]) for ability in pokemon['abilities']])
        pokemon_info = (
            f"{pokemon['id']} - {pokemon['name'].capitalize()}\n"
            f"Abilities: {abilities}\n"
            f"Types: {', '.join(pokemon['type'])}\n"
            f"Height: {pokemon['height']}m Weight: {pokemon['weight']}kg\n"
            f"Base Experience: {pokemon['base_experience']}xp\n"
            f"HP: {pokemon['hp']} Attack: {pokemon['attack']} Defense: {pokemon['defense']} Speed: {pokemon['speed']}"
        )
        info_label.config(text=pokemon_info)

        # Show frame and labels
        frame.pack(pady=30)
    except Exception as e:
        # Hide frame if loading fails
        frame.pack_forget()
        messagebox.showerror("Error", f"Could not display Pokémon data: {e}")


def load_pokemon(name_or_id: str, frame: tk.Frame, info_label: tk.Label, image_label: tk.Label):
    """
    Function that calls the necessary functions to load and display the Pokémon data.

    Args:
        name_or_id (str): The name or ID of the Pokémon to load.
        frame (tk.Frame): The frame in which the Pokémon data will be displayed.
        info_label (tk.Label): The label where Pokémon stats and abilities will be shown.
        image_label (tk.Label): The label where the Pokémon image will be displayed.

    Returns:
        None
    """
    try:
        # Load the Pokémon data
        pokemon = load_pokemon_data(name_or_id)

        # Update the GUI with the Pokémon data
        update_pokemon_info(pokemon, frame, info_label, image_label)
    except Exception as e:
        messagebox.showerror("Error", f"Could not load Pokémon: {e}")

def return_random_pokemon_id():
    """
    Returns a random Pokémon ID for selecting a random Pokémon from the available dataset.

    Returns:
        str: A string representing a random Pokémon ID between 0 and 1025.
    """
    return str(random.randint(0, 1025))

def main():
    """
    The main function that starts the Easy Pokédex application by calling `create_window()`.

    Returns:
        None
    """
    create_window()

if __name__ == "__main__":
    main()
