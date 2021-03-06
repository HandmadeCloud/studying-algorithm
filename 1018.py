# 1018 체스판 칠하기
# 8 x 8 의 체스판을 잘라서 가장 적게 색을 바꾸는 것이 문제

# 정답
n,m = map(int,input().split())
l = []
ans = []
for i in range(n):
    l.append(input())
    
# 8x8로 자르기 위해서 설정한 경우
for a in range(n-7):
    for b in range(m-7):
        # a와 b 초기화
        cnt_w = 0
        cnt_b = 0
        
        # a와 v만큼
        for i in range(a,a+8):
            for j in range(b,b+8):
              # 둘의 합이 짝수인 경우 (짝+짝, 홀+홀) 한칸씩 띄엄띄엄 있는 형태
                if (i+j) % 2 == 0:
                    # w가 아닌 경우 black이라는 의미, 그러면 w로 바꿔야 하기 때문에 1추가
                    if l[i][j] != 'W':
                        cnt_w += 1
                    
                    if l[i][j] != 'B':
                        cnt_b += 1
                        
              # 둘의 합이 홀수인 경우 (짝+홀,홀+짝)
              # 중심 대각선을 중심으로 띄엄띄엄 있는 형태
                else:
                    # 위에서 w가 아닌경우를 물어봤으니 여기선 b가 아닌 경우를 물어봐야 정산이 된다.
                    # 여기서 if문을 거치면 뒤에 if 문은 건드릴 필요가 없기 때문에....
                    if l[i][j] != 'B':
                        cnt_w += 1
                    if l[i][j] != 'W':
                        cnt_b += 1
        # 완전 탐색 과정을 거치는데,
        ans.append(min(cnt_w,cnt_b))
    
print(min(ans))

# 디테일하게 하나하나를 보는 것이 어렵다면 전체를 비교해보는 것이 좋다. 가로 세로보다 가로에만 집중해서도 보고,
# 아니면 배추 문제처럼 2차원 배열로 생각한는 등의 접근으로 다양한 루트로 고려가 필요하다.
# 완전탐색을 두려워 말고 비교를 위해선 min,max 등의 최소 최대값을 적극적으로 활용하는 방법을 찾아보자
