# Flask Video Dönüştürme Uygulaması

Bu uygulama, kullanıcıların video dosyalarını farklı çözünürlüklerde ve kalite seviyelerinde dönüştürmelerini sağlayan bir Flask web uygulamasıdır. Kullanıcılar, yükledikleri videonun çözünürlüğünü (720p, 480p, 360p) ve sıkıştırma kalitesini (CRF) seçebilirler.

## Özellikler
- Kullanıcı dostu arayüz ile video dönüştürme.
- Çözünürlük seçenekleri: 720p, 480p, 360p.
- Kalite ayarlarını CRF (Constant Rate Factor) ile kontrol etme.

## Kalite Seçenekleri
Videoların kalite seviyesini ayarlarken CRF (Constant Rate Factor) değerini kullanabilirsiniz. CRF, 0 ile 51 arasında değişen bir kalite ölçeğidir:

- **0:** En yüksek kalite (kayıpsız), dosya boyutu çok büyük olur.
- **23:** Varsayılan kalite, genellikle iyi bir denge sunar.
- **51:** En düşük kalite (çok bozuk).

### Çözünürlük ve Önerilen CRF Değerleri

#### 1. 720p Videolar
- **Önerilen CRF:** 18-23
- Daha yüksek çözünürlük için kalite biraz daha iyi olmalıdır.

#### 2. 480p Videolar
- **Önerilen CRF:** 23-28
- Daha düşük kalite genellikle yeterlidir, çünkü çözünürlük düşük.

#### 3. 360p Videolar
- **Önerilen CRF:** 28-35
- En düşük kalite genellikle yeterlidir, çünkü çözünürlük oldukça düşük.

## Kullanım
1. Projeyi klonlayın:
    ```bash
    git clone https://github.com/kullanıcı_adı/proje_adı.git
    cd proje_adı
    ```

2. Uygulamayı çalıştırın:
    ```bash
    python app.py
    ```

3. Web tarayıcınızda `http://127.0.0.1:5000` adresine gidin.

## Gereksinimler
- Python 3.7+
- Flask
- FFmpeg (Sistemde kurulu olmalı)

