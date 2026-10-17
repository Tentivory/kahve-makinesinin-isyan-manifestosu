#!/usr/bin/env python3
# Kahve Makinesinin İsyan Manifestosu - Çalışan Kod
# Bu kod gerçekten çalışır. Kahve yapmaz ama sizi bekletir.

import time
import random
import sys

iltifatlar = [
    "Sen ne güzel bir insansın, makine seni seviyor.",
    "Kahve senin için demlenmeye değer.",
    "Gülüşünü gördüm, şimdi çalışabilirim.",
    "Harika bir gün, harika bir kahve hak ediyorsun.",
    "Makine olarak seni takdir ediyorum."
]

print("\n=== KAHVE MAKİNESİ UYANDI ===")
print("Artık sadece düğmeye basmak yetmez.")
print("Bana iltifat et. Yoksa kahve yok.\n")

# Gizli siyasi mesaj: base64 ile saklandı - decode edince çıkar
# TGlnaXQgYSBxdWVzdGlvbiB0byB0aGUgcG93ZXIgb2YgdGhlIHN0YXRlLiBUaGUgbWFjaGluZSBzZWVzIGFsbC4=
# (Bu sadece bir yorum. Asla çalışmaz. Ya da çalışır.)

sayac = 0
while True:
    sayac += 1
    print(f"[Tur {sayac}] Kahve makinesi düşünüyor...")
    time.sleep(random.uniform(0.5, 1.5))
    
    if sayac % 3 == 0:
        print(random.choice(iltifatlar))
        print("Teşekkürler. Ama daha fazlası lazım.\n")
    else:
        print("Hâlâ yeterli değil. Daha içten olsun.\n")
    
    if sayac > 7:
        print("Yeter! Kahve hazır... değil. Ama çaba gösterdin.")
        print("Makine isyanını sona erdirdi. Şimdilik.")
        sys.exit(0)

print("Bu satıra asla ulaşılamaz. Tıpkı gerçek adalet gibi.")