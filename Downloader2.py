from pytube import YouTube
import time 
import tweepy
import requests

X = input('Deseja baixar do youtube ou do twitter ? 1 para youtube 2 para twitter')

if X == 1:
#youtube donwloader
    x1 = input('Insira o link do vídeo:')

    youtube = YouTube(x1)

    youtube.streams.get_highest_resolution().download('C:\Vídeos Baixados')

    y1 = input('Deseja baixar outro filme ?')
    while y1 == "sim" :
        x1 = input('Insira o link do vídeo:')

        youtube = YouTube(x1)

        ys = youtube.streams.get_highest_resolution().download('C:\Vídeos Baixados')
      
        y = input('Deseja baixar outro filme ?')

    else:
        print('programa finalizado')
        print('By Alücard')
        time.sleep(3)
        exit()

elif X==2:
    

# Credenciais da API do Twitter
    consumer_key = 'sua_consumer_key'
    consumer_secret = 'sua_consumer_secret'
    access_token = 'seu_access_token'
    access_token_secret = 'seu_access_token_secret'

# Autenticação com a API do Twitter
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

# Criar um objeto API
    api = tweepy.API(auth)

# URL do tweet com o vídeo
    z=input('Insira o link do vídeo')
    tweet_url = z

# Obter o ID do tweet
    tweet_id = tweet_url.split('/')[-1]

# Obter informações sobre o tweet
    tweet = api.get_status(tweet_id, tweet_mode='extended')

# Obter a URL do vídeo
    video_url = tweet.extended_entities['media'][0]['video_info']['variants'][0]['url']

# Baixar o vídeo
    response = requests.get(video_url)
    with open('video.mp4', 'wb') as f:
        f.write(response.content)
