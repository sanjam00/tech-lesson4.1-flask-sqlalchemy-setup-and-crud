from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

# contains definitions of tables and associated schema constructs
metadata = MetaData()

# create the Flask SQLAlchemy extension
db = SQLAlchemy(metadata=metadata)

# define a model class by inheriting from db.Model.


class Pet(db.Model):
    __tablename__ = 'pets'

    # Column names that are set up as Class Attributes
    # using db.Column() to define it as a column, then passing in the data type. add constraints here as well
    id = db.Column(db.Integer, primary_key=True) # this is now the primary key in our database
    name = db.Column(db.String(50)) # sets the maximum characters to 50
    species = db.Column(db.String)

    def __repr__(self):
        return f'<Pet {self.id}, {self.name}, {self.species}>'
