-- 입사일의 마지막 날짜
select last_day(hire_date) from employees;
-- 가입일의 1년 후
select add_months(sdate,12) from students;
-- 가입일이 6개월 이내의 회원만 출력
select name,sdate from students
where sdate >= add_months(sysdate,-6) order by sdate;

-- 월별 가입인원 출력
select substr(last_day(mdate),4,2) md,count(*) from member
group by last_day(mdate) order by md;

-- 부서별 인원 출력
select department_id,count(*) from employees group by department_id
order by department_id;

create table emp3
as select * from employees; -- 완전 복사

create table emp4
as select * from employees where 1=2; -- 구조만 복사
select * from emp4;
-- 테이블 구조가 있는 상태에서 모든 데이터를 입력
insert into emp4 select * from employees;
rollback;
-- insert, update, delete << commit,rollback

-- 제약조건(null 값 x) : 아이디 이름 입사일 값은 무조건 있어야함
insert into emp4(employee_id,emp_name,salary,hire_date)
select employee_id,emp_name,salary,hire_date from employees;

-- 테이블 : create 생성, alter 변경, drop 삭제 (복구 불가)

-- 컬럼 추가(add(컬럼이름 타입))
select * from emp4;
alter table emp4 add(hire_date2 date);

-- 컬럼 변경(modify(컬럼이름 타입) - 컬럼안에 데이터가 있을경우(ex:길이 65일때 50으로 변경 x)
alter table emp4 modify(email varchar2(70));
alter table emp4 modify(email varchar2(50));
-- 컬럼 형태 변경 (컬럼 안 데이터가 null 값이면 가능)
-- 다른 타입일 경우 데이터를 null값으로 변경 후 타입 변경
select * from emp4;
desc emp4;
alter table emp4 modify(email number(6));

-- email 데이터에 employee_id 값을 복사
update emp4 set email = employee_id;

-- employee_id 값을 phone_number에 복사 (숫자형 타입을 문자형 타입으로 복사)
update emp4 set phone_number = employee_id;
commit;

-- 문자형 > 숫자형 (문자형 데이터가 모두 숫자이기 때문에 가능)
-- but 문자가 포함되어 있으면 안된다.
update emp4 set manager_id = phone_number;
rollback;

update emp4 set phone_number = '198a' where employee_id = 198;

-- 컬럼 이름 변경(alter rename column a to b : a에서 b로 변경)
desc emp4;
alter table emp4 rename column phone_number to p_number;

-- 속성 변경
alter table emp4 modify hire_date date null;
alter table emp4 modify hire_date date not null;

-- 컬럼 삭제 (drop)
alter table emp4 drop column hire_date2;

-- 테이블 삭제
drop table emp2;

-- 테이블 이름 변경 (rename a to b : 테이블명 a를 b로 변경)
rename emp4 to emp44;

--- 무결성 제약조건
select * from departments;
desc departments;

drop table board;

-- primary key : 중복불가, null값 불가
-- unique : 중복불가, null값 허용
-- not null : 중복가능, null값 불가
-- default : 값이 입력되지 않았을때 기본값 지정 
create table bmember(
id varchar2(30) primary key,
pw varchar2(30) not null,
name varchar2(30) not null,
nicname varchar2(30),
age number(3) default 0,
gender varchar2(6) check(gender in('Male','Female')),
email varchar2(20),
bdate date default sysdate
);

desc bmember;

insert into bmember (id,pw,name,nicname,age,gender,email,bdate) values(
'aaa','1111','홍길동','길동스',20,'Male','aaa@aaa.com',sysdate
);
insert into bmember (id,pw,name,nicname,gender,email) values(
'bbb','2222','유관순','관순스','Female','bbb@bbb.com'
);

-- check(Male,Female) : male 넣으면 제약조건(check)에 맞지않음 > 입력불가
insert into bmember (id,pw,name,nicname,age,gender,email,bdate) values(
'ccc','1111','이순신','순신스',20,'male','ccc@ccc.com',sysdate
);

-- not null : null 값은 입력 안됨 (빈 공백은 가능)
insert into bmember (id,pw,name,nicname,age,gender,email,bdate) values(
'ddd',' ','강감찬','감찬스',20,'Male','ddd@ddd.com','2024/01/01'
);

-- primary key(SYS_C007354) : 중복불가, null불가 (aaa가 중복 > 입력불가)
insert into bmember (id,pw,name,nicname,age,gender,email,bdate) values(
'aaa',' ','김구','구스',20,'Male','eee@eee.com','2024/02/21'
);
commit;
select * from bmember;

create table emp3(
empno number(4) unique,
ename varchar2(30) not null,
job varchar2(9),
deptno number(2)
);

insert into emp3 values(
1,'홍','01','01'
);
insert into emp3 values(
2,'유','02','02'
);
-- unique null값은 허용
insert into emp3(ename,job,deptno) values(
'이','03','03'
);
-- unique 중복 불가 (empno : 2 중복)
insert into emp3 values(
2,'강','04','04'
);

select * from emp3;

-- primary key(x) 추가, 수정 
-- primary key 등록시 null값이 존재하면 안됨, 중복도 존재하면 안됨.
-- constraint : 이름 설정(id_pk : 닉네임(오류뜨면 나오는거))
desc member;
alter table member add constraint id_pk primary key(id);

select * from member;

insert into member values(
'fff','1111','홍길자','aaa@aaa.com','123-456-7890','Female','golf',sysdate
);
commit;

-- primary key 삭제
alter table member drop constraint id_pk;
alter table member add constraint id_pk primary key(id); -- 생성

desc bmember;

create table board(
bno number(4) primary key, 
btitle varchar2(100) not null,
bcontent clob,
id varchar2(30),
bgroup number(4),
bstep number(4),
bindent number(4),
bhit number(4),
bdate date,
bfile varchar2(100)
);

insert into board values(
board_seq.nextval,'제목1','내용1','aaa',board_seq.currval,0,0,0,sysdate,''
);
insert into board values(
board_seq.nextval,'제목2','내용2','bbb',board_seq.currval,0,0,0,sysdate,''
);
insert into board values(
board_seq.nextval,'제목5','내용5','aaa',board_seq.currval,0,0,0,sysdate,''
);
select * from board;
select * from bmember;

-- 조인(join)
select bno,btitle,bcontent,nicname,age,gender,pw,email,bgroup,bstep,bindent,bhit,bfile
from board,bmember -- 5개 테이블 2개 > 25개
where board.id = bmember.id; -- id가 같은부분만 board.id : foreign key, bmember.id : primary key

select employee_id,emp_name,email,salary,employees.department_id,department_name
from employees,departments
where employees.department_id = departments.department_id;
select department_id,department_name from  departments
where department_id=10;

-----------------------------------------------

select * from mem2;
commit;

insert into member select * from mem2;
select * from member;

