from sklearn import svm
from sklearn.externals import joblib
import json



######데이터 학습

file_path = "./lang/freq.json"
# json 데이터 읽어오기
with open(file_path, "r", encoding="utf-8") as f:
    d = json.load(f)
    data = d[0] #0번째가 학습데이터

clf = svm.SVC()
clf.fit(data["freqs"], data["labels"])

joblib.dump(clf, "./lang/freq.pkl")
print("pkl save!")
