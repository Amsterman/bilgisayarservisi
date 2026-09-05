#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kadıköy Bilgisayar Servisi - Kapsamlı On-Page & Yerel SEO İyileştirme Scripti
-----------------------------------------------------------------------------
Bu script projenizdeki index.html ve bölgesel HTML sayfalarını analiz ederek:
1. Title & Meta Description'ları yüksek tıklama oranlı (CTR) yerel anahtar kelimelerle günceller.
2. Eksik Open Graph (og:*) ve Twitter Card etiketlerini tamamlar.
3. BreadcrumbList (Ekmek Kırıntısı) yapısal verisini ekler.
4. Görsellere loading="lazy" ve eksik alt etiketlerini otomatik tanımlar.
5. Bölgesel sayfaları (Üsküdar, Maltepe, Ataşehir) özgün yerel meta etiketleri ve canonical'lar ile optimize eder.
6. Arama motorları için güncel sitemap.xml ve robots.txt dosyalarını yeniler.
"""

import os
import re
from datetime import datetime

SITE_URL = "https://bilgisayarservisi.site"
TODAY = datetime.now().strftime("%Y-%m-%d")

# 1. Meta Ayarları ve Şablonlar
SEO_DATA = {
    "index.html": {
        "title": "Kadıköy Bilgisayar & Laptop Tamiri | Aynı Gün Ücretsiz Teşhis",
        "description": "Kadıköy Eğitim Mahallesi atölyemizde laptop tamiri, anakart onarımı ve veri kurtarma. Ücretsiz teşhis, 1 ay garanti ve aynı gün yerinde servis: 0535 431 50 62",
        "canonical": f"{SITE_URL}/",
        "h1_target": "Kadıköy Bilgisayar ve Laptop Teknik Servisi",
        "district": "Kadıköy"
    },
    "uskudar-bilgisayar-servisi.html": {
        "title": "Üsküdar Bilgisayar & Laptop Tamiri | Randevulu Yerinde Servis",
        "description": "Üsküdar, Altunizade, Acıbadem ve Bağlarbaşı bölgesine randevulu yerinde bilgisayar ve laptop onarımı. Ücretsiz arıza tespiti ve 1 ay garanti: 0535 431 50 62",
        "canonical": f"{SITE_URL}/uskudar-bilgisayar-servisi.html",
        "h1_target": "Üsküdar Bilgisayar ve Laptop Tamir Servisi",
        "district": "Üsküdar"
    },
    "maltepe-bilgisayar-servisi.html": {
        "title": "Maltepe Bilgisayar & Laptop Tamiri | Hızlı Yerinde Servis",
        "description": "Maltepe, Küçükyalı, Altayçeşme ve Cevizli bölgelerine yerinde bilgisayar ve laptop onarım desteği. Net fiyat, garantili teknik servis: 0535 431 50 62",
        "canonical": f"{SITE_URL}/maltepe-bilgisayar-servisi.html",
        "h1_target": "Maltepe Bilgisayar ve Laptop Tamir Servisi",
        "district": "Maltepe"
    },
    "atasehir-bilgisayar-servisi.html": {
        "title": "Ataşehir Bilgisayar Servisi & Laptop Tamiri | Yerinde Servis",
        "description": "Ataşehir, İçerenköy, Barbaros ve Küçükbakkalköy ofis ve evlerine yerinde bilgisayar desteği, anakart ve laptop tamiri. Hemen arayın: 0535 431 50 62",
        "canonical": f"{SITE_URL}/atasehir-bilgisayar-servisi.html",
        "h1_target": "Ataşehir Bilgisayar ve Laptop Teknik Servisi",
        "district": "Ataşehir"
    }
}

def generate_breadcrumb_schema(page_name, page_url, title):
    if page_name == "index.html":
        return ""
    return f"""
  <!-- BreadcrumbList Schema -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
      {{
        "@type": "ListItem",
        "position": 1,
        "name": "Ana Sayfa",
        "item": "{SITE_URL}/"
      }},
      {{
        "@type": "ListItem",
        "position": 2,
        "name": "{title}",
        "item": "{page_url}"
      }}
    ]
  }}
  </script>
