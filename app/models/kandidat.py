from app import db

class Kandidat(db.Model):
    __tablename__ = 'kandidat'
    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(100), nullable=False)
    nomor_urut = db.Column(db.Integer, nullable=False)
    url_gambar = db.Column(db.String(255), nullable=False)
    jenis_pemilihan = db.Column(db.Enum('gubernur', 'bupati', 'walikota'), nullable=False)
    kode_provinsi = db.Column(db.Integer, db.ForeignKey('provinsi.kode_provinsi'))
    kode_kabupaten = db.Column(db.Integer, db.ForeignKey('kabupaten_kota.kode_kabupaten'))

    provinsi = db.relationship('Provinsi', backref='kandidat')
    kabupaten_kota = db.relationship('KabupatenKota', backref='kandidat')