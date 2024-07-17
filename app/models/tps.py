from app import db

class TPS(db.Model):
    __tablename__ = 'tps'
    id = db.Column(db.Integer, primary_key=True)
    nomor = db.Column(db.Integer, nullable=False)
    kode_tps = db.Column(db.Integer, unique=True, nullable=False)
    kode_desa = db.Column(db.Integer, db.ForeignKey('kelurahan_desa.kode_desa'))

    kelurahan_desa = db.relationship('KelurahanDesa', backref='tps')