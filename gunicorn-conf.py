import os

def numCPUs():
    if not hasattr(os, "sysconf"):
        raise RuntimeError("No sysconf detected.")
    return os.sysconf("SC_NPROCESSORS_ONLN")

bind = "0.0.0.0:8000"
workers = numCPUs() * 2 + 1
pidfile = '/var/log/trends.pid'
proc_name = 'gunicorn/trends'
daemon = True
debug = True
loglevel = "debug"