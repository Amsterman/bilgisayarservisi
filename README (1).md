# Kadıköy Bilgisayar Servisi — Web Sitesi

Bu klasör, GitHub Pages üzerinde doğrudan yayınlanabilecek tek sayfalık, SEO ve GEO (yapay zeka arama motorları) için optimize edilmiş bir site içerir.

## İçerik
- `index.html` — sitenin tamamı (HTML + CSS + JS tek dosyada, hızlı yüklenir)
- `404.html` — özel hata sayfası (GitHub Pages bunu otomatik olarak kullanır, ekstra ayar gerekmez)
- `assets/og-image.png` — sosyal medyada (WhatsApp, Facebook, Twitter/X, LinkedIn) link paylaşıldığında çıkan önizleme görseli
- `robots.txt` — arama motoru botlarına tarama izni
- `sitemap.xml` — Google'a hızlı indeksleme için site haritası
- `llms.txt` — yapay zeka destekli arama/yanıt motorları (GEO) için özet bilgi dosyası
- `CNAME` — GitHub Pages'in `bilgisayarservisi.site` alan adını tanıması için gerekli dosya (içeriğine dokunmayın)

## 1) Yayına almadan önce MUTLAKA değiştirilmesi gerekenler

`index.html`, `robots.txt`, `sitemap.xml` ve `llms.txt` içinde şu yer tutucuları arayıp kendi bilgilerinizle değiştirin:

