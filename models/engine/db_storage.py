#!/usr/bin/python3
"""DBStorage module for HBNB project"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:
    """DBStorage class"""
    __engine = None
    __session = None

    def __init__(self):
        """Initialization method"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                       .format(os.getenv('HBNB_MYSQL_USER'),
                                               os.getenv('HBNB_MYSQL_PWD'),
                                               os.getenv('HBNB_MYSQL_HOST'),
                                               os.getenv('HBNB_MYSQL_DB')),
                                       pool_pre_ping=True)
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

        # Create all tables in the database
        Base.metadata.create_all(self.__engine)

    def all(self, cls=None):
        """Query on the current database session"""
        objects = {}
        classes = [User, State, City, Amenity, Place, Review]
        if cls:
            classes = [cls]
        for cl in classes:
            objs = self.__session.query(cl).all()
            for obj in objs:
                key = "{}.{}".format(obj.__class__.__name__, obj.id)
                objects[key] = obj
        return objects

    def new(self, obj):
        """Add the object to the current database session"""
        if obj:
            self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database"""
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)
