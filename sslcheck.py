#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    sslcheck.py - checks SSL certificates for validity

    Author   : Jonas Björk <jonas.bjork@gmail.com>
    License  : GNU General Public License v2
    Copyright: 2014, Jonas Björk
"""
import socket, ssl

""" Change this list to test your own sites. """
sites = [
    'www.jonasbjork.net',
    'www.google.com'
]

def check_ssl(host, port=443):
    """ The function that checks the target site for SSL cert. """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ssl_sock = ssl.wrap_socket(s, ca_certs="AllCA.pem", cert_reqs=ssl.CERT_REQUIRED )
    ssl_sock.connect((host, port))
    cert = ssl_sock.getpeercert()
    certhost = None
    for field in cert['subject']:
        if field[0][0] == 'commonName':
            certhost = field[0][1]
    s.close()
    return certhost

# Counters
cert_ok = cert_fail = cert_wrng = 0

print "\n>>> SSLcheck by Jonas Björk <jonas.bjork@gmail.com> 2014 <<<"
print ""
print "=== Testing SSL on %s sites ===" % len(sites)
for site in sites:
    try:
        chk = check_ssl(site)
        cert_end = chk[2:]
        if site.endswith(cert_end):
            print "[CERT_OK  ] > Testing SSL on %s ... (%s)" % (site, chk)
            cert_ok = cert_ok + 1
        else:
            print "[CERT_WRNG] > Testing SSL on %s ... (%s)" % (site, chk)
            cert_wrng = cert_wrng + 1
    except ssl.SSLError, e:
        print "[CERT_FAIL] > Testing SSL on %s ... " % (site)
        cert_fail = cert_fail + 1

print "\n=== Result ==="
print "Certificates OK                      : ", cert_ok
print "Certificates OK, but wrong for domain: ", cert_wrng
print "Certificates FAILED                  : ", cert_fail, "\n"

if cert_wrng > 0 or cert_fail > 0:
    print "!!! Note: You have failing certificates, please investigate. !!!\n"
    exit(1)

exit(0)
