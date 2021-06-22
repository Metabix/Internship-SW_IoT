from cpppo.server.enip import client

HOST = "192.168.137.100"
TAGS = ["@4/100/3"]

with client.connector(host=HOST) as conn:
    for index, descr, op, reply, status, value in conn.synchronous(
            operations=client.parse_operations(TAGS)):
        print(": %20s: %s" % (descr,value))
