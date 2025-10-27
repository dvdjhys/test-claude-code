#!/usr/bin/env python3
"""
Premier League Table PDF Generator

This script reads the Premier League standings from a CSV file and generates
a formatted PDF document containing the table.
"""

import csv
from datetime import datetime
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.enums import TA_CENTER


def read_standings_csv(csv_file):
    """Read the Premier League standings from a CSV file."""
    standings = []
    with open(csv_file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            standings.append(row)
    return standings


def create_pdf(standings, output_file='premier_league_table.pdf'):
    """Create a PDF document with the Premier League table."""

    # Create PDF document
    doc = SimpleDocTemplate(
        output_file,
        pagesize=landscape(A4),
        rightMargin=30,
        leftMargin=30,
        topMargin=30,
        bottomMargin=30
    )

    # Container for the 'Flowable' objects
    elements = []

    # Define styles
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=colors.HexColor('#37003C'),  # Premier League purple
        spaceAfter=30,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )

    date_style = ParagraphStyle(
        'DateStyle',
        parent=styles['Normal'],
        fontSize=10,
        textColor=colors.grey,
        spaceAfter=20,
        alignment=TA_CENTER
    )

    # Add title
    title = Paragraph("Premier League Standings", title_style)
    elements.append(title)

    # Add current date
    current_date = datetime.now().strftime("%B %d, %Y")
    date_text = Paragraph(f"Generated on {current_date}", date_style)
    elements.append(date_text)

    # Prepare table data
    table_data = [
        ['Pos', 'Team', 'P', 'W', 'D', 'L', 'GF', 'GA', 'GD', 'Pts']
    ]

    for row in standings:
        table_data.append([
            row['Position'],
            row['Team'],
            row['Played'],
            row['Won'],
            row['Drawn'],
            row['Lost'],
            row['GF'],
            row['GA'],
            row['GD'],
            row['Points']
        ])

    # Create table
    table = Table(table_data, colWidths=[
        0.4*inch,  # Position
        2.2*inch,  # Team
        0.4*inch,  # Played
        0.4*inch,  # Won
        0.4*inch,  # Drawn
        0.4*inch,  # Lost
        0.4*inch,  # GF
        0.4*inch,  # GA
        0.5*inch,  # GD
        0.5*inch   # Points
    ])

    # Style the table
    table_style = TableStyle([
        # Header row
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#37003C')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('TOPPADDING', (0, 0), (-1, 0), 12),

        # Team name column - left aligned
        ('ALIGN', (1, 1), (1, -1), 'LEFT'),

        # Data rows
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 9),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#F0F0F0')]),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('TOPPADDING', (0, 1), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 8),

        # Highlight top 4 (Champions League spots)
        ('TEXTCOLOR', (0, 1), (-1, 4), colors.HexColor('#00FF87')),
        ('FONTNAME', (0, 1), (0, 4), 'Helvetica-Bold'),

        # Highlight relegation zone (bottom 3)
        ('TEXTCOLOR', (0, 18), (-1, 20), colors.HexColor('#FF0000')),
        ('FONTNAME', (0, 18), (0, 20), 'Helvetica-Bold'),
    ])

    table.setStyle(table_style)
    elements.append(table)

    # Add legend
    elements.append(Spacer(1, 20))
    legend_style = ParagraphStyle(
        'Legend',
        parent=styles['Normal'],
        fontSize=8,
        textColor=colors.grey,
        alignment=TA_CENTER
    )
    legend = Paragraph(
        "<font color='#00FF87'>■</font> Champions League Qualification   "
        "<font color='#FF0000'>■</font> Relegation Zone",
        legend_style
    )
    elements.append(legend)

    # Build PDF
    doc.build(elements)
    print(f"PDF generated successfully: {output_file}")


def main():
    """Main function to generate the PDF."""
    csv_file = 'premier_league_standings.csv'
    output_file = 'premier_league_table.pdf'

    try:
        standings = read_standings_csv(csv_file)
        create_pdf(standings, output_file)
    except FileNotFoundError:
        print(f"Error: Could not find {csv_file}")
        print("Please ensure the CSV file exists in the current directory.")
    except Exception as e:
        print(f"Error generating PDF: {e}")


if __name__ == '__main__':
    main()
