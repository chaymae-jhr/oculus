import time
from zapv2 import ZAPv2
from termcolor import colored
from zapv2.ascan import ascan
from zapv2.core import core
import os
#we tried to implement zap API basic scans 

ocpath='./'
apiKey = 'q3qmcldb47fruoq48oojulsi2u'

# By default ZAP API client will connect to port 8080
zap = ZAPv2(apikey=apiKey)
def spidering(target):
    print(colored('[-] Spidering target {}'.format(target),"yellow"))
    # The scan returns a scan id to support concurrent scanning
    scanID = zap.spider.scan(target)
    while int(zap.spider.status(scanID)) < 100:
        # Poll the status until it completes
        print(colored('[~] Spider progress %: {}'.format(zap.spider.status(scanID)),"blue"))
        time.sleep(1)

    print(colored('[-] Spider has completed!',"green"))
    # Prints the URLs the spider has crawled
    print(colored('\n'.join(map(str, zap.spider.results(scanID))),"magenta"))
    
def activescan(target,report_path): # ZAP ACTIVE SCAN
    print(colored("[~] Running OWASP zed attack proxy active scan:", 'blue'))
    print(colored('Active Scanning target {}'.format(target),"yellow"))
    scanID = zap.ascan.scan(target)
    while int(zap.ascan.status(scanID)) < 100:
        # Loop until the scanner has finished
        print(colored('[~] Scan progress %: {}'.format(zap.ascan.status(scanID)),"blue"))
        time.sleep(5)

    print(colored('[-] Active scan completed!',"green"))
    print(colored('Hosts: {}'.format(', '.join(zap.core.hosts)),"magenta"))
    if zap.core.alerts(baseurl=target):
        print(colored('[!] Scan Done : Vulnerabilities were found','red'))
    else:
        print(colored('[-] Scan Done : No alerts found','green'))
    print(colored('[-] HTML report generated','green'))
    #generate HTML report 
    os.system('/usr/bin/qterminal 2> /dev/null -e curl http://127.0.0.1:8080/OTHER/core/other/htmlreport/?apikey='+apiKey+' -o '+report_path)
