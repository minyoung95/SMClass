a = ['1만','3,450','1.7만','500','1,000']

## float 타입으로 변경

def chg(val):
  r_val = 0
  if '만' in val:
    r_val = float(val[:-1])*10000
  else:
    r_val = float(val.replace(',',''))
  return r_val

a_list = list(map(chg,a)) # af를 하나하나 함수(chg)에 넣어서(map) 리스트로 만들기
print(a_list)

a_list.sort()
print(a_list)
a_list.sort(reverse=True)
print(a_list)