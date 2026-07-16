#!/usr/bin/env python3
import os
import sys
import time
import random
import json
import platform
import subprocess
from datetime import datetime

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def banner():
    print("\033[1;36m" + "="*50)
    print("  FULEX TOOL V15 - 30+ MODÜL - PROFESSIONAL")
    print("="*50 + "\033[0m")

# ---------- SIZMA & ZAFİYET (1-4) ----------
def sql_injection():
    print("[1] SQL Injection – hedef: http://test.com/login")
    payloads = ["' OR '1'='1", "'; DROP TABLE users; --", "' UNION SELECT null,username,password FROM users--"]
    for p in payloads:
        print(f"  Deneniyor: {p}")
        time.sleep(0.5)
    print("  [BULUNDU] Tablo: users, sütunlar: id, username, password")
    with open("sql_result.txt", "w") as f:
        f.write("admin:pass123\nroot:toor\ntest:test")

def admin_bulma():
    print("[2] Admin panel taranıyor (ortak dizinler)...")
    dirs = ["/admin", "/login", "/administrator", "/panel", "/yonetim", "/admin.php"]
    found = random.sample(dirs, 3)
    for d in found:
        print(f"  + {d}")
    with open("admin_panels.txt", "w") as f:
        f.write("\n".join(found))

def subdomain_bulma():
    print("[3] Subdomain bulma – hedef: test.com")
    subs = ["mail", "dev", "api", "ftp", "blog", "panel", "admin"]
    found = random.sample(subs, 4)
    for s in found:
        print(f"  {s}.test.com")
    with open("subdomains.txt", "w") as f:
        f.write("\n".join([s+".test.com" for s in found]))

def port_tarama():
    print("[4] Port tarama (1-1024) – hedef: 127.0.0.1")
    open_ports = [22, 80, 443, 3306, 8080]
    for port in open_ports:
        print(f"  Port {port} AÇIK")
        time.sleep(0.2)
    with open("ports.txt", "w") as f:
        f.write(str(open_ports))

# ---------- HEDEF BİLGİ (5-8) ----------
def discord_id_info():
    uid = input("  Discord ID girin: ")
    print(f"[5] ID: {uid} – Kullanıcı: FakeUser#1234, Avatar: https://cdn.discordapp.com/...")
    print("  Ortak sunucu sayısı: 3 (Demo)")

def webhook_tuzak():
    url = "https://discord.com/api/webhooks/123456/abcdef"
    print(f"[6] Tuzak webhook oluşturuldu: {url}")
    with open("webhook.txt", "w") as f:
        f.write(url)

def osint():
    email = input("  E-posta adresi girin: ")
    print(f"[7] OSINT – {email} ile bağlantılı hesaplar:")
    print("  Twitter: @fakeuser, Instagram: fakeuser, GitHub: fakeuser")
    with open("osint_data.txt", "w") as f:
        f.write(f"Email: {email}\nTwitter: @fakeuser\nInstagram: fakeuser")

def discord_id_ip():
    uid = input("  Discord ID girin: ")
    ip = f"192.168.{random.randint(1,255)}.{random.randint(1,255)}"
    print(f"[8] ID: {uid} – IP: {ip}, Konum: İstanbul, TR (demo)")

# ---------- TOKEN & HESAP (9-12) ----------
def token_grabber():
    print("[9] Token grabber – local disk'te token aranıyor...")
    tokens = ["token1_fake", "token2_fake", "token3_fake"]
    for t in tokens:
        print(f"  + {t}")
    with open("grabbed_tokens.txt", "w") as f:
        f.write("\n".join(tokens))

def token_checker():
    print("[10] Token kontrolü:")
    tokens = ["gecerli_token", "gecersiz_token", "gecerli_token2"]
    for t in tokens:
        status = "✓ Geçerli" if "gecerli" in t else "✗ Geçersiz"
        print(f"  {t} -> {status}")
        time.sleep(0.3)

def sifre_hirsizi():
    print("[11] Şifre hırsızı – tarayıcı şifreleri çekiliyor (demo):")
    sites = {"facebook.com": "user:pass", "gmail.com": "mail:şifre", "instagram.com": "insta:123"}
    for site, cred in sites.items():
        print(f"  {site} -> {cred}")
    with open("passwords.txt", "w") as f:
        json.dump(sites, f)

def cookie_stealer():
    print("[12] Cookie Stealer – çerezler toplanıyor:")
    cookies = {"sessionid": "abc123", "token": "xyz789", "user": "admin"}
    for k, v in cookies.items():
        print(f"  {k}: {v}")
    with open("cookies.txt", "w") as f:
        json.dump(cookies, f)

# ---------- VERİ TOPLAMA (13-17) ----------
def keylogger():
    print("[13] Keylogger başlatıldı. Tuş vuruşları 'logs.txt' dosyasına yazılıyor.")
    with open("logs.txt", "a") as f:
        f.write(f"[{datetime.now()}] Keylog başladı (demo)\n")
    for i in range(3):
        time.sleep(0.5)
        print(f"  [sanal tuş] {chr(random.randint(97,122))}")
    print("  (Sadece simülasyon – gerçek keylogger yok)")

def ekran_kaydi():
    print("[14] Ekran kaydı başlatıldı – screenshot 'screen.png' alındı.")
    with open("screen.png", "w") as f:
        f.write("Fake screenshot data")
    print("  Dosya: screen.png (sahte içerik)")

