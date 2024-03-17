"""Access the COP csv file.

The Code of Points is determined by the FIG roughly every quad. Manual transcription from pdf to Google Sheets is
currently required.
"""

from enum import Enum

import pandas as pd

from apparatus import Apparatus


class Sport(Enum):
    """Sport of competition."""
    WAG = 'WAG'
    MAG = 'MAG'


class Level(Enum):
    """Level of competition."""
    ELITE = 'Elite'
    NCAA = 'NCAA'
    LEVEL_10 = 'Level 10'


class COP:
    """COP table loaded from Google Sheet.
    
    Attributes:
        VERSIONS (dict): Spreadsheet and sheet IDs indexed by sports, levels, and year ranges.
        table (dict): Tables of elements indexed by apparatus.
    """
    VERSIONS = {
        Sport.WAG: {
            Level.ELITE: {
                '2022-2024': {
                    'sheet': '1wUqoO0gyoenjGfmjjfv9H43j6yspyeXeshkX3N1eoxM',
                    Apparatus.VT: '766515617',
                    Apparatus.UB: '0',
                    Apparatus.BB: '1712667509',
                    Apparatus.FX: '1161968013'
                }
            }
        }
    }
    
    def __init__(self, sport, level, start_year=None, end_year=None):
        """_summary_

        Args:
            sport (Sport): Sport of competition.
            level (Level): Level of competition, as different levels have different COPs.
            start_year (int, optional): Starting year for the desired COP. Defaults to None.
            end_year (int, optional): Ending year for the desired COP. Defaults to None.

        Raises:
            ValueError: Either start_year or end_year must be specified.
            ValueError: Specified start_year and end_year must correspond to a valid COP.
        """
        end_year = 2021 if end_year == 2020 else end_year  # COVID reasons aka Morgan Hurd's year
        if not start_year and not end_year:
            raise ValueError('Either start_year or end_year must be specified.')
        if not self.VERSIONS.get(sport):
            raise ValueError(f'Sport {sport.value} COP not supported yet.')
        if not self.VERSIONS[sport].get(level):
            raise ValueError(f'Sport {sport.value} level {level.value} COP not supported yet.')
        
        version = self.VERSIONS[sport][level]
        if start_year and end_year:
            if f'{start_year}-{end_year}' not in version:
                raise ValueError('Specified start_year and end_year do not correspond to a valid COP.')
            years = f'{start_year}-{end_year}'
        elif start_year:
            find_start_year = [f'{start_year}-' in years for years in version.keys()]
            if any(find_start_year):
                years = version.keys()[find_start_year.index(True)]
            else:
                raise ValueError('Specified start_year does not correspond to a valid COP.')
        else:
            find_end_year = [f'-{end_year}' in years for years in version.keys()]
            if any(find_end_year):
                years = version.keys()[find_end_year.index(True)]
            else:
                raise ValueError('Specified end_year does not correspond to a valid COP.')
        
        version = version[years]
        sheet_prefix = f'https://docs.google.com/spreadsheets/d/{version["sheet"]}/export?gid='
        for apparatus in Apparatus:
            self.table[apparatus] = pd.read_csv(f'{sheet_prefix}{version[apparatus]}&format=csv')
