#!/usr/bin/python3

from pinglog.pinglog import PingLog

file="log.csv"
pinglogger = PingLog(file)
pinglogger.pingandlog()
