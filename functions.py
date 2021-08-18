import os
import nmap
from pathlib import Path
from termcolor import colored

netpath='/home/thevbait/Nettacker/nettacker.py'

def save_csv_data(nm_csv,path):
    with open(path+'nmap.csv','w') as output:
        output.write(nm_csv)


def tcp_protocols_test(ip):
    print(colored("[~] Running Nmap:", 'blue'))
    nm=nmap.PortScanner()
    nm.scan(ip,'-','-A')
    csv=nm.csv()
    path='/home/thevbait/Downloads/studies/oculus/reports/'+str(ip)+'/nmap.csv'
    save_csv_data(csv,path)
    print(colored("[-] Nmap run succesfully:",'green'))
    tcp_p=[]
    for port in nm[ip].all_tcp():
        state = nm[ip]['tcp'][port]['state']
        p_name=nm[ip]['tcp'][port]['name']
        if state == 'open':
            tcp_p.append((port,p_name))
            if p_name == 'http':
                try :
                    cms=nm[ip]['tcp'][port]['script']['http-generator']
                except:
                    cms=''
    return tcp_p,cms

# protocols from nmap output -----------------------------------

def protocols(tcp_ports):
    l=[(),()]
    for i in tcp_ports:
        if i[1] == 'http':
            l[0]=i
        elif i[1] == 'ftp':
            l[1]=i
    return l

#HTTP ----------------------------------------------------------------------------

def wordpress_att(wp_modules,ip):
    p = Path(wp_modules)
    commandl = p.read_text().splitlines()
    command_string=','.join(commandl)
    try:
        print(colored("[~] Wordpress brute force in process, please wait:", 'blue'))
        os.system('/usr/bin/qterminal -e sudo python '+netpath+' -i'+ip+' -m'+command_string+' >> /home/thevbait/Downloads/studies/oculus/reports/'+str(ip)+'/wordpress.txt')
        os.system('/usr/bin/qterminal -e sudo wpscan --url'+ip+' -P /home/thevbait/Downloads/studies/oculus/wordlists/rock100.txt >> /home/thevbait/Downloads/studies/oculus/reports/'+str(ip)+'/wordpress.txt')
        print(colored("[-] Wordpress brute force successful:", 'green'))
    except:
        print(colored("[!] you need root privilege to run the scanner", 'red'))


#********************** JOOMLA SCAN ***********************************

def joomla_nettacker(joomla_modules,ip):
    p = Path(joomla_modules)
    commandl = p.read_text().splitlines()
    command_string=','.join(commandl)
    try:
        print(colored("[~] joomla scan in process, please wait:", 'blue'))
        os.system('/usr/bin/qterminal -e sudo python '+netpath+' -i'+ip+' -m'+command_string+' >> /home/thevbait/Downloads/studies/oculus/reports/'+str(ip)+'/joomla.txt')
        print(colored("[-] joomla scan successful:", 'green'))
    except:
        print(colored("[!] you need root privilege to run the scanner", 'red'))



#***********************   DRUPAL SCAN ********************************
def drupal_nettacker(drupal_modules,ip):
    p = Path(drupal_modules)
    commandl = p.read_text().splitlines()
    command_string=','.join(commandl)
    try:
        print(colored("[~] drupal scan in process, please wait:", 'blue'))
        os.system('/usr/bin/qterminal -e sudo python '+netpath+' -i'+ip+' -m'+command_string+' >> /home/thevbait/Downloads/studies/oculus/reports/'+str(ip)+'/drupal.txt')
        print(colored("[-] drupal scan successful:", 'green'))
    except:
        print(colored("[!] you need root privilege to run the scanner", 'red'))

def general():
    pass



#FTP ----------------------------------------------------------------------------
def ftp_brute(ip,port):
    print(colored("[~] Running ncrack, please wait:", 'blue'))
    print(str(ip)+':'+str(port))
    os.system('/usr/bin/qterminal -e sudo ncrack --pairwise '+str(ip)+':'+str(port)+' -oN /home/thevbait/Downloads/studies/oculus/reports/'+str(ip)+'/ftp.txt')
    print('salam')

def ftp_nettacker(ftp_modules,ip):
    print(colored("[~] Nettacker FTP modules running:", 'blue'))
    p = Path(ftp_modules)
    commandl = p.read_text().splitlines()
    command_string=','.join(commandl)
    print(command_string)
    try:
        os.system('/usr/bin/qterminal -e sudo python '+netpath+' -i'+ip+' -m '+command_string+' -o /home/thevbait/Downloads/studies/oculus/reports/'+str(ip)+'/ftp_nettacker.txt')
    except:
        print(colored("[!] you need root privilege to run nettacker ", 'red'))

#*************** OWASP ZAP ******************

def owasp_zap(ip):
    print(colored("[~] Running OWASP ZAP, please wait:", 'blue'))
    try:
        print(colored("[~] owasp zap scan in process, please wait:", 'blue'))
        os.system('/usr/bin/qterminal -e sudo docker run -t owasp/zap2docker-stable zap-full-scan.py -t http://'+ip+'/ > /root/tools/oculus-main/reports/'+str(ip)+'/zap.txt')
        print(colored("[-] owasp zap scan successful:", 'green'))
    except:
        print(colored("[!] you need root privilege to run the scanner", 'red'))
