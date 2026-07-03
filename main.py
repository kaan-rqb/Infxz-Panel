import requests
import os
import sys
import time
from datetime import datetime

class Colors:
    RED_1 = '\033[38;5;196m'       
    RED_2 = '\033[38;5;160m'       
    RED_3 = '\033[38;5;124m'       
    DARK_RED = '\033[38;5;88m'     
    DEEP_BLOOD = '\033[38;5;52m'   
    WHITE = '\033[38;5;255m'       
    GRAY = '\033[38;5;244m'        
    GREEN = '\033[38;5;46m'        
    END = '\033[0m'                

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/120.0.0.0'
}

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def type_writer(text, delay=0.03):
    """Metni ekrana klavyeyle yazılıyormuş gibi harf harf döker."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

def scan_animation(message="VERI TABANI SORGULANIYOR"):
    """Siber analiz ve tarama efekti."""
    print(f"\n{Colors.GRAY}[{Colors.RED_1}*{Colors.GRAY}] {Colors.WHITE}{message}...", end="")
    sys.stdout.flush()
    
    animation = ["[■□□□□□□□□□]", "[■■□□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■■]"]
    for i in range(len(animation)):
        time.sleep(0.2)
        sys.stdout.write(f"\r{Colors.GRAY}[{Colors.RED_2}*{Colors.GRAY}] {Colors.WHITE}{message} {Colors.RED_1}{animation[i]}")
        sys.stdout.flush()
    print(f" {Colors.GREEN}[BAŞARILI]{Colors.END}\n")
    time.sleep(0.3)

def banner():
    print(f"{Colors.RED_1}██╗███╗   ██╗███████╗██╗  ██╗███████╗        ██████╗  █████╗ ███╗   ██╗███████╗██║     ")
    print(f"{Colors.RED_2}██║████╗  ██║██╔════╝╚██╗██╔╝╚══███╔╝        ██╔══██╗██╔══██╗████╗  ██║██╔════╝██║     ")
    print(f"{Colors.RED_3}██║██╔██╗ ██║█████╗   ╚███╔╝   ███╔╝  ██████╗██████╔╝███████║██╔██╗ ██║█████╗  ██║     ")
    print(f"{Colors.DARK_RED}██║██║╚██╗██║██╔══╝   ██╔██╗  ███╔╝   ╚═════╝██╔═══╝ ██╔══██║██║╚██╗██║██╔══╝  ██║     ")
    print(f"{Colors.DEEP_BLOOD}██║██║ ╚████║██║     ██╔╝ ██╗███████╗        ██║     ██║  ██║██║ ╚████║███████╗███████╗")
    print(f"{Colors.DEEP_BLOOD}╚═╝╚═╝  ╚═══╝╚═╝     ╚═╝  ╚═╝╚══════╝        ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝╚══════╝")
    
    print(f"{Colors.GRAY}┌──────────────────────────────────────────────────────────────────────────────────────┐")
    print(f"  {Colors.RED_1}»»{Colors.WHITE} MADE BY INFXZ TEAM {Colors.RED_1}««{Colors.GRAY}                  |           OSINT STATUS: {Colors.RED_2}ACTIVE {Colors.GRAY}")
    print(f"└──────────────────────────────────────────────────────────────────────────────────────┘{Colors.END}")

def log_result(data):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("sorgu_arsivi.txt", "a", encoding="utf-8") as f:
        f.write(f"\n--- {timestamp} ---\n{str(data)}\n")

def print_data(data):
    print(f"{Colors.GRAY}┌─── {Colors.RED_1}ÇIKARILAN ISTIHBARAT VERILERI{Colors.GRAY} ────────────────────┐{Colors.END}")
    if isinstance(data, list):
        for item in data:
            for k, v in item.items():
                print(f" {Colors.GRAY}│ {Colors.RED_2}{k.upper():<15} {Colors.GRAY}: {Colors.WHITE}{v}{Colors.END}")
            print(f" {Colors.DARK_RED}├────────────────────────────────────────────────┤{Colors.END}")
    elif isinstance(data, dict):
        for k, v in data.items():
            print(f" {Colors.GRAY}│ {Colors.RED_2}{k.upper():<15} {Colors.GRAY}: {Colors.WHITE}{v}{Colors.END}")
    else:
        print(f" {Colors.GRAY}│ {Colors.WHITE}{data}{Colors.END}")
    print(f"{Colors.GRAY}└────────────────────────────────────────────────┘{Colors.END}")

def infxz_creator():
    clear()
    banner()
    print(f"{Colors.RED_1}[+] INFXZ CREATOR: INSANDAN GELIŞ / SOSYAL MÜHENDISLIK MODU{Colors.END}\n")
    sanal_adi = input(f"{Colors.DARK_RED}» Hedef Sanal Adı (Opsiyonel): {Colors.WHITE}").strip()
    tc = input(f"{Colors.DARK_RED}» Hedef TC No > {Colors.WHITE}").strip()
    
    scan_animation("SOSYAL AĞ VE AILE BAGLANTILARI HARITALANDIRILIYOR")
    
    try:
        r_tc = requests.get(f"https://arastir.vip/api/tc.php?tc={tc}", headers=HEADERS, timeout=15)
        r_sulale = requests.get(f"https://arastir.vip/api/sulale.php?tc={tc}", headers=HEADERS, timeout=15)
        
        if r_tc.status_code == 200 and r_sulale.status_code == 200:
            data_tc = r_tc.json()
            data_sulale = r_sulale.json()
            
            g_adi = data_tc.get("adi", "Bilinmiyor")
            a_adi = data_tc.get("anne_adi", "Bilinmiyor")
            b_adi = data_tc.get("baba_adi", "Bilinmiyor")
            a_tc = data_tc.get("anne_tc", "Bilinmiyor")
            b_tc = data_tc.get("baba_tc", "Bilinmiyor")
            amca = data_sulale[0].get("amca_adi", "Bilinmiyor") if isinstance(data_sulale, list) else "Bilinmiyor"
            hala = data_sulale[0].get("hala_adi", "Bilinmiyor") if isinstance(data_sulale, list) else "Bilinmiyor"
            yenge = data_sulale[0].get("yenge_adi", "Bilinmiyor") if isinstance(data_sulale, list) else "Bilinmiyor"
            
            print(f"{Colors.GRAY}┌──────────────────────────────────────────────────────────────────────────────────────┐{Colors.WHITE}")
            
            output_text = (
                f" [!] Veri Sızıntısı Analizi Tamamlandı...\n\n"
                f" {sanal_adi} İnfxzin Gerceklesti. Artık Sana {Colors.RED_1}{g_adi}{Colors.WHITE} Demelimiyim? Ah Ah {Colors.RED_1}{g_adi}{Colors.WHITE}...\n"
                f" O İşlere Bulaşmayacaktın. Şimdi Bu İnfxzi Bile Bile Yönlendireceğim.\n"
                f" Annenin Adı {Colors.RED_2}{a_adi}{Colors.WHITE} | Babanın Adı {Colors.RED_2}{b_adi}{Colors.WHITE}\n"
                f" Kimlik (TC) No: {Colors.RED_1}{tc}{Colors.WHITE} Olduğunu Bilmelisin. Buraya Kadar Çok Korkmuşsundur,\n"
                f" Ama Bu Daha Başlangıç! Zafiyetim Seni En Acı Ölüme Kadar Korkutmak.\n"
                f" Amcanın {Colors.DARK_RED}{amca}{Colors.WHITE}, Halanın {Colors.DARK_RED}{hala}{Colors.WHITE} Hatta Yengenin Adının {Colors.DARK_RED}{yenge}{Colors.WHITE} Olduğunu Bile Bile Konuşuyorum.\n"
                f" Annenin TCsı: {Colors.RED_3}{a_tc}{Colors.WHITE} | Babanın TCsı: {Colors.RED_3}{b_tc}{Colors.WHITE}\n"
                f" Bu İşi Baya Uzatmayacağım, İşleri Kana Çıkarmayalım.\n\n"
                f" {Colors.RED_1}[ SYSTEM LOG ]: /ınfxz\n"
            )
            type_writer(output_text, delay=0.02)
            
            print(f"{Colors.GRAY}└──────────────────────────────────────────────────────────────────────────────────────┘{Colors.END}")
    except Exception as e:
        print(f"\n{Colors.RED_1}[!] İstihbarat Çekilemedi: {e}{Colors.END}")
    input(f"\n{Colors.GRAY}[{Colors.DARK_RED} ANA MENÜYE DÖNMEK IÇIN ENTER {Colors.GRAY}]{Colors.END}")

def sorgu_taslagi(baslik, url_param, api_path):
    clear(); banner()
    print(f"{Colors.RED_2}[+] {baslik} AKTIF{Colors.END}\n")
    inp = input(f"{Colors.DARK_RED}» {url_param.upper()} GIRIN > {Colors.WHITE}").strip()
    
    scan_animation(f"{url_param.upper()} VERILERI SORGULANIYOR")
    
    url = f"https://arastir.vip/api/{api_path}.php?{url_param}={inp}"
    try:
        r = requests.get(url, headers=HEADERS, timeout=15)
        if r.status_code == 200:
            data = r.json()
            if data: print_data(data); log_result(data)
            else: print(f"\n{Colors.DARK_RED}[!] Sisteme Kayıtlı Veri Bulunamadı.{Colors.END}")
    except Exception as e: print(f"\n{Colors.RED_1}[!] API Bağlantı Hatası: {e}{Colors.END}")
    input(f"\n{Colors.GRAY}[{Colors.DARK_RED} ENTER'A BASIN {Colors.GRAY}]{Colors.END}")

def sulale_sorgu(): sorgu_taslagi("SÜLALE VERI ANALIZI", "tc", "sulale")
def adres_sorgu(): sorgu_taslagi("COĞRAFI ADRES TESPITI", "tc", "adres")
def sgk_sorgu(): sorgu_taslagi("SGK / ISYERI ISTHBARATI", "tc", "isyeri")
def gsmtc_sorgu(): sorgu_taslagi("GSM CELLULAR TO TC", "gsm", "gsmtc")
def tcgsm_sorgu(): sorgu_taslagi("TC TO GSM CELLULAR", "tc", "tcgsm")
def tc_sorgu(): sorgu_taslagi("MERKEZI KIMLIK SISTEMI (MERNIS)", "tc", "tc")

def ad_soyad_sorgu():
    clear(); banner()
    print(f"{Colors.RED_2}[+] AD SOYAD SORGULAMA PANELİ{Colors.END}\n")
    adi = input(f"{Colors.DARK_RED}» İsim   > {Colors.WHITE}").strip()
    soyadi = input(f"{Colors.DARK_RED}» Soyad  > {Colors.WHITE}").strip()
    il = input(f"{Colors.DARK_RED}» İl     > {Colors.WHITE}").strip()
    ilce = input(f"{Colors.DARK_RED}» İlçe   > {Colors.WHITE}").strip()
    
    scan_animation("AD SOYAD EŞLEŞMELERI ARANIYOR")
    
    url = f"https://arastir.vip/api/adsoyad.php?adi={adi}&soyadi={soyadi}&il={il}&ilce={ilce}"
    try:
        r = requests.get(url, headers=HEADERS, timeout=15)
        if r.status_code == 200:
            data = r.json()
            if data: print_data(data); log_result(data)
            else: print(f"\n{Colors.DARK_RED}[!] Eşleşen kişi bulunamadı.{Colors.END}")
    except Exception as e: print(f"\n{Colors.RED_1}[!] Hata: {e}{Colors.END}")
    input(f"\n{Colors.GRAY}[{Colors.DARK_RED} ENTER'A BASIN {Colors.GRAY}]{Colors.END}")

def main():
    clear()
    print(f"{Colors.RED_1}[*] INFXZ SHELL BAŞLATILIYOR...")
    time.sleep(0.4)
    print(f"{Colors.RED_2}[*] MODÜLLER YÜKLENIYOR...")
    time.sleep(0.4)
    
    while True:
        clear(); banner()
        print(f" {Colors.GRAY}┌───────────────────────────────────────┐ ┌───────────────────────────────────────┐")
        print(f"   {Colors.RED_1}[01] {Colors.WHITE}Ad Soyad Sorgu                       {Colors.RED_1}[06] {Colors.WHITE}Adres Sorgu")
        print(f"   {Colors.RED_1}[02] {Colors.WHITE}TC Sorgu                             {Colors.RED_1}[07] {Colors.WHITE}Sülale Sorgu")
        print(f"   {Colors.RED_1}[03] {Colors.WHITE}TC - GSM Sorgu                       {Colors.RED_1}[08] {Colors.WHITE}Arşivleri Gör")
        print(f"   {Colors.RED_1}[04] {Colors.WHITE}GSM - TC Sorgu                       {Colors.RED_1}[09] {Colors.WHITE}İnfxz Creator")
        print(f"   {Colors.RED_1}[05] {Colors.WHITE}SGK Sorgu                            {Colors.RED_1}[10] {Colors.WHITE}Güvenli Çıkış")
        print(f" {Colors.GRAY}└───────────────────────────────────────┘ └───────────────────────────────────────┘")
        
        choice = input(f"\n{Colors.RED_1} Kararın {Colors.GRAY}» {Colors.WHITE}").strip()
        
        if choice in ["1", "01"]: ad_soyad_sorgu()
        elif choice in ["2", "02"]: tc_sorgu()
        elif choice in ["3", "03"]: tcgsm_sorgu()
        elif choice in ["4", "04"]: gsmtc_sorgu()
        elif choice in ["5", "05"]: sgk_sorgu()
        elif choice in ["6", "06"]: adres_sorgu()
        elif choice in ["7", "07"]: sulale_sorgu()
        elif choice in ["8", "08"]: 
            clear(); banner()
            print(f"{Colors.RED_2}[+] YEREL ISTIHBARAT ARŞIVI{Colors.END}\n")
            if os.path.exists("sorgu_arsivi.txt"):
                with open("sorgu_arsivi.txt", "r", encoding="utf-8") as f: 
                    print(f"{Colors.WHITE}{f.read()}{Colors.END}")
            else:
                print(f"{Colors.DARK_RED}[!] Arşiv dosyası boş veya bulunamadı.{Colors.END}")
            input(f"\n{Colors.GRAY}[{Colors.DARK_RED} ENTER'A BASIN {Colors.GRAY}]{Colors.END}")
        elif choice in ["220", "0220"]: infxz_creator()
        elif choice == "10": 
            print(f"\n{Colors.DARK_RED}[!] Oturum kapatılıyor...{Colors.END}"); time.sleep(0.8); sys.exit()

if __name__ == "__main__":
    main()

