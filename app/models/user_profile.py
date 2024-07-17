from app import db
from app.models.users import User

class UserProfile(db.Model):
    __tablename__ = 'user_profile'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), unique=True, nullable=False)
    full_name = db.Column(db.String(100))
    NIK = db.Column(db.String(16), unique=True, nullable=False)
    no_WA = db.Column(db.String(20))
    no_telp_hp = db.Column(db.String(20))
    telegram = db.Column(db.String(50))
    alamat = db.Column(db.String(255))
    birth_date = db.Column(db.Date)
    profile_picture = db.Column(db.String(255))

    user = db.relationship('User', backref=db.backref('profile', uselist=False))