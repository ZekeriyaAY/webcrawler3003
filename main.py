from get_links import get_links
from get_imgs import get_imgs

TARGET_URL = "http://kalaycinakliyat.com"


def main():
    print(f'\n\t[PAGE SCAN STARTED]')
    pages = get_links(TARGET_URL, TARGET_URL)
    print(f'\t[PAGE SCAN FINISHED] {len(pages)} pages found.\n')

    # print(f'\n\t[IMAGE SCAN STARTED]')
    # images = get_imgs(pages)
    # print(f'\t[IMAGE SCAN FINISHED] {len(images)} images found.\n')

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print('bye!!')


çıktı sonuçlarının kategorize edilmesi
senaryoya göre ilerleme
görsellerin indirilip metadatalarının incelenmesi
saldırı zinciri için zayıf halkanın tespit edilmesi 
literatürdeki diğer sonuçlarla karşılaştırılarak önemli özelliklerinin eklenmesi

ara rapor
    problemin açıklanması, saldırılar için ön keşif aşaması
    bunun bi problem olduğuna dair temellendirme
    benzer çözümler
    biz ne farkımız vars
    literatür taraması en az 20 adet çalışma
    yöntemde de biz ne yaptık, yapıyoruz
    performans göstergelerini, grafik ile sonuçlarda eklenmesi(kodun optimizasyonu öncesi ve sonrası gibi)
    