"""

def generate_og_tags(title, desc, url):
    return f"""  <!-- Open Graph & Social SEO -->
  <meta property="og:locale" content="tr_TR" />
  <meta property="og:type" content="website" />
  <meta property="og:title" content="{title}" />
  <meta property="og:description" content="{desc}" />
  <meta property="og:url" content="{url}" />
  <meta property="og:site_name" content="Kadıköy Bilgisayar Servisi" />
  <meta property="og:image" content="{SITE_URL}/assets/og-image.jpg" />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="{title}" />
  <meta name="twitter:description" content="{desc}" />"""

def optimize_html_file(file_path):
    file_name = os.path.basename(file_path)
    meta_info = SEO_DATA.get(file_name)

    if not meta_info:
        # Özel yapılandırması olmayan diğer HTML dosyaları için dinamik üretim
        base_title = file_name.replace(".html", "").replace("-", " ").title()
        meta_info = {
            "title": f"{base_title} | Kadıköy Bilgisayar Servisi",
            "description": f"{base_title} hizmetleri, garantili bilgisayar ve laptop tamir çözümleri. Hızlı arıza tespiti ve yerinde servis.",
            "canonical": f"{SITE_URL}/{file_name}",
            "district": "Kadıköy"
        }

    with open(file_path, "r", encoding="utf-8") as f:
        html = f.read()

    # 1. Title Güncelleme / Ekleme
    if "<title>" in html:
        html = re.sub(r"<title>.*?</title>", f"<title>{meta_info['title']}</title>", html, count=1, flags=re.DOTALL)
    else:
        html = html.replace("<head>", f"<head>\n  <title>{meta_info['title']}</title>")

    # 2. Meta Description Güncelleme / Ekleme
    if re.search(r'<meta[^>]*name=["']description["'][^>]*>', html, re.IGNORECASE):
        html = re.sub(r'<meta[^>]*name=["']description["'][^>]*content=["'][^"']*["'][^>]*>',
                      f'<meta name="description" content="{meta_info['description']}" />', html, count=1, flags=re.IGNORECASE)
    else:
        html = html.replace("</head>", f'  <meta name="description" content="{meta_info['description']}" />\n</head>')

    # 3. Canonical Etiketi
    canonical_tag = f'  <link rel="canonical" href="{meta_info['canonical']}" />'
    if '<link rel="canonical"' in html:
        html = re.sub(r'<link[^>]*rel=["']canonical["'][^>]*>', canonical_tag.strip(), html, count=1)
    else:
        html = html.replace("</head>", f"{canonical_tag}\n</head>")

    # 4. Open Graph Etiketleri Kontrolü
    if 'property="og:title"' not in html:
        og_block = generate_og_tags(meta_info['title'], meta_info['description'], meta_info['canonical'])
        html = html.replace("</head>", f"{og_block}\n</head>")

    # 5. BreadcrumbList Schema (Alt sayfalar için)
    if file_name != "index.html" and "BreadcrumbList" not in html:
        bc_schema = generate_breadcrumb_schema(file_name, meta_info['canonical'], meta_info['title'])
        html = html.replace("</head>", f"{bc_schema}\n</head>")

    # 6. Görsel Optimizasyonları (loading="lazy" ve eksik alt tanımları)
    def img_replacer(match):
        img_tag = match.group(0)
        # loading="lazy" yoksa ekle
        if 'loading=' not in img_tag:
            img_tag = img_tag.replace('<img ', '<img loading="lazy" ')
        # alt="" boşsa veya yoksa doldur
        if 'alt=""' in img_tag or 'alt=' not in img_tag:
            default_alt = f"{meta_info['district']} Bilgisayar ve Laptop Servisi"
            if 'alt=""' in img_tag:
                img_tag = img_tag.replace('alt=""', f'alt="{default_alt}"')
            else:
                img_tag = img_tag.replace('<img ', f'<img alt="{default_alt}" ')
        return img_tag

    html = re.sub(r'<img[^>]+>', img_replacer, html)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"[✓] {file_name} SEO meta ve yapısal verileri optimize edildi.")

def generate_sitemap_and_robots():
    html_files = [f for f in os.listdir(".") if f.endswith(".html")]
    if not html_files:
        html_files = ["index.html"]

    url_nodes = []
    for f in sorted(html_files):
        if f == "index.html":
            loc = f"{SITE_URL}/"
            prio = "1.0"
            freq = "weekly"
        else:
            loc = f"{SITE_URL}/{f}"
            prio = "0.8"
            freq = "weekly"
        url_nodes.append(f"""  <url>
    <loc>{loc}</loc>
    <lastmod>{TODAY}</lastmod>
    <changefreq>{freq}</changefreq>
    <priority>{prio}</priority>
  </url>""")

    sitemap_xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{"\n".join(url_nodes)}
</urlset>
"""
    with open("sitemap.xml", "w", encoding="utf-8") as f:
        f.write(sitemap_xml)
    print(f"[✓] sitemap.xml güncellendi ({len(url_nodes)} sayfa eklendi).")

    robots_txt = f"""User-agent: *
Allow: /

Sitemap: {SITE_URL}/sitemap.xml
"""
    with open("robots.txt", "w", encoding="utf-8") as f:
        f.write(robots_txt)
    print("[✓] robots.txt güncellendi.")

def main():
    print("=========================================================")
    print("  Kadıköy Bilgisayar Servisi - Tam Kapsamlı SEO Motoru   ")
    print("=========================================================")

    # Dizindeki tüm HTML dosyalarını tara
    html_files = [f for f in os.listdir(".") if f.endswith(".html")]
    if not html_files:
        print("[-] Dizin içinde HTML dosyası bulunamadı. Lütfen repo kök dizininde çalıştırın.")
        return

    for file in html_files:
        optimize_html_file(file)

    generate_sitemap_and_robots()
    print("---------------------------------------------------------")
    print("SEO optimizasyonları tamamlandı! Değişiklikleri push edebilirsiniz.")

if __name__ == "__main__":
    main()
