from pytube import YouTube
import time 

x = input('Insira o link do vídeo:')

youtube = YouTube(x)

youtube.streams.get_highest_resolution().download('C:\Vídeos Baixados')

y = input('Deseja baixar outro filme ?')
while y == "sim" :
    x = input('Insira o link do vídeo:')

    youtube = YouTube(x)

    ys = youtube.streams.get_highest_resolution().download('C:\Vídeos Baixados')
      
    y = input('Deseja baixar outro filme ?')

else:
    print('programa finalizado')
    print('By Alücard')
    time.sleep(3)
    exit()



