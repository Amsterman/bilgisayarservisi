#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kadıköy Bilgisayar Servisi - Gerçek Google Yorumlarını Entegre Etme Scripti
-------------------------------------------------------------------------
Bu script, Google İşletme Profilinizdeki gerçek müşteri değerlendirmelerini (4.8 / 5.0 Yıldız, 26 Yorum)
ve müşteri yorum metinlerini alıp index.html'deki müşteri yorumları bölümüne şık bir şekilde yerleştirir.
"""

import os
import re

INDEX_PATH = "index.html"

REVIEWS_HTML = """<!-- Google Gerçek Müşteri Yorumları -->
<section id="yorumlar" class="section reviews-section" style="padding: 60px 0; background: rgba(255, 255, 255, 0.01);">
  <div class="container" style="max-width: 1200px; margin: 0 auto; padding: 0 20px;">
    <div class="section-header" style="text-align: center; margin-bottom: 40px;">
      <span class="badge" style="background: rgba(59, 130, 246, 0.1); color: #60a5fa; padding: 6px 14px; border-radius: 20px; font-size: 0.85rem; font-weight: 600;">MÜŞTERİ DEĞERLENDİRMELERİ</span>
      <h2 style="font-size: 2.1rem; margin: 15px 0 10px; color: #fff;">Google İşletme Profilimizdeki Gerçek Yorumlar</h2>
      
      <!-- Google Rating Rozeti -->
      <div style="display: inline-flex; align-items: center; gap: 12px; background: rgba(255, 255, 255, 0.04); border: 1px solid rgba(255, 255, 255, 0.1); padding: 10px 20px; border-radius: 30px; margin-top: 10px;">
        <svg style="width: 22px; height: 22px;" viewBox="0 0 24 24">
          <path fill="#EA4335" d="M12 5c1.6 0 3 .6 4.1 1.7l3.1-3.1C17.3 1.8 14.8 1 12 1 7.5 1 3.7 3.6 1.9 7.3l3.7 2.9C6.5 7.4 9 5 12 5z"/>
          <path fill="#4285F4" d="M23.5 12.3c0-.8-.1-1.7-.2-2.3H12v4.6h6.5c-.3 1.5-1.1 2.8-2.4 3.7l3.7 2.9c2.2-2 3.7-5 3.7-8.9z"/>
          <path fill="#FBBC05" d="M5.6 14.8c-.2-.7-.4-1.5-.4-2.8s.2-2.1.4-2.8L1.9 6.3C.7 8.7 0 10.3 0 12s.7 3.3 1.9 5.7l3.7-2.9z"/>
          <path fill="#34A853" d="M12 23c3.2 0 6-1.1 8-3l-3.7-2.9c-1.1.7-2.5 1.2-4.3 1.2-3 0-5.5-2.4-6.4-5.2L1.9 16C3.7 19.7 7.5 23 12 23z"/>
        </svg>
        <span style="font-size: 1.2rem; font-weight: 700; color: #fff;">4.8</span>
        <span style="color: #f59e0b; font-size: 1.1rem; letter-spacing: 2px;">★★★★★</span>
        <span style="color: #94a3b8; font-size: 0.9rem;">(26 Google Yorumu)</span>
      </div>
    </div>

    <div class="reviews-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 24px;">
      
      <!-- Yorum 1 -->
      <div class="review-card" style="background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255, 255, 255, 0.08); border-radius: 16px; padding: 24px; display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px;">
            <div style="display: flex; align-items: center; gap: 10px;">
              <div style="width: 38px; height: 38px; border-radius: 50%; background: #2563eb; color: #fff; display: flex; align-items: center; justify-content: center; font-weight: bold; font-size: 0.95rem;">EK</div>
              <div>
                <strong style="color: #fff; font-size: 0.95rem; display: block;">Emin Kaldırım</strong>
                <span style="color: #64748b; font-size: 0.8rem;">Kadıköy Yerinde Destek</span>
              </div>
            </div>
            <span style="color: #f59e0b; font-size: 0.95rem;">★★★★★</span>
          </div>
          <p style="font-size: 0.92rem; color: #cbd5e1; line-height: 1.6; margin: 0;">"Pazar günü Kadıköy'de heryer kapalıyken gelip işimizi halletti. Kadıköy bilgisayar servisinden Furkan Bey'e çok teşekkürler."</p>
        </div>
        <div style="margin-top: 15px; padding-top: 12px; border-top: 1px solid rgba(255, 255, 255, 0.05); font-size: 0.8rem; color: #64748b;">
          Google Doğrulanmış Yorum
        </div>
      </div>

      <!-- Yorum 2 -->
      <div class="review-card" style="background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255, 255, 255, 0.08); border-radius: 16px; padding: 24px; display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px;">
            <div style="display: flex; align-items: center; gap: 10px;">
              <div style="width: 38px; height: 38px; border-radius: 50%; background: #059669; color: #fff; display: flex; align-items: center; justify-content: center; font-weight: bold; font-size: 0.95rem;">YO</div>
              <div>
                <strong style="color: #fff; font-size: 0.95rem; display: block;">Yasin Oflaz</strong>
                <span style="color: #64748b; font-size: 0.8rem;">Laptop Tamiri</span>
              </div>
            </div>
            <span style="color: #f59e0b; font-size: 0.95rem;">★★★★★</span>
          </div>
          <p style="font-size: 0.92rem; color: #cbd5e1; line-height: 1.6; margin: 0;">"Kadıköy bilgisayar servisi ararken burayı buldum, gerçekten çok memnun kaldım. Laptop tamiri hızlı ve sorunsuz yapıldı. Hem uygun fiyatlı hem de güvenilir bir teknik servis. Tavsiye ederim."</p>
        </div>
        <div style="margin-top: 15px; padding-top: 12px; border-top: 1px solid rgba(255, 255, 255, 0.05); font-size: 0.8rem; color: #64748b;">
          Google Doğrulanmış Yorum
        </div>
      </div>

      <!-- Yorum 3 -->
      <div class="review-card" style="background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255, 255, 255, 0.08); border-radius: 16px; padding: 24px; display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px;">
            <div style="display: flex; align-items: center; gap: 10px;">
              <div style="width: 38px; height: 38px; border-radius: 50%; background: #d97706; color: #fff; display: flex; align-items: center; justify-content: center; font-weight: bold; font-size: 0.95rem;">MZ</div>
              <div>
                <strong style="color: #fff; font-size: 0.95rem; display: block;">Mehtap Zengin</strong>
                <span style="color: #64748b; font-size: 0.8rem;">SSD & Performans Yükseltme</span>
              </div>
            </div>
            <span style="color: #f59e0b; font-size: 0.95rem;">★★★★★</span>
          </div>
          <p style="font-size: 0.92rem; color: #cbd5e1; line-height: 1.6; margin: 0;">"SSD yükseltme yaptırdım, bilgisayar resmen uçtu. Kadıköy bilgisayar servisi içinde fiyat/performans olarak çok iyi. Hem hızlı hem de dürüst esnaf."</p>
        </div>
        <div style="margin-top: 15px; padding-top: 12px; border-top: 1px solid rgba(255, 255, 255, 0.05); font-size: 0.8rem; color: #64748b;">
          Google Doğrulanmış Yorum
        </div>
      </div>

      <!-- Yorum 4 -->
      <div class="review-card" style="background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255, 255, 255, 0.08); border-radius: 16px; padding: 24px; display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px;">
            <div style="display: flex; align-items: center; gap: 10px;">
              <div style="width: 38px; height: 38px; border-radius: 50%; background: #7c3aed; color: #fff; display: flex; align-items: center; justify-content: center; font-weight: bold; font-size: 0.95rem;">YA</div>
              <div>
                <strong style="color: #fff; font-size: 0.95rem; display: block;">Yusuf Akpolat</strong>
                <span style="color: #64748b; font-size: 0.8rem;">Masaüstü PC Bakımı</span>
              </div>
            </div>
            <span style="color: #f59e0b; font-size: 0.95rem;">★★★★★</span>
          </div>
          <p style="font-size: 0.92rem; color: #cbd5e1; line-height: 1.6; margin: 0;">"Kadıköy bilgisayar servisi ararken yorumlara bakarak geldim ve iyi ki gelmişim. Hem masaüstü bilgisayarımın bakımını yaptılar hem de hızlandırdılar. İşçilik kaliteli, fiyatlar makul. Güvenilir bilgisayar tamircisi arayanlara kesinlikle öneririm."</p>
        </div>
        <div style="margin-top: 15px; padding-top: 12px; border-top: 1px solid rgba(255, 255, 255, 0.05); font-size: 0.8rem; color: #64748b;">
          Google Doğrulanmış Yorum
        </div>
      </div>

      <!-- Yorum 5 -->
      <div class="review-card" style="background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255, 255, 255, 0.08); border-radius: 16px; padding: 24px; display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px;">
            <div style="display: flex; align-items: center; gap: 10px;">
              <div style="width: 38px; height: 38px; border-radius: 50%; background: #0284c7; color: #fff; display: flex; align-items: center; justify-content: center; font-weight: bold; font-size: 0.95rem;">AU</div>
              <div>
                <strong style="color: #fff; font-size: 0.95rem; display: block;">Aytekin Uzunhan</strong>
                <span style="color: #64748b; font-size: 0.8rem;">HP Notebook Tamiri</span>
              </div>
            </div>
            <span style="color: #f59e0b; font-size: 0.95rem;">★★★★★</span>
          </div>
          <p style="font-size: 0.92rem; color: #cbd5e1; line-height: 1.6; margin: 0;">"Hp Notebook arızası için ulaştım. Uzaktan bağlanarak hallettiler. Ayrıca uzun zamandır yüklemek isteyip yükleyemediğim yazılımları da yüklediler. Kadıköy bilgisayar servisine çok teşekkürler."</p>
        </div>
        <div style="margin-top: 15px; padding-top: 12px; border-top: 1px solid rgba(255, 255, 255, 0.05); font-size: 0.8rem; color: #64748b;">
          Google Doğrulanmış Yorum
        </div>
      </div>

      <!-- Yorum 6 -->
      <div class="review-card" style="background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255, 255, 255, 0.08); border-radius: 16px; padding: 24px; display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px;">
            <div style="display: flex; align-items: center; gap: 10px;">
              <div style="width: 38px; height: 38px; border-radius: 50%; background: #16a34a; color: #fff; display: flex; align-items: center; justify-content: center; font-weight: bold; font-size: 0.95rem;">HD</div>
              <div>
                <strong style="color: #fff; font-size: 0.95rem; display: block;">Hakan Dursun</strong>
                <span style="color: #64748b; font-size: 0.8rem;">Fikirtepe Servis</span>
              </div>
            </div>
            <span style="color: #f59e0b; font-size: 0.95rem;">★★★★★</span>
          </div>
          <p style="font-size: 0.92rem; color: #cbd5e1; line-height: 1.6; margin: 0;">"Google'a fikirtepe bilgisayar servisi yazarak buldum. İyi ki de aramışım, anında çözüm buldular."</p>
        </div>
        <div style="margin-top: 15px; padding-top: 12px; border-top: 1px solid rgba(255, 255, 255, 0.05); font-size: 0.8rem; color: #64748b;">
          Google Doğrulanmış Yorum
        </div>
      </div>

    </div>
  </div>
