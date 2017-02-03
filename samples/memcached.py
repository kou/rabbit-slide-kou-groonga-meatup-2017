#!/usr/bin/env python

import bmemcached

servers = ("127.0.0.1:11211",)
client = bmemcached.Client(servers)
print(client.get("abc"))
client.set("abc", "Hello")
print(client.get("abc"))
# client.delete("abc")
