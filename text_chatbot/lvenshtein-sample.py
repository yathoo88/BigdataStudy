
#레벤슈타인 거리 계산
def cal_distance(a, b):
    if a==b : return 0
    a_length = len(a)
    b_length = len(b)
    if a == "" : return b_length
    if b == "" : return a_length

    ## 2차원 표
    matrix = [[] for i in range(a_length+1)]
    for i in range(a_length+1):
        matrix[i] = [0 for j in range(b_length+1)]
    # 초기값 설정
    for i in range(a_length+1):
        matrix[i][0] = i
    for j in range(b_length+1):
        matrix[0][j] = j
    for i in range(1, a_length+1):
        ac = a[i-1]
        for j in range(1,b_length+1):
            bc = b[j-1]
            cost = 0 if (ac == bc) else 1

            matrix[i][j] = min([
                matrix[i-1][j] + 1, #문자 삽입
                matrix[i][j-1] + 1, #문자 제거
                matrix[i-1][j-1] + cost #문자 수정
            ])
    return matrix[a_length][b_length]

# print(cal_distance("가나다라","가마바사"))


sample_words = ["신촌역","신천역","신촌","건대역","건대"]
base = sample_words[0]
r = sorted(sample_words, key = lambda n : cal_distance(base, n))
for n in r:
    print(cal_distance(base, n), n)
