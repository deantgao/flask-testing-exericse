from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Game(db.Model):
    """Board game."""

    __tablename__ = "games"
    game_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False, unique=True)
    description = db.Column(db.String(100))


def connect_to_db(app, db_uri="postgresql:///games"):
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    db.app = app
    db.init_app(app)


def example_data():
    """Create example data for the test database."""
    #FIXME: write a function that creates a game and adds it to the database.
    scrabble = Game(name='Scrabble', description='The best wordgame ever.')
    monopoly = Game(name='Monopoly', description='Board game - boring!')
    apples2apples = Game(name='Apples to Apples', description='Charades-like game.')
    chutesLadders = Game(name='Chutes and Ladders', description='Fun for the fam.')

    db.session.add_all([scrabble, monopoly, apples2apples, chutesLadders])
    db.session.commit()

    # print "FIXME"


if __name__ == '__main__':
    from server import app

    connect_to_db(app)
    print "Connected to DB."
 