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

SEC_PATH = "/usr/bin/"

def print_banner():
	print(colored(text2art ("OCULUS"),'cyan'))
	print(colored("|_ Version :", 'red',attrs=['bold']),colored(" 1.0#beta","cyan"))
	print(colored("|_ Authors :", 'red',attrs=['bold']),colored(" Ilham & Chaymae","cyan"))
	print(colored("|_ Usage :",'red',attrs=['bold']),colored(" python3 oculus.py [options]","cyan"))

def args_parser():
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
		tcp_ports,cms=functions.tcp_protocols_test(ip)
		print(tcp_ports)
		protocols=functions.protocols(tcp_ports)
		http=protocols[0]
		ftp=protocols[1]
		ssh=protocols[2]
		telnet=protocols[3]
		smtp=protocols[4]
		print(protocols)
		if len(http) != 0  :
			print(colored("HTTP open port found", 'yellow'))
			if 'wordpress' in cms:
				functions.wordpress_att('./net-modules/wp_modules.txt',ip)
			elif 'joomla' in cms:
				functions.joomla_nettacker('./net-modules/joomla_modules.txt',ip)
			elif 'drupal' in cms:
				functions.drupal_nettacker('./net-modules/drupal_modules.txt',ip)
	
			else:
				pass
			try:
				print(colored("[~] Running Nikto:", 'blue'))
				os.system(SEC_PATH  + 'qterminal -e "nikto +h '+url+' -output '+path_dir+'/nikto.txt"') # This will run nikto to scan the target from top 10 owasp vuln
				print(colored("[-] Nikto run successfully:", 'green'))
			except:
				print(colored("[!] Nikto couldn't be run correctly", 'red'))
			try:
				print(colored("[~] Running Gobuster:", 'blue'))
				os.system(SEC_PATH  + 'qterminal -e "gobuster -u '+url+ ' -w /home/eddie/Bureau/tools/directory-list-2.3-medium.txt /dirsearch.txt"') # This will run gobuster against the target to find hidden folders and files in the server (in will work if there is a web server) !
				print(colored("[-] Gobuster run successfully:", 'green'))
			except:
				print(colored("[!] Gobuster couldn't be run correctly", 'red'))

		if len(ftp) != 0:
			print(colored("FTP open port found", 'yellow'))
			try:
				print(ftp)
				ftp_port=ftp[0]
				print(ftp_port)
				print(colored("[~] FTP brute force in process, please wait:",'blue'))
				functions.ftp_brute(ip,ftp_port)
				functions.ftp_nettacker('/home/thevbait/Downloads/studies/oculus/net-modules/ftp_modules',ip)
				print(colored("[-] FTP brute force done:",'green'))
			except:
				print(colored("[!] FTP Testing failed", 'red'))


		if len(smtp) != 0:
			pass
		else:
			pass
	except ValueError as e:
		print(e)
	except:
		print("failed")
	
	


if __name__ == '__main__':
	print_banner()
	print("\n")
	if sys.version_info.major < 3 :
		print("use python3" )
		exit(0)
	main()
	
