import memcache

mc = memcache.Client('127.0.0.1')
x = None
key = "x1-key"
x = mc.get(key)
if x is None:
    x = "Dva"
    mc.set(key, x)
    print("Got key from script")
