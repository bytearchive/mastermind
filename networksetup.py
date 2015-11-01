import subprocess
import re

# Wraps the networksetup CLI
def networksetup(*arguments):
    return subprocess.check_output(['/usr/sbin/networksetup'] + list(arguments))

def get_webproxy(service):
    return networksetup('-getwebproxy', service)

def set_webproxy(*arguments):
    return networksetup('-setwebproxy', *arguments)

def set_secure_webproxy(*arguments):
    return networksetup('-setsecurewebproxy', *arguments)

def set_webproxy_state(*arguments):
    return networksetup('-setwebproxystate', *arguments)

def set_secure_webproxy_state(*arguments):
    return networksetup('-setsecurewebproxystate', *arguments)

def service_order():
    return networksetup('-listnetworkserviceorder')

def service_map():
    return re.findall(r'\(\d+\)\s(.*)$\n\(.*Device: (.+)\)$',
                      service_order(),
                      re.MULTILINE)