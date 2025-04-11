import base64
import Pyro4
from moviepy.editor import VideoFileClip

@Pyro4.expose
class VideoServer:
    def get_processed_video(self):
        clip = VideoFileClip("pyro_vids/video_descargado.mp4").subclip(0, 5)
        output_path = "processed_video.mp4"
        clip.write_videofile(output_path, codec="libx264", audio_codec="aac", verbose=False, logger=None)

        with open(output_path, "rb") as f:
            vid = f.read()
daemon = Pyro4.Daemon()
ns = Pyro4.locateNS()
uri = daemon.register(VideoServer)
ns.register("video.example", uri)
print("Servidor disponible en:", uri)
daemon.requestLoop()
