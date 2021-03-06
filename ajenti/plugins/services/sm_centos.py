import subprocess

from ajenti.api import *

from api import ServiceManager
from sm_sysvinit import SysVInitService


@plugin
class CentOSServiceManager (ServiceManager):
    platforms = ['centos']

    def get_all(self):
        r = []
        for line in subprocess.check_output(['chkconfig', '--list']).splitlines():
            tokens = line.split()
            if len(tokens) < 3:
                continue

            name = tokens[0]
            s = SysVInitService(name)
            s.refresh()
            r.append(s)
        return r
