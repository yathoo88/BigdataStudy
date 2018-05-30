# import urllib.request as req
# import gzip, os, os.path
# 
# savepath = "./mnist"
# baseurl = "http://yann.lecun.com/exdb/mnist"
# files = [
#     "train-images-idx3-ubyte.gz",
#     "train-labels-idx1-ubyte.gz",
#     "t10k-images-idx3-ubyte.gz",
#     "t10k-labels-idx1-ubyte.gz"
# ]
# 
# #download
# if not os.path.exists(savepath) :
#     os.mkdir(savepath)
# for f in files :
#     url = baseurl + "/" + f
#     loc = savepath + "/" + f
#     print("download : ", url)
#     if not os.path.exists(loc) :
#         req.urlretrieve(url, loc)
# 
# # gzip 압축 풀기
# for f in files:
#     gz_file = savepath + "/" + f
#     raw_file = savepath + "/" + f.replace(".gz", "")
#     print("gzip : ",f)
#     with gzip.open(gz_file, "rb") as fp :
#         body = fp.read()
#         with open(raw_file, "wb") as w:
#             w.write(body)
# print("complete!!")




# #  바이너리 파일을 csv로 변환
# import struct
# def to_csv(name, maxdata):
#     # 레이블 파일과 이미지 파일 열기
#     lbl_f = open("./mnist/"+name+"-labels-idx1-ubyte", "rb")
#     img_f = open("./mnist/"+name+"-images-idx3-ubyte", "rb")
#     csv_f = open("./mnist/"+name+".csv", "w", encoding="utf-8")
#     # 헤더 정보 읽기 --- (※1)
#     mag, lbl_count = struct.unpack(">II", lbl_f.read(8))
#     mag, img_count = struct.unpack(">II", img_f.read(8))
#     rows, cols = struct.unpack(">II", img_f.read(8))
#     pixels = rows * cols
#     # 이미지 데이터를 읽고 CSV로 저장하기 --- (※2)
#     res = []
#     for idx in range(lbl_count):
#         if idx > maxdata: break
#         label = struct.unpack("B", lbl_f.read(1))[0]
#         bdata = img_f.read(pixels)
#         sdata = list(map(lambda n: str(n), bdata))
#         csv_f.write(str(label)+",")
#         csv_f.write(",".join(sdata)+"\r\n")
#         # 잘 저장됐는지 이미지 파일로 저장해서 테스트하기 -- (※3)
#         if idx < 10:
#             s = "P2 28 28 255\n"
#             s += " ".join(sdata)
#             iname = "./mnist/{0}-{1}-{2}.pgm".format(name,idx,label)
#             with open(iname, "w", encoding="utf-8") as f:
#                 f.write(s)
#     csv_f.close()
#     lbl_f.close()
#     img_f.close()
# # 결과를 파일로 출력하기 --- (※4)
# to_csv("train", 1000)
# to_csv("t10k", 500)




from sklearn import model_selection, svm, metrics
import pandas

train_csv = pandas.read_csv("./mnist/train.csv", header=None)
tk_csv = pandas.read_csv("./mnist/t10k.csv", header=None)


def test(l):
    output = []
    for i in l:
        output.append(float(i)/256)
    return output

train_csv_data = list(map(test, train_csv.iloc[:, 1:].values))
train_csv_label = list(map(test, train_csv.iloc[:, 1:].values))
tk_csv_data = tk_csv.iloc[:, 1:]
tk_csv_label = tk_csv[0].values

clf = svm.SVC()
clf.fit(train_csv_data, train_csv_label)
predict = clf.predict(tk_csv_data)

score = metrics.accuracy_score(tk_csv_label, predict)
print("정답률 : ", score)