import pytz
from datetime import datetime
from certifier import CertInfo
from email.utils import parsedate_to_datetime

now = datetime.utcnow().replace(tzinfo=pytz.utc)

def check_host(host):

    cert = CertInfo(host, 443)
    try:
        expires = cert.expire()
    except Exception as e:
        print(f"Error with {host}: {e}")
        return 

    expires = parsedate_to_datetime(expires)
    diff = expires - now
    print(f"{host:60s} {diff.days}")


def check_certs():

    fn = '/Users/ajung/.ssl_domains'

    with open(fn) as fp:
        for line in fp:
            if ' ' in line:
                line, dummy = line.strip().split(' ', 1)
            if line:
                check_host(line)


if __name__ == '__main__':
    check_certs()
