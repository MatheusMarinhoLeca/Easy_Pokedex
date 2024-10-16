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

# Defining color palette
primary_color = "white"
secondary_color = "#aba4f2"
tertiary_color = "#8b95f2"
background_color = "#d4b7ed"

'''This function returns the background color for a given Pokémon type.'''
def get_type_color(pokemon_type: str):
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

'''This function creates the main window of the application.'''
def create_window():
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

    load_pokemon(return_random_pokemon_id(), frame, pokemon_info_label, image_label)
    window.mainloop()

'''This function loads the Pokémon data and displays it in the given label.'''
def load_pokemon(name_or_id: str, frame: tk.Frame, info_label: tk.Label, image_label: tk.Label):
    try:
        # Load Pokémon data from JSON file
        with open('pokemon_data.json', 'r') as file:
            pokemon_data = json.load(file)

        pokemon = None
        for poke in pokemon_data:
            if poke['name'].lower() == name_or_id.lower() or str(poke['id']) == name_or_id:
                pokemon = poke
                break

        if not pokemon:
            raise ValueError("Pokémon not found")
        
        # Loads and resizes the Pokémon image
        image = Image.open(pokemon['image_path'])
        image = image.resize((200, 200), Image.LANCZOS)

        # Convert the image to a PhotoImage for Tkinter
        img = ImageTk.PhotoImage(image)

        # Set the background color based on the Pokémon type
        pokemon_type = pokemon['type'][0].lower()
        image_label.config(image=img, bg=get_type_color(pokemon_type))

        image_label.image = img

        # Pokémon information
        abilities = ', '.join([str(ability[0]) for ability in pokemon['abilities']])
        pokemon_info = f"{pokemon['id']} - {pokemon['name'].capitalize()}\nAbilities: {abilities}\nTypes: {', '.join(pokemon['type'])}\nHeight: {pokemon['height']}m Weight: {pokemon['weight']}kg Base Experience: {pokemon['base_experience']}xp\nHP: {pokemon['hp']} Attack: {pokemon['attack']} Defense: {pokemon['defense']} Speed: {pokemon['speed']}"
        info_label.config(text=pokemon_info)

        # Show frame and labels when data is successfully loaded
        frame.pack(pady=30)

    except Exception as e:
        # Hide frame if loading fails
        frame.pack_forget()
        messagebox.showerror("Error", f"Could not load Pokémon: {e}")

'''This function returns a random Pokémon ID.'''
def return_random_pokemon_id():
    return str(random.randint(0, 1025))

def main():
    create_window()

main()
