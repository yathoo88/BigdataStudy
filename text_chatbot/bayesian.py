import math, sys
from konlpy.tag import Twitter

class BayesianFilter:
    def __init__(self):
        self.words = set()  #모든 단어
        self.word_dict = {} # 카테고리별 출현 횟수
        self.category_dict = {} #카테고리 출현 횟수

    def split(self, text):
        results = []
        twitter = Twitter()
        malist = twitter.pos(text, norm=True, stem=True)
        for word in malist:
            if not word[1] in  ['Josa','Eomi','Punctuation']:
                results.append(word[0])
        return results

    def inc_word(self, word, category): #단어와 카테고리 횟수 count
        if not category in self.word_dict:
            self.word_dict[category] = {}
        if not word in self.word_dict[category]:
            self.word_dict[category][word] = 0
        self.word_dict[category][word] += 1
        self.words.add(word)

    def inc_category(self, category):
        if not category in self.category_dict:
            self.category_dict[category] = 0
        self.category_dict[category] += 1


    def category_prob(self, category): #카테고리 계산
        sum_categories = sum(self.category_dict.values())
        category_v = self.category_dict[category]
        return category_v/sum_categories

    def get_word_count(self, word, category):   #카테고리 내 단어 출현 횟수
        if word in self.word_dict[category]:
            return self.word_dict[category][word]
        else :
            return 0

    def word_prob(self, word, category):    #카테고리 내 단어 출현 비율
        n = self.get_word_count(word, category) +1
        d = sum(self.word_dict[category].values()) + len(self.words)
        return n/d


    def fit(self, text, category):  #학습
        word_list = self.split(text)
        for word in word_list:
            self.inc_word(word, category)
        self.inc_category(category)

    def score(self, words, category):
        score = math.log(self.category_prob(category))
        for word in words:
            score += math.log(self.word_prob(word, category))
        return score

    def predict(self, text):
        best_category = None
        max_score = -sys.maxsize
        words = self.split(text)
        score_list = []
        for category in self.category_dict.keys():
            score = self.score(words, category)
            score_list.append((category, score))
            if score > max_score:
                max_score = score
                best_category = category
        return best_category, score_list

