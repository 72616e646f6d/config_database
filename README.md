# config_database
Simple code to use a database to store config files.

To install the dependencies:

pip install sqlalchemy


Usage:

    from config import DatabaseConfig

    config = DatabaseConfig('test_config')
    config.set('key', 'value')
    config.get('key')
