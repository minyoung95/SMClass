### 파일 입출력
# 가장 바깥 폴더의 위치에서 파일을 찾는다.
# f = open('a.txt','r',encoding='UTF-8') # r : 파일읽기, encoding : 한글지원

# 절대경로
# f = open('a.txt','r',encoding='UTF-8') # encoding : 한글지원
# while True:
#     line = f.readline() # 한줄씩 읽기
#     if not line: break
#     print(line.strip()) # strip : \n 값을 생략해줌
# f.close()

## readlines() : 모든글 읽기 (리스트 타입)
# f = open('a.txt','r',encoding='utf-8')
# lines = f.readlines()
# for line in lines:
#   print(line.strip())

# f.close()

## read()
# f = open('a.txt','r',encoding='utf-8')
# for line in f:
#   print(line.strip())

# f.close()

## w : 파일쓰기 (파일 생성 후 글자입력)
# f = open('aa.txt','w',encoding='utf-8')
# f.write("안녕하세요.\n")
# f.write("안녕하세요2.\n")
# f.write("안녕하세요3.\n")
# f.close()
# print("글쓰기 종료")

# f = open('aa.txt','w',encoding='utf-8')
# for i in range(1, 11):
#   data = f"안녕하세요. {i} \n"
#   f.write(data)

# f.close()
# print("글쓰기 종료")

## a : 이어서 쓰기
# print("[ 메모장 ]")
# while True:
#   data = input("저장하려는 글자를 입력하세요. >>")

#   f = open('aa.txt','a',encoding='utf-8')
#   f.write(data+"\n")

#   f.close()

## 파일 with : close()를 하지 않아도 됨

with open('aa.txt','w',encoding='utf-8') as f:
  f.write("안녕하세요.")