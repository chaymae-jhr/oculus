import time
from zapv2 import ZAPv2
from termcolor import colored

# The URL of the application to be tested

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
    # If required post process the spider results
    
def activescan(target):
    print(colored("[~] Running OWASP zed attack proxy active scan:", 'blue'))
    print(colored('Active Scanning target {}'.format(target),"yellow"))
    scanID = zap.ascan.scan(target)
    while int(zap.ascan.status(scanID)) < 100:
        # Loop until the scanner has finished
        print(colored('[~] Scan progress %: {}'.format(zap.ascan.status(scanID)),"blue"))
        time.sleep(5)

    print('Active Scan completed')
    # Print vulnerabilities found by the scanning
    print(colored('Hosts: {}'.format(', '.join(zap.core.hosts)),"magenta"))
    print(colored('[!] Alerts: ',"red"))
    print(colored(zap.core.alerts(baseurl=target),"red"))
    with open(str(target)+'/zap_report.html','w') as f:f.write(zap.core.htmlreport(apikey='apikey'))
    print(colored('[-] HTML report generated',"green"))

