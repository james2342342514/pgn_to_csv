# PGN to CSV Converter

This Python script converts chess games from PGN (Portable Game Notation) format to CSV (Comma-Separated Values) format. It's designed to work with PGN files exported from Chess.com, but should be compatible with standard PGN formats from other sources as well.

## Features

- Reads a PGN file and parses multiple chess games
- Extracts key information such as date, players, ratings, result, and moves
- Converts the data into a structured CSV format
- Generates a timestamped output file for easy tracking
- Handles potential errors gracefully, such as file not found

## Usage

1. Run the script: `python pgn_to_csv.py`
2. When prompted, enter the name of your PGN file
3. The script will generate a CSV file with the parsed game data

## Output

The resulting CSV file includes the following columns:
- Date
- White (player)
- Black (player)
- Result
- WhiteElo (rating)
- BlackElo (rating)
- TimeControl
- Termination
- Moves

This tool is useful for chess players and analysts who want to process their game data in spreadsheet applications or perform further analysis using data science tools.
This was built 90% with Claude 3.5 sonnet. 
