import os

### os.path.exists : 현재 폴더가 있는지 확인하는 메소드
### mkdir : 지정하는 폴더만 생성 os.mkdir('D:/bbb) - bbb폴더 생성
### makedirs : 하위폴더까지 생성
if not os.path.exists('D:/ccc/bbb'):
  os.makedirs('D:/ccc/bbb') # ccc폴더와 하위폴더 bbb까지 만듦
  print("폴더가 없습니다.")
else:
  print("폴더가 있습니다.")


f = open('D:/ccc/bbb/c.txt','w',encoding='utf-8')
f.write("안녕하세요")
f.close