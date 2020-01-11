from azapi import AZlyrics
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt

def create_cloud(artist, song):
    '''
    Takes in the name of an artist and song, and uses azapi to search for the lyrics, and creates a wordcloud. Returns None.
    '''
    api = AZlyrics()
    lyrics = api.getLyrics(artist=artist, title=song, save=False)

    wordcloud = WordCloud().generate(lyrics)

    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()

if __name__ == '__main__':
    while True:
        artist = input('Artist\'s name: ')
        song = input(artist + '\'s song: ')
        try:
            create_cloud(artist, song)
        except Exception:
            print('Unable to find lyrics for ' + song + ' by ' + artist + '. Please try again.')