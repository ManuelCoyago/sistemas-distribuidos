import Pyro4

ns=Pyro4.locateNS()
uri= ns.lookup("read and write")
archivo= Pyro4.Proxy(uri)
print(f"suma: {archivo.read_file("text.txt")}")
print(f"suma: {archivo.write_file("text.txt")}")