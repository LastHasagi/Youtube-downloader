import tweepy
import requests

# Credenciais da API do Twitter
consumer_key = 'mKwGayDodBpjuwXTb3HzQPNm6'
consumer_secret = '45fwpFgCXMnAnGqsqszmcN5nGeBUPrypi0HTCs8eow7huU0TwG'
access_token = '1643754204391956485-iG8oFMgCZhKW2VjVxZ7j2zV4wbXiJs'
access_token_secret = 'Q7WJSjD6Qq8hZGZJYlMDmH3rt5CTi8GoBWb0LTvUzLhTF'

# Autenticação com a API do Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Criar um objeto API
api = tweepy.API(auth)

# URL do tweet com o vídeo
z=input('Insira o link do vídeo:')
tweet_url = z

# Obter o ID do tweet
tweet_id = tweet_url.split('/')[-1]

# Obter informações sobre o tweet
tweet = api.get_status(tweet_id, tweet_mode='extended')

# Obter a URL do vídeo
video_url = tweet.extended_entities['media'][0]['video_info']['variants'][0]['url']

# Baixar o vídeo
response = requests.get(video_url)
with open('C:\Vídeos Baixados') as f:
    f.write(response.content)