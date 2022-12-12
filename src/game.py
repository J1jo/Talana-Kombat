from .utils import character_builder, first_move, game_narrator_energy, death

class Game:

    def __init__(self):
        print("Bienvenido a TalanaKombat")
        print("Cargando Personajes...")
        players = character_builder()
        self.game_match(players)

    def game_match(self, players):
        player = first_move(players[0], players[1])
        print("El Kombate comienza con " + player.name + "!!")
        if player == players[0]:
            player1 = players[0]
            player2 = players[1]
        else:
            player1 = players[1]
            player2 = players[0]
        turn = 0
        while player1.is_alive and player2.is_alive and turn < 5:   
            #first player turn 
            ene1 = game_narrator_energy(player1, turn)
            player2.energy = player2.energy - ene1
            if player2.energy <= 0:
                death(player2)
                print(f"Una increible victoria por parte de {player1.name}, conserva {player1.energy} de energia")
                break
            #second player turn
            ene2 = game_narrator_energy(player2, turn)
            player1.energy = player1.energy - ene2
            if player1.energy <= 0:
                death(player1)
                print(f"Una increible victoria por parte de {player2.name}, conserva {player2.energy} de energia")
            turn += 1
        if player1.is_alive and player2.is_alive:
            if player1.energy == player2.energy:
                print(f"Un increible empate por parte de {player1.name} y {player2.name}, ambos jugadores con {player1.energy} de energia restante")
            elif player1.energy > player2.energy:
                print(f"Una increible victoria por parte de {player1.name}, conserva {player1.energy} de energia")
            else:
                print(f"Una increible victoria por parte de {player2.name}, conserva {player1.energy} de energia")
