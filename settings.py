# Settings file. Set app settings here


# TODO: Put token in environment
API_TOKEN = '6ce3b9ae04f95010218caf4ffb6e8fc0b2ae3075'

RAPIDPRO_HOST = 'http://45.79.138.76:8000'
OPENMRS_DB_SETTINGS = {
    'DB_NAME':'openmrs',
    'HOSTNAME':'localhost',
    'USERNAME':'root',
    'PASSWORD':'password1234',
}

CONNECTOR_DB_SETTINGS = {
    'DB_NAME':'TRIAL',
    'HOSTNAME':'localhost',
    'USERNAME':'root',
    'PASSWORD':'password1234',
}

CONNECTOR_DB_TABLES = {
    "LAST_CHECKED":"Last_Checked",
    "USERS":'Users',
}

OPENMRS_DB_TABLES = {
    'PROGRAMS':'program',
    'PATIENT_PROGRAM':'patient_program',
    'PHONE_NUMBERS':'patient_identifier',
    'IDENTIFIER_TYPE':'patient_identifier_type',
}
