#from logic import make_empty_board
import logic
import csv
import pandas as pd
#import uuid


def read_games():
    try:
        return pd.read_csv('./games.csv')
    except FileNotFoundError:
        return pd.DataFrame(columns=[
            'Game ID',
            'Player A',
            'Player B',
            'Winner',
            'Total Moves',
            ])

def log(games, p1, p2, winner, moves):
    games.loc[len(games)] = {
        'Game ID' : len(games),
        'Player A' : p1,
        'Player B' : p2,
        "Winner" : winner,
        'Total Moves' : moves
    }




if __name__ == '__main__':
    board = logic.make_empty_board()
    winner = None
    player = None
    moves = 0
    games = read_games()
    #games = read_games()
    if player == None:
        player_with_bot = input('Are you playing alone? Please enter Y or N')
        if player_with_bot == 'N':
            player_name_a = input('Please enter your name')
            player = input('You are X. Please enter X to continue')
            print(player_name_a, ' you are ', player)
            player_b = logic.other_player(player)
            player_name_b = input('Please enter your name')
            print(player_name_b, ' you are ', player_b)
            turn = player
            while winner == None:
                if logic.board_with_space(board) is False:
                    winner = 'Even'
                    winner_name = 'Even'
                    print('This game ends in a draw')
                    log(games, player_name_a, player_name_b, winner_name, moves)
                    #games.append(pd.DataFrame({'Game ID' : str(uuid.uuid4()), 'Player A' : player_name_a, 'Player B' : player_name_b, 'Winner' : winner, 'Total Moves' : moves}))
                else:
                    print(turn, "TODO: take a turn!")
                    print('This is the current board', board)
                    player_row_choice = int(input('Please enter the row you want to change?'))
                    player_col_choice = int(input('Please enter the col you want to change?'))
                    if logic.empty_spot(board, player_row_choice, player_col_choice) is True:
                        logic.make_move(board, turn, player_row_choice, player_col_choice)
                        print('Here is the updated board: ', board)
                        moves += 1
                        if logic.get_winner(board) is not None:
                            winner = logic.get_winner(board)
                            print('Congratulations. ', winner, ' has won the game!')
                            if winner == 'X':
                                winner_name = player_name_a
                            else:
                                winner_name = player_name_b
                            log(games, player_name_a, player_name_b, winner_name, moves)
                            #games.append(pd.DataFrame({'Game ID' : str(uuid.uuid4()), 'Player A' : player_name_a, 'Player B' : player_name_b, 'Winner' : winner, 'Total Moves' : moves}))
                        else:
                            if turn == player:
                                turn = player_b
                            else:
                                turn = player
                    else:
                        print('Please re-enter your turn.')
        elif player_with_bot == 'Y':
            player_name_a = input('Please enter your name')
            player = input('You are X. Please enter X to continue')
            print(player_name_a, ' you are ', player)
            Bot = logic.bot(logic.other_player(player))
            player_name_b = "Bot"
            player_b = Bot.name()
            turn = player
            while winner == None:
                if logic.board_with_space(board) is False:
                    winner = 'Even'
                    winner_name = 'Even'
                    print('This game ends in a draw')
                    log(games, player_name_a, player_name_b, winner_name, moves)
                    #games.append(pd.DataFrame({'Game ID' : str(uuid.uuid4()), 'Player A' : player_name_a, 'Player B' : player_name_b, 'Winner' : winner, 'Total Moves' : moves}))
                else:
                    if turn == player:
                        print(turn, "TODO: take a turn!")
                        print('This is the current board', board)
                        player_row_choice = int(input('Please enter the row you want to change?'))
                        player_col_choice = int(input('Please enter the col you want to change?'))
                        if logic.empty_spot(board, player_row_choice, player_col_choice) is True:
                            logic.make_move(board, turn, player_row_choice, player_col_choice)
                            print('Here is the updated board: ', board)
                            moves += 1
                            if logic.get_winner(board) is not None:
                                winner = logic.get_winner(board)
                                if winner == 'X':
                                    winner_name = player_name_a
                                else:
                                    winner_name = player_name_b
                                print('Congratulations. ', winner, ' has won the game!')
                                log(games, player_name_a, player_name_b, winner_name, moves)
                                #games.append(pd.DataFrame({'Game ID' : str(uuid.uuid4()), 'Player A' : player_name_a, 'Player B' : player_name_b, 'Winner' : winner, 'Total Moves' : moves}))
                            else:
                                turn = player_b
                        else:
                            print('Please re-enter your turn')
                    elif turn == player_b:
                        logic.bot.move(board, player_b)
                        print('Here is the updated board: ', board)
                        moves += 1
                        if logic.get_winner(board) is not None:
                            winner = logic.get_winner(board)
                            if winner == 'X':
                                winner_name = player_name_a
                            else:
                                winner_name = player_name_b
                            print('Congratulations. ', winner, ' has won the game!')
                            log(games, player_name_a, player_name_b, winner_name, moves)
                            #games.append(pd.DataFrame({'Game ID' : str(uuid.uuid4()), 'Player A' : player_name_a, 'Player B' : player_name_b, 'Winner' : winner, 'Total Moves' : moves}))
                        else:
                            turn = player
        games.to_csv('./games.csv')





        # TODO: Show the board to the user.
        # TODO: Input a move from the player.
        # TODO: Update the board.
        # TODO: Update who's turn it is.
