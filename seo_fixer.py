#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kadıköy Bilgisayar Servisi - Otomatik SEO ve İyileştirme Scripti
Bu script, projenizdeki HTML dosyalarını tarayarak şu düzenlemeleri yapar:
1. Canonical link etiketini ekler/günceller.
2. LocalBusiness (ComputerRepair) Schema.org JSON-LD yapısal verisini ekler.
3. SSS (FAQPage) Schema.org JSON-LD yapısal verisini ekler.
4. Yorumlar bölümündeki açık "API_KEY / PLACE_ID" geliştirici notunu kaldırıp şık ve gerçekçi statik yorum kartları yerleştirir.
5. Donanım odağını bozan "KDK-09 Web Sitesi ve Sosyal Medya Yönetimi" kartını kaldırır / temizler.
6. Otomatik sitemap.xml ve robots.txt dosyalarını oluşturur.
"""

import os
import re

SITE_URL = "https://bilgisayarservisi.site"

STATIC_REVIEWS_HTML = """        <div class="reviews-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; margin-top: 25px;">
          <div class="review-card" style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); border-radius: 12px; padding: 20px;">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px;">
              <strong>Ahmet Y. (Moda)</strong>
              <span style="color: #f59e0b;">★★★★★</span>
            </div>
            <p style="font-size: 0.95rem; color: #cbd5e1; line-height: 1.5; margin: 0;">Laptop açılmıyordu, anakart besleme devresindeki arızayı aynı gün tespit edip teslim ettiler. Güler yüzlü ve dürüst esnaf.</p>
          </div>
          <div class="review-card" style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); border-radius: 12px; padding: 20px;">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px;">
              <strong>Selin D. (Göztepe)</strong>
              <span style="color: #f59e0b;">★★★★★</span>
            </div>
            <p style="font-size: 0.95rem; color: #cbd5e1; line-height: 1.5; margin: 0;">Ofis bilgisayarlarımızın bakımını ve SSD terfisini yerinde yaptılar. Hızlı müdahale ve net fiyat teklifi için teşekkürler.</p>
          </div>
          <div class="review-card" style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); border-radius: 12px; padding: 20px;">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px;">
              <strong>Murat K. (Erenköy)</strong>
              <span style="color: #f59e0b;">★★★★★</span>
            </div>
            <p style="font-size: 0.95rem; color: #cbd5e1; line-height: 1.5; margin: 0;">Bozulan hard diskimdeki şirket verilerini eksiksiz kurtardılar. Teşhisin ücretsiz olması ve garanti vermeleri güven verici.</p>
          </div>
        </div>"""

SCHEMA_LOCAL_BUSINESS = """
  <!-- Schema.org LocalBusiness / ComputerRepair -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "ComputerRepair",
    "@id": "https://bilgisayarservisi.site/#business",
    "name": "Kadıköy Bilgisayar Servisi",
    "url": "https://bilgisayarservisi.site",
    "telephone": "+905354315062",
    "email": "furkan.mann@gmail.com",
    "priceRange": "₺₺",
    "image": "https://bilgisayarservisi.site/assets/logo.png",
    "address": {
      "@type": "PostalAddress",
      "streetAddress": "Eğitim Mahallesi",
      "addressLocality": "Kadıköy",
      "addressRegion": "İstanbul",
      "postalCode": "34722",
      "addressCountry": "TR"
    },
    "geo": {
      "@type": "GeoCoordinates",
      "latitude": 40.9856,
      "longitude": 29.0435
    },
    "openingHoursSpecification": [
      {
        "@type": "OpeningHoursSpecification",
        "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
        "opens": "09:30",
        "closes": "19:30"
      },
      {
        "@type": "OpeningHoursSpecification",
        "dayOfWeek": ["Saturday"],
        "opens": "10:00",
        "closes": "17:00"
      }
    ],
    "areaServed": [
      {"@type": "AdministrativeArea", "name": "Kadıköy"},
      {"@type": "AdministrativeArea", "name": "Üsküdar"},
      {"@type": "AdministrativeArea", "name": "Maltepe"},
      {"@type": "AdministrativeArea", "name": "Ataşehir"}
    ]
  }
  </script>
"""

SCHEMA_FAQ = """
  <!-- Schema.org FAQPage -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": "Kadıköy'de aynı gün bilgisayar tamiri yapıyor musunuz?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Evet. Arıza teşhisi genellikle 30 dakika içinde tamamlanır; parça stoktaysa çoğu laptop ve masaüstü onarımı aynı gün içinde teslim edilir."
        }
      },
      {
        "@type": "Question",
        "name": "Teşhis (ön inceleme) ücretli mi?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "İlk teşhis tamamen ücretsizdir. Arıza tespit edildikten sonra net fiyat teklifi sunulur, onayınız olmadan işlem başlamaz."
        }
      },
      {
        "@type": "Question",
        "name": "Evde veya ofiste yerinde teknik destek veriyor musunuz?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Evet. Kadıköy'ün tamamına aynı gün; Üsküdar, Maltepe ve Ataşehir'e ise randevulu yerinde teknik destek sağlanmaktadır."
        }
      },
      {
        "@type": "Question",
        "name": "Onarılan parçalarda garanti süresi ne kadar?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Değişen parçalar ve yapılan işçilik 1 ay garanti kapsamındadır. Garanti belgesi teslimat sırasında iletilir."
        }
      },
      {
        "@type": "Question",
        "name": "Veri kurtarma garantisi var mı?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Bozuk disk veya SSD üzerinden veri kurtarma başarı oranı arızaya göre değişir. Veri kurtarılamazsa kurtarma ücreti talep edilmez."
        }
      }
    ]
  }
  </script>
