<h1 align="center">Welcome to OCULUS 👋</h1>
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-beta 1.0-blue.svg?cacheSeconds=2592000" />
</p>

> This is a tool that allows the automation of vulnerability scanning and some exploits on a IP/URL target using OWASP ZAP, Nikto, OWASP Nettacker, hydra, ncrack, WPscan and nmap 

## Install

before getting started, you are going to need to install the python libraries needed to run OCULUS, use the command

```sh
pip install -r requirements.txt
```
as oculus has the OWASP ZAP api integrated, you are going to need to install it from its official website 

![image](https://user-images.githubusercontent.com/67756131/141386649-b4220af5-7374-45ce-98eb-e1c0c97b5d15.png)

you are also going to need to install, if not already existing in your environement, Nikto, Nmap, Ncrack, Hydra, WPscan, and OWASP Nettacker.
please refer to : https://owasp.org/www-project-nettacker/

## Usage

```sh
python3 oculus.py -u <IP>
```

## Author

👤 **Chaymae el jouhari and Ilham Ben-nar**
