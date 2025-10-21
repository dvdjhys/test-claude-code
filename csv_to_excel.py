#!/usr/bin/env python3

import pandas as pd

def main():
    # Read the CSV file
    df = pd.read_csv('premier_league_standings.csv')

    # Write to Excel file
    df.to_excel('premier_league_standings.xlsx', index=False, sheet_name='Standings')

    print("Excel file created successfully: premier_league_standings.xlsx")

if __name__ == "__main__":
    main()
