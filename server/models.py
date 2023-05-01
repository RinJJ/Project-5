from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin
from config import db


#TODO: Clarify all serializer methods as well as make sure my models have the correct relationships because my brain is having a hard time for some reason
#TODO: Authentications !! Flask JWT? Does it do Password encoding? or can I use Werkzueg's password hash and checksession
#TODO: 


class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    serialize_rules = ( 'characters.user_id', ) #TODO

    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(50), nullable=False)

    characters = db.relationship( 'Character', backref='user' ) ## when getting a user it shows a table of all associated characters??
    groups = db.relationship( 'Group', backref='user' ) ## when getting a user it shows a table of all associated groups??

    @validates('password')
    def validate_password(self, key, password):
        if password == "":
            raise ValueError("Must provide a password")
        return password
    
    @validates('email')
    def validate_email(self, key, email):
        if (email == "") or ('@' not in email) or ('.' not in email):
            raise ValueError("Must provide a valid email")
        return email







class Character(db.Model, SerializerMixin):
    __tablename__ = 'characters'

    serialize_rules = ( 'character_groups.character', ) #TODO

    character_id = db.Column(db.Integer, primary_key=True)
    character_name = db.Column(db.String, nullable=False)
    character_race = db.Column(db.String, nullable=False)
    character_class = db.Column(db.String, nullable=False)

    user = db.Column(db.String, db.ForeignKey('users.user_id'), nullable = False)

    character_group = db.relationship( 'CharacterGroup', backref='character' )

    @validates('character_name')
    def validate_character_name(self, key, character_name):
        if character_name == "":
            raise ValueError("Must provide a name for your character")
        return character_name
    
    @validates('character_race')
    def validate_character_race(self, key, character_race):
        if character_race not in [ 'Dragonborn', 'Dwarf', 'Dwarf (Hill)', 'Dwarf (Mountain)', 'Elf', 'Elf (Drow)', 'Elf (High)', 'Elf (Wood)', 'Gnome', 'Gnome (Forest)', 'Gnome (Rock)', 'Half-Elf', 'Half-Orc', 'Halfling', 'Halfling (Lightfoot)', 'Halfling (Stout)', 'Human', 'Human (Variant)', 'Tiefling' ]:
            raise ValueError("Must provide a valid race for your character")
        return character_race
    
    @validates('character_class')
    def validate_character_class(self, key, character_class):
        if character_class not in [ 'Barbarian','Bard', 'Cleric', 'Druid', 'Fighter', 'Monk', 'Paladin', 'Ranger', 'Rogue', 'Sorcerer', 'Warlock' ]:
            raise ValueError("Must provide a valid class for your character")
        return character_class







class CharacterGroup(db.Model, SerializerMixin):
    __tablename__ = 'character_groups'

    serialize_rules = ( 'character_group', ) #TODO

    character_group_id = db.Column(db.Integer, primary_key=True)
    character_id = db.Column(db.Integer, db.ForeignKey('characters.character_id'), nullable=False)
    group_id = db.Column(db.Integer, db.ForeignKey('groups.group_id'), nullable=False)

### does this need any validations? or just in app to check post errors.





class Group(db.Model, SerializerMixin):
    __tablename__ = 'groups'

    serialize_rules = ( 'character_group.group_id', ) #TODO

    group_id = db.Column(db.Integer, primary_key=True)
    group_name = db.Column(db.String(75), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id')) ###TODO I really want the Username here dont I?

    character_group = db.relationship( 'CharacterGroup', backref='character_groups', cascade='all, delete-orphan' )
    characters = db.relationship( 'Character', secondary='character_groups', backref='characters')
    #TODO Do I need to create a relationship to see a groups users? how from here
    #TODO Do i need a back populates?

    @validates('group_name')
    def validate_character_name(self, key, group_name):
        if group_name == "":
            raise ValueError("Must provide a name for your character")
        return group_name
    
    # @validates('user_id')
    # def validate_user_id(self, key, user_id):
    #     if user_id == None:
    #         raise ValueError("You must be an authenticated user")
    #     return user_id
### is this where I need to figure out auth for this