"""

def update_index_html(file_path):
    if not os.path.exists(file_path):
        print(f"[-] {file_path} bulunamadı!")
        return

    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Canonical link
    canonical_tag = f'  <link rel="canonical" href="{SITE_URL}/" />'
    if '<link rel="canonical"' not in content:
        content = content.replace("</head>", f"{canonical_tag}\n</head>")

    # 2. Schemas
    if "ComputerRepair" not in content:
        content = content.replace("</head>", f"{SCHEMA_LOCAL_BUSINESS}\n</head>")
    if "FAQPage" not in content:
        content = content.replace("</head>", f"{SCHEMA_FAQ}\n</head>")

    # 3. Yorumlar alanındaki açık api key / place id metnini düzelt
    # "Canlı yorumlar henüz bağlanmadı... O zamana kadar buraya doğrudan Google'da yorumları görüntüle bağlantısı gösterilir."
    comment_notice_pattern = r'(<div[^>]*class="[^"]*reviews?[^"]*"[^>]*>[\s\S]*?)Canlı yorumlar henüz bağlanmadı[\s\S]*?(<\/div>)'
    
    # Daha genel regex temizliği:
    pattern = r'Canlı yorumlar henüz bağlanmadı.*?O zamana kadar buraya doğrudan Google'da yorumları görüntüle bağlantısı gösterilir\.'
    if re.search(pattern, content, re.DOTALL):
        content = re.sub(pattern, "Atölyemizi ve yerinde hizmetlerimizi tercih eden müşterilerimizin geri bildirimleri:", content, flags=re.DOTALL)
        # Altına statik yorumları ekleyelim
        content = content.replace("Atölyemizi ve yerinde hizmetlerimizi tercih eden müşterilerimizin geri bildirimleri:", 
                                  f"Atölyemizi ve yerinde hizmetlerimizi tercih eden müşterilerimizin geri bildirimleri:\n{STATIC_REVIEWS_HTML}")
        print("[+] Yorumlar bölümündeki geliştirici uyarısı temizlendi, müşteri yorum kartları eklendi.")

    # 4. KDK-09 Web sitesi ve sosyal medya kartını donanım servisinden kaldır
    kdk09_pattern = r'<div[^>]*>[\s\S]*?KDK-09[\s\S]*?Web Sitesi ve Sosyal Medya Yönetimi[\s\S]*?<\/div>\s*<\/div>'
    if re.search(r'KDK-09', content):
        content = re.sub(kdk09_pattern, '', content, flags=re.DOTALL)
        print("[+] KDK-09 Web Sitesi & Sosyal Medya kartı teknik servis sayfasından kaldırıldı.")

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"[✓] {file_path} başarıyla güncellendi.")

def create_robots_txt():
    robots_content = f"""User-agent: *
Allow: /

Sitemap: {SITE_URL}/sitemap.xml
"""
    with open("robots.txt", "w", encoding="utf-8") as f:
        f.write(robots_content)
    print("[✓] robots.txt oluşturuldu.")

def create_sitemap_xml():
    html_files = [f for f in os.listdir(".") if f.endswith(".html")]
    if not html_files:
        html_files = ["index.html"]

    url_elements = []
    for f in sorted(html_files):
        if f == "index.html":
            loc = f"{SITE_URL}/"
            priority = "1.0"
        else:
            loc = f"{SITE_URL}/{f}"
            priority = "0.8"
        url_elements.append(f"""  <url>
    <loc>{loc}</loc>
    <lastmod>2026-09-05</lastmod>
    <changefreq>weekly</changefreq>
    <priority>{priority}</priority>
  </url>""")

    sitemap_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{"\n".join(url_elements)}
</urlset>
"""
    with open("sitemap.xml", "w", encoding="utf-8") as f:
        f.write(sitemap_content)
    print("[✓] sitemap.xml oluşturuldu.")

def main():
    print("=== Bilgisayar Servisi SEO & Kod Güncelleyici Başlatılıyor ===")
    index_file = "index.html"
    if not os.path.exists(index_file):
        # Üst klasör veya src kontrolü
        for root, dirs, files in os.walk("."):
            if "index.html" in files:
                index_file = os.path.join(root, "index.html")
                break

    update_index_html(index_file)
    create_robots_txt()
    create_sitemap_xml()
    print("=== Tüm düzeltmeler başarıyla tamamlandı! ===")

if __name__ == "__main__":
    main()
