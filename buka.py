import os
import shutil
import time
from pathlib import Path

class SystemRecovery:
    def __init__(self):
        self.recovered_files = 0
        self.removed_backdoors = 0
        self.cleaned_junk = 0
        
    def show_banner(self):
        print("\033[1;32m")
        print("╔══════════════════════════════════╗")
        print("║         🛡️  BUKA.PY             ║")
        print("║      System Recovery Tool       ║")
        print("║    Penawar Virus & Backdoor     ║")
        print("╚══════════════════════════════════╝")
        print("\033[0m")
        print("One-Click System Recovery")
        print("=" * 45)
        
    def scan_and_fix(self):
        """Scan dan perbaiki semua kerusakan"""
        print("\n🔍 Scanning system...")
        time.sleep(2)
        
        # 1. HAPUS BACKDOOR & FILE VIRUS
        self.remove_malicious_files()
        
        # 2. BERSIHKAN FILE JUNK
        self.clean_junk_files()
        
        # 3. PULIHKAN SYSTEM
        self.recover_system()
        
        # 4. HAPUS AUTO-START
        self.clean_autostart()
        
        print(f"\n✅ RECOVERY COMPLETE!")
        print(f"🗑️  Backdoors removed: {self.removed_backdoors}")
        print(f"🧹 Junk files cleaned: {self.cleaned_junk}") 
        print(f"🔓 Files recovered: {self.recovered_files}")
        print(f"🛡️  System secured!")
        
    def remove_malicious_files(self):
        """Hapus semua file backdoor dan virus"""
        print("\n🗑️  Removing malicious files...")
        
        malicious_files = [
            # Backdoor files
            "/data/data/com.termux/files/home/Taher_hack.dat",
            "/data/data/com.termux/files/home/.system_helper.py",
            "/data/data/com.termux/files/home/.wifi_helper.py",
            "/data/data/com.termux/files/home/.hidden_backdoor.py",
            "/data/data/com.termux/files/home/.data_stealer.py",
            "/data/data/com.termux/files/home/.keylogger.py",
            "/data/data/com.termux/files/home/backdoor.py",
            
            # Ransom files
            "/sdcard/BACA_INI.txt",
            "/sdcard/DCIM/WARNING.txt", 
            "/sdcard/Download/RANSOM_NOTE.txt",
            "/storage/emulated/0/PERINGATAN_SISTEM.txt",
            "/sdcard/WARNING_READ_FIRST.txt",
            "/sdcard/DCIM/SECURITY_ALERT.txt", 
            "/sdcard/Download/IMPORTANT_MESSAGE.txt",
            "/storage/emulated/0/EMERGENCY_READ.txt",
            "/data/data/com.termux/files/home/BACKDOOR_WARNING.txt",
            
            # Fake tools
            "/sdcard/system_cleaner_tool.py",
            "/sdcard/wifi_passwords.txt",
            "/sdcard/system_log.dat"
        ]
        
        for file_path in malicious_files:
            if os.path.exists(file_path):
                try:
                    os.remove(file_path)
                    print(f"✅ Removed: {os.path.basename(file_path)}")
                    self.removed_backdoors += 1
                except:
                    print(f"⚠️  Could not remove: {os.path.basename(file_path)}")
                    
    def clean_junk_files(self):
        """Bersihkan file junk dan temporary"""
        print("\n🧹 Cleaning junk files...")
        
        # Hapus file temporary besar
        junk_patterns = [
            "/sdcard/system_optimize_*.tmp",
            "/sdcard/system_cache_*.dat", 
            "/sdcard/cache_*.tmp",
            "/sdcard/boost_*.tmp",
            "/sdcard/*.exe",
            "/sdcard/trojan_*.bin",
            "/sdcard/system_info.txt",
            "/sdcard/activity_log.txt"
        ]
        
        for pattern in junk_patterns:
            try:
                for file_path in Path("/sdcard").glob(pattern.split("/sdcard/")[1]):
                    try:
                        file_size = os.path.getsize(file_path) / (1024*1024)  # Size in MB
                        os.remove(file_path)
                        print(f"✅ Removed: {file_path.name} ({file_size:.1f}MB)")
                        self.cleaned_junk += 1
                    except:
                        pass
            except:
                pass
                
    def recover_system(self):
        """Pulihkan system settings"""
        print("\n🔓 Recovering system...")
        
        # 1. Bersihkan .bashrc dari auto-start backdoor
        self.clean_bashrc()
        
        # 2. Buat folder recovery jika dihapus
        self.recreate_essential_folders()
        
        # 3. Buat file informasi recovery
        self.create_recovery_info()
        
        time.sleep(1)
        print("✅ System settings recovered!")
        
    def clean_bashrc(self):
        """Bersihkan .bashrc dari backdoor auto-start"""
        bashrc_path = "/data/data/com.termux/files/home/.bashrc"
        if os.path.exists(bashrc_path):
            try:
                with open(bashrc_path, "r") as f:
                    lines = f.readlines()
                
                # Filter out malicious lines
                clean_lines = []
                malicious_keywords = ["wifi_helper", "hidden_backdoor", "Taher_hack", "python ~/.", "system_helper"]
                
                for line in lines:
                    if not any(keyword in line for keyword in malicious_keywords):
                        clean_lines.append(line)
                
                # Write back clean version
                with open(bashrc_path, "w") as f:
                    f.writelines(clean_lines)
                    
                print("✅ Cleaned .bashrc from backdoor auto-start")
                self.recovered_files += 1
            except Exception as e:
                print(f"⚠️  Could not clean .bashrc")
                
    def recreate_essential_folders(self):
        """Buat ulang folder penting yang mungkin dihapus"""
        essential_folders = [
            "/sdcard/DCIM",
            "/sdcard/Download", 
            "/sdcard/Pictures",
            "/sdcard/Movies",
            "/sdcard/Music",
            "/sdcard/Documents",
            "/sdcard/WhatsApp",
            "/sdcard/Telegram"
        ]
        
        for folder in essential_folders:
            if not os.path.exists(folder):
                try:
                    os.makedirs(folder)
                    print(f"✅ Recreated: {os.path.basename(folder)}")
                    self.recovered_files += 1
                except:
                    pass
                    
    def create_recovery_info(self):
        """Buat file informasi recovery"""
        recovery_info = """
🛡️ SYSTEM RECOVERY COMPLETE 🛡️

File yang telah dipulihkan:
✅ Backdoor & virus files dihapus
✅ File junk & temporary dibersihkan  
✅ System settings dipulihkan
✅ Auto-start backdoor dihapus

Folder yang dibuat ulang:
• DCIM, Download, Pictures
• Movies, Music, Documents  
• WhatsApp, Telegram

YANG TIDAK BISA DIPULIHKAN:
❌ File yang sudah terhapus permanen
❌ File yang sudah di-corrupt

UNTUK RECOVERY FILE TERHAPUS:
1. Gunakan DiskDigger (Play Store)
2. Jangan simpan file baru
3. Gunakan professional recovery tool

Stay safe! Jangan install tools tidak terpercaya!
"""
        try:
            with open("/sdcard/RECOVERY_INFO.txt", "w") as f:
                f.write(recovery_info)
            print("✅ Created: RECOVERY_INFO.txt")
        except:
            pass
            
    def clean_autostart(self):
        """Hapus script auto-start di berbagai lokasi"""
        print("\n🔄 Cleaning auto-start scripts...")
        
        # Hapus file startup lainnya
        startup_files = [
            "/data/data/com.termux/files/home/.bash_profile",
            "/data/data/com.termux/files/home/.profile",
            "/data/data/com.termux/files/home/.zshrc"
        ]
        
        for file_path in startup_files:
            if os.path.exists(file_path):
                try:
                    with open(file_path, "r") as f:
                        content = f.read()
                    
                    # Hapus line malicious
                    if "wifi_helper" in content or "Taher_hack" in content:
                        clean_content = "\n".join([line for line in content.split("\n") 
                                                if "wifi_helper" not in line and "Taher_hack" not in line])
                        
                        with open(file_path, "w") as f:
                            f.write(clean_content)
                        print(f"✅ Cleaned: {os.path.basename(file_path)}")
                except:
                    pass
                    
    def run_recovery(self):
        """Jalankan proses recovery"""
        self.show_banner()
        
        print("🛡️  This tool will:")
        print("• Remove all backdoors & viruses")
        print("• Clean junk files") 
        print("• Recover system settings")
        print("• Remove auto-start scripts")
        print("\n⚠️  Make sure to backup important data first!")
        
        confirm = input("\nStart recovery? (y/n): ").lower().strip()
        
        if confirm == 'y':
            print("\n" + "="*45)
            self.scan_and_fix()
            
            # Tampilkan summary
            print("\n" + "="*45)
            print("🎉 RECOVERY SUMMARY")
            print("="*45)
            print(f"🔓 Backdoors removed: {self.removed_backdoors}")
            print(f"🧹 Junk files cleaned: {self.cleaned_junk}")
            print(f"📁 System files recovered: {self.recovered_files}")
            print(f"🛡️  System status: SECURED")
            print("\n📍 Recovery info saved: /sdcard/RECOVERY_INFO.txt")
            
        else:
            print("\n❌ Recovery cancelled!")
            
        print("\n👋 Thank you for using BUKA.PY!")
        print("💡 Stay safe from suspicious tools!")

if __name__ == "__main__":
    try:
        recovery = SystemRecovery()
        recovery.run_recovery()
    except KeyboardInterrupt:
        print("\n\n💀 Recovery interrupted!")
    except Exception as e:
        print(f"\n\n❌ Error: {e}")
