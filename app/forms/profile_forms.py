from flask_wtf import FlaskForm
from wtforms import StringField, DateField, FileField, SubmitField
from wtforms.validators import DataRequired, Length, Optional
from flask_wtf.file import FileAllowed

class ProfileForm(FlaskForm):
    full_name = StringField('Nama Lengkap', validators=[Length(max=100)])
    NIK = StringField('NIK', validators=[DataRequired(), Length(16)])
    no_WA = StringField('Nomor WhatsApp', validators=[Length(max=20)])
    no_telp_hp = StringField('Nomor Telepon/HP', validators=[Length(max=20)])
    telegram = StringField('Username Telegram', validators=[Length(max=50)])
    alamat = StringField('Alamat', validators=[Length(max=255)])
    birth_date = DateField('Tanggal Lahir', format='%Y-%m-%d', validators=[Optional()])
    profile_picture = FileField('Foto Profil', validators=[FileAllowed(['jpg', 'png','jpeg'], 'Hanya menerima file gambar!')])
    submit = SubmitField('Simpan Perubahan')