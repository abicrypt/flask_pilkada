from app import db

class KelurahanDesa(db.Model):
    __tablename__ = 'kelurahan_desa'
    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(100), nullable=False)
    kode_desa = db.Column(db.Integer, unique=True, nullable=False)
    kode_kecamatan = db.Column(db.Integer, db.ForeignKey('kecamatan.kode_kecamatan'))

    kecamatan = db.relationship('Kecamatan', backref='kelurahan_desa')