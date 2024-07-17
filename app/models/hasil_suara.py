from app import db

class HasilSuara(db.Model):
    __tablename__ = 'hasil_suara'
    id = db.Column(db.Integer, primary_key=True)
    kode_tps = db.Column(db.Integer, db.ForeignKey('tps.kode_tps'))
    kandidat_id = db.Column(db.Integer, db.ForeignKey('kandidat.id'))
    jumlah_suara = db.Column(db.Integer, nullable=False)
    timestamp = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp())

    tps = db.relationship('TPS', backref='hasil_suara')
    kandidat = db.relationship('Kandidat', backref='hasil_suara')