import random

print("오징어 게임에 오신 것을 환영합니다")
print("홀짝 게임을 시작합니다")

# 구슬로 홀짝 게임 규칙

# 참가자가 가진 구슬의 갯수
marble = 10

# 한번은 반복을 했으면 좋겠다
for i in range(20):
    # 구슬의 갯수를 알려주자
    print("당신의 구슬의 갯수: {}".format(marble)) #print("당신의 구슬의 갯수: ",marble)
    try:
        # 구슬의 갯수 베팅
        bet = int(input("구슬 몇 개 베팅? "))
    except:
        print("숫자만 입력해라")
        continue
    
    if marble < bet:
        print("당신이 가진 구슬이 부족하다 다시 베팅하시오")
        continue

    # 내가 홀 또는 짝을 얘기한다
    my = input("홀 or 짝? (잘못쓰면 빵이지만 한번은 기회줄게)")
    print(my)
    # 만약에 홀, 짝이 아니면 잘못입력 메세지
    if my == "홀" or my == "짝":
        # 상대방이 구슬의 갯수를 정한다
        a = random.randint(1,10)
        print(a)
        # 상대방의 구슬의 갯수에서 2로 나누어서 나머지가 0이면 짝
        if a % 2 == 0:
            print("짝")
            dab = "짝"
        # 나머지가 1이면 홀
        else:
            print("홀")
            dab = "홀"
        # 만약에 내가 얘기한 홀과 짝 중에 맞으면 맞다
        if dab == my:
            print("이겼다 구슬 가져와")
            marble = marble + bet #marble += bet
            print("당신의 구슬의 갯수: {}개".format(marble))
        # 틀리면 틀렸다
        else:
            print("졌다 아 뺏겼네")
            marble = marble - bet
            print("당신의 구슬의 갯수: {}개".format(marble))

        # 만약에 구슬의 갯수가 0 이하면 게임오버
        if marble <= 0:
            print("빵 으악 게임오버")
            break
        # 만약에 구슬의 갯수가 20 이상이면 이겼다 다음 스테이지
        if marble >= 20:
            print("이겼다 다음 스테이지")
            break
    else:
        print("잘못 입력 다시 입력해라")