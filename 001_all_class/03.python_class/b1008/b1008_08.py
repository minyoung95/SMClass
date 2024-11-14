import copy
# 얕은 복사
name = ["홍길동", "유관순", "이순신"]
score = [100, 90, 95]

n_dic = dict(zip(name, score))

a = n_dic # 얕은 복사
a = copy.deepcopy(n_dic) # 깊은 복사

a['홍길동'] = 0

print(a)
print(n_dic)

# n = name
# n[2] = "김구"
# print(n) # 이순신 >> 김구

# # 깊은 복사
# name = ["홍길동", "유관순", "이순신"]
# n = name[:] # 깊은 복사 : n의 리스트만 변경
# print(n)