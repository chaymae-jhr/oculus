#!/usr/bin/python3
import argparse
import os
import sys
sys.path.append('__init__')
import get_ip as ad
import file_mg as file 
from art import *
from termcolor import colored
import functions
import zap_scan

SEC_PATH = "/usr/bin/"
ocpath='/home/administrateur/oculus/oculus'
def print_banner(): #Print the oculus banner 
	print(colored(text2art ("OCULUS"),'cyan'))
	print(colored("|_ Version :", 'red',attrs=['bold']),colored(" 1.0#beta","cyan"))
	print(colored("|_ Authors :", 'red',attrs=['bold']),colored(" Ilham & Chaymae","cyan"))
	print(colored("|_ Usage :",'red',attrs=['bold']),colored(" python3 oculus.py [options]","cyan"))

def args_parser():#parse the argument given and select the ip 
	parser = argparse.ArgumentParser()
	parser.add_argument('-u', help='valid url or ip of the target')
	return parser.parse_args()

def main():
	try:	
		args = vars(args_parser())
		url= args['u']
		path_dir ="reports/" + url
		file.create_dir(path_dir)
		ip = ad.get(url)
		print('The IP Address is :',ip)	
		tcp_ports,cms=functions.tcp_protocols_test(ip) #get a dictionnary of services running on the vm and the cms if used 
		protocols=functions.protocols(tcp_ports)
		# define important TCP protocols	
		http=protocols[0]
		ftp=protocols[1]
		ssh=protocols[2]
		telnet=protocols[3]
		smtp=protocols[4]
		print(colored('the protocols that were detected : ','green',colored(protocols,'cyan')))
		if len(http) != 0  :
			print(colored("HTTP open port found", 'yellow')) 
			if 'wordpress' in cms:
				print(colored("Wordpress template found", 'yellow'))
				functions.wordpress_att('./net-modules/wp_modules',ip)
			elif 'joomla' in cms:
				print(colored("Joomla template found", 'yellow'))
				functions.joomla_nettacker('./net-modules/joomla_modules',ip)
			elif 'drupal' in cms:
				print(colored("Drupal template found", 'yellow'))
				functions.drupal_nettacker('./net-modules/drupal_modules',ip)
	
			else:
				pass
			try:
				print(colored("[~] Running Nikto:", 'blue'))
				os.system(SEC_PATH  + 'qterminal 2> /dev/null -e nikto +h '+url+' -output '+path_dir+'/nikto.txt') # This will run nikto to scan the target from top 10 owasp vuln
				print(colored("[-] Nikto run successfully:", 'green'))
			except:
				print(colored("[!] Nikto couldn't be run correctly", 'red'))
			try:
				print(colored("[~] Running OWASP zed attack proxy active scan:", 'blue'))
				urlzap=functions.formaturl(url)
				zap_scan.spidering(urlzap)
				zap_scan.activescan(urlzap,ocpath+'/reports/'+ip+'/zap_report.html')
			except:
				print(colored("[!] owasp zap couldn't be run correctly, plase check the url format, set the port to 8080 and check the key ", 'red'))

		if len(ftp) != 0:
			print(colored("FTP open port found", 'yellow'))
			try:
				ftp_port=ftp[0]
				print(colored("[~] FTP brute force in process, please wait:",'blue'))
				functions.ftp_brute(ip,ftp_port)
				functions.ftp_nettacker(ocpath+'/net-modules/ftp_modules',ip)
				print(colored("[-] FTP brute force done:",'green'))
			except:
				print(colored("[!] FTP Testing failed", 'red'))

		if len(ssh) != 0:
			try:
				ssh_port = ssh[0]
				print(colored("[~] SSH brute force in process, please wait:",'blue'))
				functions.ssh_brute(ip,ssh_port)
			except:
				print(colored("[!] SSH Testing failed", 'red'))
		
		if len(telnet) != 0:
			try:
				telnet_port = telnet[0]
				print(ssh_port)
				print(colored("[~] telnet brute force in process, please wait:",'blue'))
				functions.telnet_brute(ip)
			except:
				print(colored("[!] telnet Testing failed", 'red'))
		if len(smtp) != 0:
			try:
				smtp = smtp[0]
				print(colored("[~] SMTP exploit in process, please wait:",'blue'))
				functions.smtp_enum('/usr/share/wordlists/fern-wifi/common.txt',ip)
			except:
				print(colored("[!] SMTP Testing failed", 'red'))
		print(colored("[-] OCULUS scan done:",'green'))

	except ValueError as e:
		print(e)
	except:
		print(colored("[!] OCULUS scan failed",'red'))
	
	


if __name__ == '__main__':
	print_banner()
	print("\n")
	if sys.version_info.major < 3 :
		print("use python3" )
		exit(0)
	main()
	
