import os
import multiprocessing

bind= '127.0.0.1:8000'
backlog = 2048
keepalive = 5
timeout = 1024
workers = multiprocessing.cpu_count()*2+1
worker_class = 'sync'
debug = False
proc_name = 'gunicorn.proc'