| Yer tutucu | Durum |
|---|---|
| `bilgisayarservisi.site` | ✅ Alan adınız — `canonical`, `og:url`, JSON-LD, `robots.txt`, `sitemap.xml` içine işlendi. Bir de `CNAME` dosyası eklendi (GitHub Pages'in alan adını tanıması için gerekli). |
| Telefon (0535 431 50 62) | ✅ Güncellendi (tel: linki, buton, footer) |
| WhatsApp (0535 431 50 62) | ✅ Güncellendi (yüzen buton, buton, footer) |
| E-posta (furkan.mann@gmail.com) | ✅ Güncellendi (iletişim formu, mailto linki, footer, schema) |
| Adres | ✅ Genel seviyede güncellendi — "Eğitim Mahallesi, Kadıköy / İstanbul". Fiziksel dükkan olmadığı için tam sokak/bina adresi ve o binaya işaret eden harita kasıtlı olarak kaldırıldı. |
| `KULLANICI_ADI` (Instagram linki) | Hâlâ değiştirilmeli |
| Müşteri yorumları | ✅ Sahte yorumlar kaldırıldı, yerine canlı Google Yorumları alanı eklendi (aşağıya bakın) |
| İstatistikler (12+ yıl, %98, vb.) | Hâlâ örnek — kendi işletmenizin gerçek rakamlarıyla değiştirin |

## Harita

Fiziksel bir dükkanınız olmadığı için (yerinde/mobil teknik servis modeli) adres ve haritalar bilinçli olarak **genel bölge seviyesinde** ("Eğitim Mahallesi, Kadıköy / İstanbul") tutuldu; tam sokak/bina adresi ve "Yol Tarifi Al" gibi bir binaya yönlendiren öğeler kaldırıldı. Bu, hem daha doğru bir temsil hem de Google'ın kurallarıyla uyumludur: Google Business Profile'da fiziksel mekânı olmayan işletmeler için "hizmet bölgesi işletmesi" (service-area business) seçeneği vardır — bu seçenekte tam adres gizlenir, sadece hizmet verilen bölge/mesafe gösterilir. Google İşletme Profili kaydınızı oluştururken bu seçeneği kullanmanızı öneririm.

## Servis Formu — Neden "Çalışmıyor" Görünebilir?

İletişim formu `formsubmit.co` adlı ücretsiz bir servisle **furkan.mann@gmail.com** adresine mail gönderecek şekilde ayarlı. Bu servisin bilinen bir davranışı var:

1. **İlk aktivasyon şart.** Yeni bir e-posta adresine giden ilk form gönderimi doğrudan iletilmez; formsubmit.co önce **furkan.mann@gmail.com** adresine bir aktivasyon e-postası gönderir. Bu e-postadaki (genelde "Confirm Email Address" / "Aktivasyon" başlıklı, gelen kutusunda yoksa **spam/gereksiz** klasöründe olabilir) linke tıklanana kadar sonraki formlar da iletilmez. Siteyi yayınladıktan sonra formu bir kez test edin, ardından o e-postaya gidip aktivasyon linkine tıklayın — bundan sonraki tüm talepler otomatik gelir.
2. **Yerelde (file:// ile) test etmeyin.** Formu bilgisayarınızda dosyayı çift tıklayıp açarak test ederseniz bazı tarayıcılar isteği engelleyebilir. En sağlıklı test, siteyi GitHub Pages'e yükledikten sonra gerçek `https://...` adresinden yapılan testtir.
3. Bu güncellemeyle form artık sayfayı yenilemiyor; gönderim sonrası buton altında yeşil bir **"Talebiniz alındı"** ya da (bir sorun olursa) kırmızı bir hata mesajı ve doğrudan arama/WhatsApp linki gösteriyor — böylece bir sorun olursa müşteri boşlukta kalmıyor.

Formu tamamen formsubmit.co'ya bağımlı olmaktan çıkarmak isterseniz, alternatif olarak Google Formlar (ücretsiz, kurulumu kolay) veya WhatsApp'a yönlendiren basit bir "mesaj gönder" butonu da kullanılabilir — isterseniz bunu da ekleyebilirim.

## Canlı Google Yorumları

Sahte yorumlar kaldırıldı. Yerine, "Yorumlar" bölümünde Google İşletme Profili'nizdeki gerçek yorumları **otomatik çekebilen** bir kod hazır durumda (`index.html` içinde `GOOGLE_MAPS_API_KEY` ve `GOOGLE_PLACE_ID` değişkenlerini arayın). Aktif etmek için:

1. [Google Cloud Console](https://console.cloud.google.com/) üzerinde bir proje oluşturun, faturalandırmayı etkinleştirin (küçük işletme kullanımı genelde Google'ın aylık ücretsiz kotasının içinde kalır, yine de kredi kartı istenir).
2. **Places API**'yi etkinleştirin ve bir API anahtarı oluşturun.
3. Güvenlik için anahtarı **HTTP referrer kısıtlaması** ile sadece kendi alan adınıza kısıtlayın (`https://bilgisayarservisi.site/*`) — aksi halde anahtarınızı başkaları kullanabilir.
4. İşletmenizin **Place ID**'sini [Google'ın Place ID bulucu aracından](https://developers.google.com/maps/documentation/places/web-service/place-id) alın.
5. `index.html` içinde `GOOGLE_MAPS_API_KEY = "BURAYA_API_ANAHTARINIZI_YAZIN"` ve `GOOGLE_PLACE_ID = "BURAYA_PLACE_ID_YAZIN"` satırlarını kendi değerlerinizle değiştirin.

Not: Google Places API bir işletme için en fazla 5 yorum döndürür (Google'ın kendi kısıtı) ve hangi 5 yorumun gösterileceğini Google belirler; bunu değiştiremezsiniz. Daha fazla yorum, özelleştirme veya API/faturalandırma ile uğraşmak istemiyorsanız, aynı işi yapan hazır (genelde ücretli, bazılarının sınırlı ücretsiz planı olan) widget servisleri de var: **Elfsight**, **EmbedSocial**, **Trustmary** gibi — bunlar Google Business Profile'ınıza bağlanıp verilen bir `<script>` kodunu `index.html`'e yapıştırmanız yeterli olacak şekilde çalışır. API/anahtar kısıtlaması hâlâ girilmediyse, bölüm otomatik olarak "Google'da Yorumları Görüntüle" bağlantısına düşer, sayfa bozulmaz.

> Önemli: Sahte yorum, sahte puan veya doğrulanamayan istatistik kullanmak Google'ın kalite politikalarına aykırıdır ve zamanla sıralamanızı olumsuz etkiler.

## 2) GitHub'a yükleme, GitHub Pages ile yayınlama ve `bilgisayarservisi.site` alan adını bağlama

### A) Dosyaları yükleyin
1. GitHub'da yeni bir repo oluşturun (örn. `kadikoy-bilgisayar-servisi`).
2. Bu klasördeki **tüm dosyaları** (görünmeyen `CNAME` dosyası dahil!) o reponun kök dizinine yükleyin.
3. Repo içinde **Settings → Pages** yolunu izleyin.
4. "Build and deployment" bölümünde **Source: Deploy from a branch** seçin, branch olarak `main` ve klasör olarak `/ (root)` seçip **Save** deyin.
5. Birkaç dakika içinde siteniz `https://KULLANICI-ADINIZ.github.io/REPO-ADI/` adresinde geçici olarak yayında olur.

### B) `bilgisayarservisi.site` alan adını bağlayın
Repoya zaten alan adınızı içeren bir **`CNAME`** dosyası eklendi — GitHub Pages'in özel alan adınızı tanıması için bu dosya şart, silmeyin.

1. **Settings → Pages → Custom domain** kutusuna `bilgisayarservisi.site` yazıp kaydedin (GitHub bunu zaten `CNAME` dosyasından okuyacaktır, ama kutuya da yazmanız GitHub'ın DNS doğrulaması başlatması için gerekir).
2. Alan adını satın aldığınız yerin (Natro, GoDaddy, isimtescil, Cloudflare vb.) **DNS yönetim paneline** girin ve aşağıdaki kayıtları ekleyin:

**Kök alan adı için (`bilgisayarservisi.site`) — 4 adet A kaydı:**

| Tür | Ad/Host | Değer |
|---|---|---|
| A | @ (veya boş) | 185.199.108.153 |
| A | @ (veya boş) | 185.199.109.153 |
| A | @ (veya boş) | 185.199.110.153 |
| A | @ (veya boş) | 185.199.111.153 |

**`www` alt alan adı için (isteğe bağlı ama önerilir) — 1 adet CNAME kaydı:**

| Tür | Ad/Host | Değer |
|---|---|---|
| CNAME | www | KULLANICI-ADINIZ.github.io |

> **A kaydı nedir?** Bir alan adını doğrudan bir IP adresine bağlar. Yukarıdaki 4 IP, GitHub Pages'in sunucularına ait sabit adreslerdir; `bilgisayarservisi.site` yazan biri bu IP'lerden birine yönlendirilir.
>
> **CNAME kaydı nedir?** Bir alan adını IP yerine **başka bir alan adına** yönlendirir. `www.bilgisayarservisi.site` gibi bir alt alan adını doğrudan IP ile uğraşmadan `KULLANICI-ADINIZ.github.io` adresine işaret eder. Kök alan adında (yani `@` / `bilgisayarservisi.site`'ın kendisinde) CNAME kullanılamaz, bu yüzden kök için A kaydı, `www` için CNAME kullanılır.

3. DNS değişikliklerinin yayılması genelde birkaç dakika, bazen birkaç saat sürebilir.
4. DNS doğru şekilde yayıldıktan sonra GitHub, **Settings → Pages** sayfasında yeşil bir onay ve "Enforce HTTPS" seçeneğini sunacaktır — bunu mutlaka işaretleyin, siteniz `https://` ile güvenli şekilde yayınlanır.

## 3) Google'da hızlı görünmek için yapılması gerekenler

Sadece siteyi yayınlamak yeterli değildir; Google'a "burada bir site var" demeniz gerekir:

1. **Google Search Console**'a (search.google.com/search-console) gidin, siteyi mülk olarak ekleyin (URL doğrulama yöntemiyle).
2. `sitemap.xml` dosyanızın tam adresini (`https://.../sitemap.xml`) Search Console'da **Sitemaps** bölümüne gönderin.
3. Ana sayfanız için **URL Denetimi** aracını kullanıp "Dizine Eklenmesini İste" (Request Indexing) butonuna basın.
4. **Google İşletme Profili** (business.google.com) üzerinden işletmenizi kaydedin/doğrulayın — konum bazlı aramalarda ("kadıköy bilgisayar tamircisi") çıkabilmenin en etkili yolu budur, web sitesinden bile daha önemlidir.
5. Gerçek müşterilerinizden Google İşletme Profili üzerinden yorum isteyin; yorum sayısı ve güncelliği yerel sıralamayı doğrudan etkiler.
6. Sosyal medya hesaplarınızda (Instagram, Facebook) siteye link verin; bu, sitenin daha hızlı keşfedilmesine yardımcı olur.

Bu adımlar tamamlandığında site genelde birkaç gün ile birkaç hafta içinde Google'da görünmeye başlar; kesin bir süre garanti edilemez çünkü indeksleme hızı Google'ın kendi taktirindedir.

## 4) Sitede halihazırda yapılmış SEO/GEO çalışmaları

- Başlık, açıklama, anahtar kelime ve Open Graph etiketleri
- **Gerçek bir paylaşım görseli (`og:image`/`twitter:image`, 1200×630)** — linkin WhatsApp/Facebook/Twitter'da düzgün önizleme ile çıkması için
- **Özel 404 hata sayfası** — marka diliyle tutarlı, ana sayfaya ve iletişime yönlendiren, `noindex` etiketli (arama sonuçlarına karışmaz)
- `geo.region`, `geo.position` ile yerel arama sinyalleri
- `ElectronicsStore` ve `FAQPage` için Schema.org (JSON-LD) yapılandırılmış veri
- Anlamsal (semantic) HTML5 başlık hiyerarşisi (tek `h1`, sıralı `h2`/`h3`)
- Mobil uyumlu, hızlı yüklenen tek dosyalık yapı (harici görsel yok, sadece sistem fontları + Google Fonts)
- `llms.txt` ile yapay zeka tabanlı arama/yanıt motorları için düz metin özet (GEO)
- Erişilebilirlik: klavye ile odaklanılabilir öğeler, `prefers-reduced-motion` desteği

## SEO/GEO İncelemesi — Neler Güçlendirildi, Sırada Ne Var

### Bu turda yapılan iyileştirmeler
- Haritalar, fiziksel dükkan olmadığı için genel bölge seviyesinde ("Eğitim Mahallesi, Kadıköy") gösterilecek şekilde ayarlandı; tam bina adresine işaret eden özel konum kimliği (CID) ve "Yol Tarifi Al" butonu kasıtlı olarak kaldırıldı (bkz. "Harita" bölümü).
- Var olmayan bir dosyaya işaret eden hatalı `image` alanı şemadan kaldırıldı (gerçek bir fotoğrafınız olduğunda ekleyin, aşağıya bakın).
- Sayfaya, hem klasik SEO (içerik derinliği) hem GEO (yapay zeka motorlarının alıntılayabileceği net cümleler) için **"Kadıköy'de bilgisayar tamiri neden yerinde çözülmeli?"** başlıklı kısa bir içerik bloğu eklendi; Eğitim Mahallesi ismi görünür metne işlendi.

### Öncelik sırasına göre sizin yapmanız gerekenler
1. **Google İşletme Profili (Google Business Profile) kaydı/doğrulaması** — Bu, "kadıköy bilgisayar tamircisi" gibi aramalarda haritalı sonuçlarda (local pack) çıkmanın *en etkili* yoludur; web sitesinden bile daha önemlidir. Adresiniz zaten Google'da kayıtlıysa, işletmenizi bu kayda **sahiplenip** (claim) doğrulayın.
2. **Gerçek fotoğraflar ekleyin** — atölye, tamir sırası, önce/sonra görüntüleri. Hem Google Business Profile'a hem siteye eklenecek gerçek bir fotoğraf, şemadaki `image` alanına da eklenmeli (şu an bilinçli olarak boş bırakıldı).
3. **Gerçek Google yorumları** — "Canlı Google Yorumları" bölümündeki API anahtarı/Place ID adımlarını tamamlayın (yukarıda anlatıldı).
4. ✅ **Alan adı tamamlandı** — `bilgisayarservisi.site`, `canonical`, `og:url`, JSON-LD şeması, `robots.txt` ve `sitemap.xml` içine işlendi; GitHub Pages'e bağlamak için `CNAME` dosyası eklendi (2. bölümdeki DNS adımlarını uygulayın).
5. **Search Console + sitemap gönderimi** — 3. bölümdeki adımları uygulayın.
6. **NAP tutarlılığı** — Telefon/adres/işletme adınızın Google Business Profile, Instagram, Facebook ve sitede birebir aynı yazıldığından emin olun; tutarsızlık yerel sıralamayı zayıflatır.

Bu maddeler tamamlandığında site, sadece "doğru yapılandırılmış" değil, Kadıköy ve çevresi aramalarında gerçekten rekabet edebilecek bir temele sahip olur.

## 5) İsteğe bağlı geliştirmeler

- Gerçek işletme fotoğrafları eklemek (teknisyen, atölye, önce/sonra onarım fotoğrafları) güveni artırır.
- Blog/İçerik sayfaları eklemek ("Laptop şarj olmuyor ne yapmalı?" gibi) organik trafiği büyütür.
- Google Analytics veya Plausible gibi bir analiz aracı eklemek performans takibi sağlar.
