import os
import subprocess
import time  # Zaman damgası eklemek için

def video_ölçekle_ve_sıkıştır(input_path, output_path, resolution, quality):
    """
    FFmpeg ile video ölçekleme ve sıkıştırma işlemi yapar.
    :param input_path: Giriş videosunun yolu.
    :param output_path: Çıkış videosunun yolu.
    :param resolution: Çözünürlük tuple (genişlik, yükseklik) şeklinde.
    :param quality: Sıkıştırma kalitesi (0-51, 0 en yüksek kalite, 51 en düşük kalite).
    """
    if not os.path.exists(input_path):
        print(f"Hata: Dosya bulunamadı - {input_path}")
        return

    width, height = resolution
    command = [
        'ffmpeg',  # FFmpeg komutunun başlatılması
        '-i', input_path,  # Giriş video dosyası
        '-vf', f'scale={width}:{height}',  # Videoyu istenilen çözünürlüğe boyutlandır
        '-crf', str(quality),  # Sıkıştırma kalitesi (0-51)
        '-preset', 'fast',  # Hız ve kalite dengelemesi
        output_path  # Çıkış video dosyası
    ]

    try:
        subprocess.run(command, check=True)
        print(f"Video başarıyla {resolution} çözünürlüğüne ölçeklendi ve {quality} kalite ile sıkıştırıldı: {output_path}")
    except subprocess.CalledProcessError as e:
        print(f"FFmpeg hatası: {e}")
    except Exception as e:
        print(f"Bilinmeyen hata: {e}")

def main():
    # Giriş videosunun yolunu al
    input_video = input("Giriş videosunun yolunu girin (örneğin C:\\video.mp4): ").strip()

    # Dosyanın varlığını kontrol et
    if not os.path.exists(input_video):
        print(f"Hata: Girdiğiniz dosya yolu mevcut değil: {input_video}")
        return

    print("Seçenekler: 720p (1280x720), 480p (854x480), 360p (640x360)")
    resolution_option = input("Hedef çözünürlüğü seçin (720p, 480p, 360p): ").lower()

    resolutions = {
        "720p": (1280, 720),
        "480p": (854, 480),
        "360p": (640, 360)
    }

    if resolution_option not in resolutions:
        print("Geçersiz çözünürlük seçimi!")
        return

    try:
        quality = int(input("Sıkıştırma kalitesini girin (0-51, 0 en yüksek kalite): "))
        if not (0 <= quality <= 51):
            print("Geçersiz kalite değeri. 0 ile 51 arasında olmalı.")
            return
    except ValueError:
        print("Geçersiz kalite değeri! Lütfen sayısal bir değer girin.")
        return

    # Çıkış videosu için benzersiz bir dosya adı oluşturmak için zaman damgası ekle
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    output_video = f'output_{resolution_option}_{timestamp}.mp4'

    # Videoyu ölçekle ve sıkıştır
    video_ölçekle_ve_sıkıştır(input_video, output_video, resolutions[resolution_option], quality)

if __name__ == "__main__":
    main()
