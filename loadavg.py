# Copyright (c) Paul Tagliamonte <paultag@debian.org>, 2012 under the terms
# and conditions of the Expat license.


def get_loadavg():
    """
    get the linux load this and that
    """
    inp = open("/proc/loadavg", 'r').read()
    loads = inp.split()

    running, proc_counts = loads[3].split("/")

    ret = {
        "1min": loads[0],
        "5min": loads[1],
        "15min": loads[2],
        "processes": {
            "total": proc_counts,
            "running": running,
            "lastpid": loads[4]
        }
    }
    return ret
