from sklearn import svm, metrics

# 데이터 학습
clf = svm.SVC()
# clf.fit(데이터, 답)
# clf.fit([
#     [0,0],
#     [0,1],
#     [1,0],
#     [1,1]
# ], [
#     0,
#     1,
#     1,
#     0
# ])
datas = [[0,0], [0,1], [1,0], [1,1]]
labels = [0, 1, 1, 0]
clf.fit(datas, labels)


examples = [[0,0], [0,1]]
examples_label = [0, 1]



#데이터 예측
results = clf.predict(examples)
print(results)


score = metrics.accuracy_score(examples_label,results)
print("정답률 : ", score)