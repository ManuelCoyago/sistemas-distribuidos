import Pyro4
import base64
import os
import platform

def guardar_video(video_bytes, filename):
    with open(filename, "wb") as f:
        f.write(video_bytes)

def reproducir_video(ruta):
    sistema = platform.system()
    try:
        if sistema == "Windows":
            os.startfile(ruta)
        elif sistema == "Darwin":  # macOS
            os.system(f"open '{ruta}'")
        elif sistema == "Linux":
            os.system(f"xdg-open '{ruta}'")
        else:
            print(f"No se reconoce el sistema operativo: {sistema}")
    except Exception as e:
        print("Error al abrir el reproductor:", e)

def main():
    print("Conectando al servidor Pyro4...")
    uri = Pyro4.locateNS().lookup("video.example")
    video_server = Pyro4.Proxy(uri)

    print("Solicitando video procesado (base64)...")
    video_b64 = video_server.get_processed_video()

    # Decodificar base64 a bytes
    video_bytes = base64.b64decode(video_b64)

    filename = "video_procesado_cliente.mp4"
    guardar_video(video_bytes, filename)
    print(f"Video guardado como {filename}")

    print("Reproduciendo...")
    reproducir_video(filename)

if __name__ == "__main__":
    main()
