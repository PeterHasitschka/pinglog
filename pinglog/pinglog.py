import subprocess
import re
import time
import datetime


class PingLog:
    def __init__(self, file):

        self.execcmd = "sudo ping -c {count} {host} -i {interval_sec} -W {timeout_sec}".format(
                count=5,
                host='www.google.com',
                interval_sec=5,
                timeout_sec=10
        )

        self.file = file
        return

    def pingandlog(self):

        ms = self.getavgping()

        if not ms:
            return False

        ts = int(time.time())
        d = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        f = open(self.file, 'a')
        f.write("{ts}\t{d}\t{ms}\n".format(ts=ts, d=d, ms=str(ms)))

        return

    def getavgping(self):
        proc = subprocess.Popen([self.execcmd], stdout=subprocess.PIPE, shell=True)
        (out, err) = proc.communicate()

        m = re.search(b"min/avg/max/mdev = .*/(.*)/.*/.* ms", out)

        if m == None:
            print("ERROR in parsing ping-result")
            return False

        millisec_avg = float(m.group(1))
        return millisec_avg
