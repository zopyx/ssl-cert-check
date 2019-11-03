import os
import pytz
import plac
from datetime import datetime
from certifier import CertInfo
from email.utils import parsedate_to_datetime

now = datetime.utcnow().replace(tzinfo=pytz.utc)
domains_filename = os.path.expandvars('$HOME/.ssl_domains')

def check_host(host):

    try:
        cert = CertInfo(host, 443)
        expires = cert.expire()
    except Exception as e:
        print(f"Error with {host}")
        return 
    expires = parsedate_to_datetime(expires)
    diff = expires - now
    print(f"{host:60s} {diff.days}")


def check_certs(domains_filename=domains_filename):

    print(f"Reading configuration {domains_filename}")
    with open(domains_filename) as fp:
        for line in fp:
            line = line.strip()
            if not line:
                continue
            if ' ' in line:
                line, dummy = line.split(' ', 1)
            check_host(line)


def main():
    import plac; plac.call(check_certs)

if __name__ == '__main__':
    main()