</section>
"""

# Ayrıca LocalBusiness Schema içine aggregateRating ekleyen JSON
AGGREGATE_RATING_SCHEMA = """
    "aggregateRating": {
      "@type": "AggregateRating",
      "ratingValue": "4.8",
      "reviewCount": "26",
      "bestRating": "5",
      "worstRating": "1"
    },
"""

def update_reviews():
    if not os.path.exists(INDEX_PATH):
        print(f"[-] {INDEX_PATH} bulunamadı!")
        return

    with open(INDEX_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    # Yorumlar bölümünü regex ile bul ve gerçek yorumlarla değiştir
    # <section ... id="yorumlar" veya class="...reviews...">
    reviews_pattern = r'<section[^>]*id=["'](?:yorumlar|reviews)["'][^>]*>[\s\S]*?<\/section>'
    if re.search(reviews_pattern, content):
        content = re.sub(reviews_pattern, REVIEWS_HTML.strip(), content, flags=re.DOTALL)
        print("[+] Mevcut yorumlar bölümü gerçek Google yorumlarıyla değiştirildi.")
    else:
        # Alternatif olarak SSS bölümünün hemen öncesine yerleştir
        faq_match = re.search(r'<section[^>]*id=["'](?:sss|faq)["'][^>]*>', content)
        if faq_match:
            idx = faq_match.start()
            content = content[:idx] + REVIEWS_HTML + "\n\n" + content[idx:]
            print("[+] Yorumlar bölümü SSS öncesine eklendi.")
        else:
            # Footer öncesine ekle
            footer_match = re.search(r'<footer[^>]*>', content)
            if footer_match:
                idx = footer_match.start()
                content = content[:idx] + REVIEWS_HTML + "\n\n" + content[idx:]
                print("[+] Yorumlar bölümü footer öncesine eklendi.")

    # Schema içine aggregateRating ekle (SERP'te yıldızların çıkması için)
    if '"aggregateRating"' not in content and '"@type": "ComputerRepair"' in content:
        content = content.replace('"@type": "ComputerRepair",', f'"@type": "ComputerRepair",\n{AGGREGATE_RATING_SCHEMA}')
        print("[+] Schema.org içine 4.8 Yıldız ve 26 Yorum (AggregateRating) yapısal verisi eklendi.")

    with open(INDEX_PATH, "w", encoding="utf-8") as f:
        f.write(content)

    print("[✓] index.html başarıyla güncellendi! Gerçek Google yorumları sitede yayına hazır.")

if __name__ == "__main__":
    update_reviews()
