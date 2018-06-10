import codecs
from bs4 import BeautifulSoup
from konlpy.tag import Twitter
from gensim.models import word2vec

f = codecs.open("BEXX0003.txt", "r", encoding="utf-16")
soup = BeautifulSoup(f, "html.parser")
body = soup.select_one("body > text")
text = body.getText()

# twitter = Twitter()
# word_dic = {}
# lines = text.split("\n")
#
# for line in lines:
#     malist = twitter.pos(line)
#     for word in malist :
#         if word[1] == "Noun" :
#             if not (word[0] in word_dic):
#                 word_dic[word[0]] = 0
#             word_dic[word[0]] += 1
#
# keys = sorted(word_dic.items(), key=lambda x:x[1], reverse=True)
# for word, count in keys[:50] :
#     print(word,":",count,",")
#




twitter = Twitter()
results = []
lines = text.split("\n")

for line in lines:
    malist = twitter.pos(line, norm=True, stem=True)
    r = []
    for word in malist:
        if not word[1] in ['Josa','Eomi', 'Punctuation']:
            r.append(word[0])
    rl = (" ".join(r)).strip()
    results.append(rl)
    print(rl)

toji_file = "toji.wakati"
with open(toji_file, 'w', encoding='utf-8') as f:
    f.write('\n'.join(results))

##word2vec model!
data = word2vec.LineSentence(toji_file)
model = word2vec.Word2Vec(data, size=200, window=10, hs=1, min_count=2, sg=1)
model.save("toji.model")
print("saved!")