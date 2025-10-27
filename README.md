# Premier League Table PDF Generator

A Python utility to generate a formatted PDF document containing the current Premier League standings.

## Features

- Reads Premier League standings from CSV
- Generates a professionally formatted PDF with:
  - Team positions, stats (Played, Won, Drawn, Lost, Goals For/Against, Goal Difference, Points)
  - Color-coded Champions League qualification spots (green)
  - Color-coded relegation zone (red)
  - Premier League branding colors
  - Current date stamp

## Requirements

```bash
pip install -r requirements.txt
```

## Usage

1. Ensure `premier_league_standings.csv` is in the current directory
2. Run the generator:

```bash
python3 generate_pl_table_pdf.py
```

3. The PDF will be created as `premier_league_table.pdf`

## Files

- `generate_pl_table_pdf.py` - Main PDF generator script
- `premier_league_standings.csv` - Source data for the table
- `csv_to_excel.py` - Utility to convert CSV to Excel format
- `requirements.txt` - Python dependencies

## CSV Format

The input CSV should have the following columns:
- Position, Team, Played, Won, Drawn, Lost, GF, GA, GD, Points
