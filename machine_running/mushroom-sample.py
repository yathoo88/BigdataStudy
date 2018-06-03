#랜덤 포레스트

# mushroom data download
# import urllib.request as req
#
# local = "mushroom.csv"
#
# url = "https://archive.ics.uci.edu/ml/machine-learning-databases/mushroom/agaricus-lepiota.data"
#
# req.urlretrieve(url, local)
# print("download!")




# # 랜덤 포레스트로 버섯 분류 -> 연속변수라고 가정하고 단순하게 출력
# import pandas as pd
# from sklearn.ensemble import RandomForestClassifier
# from sklearn import metrics
# from sklearn.model_selection import train_test_split
#
# mushrooms = pd.read_csv("mushroom.csv", header=None)
#
# labels = []
# datas = []
# # attr_list = []
# for index, row in mushrooms.iterrows():
#     labels.append(row.ix[0])
#     row_data = []
#     for v in row.ix[1:] :
#         row_data.append(ord(v)) #숫자로 바꿔줘야해!!
#     datas.append(row_data)
#
# # 학습데이터, 테스트 데이터 나누기
# data_train, data_test, label_train, label_test =  train_test_split(datas, labels)
#
#
# # 랜덤포레스트로 data train
# clf = RandomForestClassifier()
# clf.fit(data_train, label_train)
#
# predict = clf.predict(data_test)
#
# score = metrics.accuracy_score(label_test, predict)
# print(score)
#
# report = metrics.classification_report(label_test,predict)
# print(report)



# 데이터를 더 정밀하게 나눠서 적용(상관관계 여부를 확인해서 벡터화 시킨다.)
# -> 분류변수
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.model_selection import train_test_split

mushrooms = pd.read_csv("mushroom.csv", header=None)

labels = []
datas = []
attr_list= []
for index, row in mushrooms.iterrows():
    labels.append(row.ix[0])
    exdata = []
    for col, v in enumerate(row.ix[1:]):
        if index == 0 :
            attr = {"dic":{}, "cnt":0}
            attr_list.append(attr)
        else :
            attr = attr_list[col]

        # 숫자로 변환(벡터화
        d = [0,0,0,0,0,0,0,0,0,0,0,0] # 특징이 가장 많은 분류가 12개 이므로
        if v in attr["dic"]:
            idx = attr["dic"][v]
        else:
            idx = attr["cnt"]
            attr["dic"][v] = idx
            attr["cnt"] += 1
        d[idx] = 1
        exdata +=d
    datas.append(exdata)

# 학습데이터, 테스트 데이터 나누기
data_train, data_test, label_train, label_test =  train_test_split(datas, labels)


# 랜덤포레스트로 data train
clf = RandomForestClassifier()
clf.fit(data_train, label_train)

predict = clf.predict(data_test)

score = metrics.accuracy_score(label_test, predict)
print(score)

report = metrics.classification_report(label_test,predict)
print(report)