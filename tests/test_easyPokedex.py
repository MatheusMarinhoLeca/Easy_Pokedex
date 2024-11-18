"""
Copyright Matheus Marinho de Morais Leça, 2024
Licensed under MIT license.
See LICENSE for more information. 
"""

import pytest
from unittest.mock import mock_open, patch
from easy_pokedex import get_type_color, load_pokemon_data, return_random_pokemon_id

def test_get_type_color_valid_type():
    assert get_type_color("fire") == "#FBC6A4"
    assert get_type_color("WATER") == "#A9D4F5"
    assert get_type_color("Electric") == "#FAE696"

def test_get_type_color_invalid_type():
    assert get_type_color("unknown") == "#FFFFFF"
    assert get_type_color("") == "#FFFFFF"

@patch("easy_pokedex.open", new_callable=mock_open, read_data='[{"id": 1, "name": "bulbasaur", "type": ["grass", "poison"], "image_path": "image.png", "abilities": [["overgrow"]], "height": 0.7, "weight": 6.9, "base_experience": 64, "hp": 45, "attack": 49, "defense": 49, "speed": 45}]')
def test_load_pokemon_data_valid(mock_open_file):
    pokemon = load_pokemon_data("bulbasaur")
    assert pokemon["name"] == "bulbasaur"
    assert pokemon["id"] == 1
    assert "grass" in pokemon["type"]

@patch("easy_pokedex.open", new_callable=mock_open, read_data="[]")
def test_load_pokemon_data_not_found(mock_open_file):
    with pytest.raises(Exception, match="Pokémon not found"):
        load_pokemon_data("unknown")

def test_return_random_pokemon_id():
    with patch("random.randint", return_value=500):
        assert return_random_pokemon_id() == "500"
