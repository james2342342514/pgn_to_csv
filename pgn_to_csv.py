import re
import csv
from datetime import datetime

def parse_pgn(pgn_text):
    games = re.split(r'\n\n\[Event', pgn_text)
    games = ['[Event' + game if i > 0 else game for i, game in enumerate(games)]
    
    parsed_games = []
    for game in games:
        game_data = {}
        headers = re.findall(r'\[(\w+)\s+"(.+?)"\]', game)
        for key, value in headers:
            game_data[key] = value
        
        moves = re.search(r'(1\..+?(?=\n\n|\Z))', game, re.DOTALL)
        if moves:
            game_data['Moves'] = moves.group(1).replace('\n', ' ')
        
        parsed_games.append(game_data)
    
    return parsed_games

def pgn_to_csv(pgn_text, output_file):
    games = parse_pgn(pgn_text)
    
    if not games:
        print("No games found in the PGN text.")
        return
    
    fieldnames = ['Date', 'White', 'Black', 'Result', 'WhiteElo', 'BlackElo', 'TimeControl', 'Termination', 'Moves']
    
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for game in games:
            row = {
                'Date': game.get('Date', ''),
                'White': game.get('White', ''),
                'Black': game.get('Black', ''),
                'Result': game.get('Result', ''),
                'WhiteElo': game.get('WhiteElo', ''),
                'BlackElo': game.get('BlackElo', ''),
                'TimeControl': game.get('TimeControl', ''),
                'Termination': game.get('Termination', ''),
                'Moves': game.get('Moves', '')
            }
            writer.writerow(row)
    
    print(f"CSV file '{output_file}' has been created successfully.")

# Ask for the input filename
input_filename = input("Enter the name of your PGN file: ")

# Read the PGN content from the file
try:
    with open(input_filename, 'r') as file:
        pgn_content = file.read()
except FileNotFoundError:
    print(f"Error: The file '{input_filename}' was not found.")
    exit()

# Generate output filename with current timestamp
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
output_filename = f'chess_games_{timestamp}.csv'

# Convert PGN to CSV
pgn_to_csv(pgn_content, output_filename)