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
    l=[(),(),(),(),()]
    g=[]
    for i in tcp_ports:
        if 'http' not in g:
            if i[1] == 'http':
            
                print(l)
                l[0]=i
                g.append('http')
        if 'ftp' not in g:
            if i[1] == 'ftp':
                print(l)
                l[1]=i
                print(l)
                g.append('ftp')
                print(g)
        if 'ssh' not in g:
            if i[1] == 'ssh':
                print(l)
                l[2]=i
                g.append('ssh')
        if 'telnet' not in g:
            if i[1] == 'telnet':
                print(l)
                l[3]=i
                g.append('telnet')
        if 'smtp' not in g:
            if i[1] == 'smtp':
                print(l)
                l[4]=i
                g.append('smtp')
                print(g)
    return l

#HTTP ----------------------------------------------------------------------------

def wordpress_att(wp_modules,ip):
    p = Path(wp_modules)
    commandl = p.read_text().splitlines()
    command_string=','.join(commandl)
    try:
        print(colored("[~] Wordpress brute force in process, please wait:", 'blue'))
        os.system('/usr/bin/qterminal -e sudo python '+netpath+' -i'+ip+' -m'+command_string+' -o /home/thevbait/Downloads/studies/oculus/reports/'+str(ip)+'/wordpress.txt')
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
        os.system('/usr/bin/qterminal -e sudo python '+netpath+' -i'+ip+' -m'+command_string+' -o /home/thevbait/Downloads/studies/oculus/reports/'+str(ip)+'/joomla.txt')
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
        os.system('/usr/bin/qterminal -e sudo python '+netpath+' -i'+ip+' -m'+command_string+' -o /home/thevbait/Downloads/studies/oculus/reports/'+str(ip)+'/drupal.txt')
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

#SSH ----------------------------------------------------------------------------
def ssh_brute(ip,port):
    ssh_users='/home/thevbait/Downloads/studies/oculus/wordlists/ssh_default_users.txt'
    ssh_pw='/home/thevbait/Downloads/studies/oculus/wordlists/ssh_default_passwords.txt'
    print(colored("[~] Running Hydra to brute force SSH, please wait:", 'blue'))
    try:
        os.system('/usr/bin/qterminal -e sudo hydra -L '+str(ssh_users)+' -P '+str(ssh_pw)+' ssh://'+str(ip)+' -t 4 -s'+str(port)+' -o /home/thevbait/Downloads/studies/oculus/reports/'+str(ip)+'/ssh.txt')
    except:
        print(colored("[!] problem running Hydra", 'red'))
#SMTP ----------------------------------------------------------------------------
def smtp_brute(enum_wordlist,ip):
    print(colored("[~] Enumerating users using SMTP VRFY, please wait:", 'blue'))
    try:
        os.system('/usr/bin/qterminal -e sudo smtp-user-enum -M VRFY -U '+enum_wordlist+' -t '+str(ip)+' >> /home/thevbait/Downloads/studies/oculus/reports/'+str(ip)+'/smtp_enum.txt')
    except:
        print(colored("[!] problem running smtp_user_enum", 'red'))


