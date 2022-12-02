#!/usr/bin/env python

import json
import socket
import sys, errno
import os
import mcstatus
from mcstatus import JavaServer

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

data = json.load(open("./out.json"))
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
opened_servers = []

for server in data:
	#print("looking at " + server["ip"])
	result = sock.connect_ex((server["ip"], 25565))
	if result == 0:
		pass
	else:
		jav = JavaServer(server["ip"], 25565)
		opened_servers.append([jav, server["ip"]])
	# result = None
	# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	# 	result = (s.connect_ex((server["ip"], 25565)) == 0)
	# print(is_port_in_use(server["ip"]))

for server in opened_servers:
	try:
		status = server[0].status()
		print(f"There is {status.players.online} connected ({server[1]})")
	except Exception:
		pass