from pathlib import Path

import geopandas as gpd
import pandas as pd

ARCHIVE_PATH = Path('/share/appdata/qgreenland-private-archive/eva_placenames/')
DATA_PATH = ARCHIVE_PATH / '20201112_Oqaasileriffik_place-name register/20201112_Oqaasileriffik_place-name register.TAB'
TRANSLATION_PATH = ARCHIVE_PATH / '2021 0119_Oqaasileriffik_place-name categories_ENG.csv'


data_ds = gpd.read_file(DATA_PATH, encoding='utf8')
data_join_column = 'Genstand'
translated_ds = pd.read_csv(TRANSLATION_PATH)

# rename the columns in the translation document
translated_ds = translated_ds.rename(columns={
    'Danish abbreviation\n\nNaalisaat': data_join_column,
    'Danish explanation on what \nthe abbreviation stands for\n\nSuussuseq qallunaatut': 'Danish explanation of Object designation',
    'Greenlandic explanation on what \nthe abbreviation stands for\n\nSuussuseq kalaallisut': 'Greenlandic explanation of Object designation',
    'Appearence\n\nAmerlassutsit': 'Appearence',
    '(suggestions)\nEnglish explanation on what \nthe abbreviation stands for\n\nSiunnersuutit': 'English explanation of Object designation',
    'Notes\n\nMaluginiagassat': 'Notes',
}, errors='raise')

# Join the translations to the placenames data via the 'Genstand' attribute.
joined = data_ds.merge(translated_ds, on=data_join_column)

# Rename the fields that were provided in dutch.
joined = joined.rename(columns={
    'Ny_grønlandsk': 'New Greenlandic',
    'Gammel_grønlandsk': 'Old Greenlandic',
    'Dansk': 'Danish',
    'Alternativt_stednavn': 'Alternative placename',
    'Genstand': 'Object designation',
    'Kilde': 'Source',
    'Kommune': 'Municipality',
    'Noter': 'Notes',
    'Oprettelsesdato': 'Date of registration',
    'Senest_rettet': 'Modification date',
    'Autoriseret': 'Authorized',
    'Autoriseret_dato': 'Authorized date',
    'Projektstyrer': 'Project manager',
    'Bredde': 'Latitude',
    'Længde': 'Longitude',
    'Blad': 'Card',
    'DMS_længde': 'DMS longitude',
    'DMS_bredde': 'DMS latitude',
    'KMS_kartografi': 'KMS cartography',
    'Navngiver': 'Namer',
    'Navngivet': 'Namesake',
    'Betydning': 'Meaning of the placename',
    'Historie': 'History',
}, errors='raise')

# TODO: drop the 'KMS Cartography' column? All empty strings.

joined.to_file(ARCHIVE_PATH / 'translations_joined.gpkg', driver='GPKG')
