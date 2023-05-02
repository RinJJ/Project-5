from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import date
from app import app
from models import *
from config import db

if __name__ == '__main__':
    with app.app_context():
        print("Starting seed...")

        engine = create_engine('sqlite:///instance/app.db')
        Session = sessionmaker(bind=engine)
        session = Session()
        
        session.query(User).delete()
        session.query(Character).delete()
        session.query(CharacterGroup).delete()
        session.query(Group)

        






    session.bulk_save_objects( [  ] )
    session.commit()
    session.close()