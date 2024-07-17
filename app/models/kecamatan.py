from app import db

class Kecamatan(db.Model):
    __tablename__ = 'kecamatan'
    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(100), nullable=False)
    kode_kecamatan = db.Column(db.Integer, unique=True, nullable=False)
    kode_kabupaten = db.Column(db.Integer, db.ForeignKey('kabupaten_kota.kode_kabupaten'))

    kabupaten_kota = db.relationship('KabupatenKota', backref='kecamatan')