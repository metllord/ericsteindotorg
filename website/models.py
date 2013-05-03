from website import db
from passlib.context import CryptContext
import datetime
from urllib import urlencode

pwd_context = CryptContext(
    schemes=['sha512_crypt', 'bcrypt'],
    default='sha512_crypt',
    all__vary_rounds=0.1,
    pbkdf2_sha256__default_rounds=8000
)


class User(db.Model):
    username = db.Column(db.String(15), primary_key=True)
    password = db.Column(db.String(500))
    email = db.Column(db.String(120), index=True, unique=True)
    first_name = db.Column(db.String(120), index=True, nullable=True)
    last_name = db.Column(db.String(120), index=True, nullable=True)
    date_created = db.Column(db.DateTime)

    def __init__(self, username, email):
        self.username = username
        self.email = email
        if not self.date_created:
            self.data_created = datetime.datetime.now()
        if not self.password:
            pw = input('Enter a password: ')
            self.set_password(pw)

    def __repr__(self):
        return 'User: {}'.format(self.username)

    def __unicode__(self):
        return self.username

    def set_password(self, pw):
        self.password = pwd_context.encrypt(pw)

    def login(self, pw):
        return pwd_context.verify(pw, self.password)


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    posts = db.relationship('BlogPost', backref='title', lazy='dynamic')


class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    slug = db.Column(db.String(120), nullable=False)
    pub_date = db.Column(db.DateTime)
    body = db.Column(db.Text)
    author = db.Column(db.String(15), db.ForeignKey('user.username'))
    category = db.Column(db.Integer, db.ForeignKey('category.id'))

    def __init__(self, title, slug, pub_date, body, author, category):
        self.title = title
        self.slug = urlencode(slug)  # used for address to entry
        if not self.pub_date:
            self.pub_date = datetime.datetime.now()
        self.body = body
        self.author = author
        self.category = category

    def __repr__(self):
        return '{0} by {1}'.format([self.title, self.author])
