from app import db

class KabupatenKota(db.Model):
    __tablename__ = 'kabupaten_kota'
    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(100), nullable=False)
    kode_kabupaten = db.Column(db.Integer, unique=True, nullable=False)
    kode_provinsi = db.Column(db.Integer, db.ForeignKey('provinsi.kode_provinsi'))

    provinsi = db.relationship('Provinsi', backref='kabupaten_kota')