from pytube import Playlist
import colorama
#init colorama
colorama.init();

#get url for playlist
url = input(colorama.Fore.GREEN+"Entrer l'url: ");

playlist = Playlist(url);

def on_progress(stream,chunk,bytes_remaining):
    
    print(f"100-{round(bytes_remaining / stream.filesize*100,2)}%");

for video in playlist.videos:
    video.register_on_progress_callback(on_progress);
    video.streams.get_by_resolution("360p").download('./nice_playlist')