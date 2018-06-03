from sklearn import svm, metrics
import glob, os.path, re, json
import matplotlib.pyplot as plt
import pandas as pd


######데이터 학습

# glob을 이용해 file들을 가져온다.
files = glob.glob("./lang/train/*.txt")
print("glob ::: ", files)

train_data = []
train_label = []
for file_name in files:
    basename = os.path.basename(file_name)
    # print("basename" , basename)    #basename : file 경로를 제외하고 file명을 추출한다.
    lang = basename.split('-')[0]   # lang만 잘라낸다.
    with open(file_name, "r", encoding="utf-8") as f:
        text = f.read()
        text = text.lower()

    # 알파벳 출현 빈도
    code_a = ord("a")
    code_z = ord("z")
    count = [0 for n in range(0, 26)]
    for char in text:
        code_current = ord(char)
        if code_a <= code_current <= code_z :
            #'a'97 - 'a'97 = 0
            #'b'98 - 'a'97 = 1 ... 으로 알파벳 순서대로 count를 구해준다.
            count[code_current - code_a] += 1
    print(lang, " ", count)

    #정규화
    total = sum(count)
    count = list(map(lambda n : n/total, count))

    train_data.append(count)
    train_label.append(lang)



# print(train_label)
# print(train_data)



# files = glob.glob("./lang/test/*.txt")
# test_data = []
# test_label = []
# for file_name in files:
#     basename = os.path.basename(file_name)
#     # print("basename" , basename)    #basename : file 경로를 제외하고 file명을 추출한다.
#     lang = basename.split('-')[0]   # lang만 잘라낸다.
#     with open(file_name, "r", encoding="utf-8") as f:
#         text = f.read()
#         text = text.lower()
#
#     # 알파벳 출현 빈도
#     code_a = ord("a")
#     code_z = ord("z")
#     count = [0 for n in range(0, 26)]
#     for char in text:
#         code_current = ord(char)
#         if code_a <= code_current <= code_z :
#             #'a'97 - 'a'97 = 0
#             #'b'98 - 'a'97 = 1 ... 으로 알파벳 순서대로 count를 구해준다.
#             count[code_current - code_a] += 1
#     print(lang, " ", count)
#
#     #정규화
#     total = sum(count)
#     count = list(map(lambda n : n/total, count))
#
#     test_data.append(count)
#     test_label.append(lang)
#
# #학습
# clf = svm.SVC()
# clf.fit(train_data, train_label)
# predict = clf.predict(test_data)
# score = metrics.accuracy_score(test_label, predict)
# print("score ", score)
# report = metrics.classification_report(test_label, predict)
# print("report-----")
# print(report)



######그래프 그리기

#그래프 그릴 dataFrame 생성
graph_dict = {}
for i in range(0, len(train_label)):
    label = train_label[i]
    data = train_data[i]
    if not (label in graph_dict) :
        graph_dict[label] = data

asclist = [[chr(n) for n in range(97, 97+26)]]
print(asclist)
df = pd.DataFrame(graph_dict, index=asclist)


#그래프 그리기
plt.style.use('ggplot')
df.plot(kind="bar", subplots=True, ylim=(0,0.15))
plt.savefig("lang-plot.png")