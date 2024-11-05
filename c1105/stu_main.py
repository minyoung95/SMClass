import oracledb
import stu_func


while True:
    choice = stu_func.main_print()
    
    if choice == '1':
        print('[학생성적 입력]')
        print()
        stu_func.stu_insert()        
        
    elif choice == '2':
        print('[ 학생성적 출력 ]')
        print()
        stu_func.stu_output()
    elif choice == '3':
        print('[ 학생성적 검색 ]')
        print()
        stu_func.stu_search()
    elif choice == '4':
        print('[ 학생성적 정렬 ]')
        print()
        stu_func.stu_order()
    elif choice == '5':
        print('[ 등수 처리 ]')
        print()
        stu_func.stu_rank()
    elif choice == '0':
        print('프로그램을 종료합니다.')
        break