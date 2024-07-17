from flask import Blueprint, render_template, redirect, url_for, flash, request, current_app
from flask_login import login_user, logout_user, login_required, current_user
from urllib.parse import urlparse
from app import db
from app.models.user_profile import UserProfile
from app.forms.profile_forms import ProfileForm
from werkzeug.utils import secure_filename
import os
from app.models.users import User
from app.forms.auth_forms import LoginForm, RegistrationForm
from app.extensions import login_manager
from functools import wraps
from PIL import Image
import time

auth_bp = Blueprint('auth', __name__)

def allowed_file(filename):
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def validate_image(file_path):
    try:
        img = Image.open(file_path)
        img.verify()
        return True
    except:
        return False

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or current_user.role != 'admin':
            flash('You do not have permission to access this page.', 'error')
            return redirect(url_for('auth.index'))
        return f(*args, **kwargs)
    return decorated_function

@auth_bp.route('/')
@auth_bp.route('/index')
def index():
    return render_template('index.html', title='Home')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('auth.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid email or password')
            return redirect(url_for('auth.login'))
        login_user(user)
        next_page = request.args.get('next')
        if not next_page or urlparse(next_page).netloc != '':
            next_page = url_for('auth.index')
        return redirect(next_page)
    return render_template('auth/login.html', title='Sign In', form=form)

@auth_bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.index'))

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('auth.index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, role='user')
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', title='Register', form=form)

@auth_bp.route('/hasil-perhitungan')
def hasil_perhitungan():
    # Logika untuk mengambil dan menampilkan hasil perhitungan
    return render_template('hasil_perhitungan.html')

@auth_bp.route('/data-pemilih')
@login_required
@admin_required
def data_pemilih():
    # Logika untuk menampilkan data pemilih
    return render_template('data_pemilih.html')

@auth_bp.route('/informasi-tps')
@login_required
@admin_required
def informasi_tps():
    # Logika untuk menampilkan informasi TPS
    return render_template('informasi_tps.html')

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@auth_bp.route('/profile/<username>')
@login_required
def profile(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('profile.html', user=user)

@auth_bp.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = ProfileForm()
    
    if form.validate_on_submit():
        if not current_user.profile:
            profile = UserProfile(user_id=current_user.id)
            db.session.add(profile)
        else:
            profile = current_user.profile
        
        profile.full_name = form.full_name.data
        profile.NIK = form.NIK.data
        profile.no_WA = form.no_WA.data
        profile.no_telp_hp = form.no_telp_hp.data
        profile.telegram = form.telegram.data
        profile.alamat = form.alamat.data
        profile.birth_date = form.birth_date.data
        
        if form.profile_picture.data:
            file = form.profile_picture.data
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                # Tambahkan timestamp ke nama file untuk keunikan
                filename = f"{int(time.time())}_{filename}"
                upload_folder = current_app.config['UPLOAD_FOLDER']
                if not os.path.exists(upload_folder):
                    os.makedirs(upload_folder)
                
                # Hapus foto profil lama jika ada
                if profile.profile_picture:
                    old_file_path = os.path.join(upload_folder, profile.profile_picture)
                    if os.path.exists(old_file_path):
                        os.remove(old_file_path)
                
                file_path = os.path.join(upload_folder, filename)
                file.save(file_path)
                
                # Validasi file gambar
                if validate_image(file_path):
                    profile.profile_picture = filename
                else:
                    os.remove(file_path)
                    flash('File yang diunggah bukan gambar yang valid.', 'error')
                    return redirect(url_for('auth.edit_profile'))
            else:
                flash('Tipe file tidak diizinkan.', 'error')
                return redirect(url_for('auth.edit_profile'))
        
        db.session.commit()
        flash('Profil Anda telah diperbarui.', 'success')
        return redirect(url_for('auth.profile', username=current_user.username))
    
    elif request.method == 'GET':
        if current_user.profile:
            form.full_name.data = current_user.profile.full_name
            form.NIK.data = current_user.profile.NIK
            form.no_WA.data = current_user.profile.no_WA
            form.no_telp_hp.data = current_user.profile.no_telp_hp
            form.telegram.data = current_user.profile.telegram
            form.alamat.data = current_user.profile.alamat
            form.birth_date.data = current_user.profile.birth_date
    
    return render_template('edit_profile.html', form=form)