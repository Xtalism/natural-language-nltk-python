import gensim.downloader as api
wv = api.load("word2vec-google-news-300")

wv.similarity(w1="great", w2="good")