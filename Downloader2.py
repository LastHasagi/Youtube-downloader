import re
from pytube import YouTube
import time
from alive_progress import alive_bar

def download_video(url):
    video = YouTube(url, on_progress_callback=progress_callback)
    stream = video.streams.get_highest_resolution()
    file_path = stream.download('C:\Vídeos Baixados')

    print("Download concluído!")

def progress_callback(stream, chunk, bytes_remaining):
    total_bytes = stream.filesize
    bytes_downloaded = total_bytes - bytes_remaining
    percentage = (bytes_downloaded / total_bytes) * 100
    progress_bar(int(percentage))

r = input("Deseja baixar um vídeo? ")
while r.lower() == "sim":
    x = input("Insira o link do vídeo: ")

    youtube_regex = r"^(https?\:\/\/)?(www\.youtube\.com|youtu\.?be)\/.+$"
    if re.match(youtube_regex, x):
        with alive_bar(100, bar='blocks') as progress_bar:
            download_video(x)
    else:
        print("Link inválido!")
        retry = input("Deseja inserir um novo link válido? (sim/não): ")
        if retry.lower() == "sim":
            continue
        else:
            print('Finished, thanks for using')
            print('Developed Alücard')
            time.sleep(4)
            exit()

    r = input("Deseja baixar outro vídeo? (sim/não): ")
    if r == "não":
        print('Finished, thanks for using')
        print('Developed Alücard')
        time.sleep(4)
        exit()


