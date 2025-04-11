from pytubefix import YouTube


yt = YouTube('https://www.youtube.com/watch?v=22tVWwmTie8&pp=ygUHaG91ZGluaQ%3D%3D')

# Obtener el stream con la mejor resolución
video_stream = yt.streams.get_highest_resolution()

# Descargar el video
video_stream.download(output_path='.', filename='video_descargado_3.mp4')

print("Descarga completada.")
