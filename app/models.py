from secrets import token_hex
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import generate_password_hash

db = SQLAlchemy()


userBets = db.Table('userBets',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('bet_slip_id', db.Integer, db.ForeignKey('bet_slip.id')),
    db.Column('active', db.Boolean, unique=False, default=True),
    db.Column('won', db.Boolean, unique=False, default=False),
)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(250), nullable=False)
    apitoken = db.Column(db.String, default=None, nullable=True) 
    level = db.Column(db.Integer, default = 1)
    money = db.Column(db.Integer, default = 150) 

    bets = db.relationship('BetSlip',
        secondary = userBets,
        backref = 'Betters',
        lazy = 'dynamic'
    )  
    post = db.relationship("Post", backref='author', lazy=True)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)
        self.apitoken = token_hex(16)



    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'token': self.apitoken,
            'level': self.level,
            'money': self.money
        }

    



class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    caption = db.Column(db.String(300))
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __init__(self, caption, user_id):
        self.caption = caption
        self.user_id = user_id

    def save(self):
        db.session.add(self)
        db.session.commit()

    def to_dict(self):
        return {
            'id': self.id,
            'caption': self.caption,
            'date_created': self.date_created,
            'user_id': self.user_id,
            'author': self.author.username
        }

class BetSlip(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    teamWon = db.Column(db.String(300))
    odds = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __init__(self, teamWon, odds, user_id):
        self.teamWon = teamWon
        self.odds = odds
        self.user_id = user_id

    def save(self):
        db.session.add(self)
        db.session.commit()




