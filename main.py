import random

print("오징어 게임에 오신 것을 환영합니다")
print("홀짝 게임을 시작합니다")

# 구슬로 홀짝 게임 규칙
# 내가 홀 또는 짝을 얘기한다
my = input("홀 or 짝? ")
print(my)
# 상대방이 구슬의 갯수를 정한다
a = random.randint(1,10)
print(a)
# 상대방의 구슬의 갯수에서 2로 나누어서 나머지가 0이면 짝
# 나머지가 1이면 홀
if a % 2 == 0:
    print("짝")
    dab = "짝"
else:
    print("홀")
    dab = "홀"
# 만약에 내가 얘기한 홀과 짝 중에 맞으면 맞다
# 틀리면 틀렸다
if dab == my:
    print("맞다")
else:
    print("빵!")