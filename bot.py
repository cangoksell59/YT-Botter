import os
import time
import webbrowser

os.system("sudo apt-get install figlet")
os.system("clear")


os.system("figlet XALE")
print(" ")
print("YT-BoTTeR v2.0 - By Xale - GitHub: @xaletr")
print(" ")

video = input("https://www.youtube.com/watch?v=2tDkof8bp-8 : ")

os.system("clear")
time.sleep(3)
print("Yükleniyor...")
print("Gönderilecek İzlenme : 1000")
time.sleep(2)
os.system("clear")


def send():
 os.system("anonsurf stop")
 print("1 İzlenme Gönderildi.. 15 Saniye Bekleniyor..")
 os.system("anonsurf start")
 webbrowser.open(video)
 time.sleep(15)

# 5 view:
send()
send()
send()
send()
send()

# 5 view:
send()  
send()
send()
send()
send()

# total : 10

# 5 view:
send()  
send()
send()
send()
send()

# 5 view:
send()  
send()
send()
send()
send()

# total : 20

os.system("clear")
print("İzlenmeler Gönderildi , Gönderilen Toplam İzlenme Sayısı : 20")
print("İzlenme Gönderilen Video : " + video)
print("xalesecurity.wordpress.com")
