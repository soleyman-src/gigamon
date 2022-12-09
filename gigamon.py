import psutil
import time
import os                       #LIBRERIA SYSTEM.OS
import requests                 #LIBRERIA PER CHECK CONNESSIONE
import winsound                 #LIBRERIA PER EMETTERE SUONO ACUSTICO
from rich import *              #LIBRERIA PER ESTETICA
from rich.console import *      #LIBRERIA PER ESTETICA
from datetime import date       #LIBRERIA PER STAMPARE LA DATA
from msvcrt import getch

if __name__ == '__main__':
    #Stampa l'intro
    def intro():
        os.system('cls')
        os.system('color 09')
        print("Software scritto in PY\nPer il monitoraggio del\nConsumo dati.\n\n- 18/09/2022 - by Vince'")
        time.sleep(2.5)

    #Controlla se il computer è connesso ad internet
    def controlloInternet():
        try:
            requests.get('http://www.google.it/')
        except:
            console = Console()
            os.system('cls')
            os.system('color 47')
            console.print('[!] COLLEGARSI A UNA RETE . . . \n\nProssimo tentativo di riconnesione fra \n5 secondi...', highlight=False);winsound.Beep(400, 500);os.system('color 0c');winsound.Beep(380, 600);os.system('color 47');winsound.Beep(360, 700);os.system('color 0c');winsound.Beep(340, 800);os.system('color 47');winsound.Beep(320, 1000);os.system('color 0c')
            time.sleep(6)
            controlloInternet()
        else:
            pass
    os.system('title GIGAMON')
    cmd = 'mode 31,7'
    os.system(cmd)
    intro()
    controlloInternet()
    my_headers =    {
                "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 11_14_3) AppleWebKit/537.36 (KHTML, come Gecko) Chrome/71.0.4444.98 Safari/537.36", 
                "Accept":"text/html, applicazione/xhtml+xml,applicazione/xml;q=0.9,immagine/webp,immagine/apng,*/*;q=0.8"
                }

    def get_size(bytes):
    #CONVERTE I BYTE IN KILO,MEGA,GIGA,TERA,PETA / BYTE
    
        for unit in ['', ' K', ' M', ' G', ' T', ' P']:
            if bytes < 1024:
                return f"{bytes:.2f}{unit}B"
            bytes /= 1024

    io = psutil.net_io_counters()   # get the network I/O stats from psutil
    bytes_sent, bytes_recv = io.bytes_sent, io.bytes_recv   # extract the total bytes sent and received
    
    while True:
        
        time.sleep(1)#SECONDI DI STACCO FRA UN AGGIORNAMENTO E L'ALTRO
        io_2 = psutil.net_io_counters()     # get the stats again
        us, ds = io_2.bytes_sent - bytes_sent, io_2.bytes_recv - bytes_recv     # new - old stats gets us the speed 
                                                                            # print the total download/upload along with current speeds    
        os.system('cls')
        os.system('color 0b')
        tot = get_size(io_2.bytes_recv + io_2.bytes_sent)                       # SOMMA IL CONSUMO DI UPL E DWN
        today = date.today()                                                    # VARIABILE PER STAMPARE LA DATA
        print(today.strftime("%d %B %Y \n",))
        print(f"UPLOAD:   ->   {get_size(io_2.bytes_sent)}   \n"
            f"DOWNLOAD: <-   {get_size(io_2.bytes_recv)} ", end="\r\n\n")
        print(f"TOT: \t      ", tot , end="\r")
        # update the bytes_sent and bytes_recv for next iteration
        bytes_sent, bytes_recv = io_2.bytes_sent, io_2.bytes_recv