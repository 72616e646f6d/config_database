from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from schema import Config, Item, Base

class DatabaseConfig():

    def __init__(self, config_name, database_name='config.db'):
        self.engine = create_engine('sqlite:///{}'.format(database_name))
        Config.metadata.create_all(self.engine)
        self.sessionmaker = sessionmaker(bind=self.engine)
        self.config_name = config_name
        config = self.get_or_create_config(config_name)
        self.config_id = config.id

    def get(self, keyname):
        session = self.sessionmaker()
        result = session.query(Item.value).filter(Item.config_id == self.config_id).filter(Item.key == keyname).first()
        session.close()
        return result[0]

    def set(self, keyname, value):
        self.set_or_insert_item(keyname, value)

    def set_or_insert_item(self, keyname, value):
        session = self.sessionmaker()
        item = session.query(Item).filter(Config.id == self.config_id).filter(Item.key == keyname).first()
        if item:
            item.value = value
        else:
            item = Item(config_id=self.config_id, key=keyname, value=value)
        session.add(item)
        session.commit()
        session.close()

    def get_or_create_config(self, config_name):
        session = self.sessionmaker()
        instance = session.query(Config).filter(Config.name == self.config_name).first()
        if instance:
            return instance
        else:
            instance = Config(name=self.config_name)
            session.add(instance)
            session.commit()
            return instance

    def __del__(self):
        self.sessionmaker.close_all()
