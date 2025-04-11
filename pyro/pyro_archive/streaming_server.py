#servidor de lectura de archivos

import Pyro4
@Pyro4.expose

class Archivo:

    def read_file(self,filename):
        try:
            with open(filename,"r") as archivo:
                content = archivo.read()
            return content
        except FileNotFoundError:
            return "File not found"


    def write_file(self, filename):
        try:
            with open(filename, "w") as archivo:
                content = archivo.read()
            return content
        except FileNotFoundError:
                return "File not found"


daemon = Pyro4.Daemon()
ns = Pyro4.locateNS()

uri = daemon.register(Archivo)
ns.register("read and write", uri)
print("servidor listo", uri)
daemon.requestLoop()

