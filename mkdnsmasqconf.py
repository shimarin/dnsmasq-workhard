#!/usr/bin/python2.7

import sys,glob,argparse

def generate(outfile):
    print >> outfile, "domain-needed"
    print >> outfile, "bogus-priv"
    print >> outfile, "log-queries"
    print >> outfile, "log-facility=/var/log/dnsmasq.log"
    print >> outfile, "no-resolv"
    print >> outfile, "server=/in-addr.arpa/8.8.4.4"

    for domains_file in glob.glob("*.domains"):
        for line in open(domains_file).readlines():
            domain = line.strip()
            if domain == "" or domain.startswith('#'): continue
            print >> outfile, "server=/%s/8.8.8.8" % domain

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--direct-overwrite', "-d", action='store_true', help='Overwrite /etc/dnsmasq.conf directly')
    args = parser.parse_args()

    if args.direct_overwrite:
        with open("/etc/dnsmasq.conf", "w") as f:
            generate(f)
    else:
        generate(sys.stdout)
