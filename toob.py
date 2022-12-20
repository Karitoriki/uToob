from pytube import YouTube, Playlist
import subprocess
import os
import mutagen.id3 as mp3tag
parent_dir = 'C:/Users/andre/Documents/Uni/Local Stuff/'


def setTags(path: str, title: str = "", artist: str = "", album: str = "") -> None:
    audio = mp3tag.ID3(path)
    audio.add(mp3tag.TIT2(encoding=3, text=[title]))   # Title
    audio.add(mp3tag.TPE1(encoding=3, text=[artist]))  # Artist
    audio.add(mp3tag.TALB(encoding=3, text=[album]))   # Album
    audio.save()


def mp4_to_mp3(vid_path: str) -> str:
    subprocess.run(['ffmpeg', '-i',
                    os.path.join(vid_path),                 # Videofilename
                    os.path.join(filename := vid_path[:-4] + ".mp3")])  # Audiofilename
    os.remove(vid_path)
    return filename


def Download(link: str, title: str = "", artist: str = "", album: str = "") -> None:
    youtubeObject = YouTube(link).streams.get_audio_only()
    youtubeObject.download(output_path="downloadMusic")
    setTags(mp4_to_mp3("downloadMusic/" + youtubeObject.default_filename), title=title, artist=artist, album=album)


def get_playlist(list: str) -> None:
    playlist = Playlist(list)
    for item in playlist:
        song = YouTube(item)
        Download(item, title=song.title, artist=song.author[:-8]if song.author[-8:] == ' - Topic' else song.author[:])


if __name__ == "__main__":
    get_playlist(input("Paste your Playlist link here: "))