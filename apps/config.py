
def config(environment: str) -> dict:
    config = {
        'DEV': {
            'backups_location': 'F:\\BACKUPS-DEV\\',
            'app_email': 'ucfactorio-dev@ucfactor.io',
            'database_type': 'mysql',
            'database_server': 'localhost',
            'database_name': 'ucfactorio_dev',
            'database_user': 'ucfactorio-dev'
        },
        'UAT': {
            'backups_location': 'F:\\BACKUPS-UAT\\',
            'app_email': 'ucfactorio-uat@ucfactor.io',
            'database_type': 'mysql',
            'database_server': 'localhost',
            'database_name': 'ucfactorio_uat',
            'database_user': 'ucfactorio-uat',
        }
    }
    if environment == 'DEV':
        return config['DEV']
    elif environment == 'UAT':
        return config['UAT']
    else:
        raise Exception

