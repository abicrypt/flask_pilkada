from app import db

class GambarHasil(db.Model):
    __tablename__ = 'gambar_hasil'
    id = db.Column(db.Integer, primary_key=True)
    kode_tps = db.Column(db.Integer, db.ForeignKey('tps.kode_tps'))
    url_gambar = db.Column(db.String(255), nullable=False)
    timestamp = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp())

    tps = db.relationship('TPS', backref='gambar_hasil')