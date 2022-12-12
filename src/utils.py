import json
import os
import re
import sys
from .characters import Character

FIGHT_SCRIPT_PATH = os.path.join("src", "../fight_script.json")
CHARACTERS_PATH = os.path.join("src", "../characters_data.json")
MOVES = ('W', 'A', 'S', 'D')
HITS = ('P', 'K')
MOVE_DICT = {
            "A": "retrocede",
            "S": "se agacha",
            "D": "avanza",
            "W": "salta"
        }

def json_validator(file_path: str):
    path = file_path
    with open(path, 'r', encoding='utf-8') as json_file:
        try:
            data = json.load(json_file)
            return data
        except json.JSONDecodeError as e:
            print("Error en el formato del archivo JSON")
            raise e

def get_characters():
    data = json_validator(CHARACTERS_PATH)
    return data

def death(player):
    #deth
    player.is_alive = 0

def get_fight_script():
    data = json_validator(FIGHT_SCRIPT_PATH)
    return data

def name_prettier(name):   
    return re.sub("_.+","", name).capitalize()

def character_builder():
    characters = get_characters()
    fight_script = get_fight_script()
    index = 1
    for character in characters:
        character.update(fight_script['player'+str(index)])
        index += 1
    player1 = Character(name_prettier(characters[0]['name']), characters[0]['movimientos'], characters[0]['golpes'], characters[0]['techniques'])
    player2 = Character(name_prettier(characters[1]['name']), characters[1]['movimientos'], characters[1]['golpes'], characters[1]['techniques'])
    players= player1, player2
    actions_validator(players)
    return player1, player2
    
def first_move(player1: Character, player2: Character) -> Character:
    player1_moves = len([moves for moves in player1.movements if moves != ''])
    player1_hits = len([hits for hits in player1.hits if hits != ''])

    player2_hits = len([hits for hits in player2.hits if hits != ''])
    player2_moves = len([moves for moves in player2.movements if moves != ''])
    
    player1_actions = player1_moves + player1_hits
    player2_actions = player2_moves + player2_hits
    if player1_actions < player2_actions:
        return player1
    elif player1_actions == player2_actions:
        if player1_moves < player2_moves:
            return player1
        elif player1_moves == player2_moves:
            if player1_hits < player2_hits:
                return player1
            else:
                return player1
        else:
            return player2
    else:
        return player2

def actions_validator(players):
    for player in players:
        if len(player.movements) > 5:
            sys.exit("Error: Cantidad maxima de movimientos superada.")
        if len(player.hits) > 5:
            sys.exit("Error: Cantidad maxima de golpes superada.")
        for movement in player.movements:
            for letter in movement:
                if any(letter in moves for moves in MOVES):
                    pass
                else:
                    sys.exit("Error: Movimiento invalido.")
        for hits in player.hits:
            for letter in hits:
                if any(letter in hit for hit in HITS):
                    pass
                else:
                    sys.exit("Error: Golpe invalido.")
                if len(hits) > 1:
                    sys.exit("Error: Cantidad maxima de golpes superada.")

def check_technique(player, turn):
    player_action = player.movements[turn] + player.hits[turn]
    for technique in player.specials:
        if player_action == technique['combination']:
            if technique['name'] == "punch" or technique['name'] == "kick":
                return None
            return technique['name']

def check_movement(move_dict, movements):
    move_list = []
    d_keys = move_dict.keys()
    for move in movements:
        for pattern in d_keys:
            if move == pattern:
                move_list.append(move_dict[move])
    return move_list
   
def action_prettier(action):
    if len(action) == 1:
        return action[0]
    replacement = " y"
    delimiter = ","
    start, _, end = ', '.join(action).rpartition(delimiter)
    return start + replacement + end

def check_hit(hit):
    if hit == "P": 
        return "da un puñetazo" 
    if hit == "K": 
        return "da una patada" 

def check_combination(movements, hit):
    d_moves = check_movement(MOVE_DICT, movements)
    d_hit = check_hit(hit)
    d_moves.append(d_hit)
    return action_prettier(d_moves)

def technique_cost(technique, player):
    for special in player.specials:
        if special['name'] == technique:
            return special['energy_points'] 

def game_narrator_energy(player, turn):
    if player.name == "Arnaldor":
        #technique
        technique = check_technique(player, turn)
        if player.movements[turn] == "" and player.hits[turn] == "":
            print(f"{player.name} pasa su turno")
            return 0
        elif technique:
            print(f"{player.name} lanza un devastador {technique}")
            return technique_cost(technique, player)
        #only movement
        elif player.movements[turn] != "" and player.hits[turn] == "":
            movements = check_movement(MOVE_DICT, player.movements[turn])
            print(f"{player.name} {action_prettier(movements)}")
            return 0
        #only hit
        elif player.movements[turn] == "" and player.hits[turn] != "":
            print(f"{player.name} {check_hit(player.hits[turn])}")
            return 1
        else:
            combinations = check_combination(player.movements[turn], player.hits[turn])
            print(f"{player.name} {combinations}")
            return 1

    elif player.name == "Tony":
        #technique
        technique = check_technique(player, turn)
        if player.movements[turn] == "" and player.hits[turn] == "":
            print(f"{player.name} pasa su turno")
            return 0
        elif technique:
            print(f"{player.name} lanza un devastador {technique}")
            return technique_cost(technique, player)
        #only movement
        elif player.movements[turn] != "" and player.hits[turn] == "":
            movements = check_movement(MOVE_DICT, player.movements[turn])
            print(f"{player.name} {action_prettier(movements)}")
            return 0
        #only hit
        elif player.movements[turn] == "" and player.hits[turn] != "":
            print(f"{player.name} {check_hit(player.hits[turn])}")
            return 1
        else:
            combinations = check_combination(player.movements[turn], player.hits[turn])
            print(f"{player.name} {combinations}")
            return 1

        
        
        
    
