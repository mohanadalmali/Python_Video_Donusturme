import os
import subprocess
import time
from flask import Flask, render_template, request, redirect, url_for, flash, send_from_directory

app = Flask(__name__)
app.secret_key = "secret_key"  # Flash mesajları için
UPLOAD_FOLDER = 'uploads'
OUTPUT_FOLDER = 'output'

# Yüklenen dosyaların kaydedileceği klasörler
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['OUTPUT_FOLDER'] = OUTPUT_FOLDER

def dönusturme(input_path, output_path, resolution, quality):
    width, height = resolution
    command = [
        'ffmpeg',
        '-i', input_path,
        '-vf', f'scale={width}:{height}',
        '-crf', str(quality),
        '-preset', 'fast',
        output_path
    ]
    try:
        subprocess.run(command, check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"FFmpeg hatası: {e}")
        return False
    except Exception as e:
        print(f"Bilinmeyen hata: {e}")
        return False

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'video' not in request.files:
            flash('Video dosyası seçilmedi.')
            return redirect(request.url)
        file = request.files['video']
        if file.filename == '':
            flash('Dosya adı boş olamaz.')
            return redirect(request.url)
        if file:
            filename = file.filename
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            resolution_option = request.form.get('resolution')
            quality = int(request.form.get('quality'))

            resolutions = {
                "720p": (1280, 720),
                "480p": (854, 480),
                "360p": (640, 360)
            }

            if resolution_option not in resolutions:
                flash('Geçersiz çözünürlük seçimi.')
                return redirect(request.url)

            timestamp = time.strftime("%Y%m%d_%H%M%S")
            output_filename = f'output_{resolution_option}_{timestamp}.mp4'
            output_path = os.path.join(app.config['OUTPUT_FOLDER'], output_filename)

            success = dönusturme(filepath, output_path, resolutions[resolution_option], quality)

            if success:
                flash('Video başarıyla dönüştürüldü.')
                return redirect(url_for('download', filename=output_filename))
            else:
                flash('Video dönüştürme işlemi başarısız oldu.')
                return redirect(request.url)

    return render_template('index.html')

@app.route('/download/<filename>')
def download(filename):
    return send_from_directory(app.config['OUTPUT_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)
