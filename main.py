from bs4 import BeautifulSoup

# Kaydedilen HTML dosyasını aç
with open("imdb_top_250_movies.html", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser")

# Kullanıcıdan film sayısı al
while True:
    try:
        limit_0 = int(input("Sıralanacak film sayısını giriniz (max 250): "))

        if 0 < limit_0 <= 250:
            # IMDb Top 250 listesindeki filmleri çek
            liste = soup.find("ul", {"class": "ipc-metadata-list"}).find_all("li", limit=limit_0)

            # Filmleri sırala ve ekrana yazdır
            for idx, item in enumerate(liste, start=1):
                filmadi = item.find("h3", {"class": "ipc-title__text"}).text.strip()
                puan_tag = item.find("span", {"class": "ipc-rating-star"})
                puan = puan_tag.text.strip() if puan_tag else "N/A"

                print(f"{idx}. {filmadi} - Puan: {puan}")
            break
        else:
            print("Lütfen 1 ile 250 arasında bir sayı giriniz.")
    except ValueError:
        print("Geçerli bir sayı giriniz.")