def webcam():
    print("[15] Webcam erişimi – kamera açılıyor...")
    time.sleep(1)
    print("  [UYARI] Gerçek kamera yok, simülasyon.")
    with open("webcam.jpg", "w") as f:
        f.write("Fake webcam image")

def sistem_bilgisi():
    print("[16] Sistem bilgisi:")
    print(f"  OS: {platform.system()} {platform.release()}")
    print(f"  Makine: {platform.machine()}")
    print(f"  İşlemci: {platform.processor()}")
    print(f"  Python: {sys.version}")
    with open("sysinfo.txt", "w") as f:
        f.write(f"{platform.uname()}")

def wifi_sifre():
    print("[17] Wi-Fi şifreleri (iOS'ta bu modül çalışmaz, simüle ediliyor):")
    networks = {"WiFi1": "12345678", "WiFi2": "password", "WiFi3": "qwerty"}
    for ssid, pwd in networks.items():
        print(f"  {ssid} -> {pwd}")
    with open("wifi_passwords.txt", "w") as f:
        json.dump(networks, f)

# ---------- DOSYA TARAMA (18-23) ----------
def kripto_cuzdan():
    print("[18] Kripto cüzdan dosyaları taranıyor:")
    wallets = ["wallet.dat", "metamask.json", "btc_private.key"]
    for w in wallets:
        print(f"  + {w}")
    with open("wallets.txt", "w") as f:
        f.write("\n".join(wallets))

def ssh_anahtar():
    print("[19] SSH anahtarları:")
    keys = ["id_rsa", "id_ed25519", "id_ecdsa"]
    for k in keys:
        print(f"  + {k}")
    with open("ssh_keys.txt", "w") as f:
        f.write("\n".join(keys))

def whatsapp_oturum():
    print("[20] WhatsApp oturum dosyaları:")
    files = ["wa_session.db", "credentials.json", "backup.crypt"]
    for f in files:
        print(f"  + {f}")

def vpn_config():
    print("[21] VPN config dosyaları:")
    configs = ["vpn.ovpn", "openvpn.conf", "wireguard.conf"]
    for c in configs:
        print(f"  + {c}")

def ftp_bilgileri():
    print("[22] FTP bilgileri çekildi:")
    data = {"host": "ftp.test.com", "user": "admin", "pass": "demo123"}
    print(f"  Host: {data['host']}\n  User: {data['user']}\n  Pass: {data['pass']}")
    with open("ftp.txt", "w") as f:
        json.dump(data, f)

def tarayici_gecmis():
    print("[23] Tarayıcı geçmişi (son 5 site):")
    sites = ["https://google.com", "https://youtube.com", "https://github.com", "https://stackoverflow.com", "https://reddit.com"]
    for s in sites:
        print(f"  {s}")
    with open("history.txt", "w") as f:
        f.write("\n".join(sites))

# ---------- DİĞER (24-28) ----------
def usb_yayilma():
    print("[24] USB yayılma – takılı USB sürücülerine kopyalanıyor...")
    drives = ["/Volumes/USB1", "/Volumes/USB2"] if os.name == 'posix' else ["D:\\", "E:\\"]
    for d in drives:
        print(f"  + {d} hedeflendi (simülasyon)")

def keylog_analiz():
    print("[25] Keylog analiz – logs.txt okunuyor...")
    try:
        with open("logs.txt", "r") as f:
            content = f.read()
        print(f"  İçerik: {content[:50]}...")
    except:
        print("  logs.txt bulunamadı, önce keylogger çalıştırın.")

def rapor_olustur():
    print("[26] Rapor oluşturuluyor...")
    rapor = {
        "tarih": str(datetime.now()),
        "sistem": platform.uname()._asdict(),
        "bulunan_dosyalar": os.listdir(".")
    }
    with open("rapor.json", "w") as f:
        json.dump(rapor, f, indent=2)
    print("  rapor.json oluşturuldu.")

def kalicilik_ekle():
    print("[27] Kalıcılık eklendi – crontab veya systemd (demo):")
    cmd = "python3 /path/to/fulex.py"
    print(f"  Eklenen: */5 * * * * {cmd}")
    with open("cron.txt", "w") as f:
        f.write(f"*/5 * * * * {cmd}")

def tumunu_calistir():
    print("[28] TÜM MODÜLLER ÇALIŞTIRILIYOR...")
    for func in [sql_injection, admin_bulma, subdomain_bulma, port_tarama,
                 discord_id_info, webhook_tuzak, osint, discord_id_ip,
                 token_grabber, token_checker, sifre_hirsizi, cookie_stealer,
                 keylogger, ekran_kaydi, webcam, sistem_bilgisi, wifi_sifre,
                 kripto_cuzdan, ssh_anahtar, whatsapp_oturum, vpn_config,
                 ftp_bilgileri, tarayici_gecmis, usb_yayilma, keylog_analiz,
                 rapor_olustur, kalicilik_ekle]:
        print("\n---")
        func()
        time.sleep(0.5)
    print("\n[+] Tüm modüller tamamlandı.")

def cikis():
    print("Çıkış yapılıyor. Hoşçakal.")
    sys.exit(0)

def main():
    while True:
        clear()
        banner()
        print("\033[1;33mSIZMA & ZAFİYET (1-4)\033[0m")
        print("[1] SQL Injection")
        print("[2] Admin Panel Bulma")
        print("[3] Subdomain Bulma")
        print("[4] Port Tarama")
        print("\n\
