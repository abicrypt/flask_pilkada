from app import db

class Provinsi(db.Model):
    __tablename__ = 'provinsi'
    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(100), nullable=False)
    kode_provinsi = db.Column(db.Integer, unique=True, nullable=False)