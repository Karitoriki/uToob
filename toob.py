from pytube import YouTube, Playlist
from Spotify import get_token, get_track, download_cover
import subprocess
import os
import mutagen.id3 as mp3tag

parent_dir = 'C:/Users/andre/Documents/Uni/Local Stuff/'
spot_token = get_token()


def setTags(path: str, title: str = "", artist: str = "") -> str | None:
    audio = mp3tag.ID3(path)

    audio.add(mp3tag.TIT2(encoding=3, text=[title]))   # Title

    audio.add(mp3tag.TPE1(encoding=3, text=[artist]))  # Artist

    if (track := get_track(token=spot_token, title=title, artist=artist)) is not None:
        audio.add(mp3tag.TALB(encoding=3, text=[
                  track["album"]["name"]]))   # Album

        album_art = mp3tag.APIC(data=download_cover(
            track["album"]["images"][0]["url"]), mime="image/jpeg", type=3)
        audio.add(album_art)

        audio.add(mp3tag.TDRC(encoding=3, text=[
                  track['album']['release_date'][:-6]]))
    else:
        print("Did not find a title")
        return path
    audio.save()


def mp4_to_mp3(vid_path: str) -> str:
    subprocess.run(['ffmpeg', '-i',
                    os.path.join(vid_path),                 # Videofilename
                    os.path.join(filename := vid_path[:-4] + ".mp3")])  # Audiofilename
    os.remove(vid_path)
    return filename


def Download(link: str, title: str = "", artist: str = "") -> None | str:
    youtubeObject = YouTube(link).streams.get_audio_only()
    youtubeObject.download(output_path="downloadMusic")
    return setTags(
        mp4_to_mp3("downloadMusic/" + youtubeObject.default_filename),
        title=title,
        artist=artist
    )


def get_playlist(list: str) -> None:
    playlist = Playlist(list)
    errorList: list[str] = []
    for song in playlist.videos:
        if isinstance(
            err := Download(
                song.watch_url,
                title=song.title,
                artist=song.author[:-8]
                if song.author[-8:] == ' - Topic'
                else song.author[:]
            ),
            str
        ):
            errorList.append(err)
    print(errorList)


if __name__ == "__main__":
    get_playlist(input("Paste your Playlist link here: "))
    # setTags("downloadMusic/.mp3", "", "")
