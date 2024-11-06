import random
## 임시비밀번호 생성 함수

a = random.randrange(0, 10000) # 0~9999
ran_num = f'{a:04}'
print('랜덤번호 : ',ran_num)
