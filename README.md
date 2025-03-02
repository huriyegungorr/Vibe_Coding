# Vibe_Coding  
Proje Amacı:    
Bu proje, X (Twitter) API'sini kullanarak belirlenen bir konu veya hashtag üzerinde duygu analizi (sentiment analysis) yapmayı amaçlamaktadır.   
Çalışma kapsamında 100 tweet üzerinde analiz yapılmış ve sonuçlar grafiklerle görselleştirilmiştir.    

Kullanılan Teknolojiler:

Python (Veri çekme, analiz ve görselleştirme için)
Tweepy (X API'sinden veri almak için)
TextBlob (Sentiment analizi için)
Matplotlib (Görselleştirme için)
dotenv (API anahtarlarını güvenli şekilde yüklemek için)  

Proje Adımları:  

1) API Bağlantısı  
.env dosyasından BEARER_TOKEN okunarak API bağlantısı kuruldu.
API anahtarı bulunamazsa hata mesajı görüntüleniyor.

2) Tweetlerin Çekilmesi
Tweepy Client kullanılarak belirlenen hashtag için 100 tweet çekildi.
Retweetler hariç tutuldu ve Türkçe tweetler filtrelendi.(Twitter api bir ayda yalnızca 100 tweet çekilmesine izin verir.)

3) Sentiment Analizi
TextBlob ile tweetlerin duygu analizi yapıldı.
Tweetler pozitif, nötr ve negatif olarak sınıflandırıldı.

4) Sonuçların Görselleştirilmesi
Matplotlib ile duygu dağılımı bar grafiği olarak çizildi.   

 Kurulum ve Kullanım:

Gerekli kütüphaneleri yükleyin:
pip install -r requirements.txt

API anahtarınızı .env dosyanıza ekleyin:
BEARER_TOKEN='Twitter developer dashboard dan aldığınız anahtarınız'

Analizi çalıştırın:
python src/main.py  

 Çıktılar ve Sonuçlar:

Belirtilen hashtag için tweetler çekildi ve analiz edildi.
Duygu analizi sonuçları bar grafiği ile gösterildi.
Pozitif, nötr ve negatif tweet sayıları raporlandı. 
Sonuçlarınız görseldeki gibi oluşacaktır.  
![image](https://github.com/user-attachments/assets/6b138bfc-a4ba-4be6-a9be-6abdf8991b59)
