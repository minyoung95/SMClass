-- dual : 임시로 넣는 가상테이블
select sysdate from dual;

select sysdate from dual;

select hire_date-1,hire_date,hire_date+1 from employees;

-- 날짜 범위검색 가능, 정렬 order by (asc) - 순차, order by dsc - 역순
select emp_name,hire_date from employees 
where hire_date >= '02/01/01' and hire_date <= '041231'
order by hire_date;

-- like
select emp_name from employees
where emp_name like '___a%';

select emp_name from employees
where emp_name like '%a_';

-- 정렬 : desc - null값이 제일 위, asc - null값이 제일 아래
select department_id from employees
order by department_id desc;

-- salary 역순정렬
select emp_name,salary from employees
order by salary desc;

-- students테이블에서 total 역순정렬
select no,name,total from students
order by total desc;

-- hire_date 기준, 순차정렬
select emp_name,hire_date from employees
order by hire_date;

select name,kor,eng,math from students
order by kor desc, eng desc; -- kor값을 기준으로 정렬 후 같은 값일때 eng 정렬

select name from students
order by name;

-- 입사일이 빠른 순으로 정렬, 이름은 역순
select emp_name,hire_date from employees
order by hire_date, emp_name desc;

-- abs : 절대값 // as : 컬럼명 변경
select -10, abs(-10) as 절대값 from dual;
select kor, kor-eng,abs(kor-eng) abs from students
order by abs desc;

-- floor : 소숫점 이하 버림
select 3.141592,floor(3.141592) from dual; 
-- trunc : 버림, 자리수 지정 가능
select 34.5678,trunc(34.5678,2) from dual;
select 34.5678, trunc(34.5678,-1) from dual;
-- ceil : 소숫점 이하 올림
select 34.5678, ceil(34.5678) from dual;
--round 반올림 , 자리수 범위지정 가능
select 34.5678, round(34.5678) from dual;

-- 소숫점 둘째자리까지 (셋째자리에서 반올림)
select 34.5678, round(34.5678,2) from dual;
-- mod : 나머지
select 27/2, mod(27,2) from dual;
select 30/3, mod(31,7) from dual;

-- 사원번호가 홀수 번호인 사원 출력
select employee_id,emp_name from employees
where mod(employee_id,2)=1
order by employee_id;

-- 최종연봉 : 월급*12 +(월급*12)*커미션, 소수점 2자리에서 반올림 // nvl(x,0) : null 값을 0으로 표시
select emp_name,round((salary*12 + (salary*12)*nvl(commission_pct,0))*1381.86795,1) as 연봉
from employees;

-- 시퀀스 : 자동으로 번호부여(중복 x)
create sequence stu_seq -- 시퀀스 이름
start with 1 -- 시작번호
increment by 1 -- 증가량
minvalue 1 -- 최솟값
maxvalue 9999 -- 최댓값
nocycle -- 1~9999 이상이되면 다시 1로 돌아감 (nocycle은 안돌아가고 에러남)
nocache; -- 메모리에 시퀀스값을 미리 할당하여 진행할것인가?


-- 다음 시퀀스 번호생성
select stu_seq.nextval from dual;

-- 시퀀스 현재번호확인
select stu_seq.currval from dual;

-- 게시판 테이블 생성
create table board(
bno number(4),
btitle varchar2(100),
bcontent varchar2(4000),
id varchar2(30),
bhit number(10),
bdate date
);

insert into board values(
1,'제목입니다','내용입니다.','aaa',1,sysdate
);

insert into board values(
2,'제목입니다','내용입니다.','aaa',2,sysdate
);

insert into board values(
stu_seq.nextval,'제목입니다','내용입니다.','aaa',2,sysdate
);

select * from board;
commit;

create sequence board_seq
start with 14
increment by 1
minvalue 1
maxvalue 9999
nocycle
nocache
;

desc board; -- 컬럼갯수 확인

insert into board values(
board_seq.nextval,'제목14','내용14','aaa',2,sysdate
);

select * from board;

update board set btitle='제목을 다시변경' where bno=14;
commit;

create table board(
bno number(4),
btitle varchar2(100),
bcontent clob, -- clob : varchar2 최댓값 (대용량 글자타입)
id varchar2(20),
bgroup number(4), -- 답변달기 그룹핑
bstep number(4), -- 답변달기 경우 순서정의
bindent number(4), -- 답변달기 들여쓰기
bhit number(10), -- 조회수
bdate date -- 등록일
);

select board_seq.currval from dual;

insert into board values(
1,'제목1','내용1','aaa',1,0,0,1,sysdate
);

-- 시퀀스 생성 sutdents_seq.nextval
-- students 테이블 100 > 101
-- 101,홍길순,100,99,90,total,avg,rank,날짜

select * from students;
insert into students values(
students_seq.nextval,'홍길순',100,99,90,100+99+90,(100+99+90)/3,0,sysdate
);
commit;

select round(avg,2) from students;
select s.*,round(avg,2) from students s; -- s : 별칭 // s의 모든것과 avg 찍어주기

select dept_seq.nextval from dual;

-- s_seq 시작 1 증분 1 최댓값 99999
create sequence s_seq
start with 1
increment by 1
minvalue 1
maxvalue 99999
nocycle
nocache
;

select s_seq.nextval from dual;

-- 타입 : 문자형,숫자형,날짜형
-- 문자형 : char,varchar2,nchar,nvarchar2,(long,clob) 대용량
-- char,varchar2 : 한글문자 입력 시 3byte 사용 (varchar2(6) : 한글 2글자 입력)
-- nvarchar2(5) : 한글 5글자까지 입력가능 ,2byte 사용
-- 숫자형 : number
-- 날짜형 : date(초 단위까지),timestamp(밀리세컨드(1/1000초)까지)

select '홍길동' from dual;
select length('홍길동') from dual; -- 문자길이 : 3
select lengthb('홍길동') from dual; -- byte크기 : 9

-- 이름길이로 역순정렬
select name, length(name) n from students
order by n desc;
-- 합계 200점 이상, 번호 10에서 50, 이름 2번째자가 e가 포함되어있는 학생 출력
select * from students where total>=200 and no>=10 and no<=50 and name like '_e%';

-- 2중
select * from(
select * from students where total>=200
)where name like '_e%' and no >=30;

rollback;

select * from students;
select no,name,total,rank from students;
-- rank함수 : rank()over(기준점)//no 중복x(유일키,기본키,프라이머리 키(primary key))
select no,rank()over(order by total desc) ranks from students; -- 컬럼 2개
select ranks from (select no,rank()over(order by total desc) ranks from students);

select no,name,total,rank from students
order by total desc;

-- update 수정
update students a -- a의 번호(no)는 1,2,3,4,...
-- b의 번호는 101,96,64,...
set rank=(
select ranks from(select no,rank()over(order by total desc) ranks from students) b
where a.no=b.no -- 넘버 값을 찾아야함
);
select * from students order by rank;

rollback;

select no,rank()over(order by total desc) as ranks from students;

select * from students order by total desc;
update students
set rank = 1
where no = 101;

update students
set rank = 2
where no = 96;

update students
set rank = 3
where no = 64;

update students
set rank = 4
where no = 49;

update students
set rank = 5
where no = 14;

-- 사원번호가 높은순으로 등수를 생성하고 사원번호,사원명,등수
select employee_id,rank()over(order by employee_id desc)ranks from employees;

-- 테이블 생성 후 복사
create table emp2 as select * from employees;

select rank()over(order by employee_id desc)from employees;

alter table emp2 add rank number(4); -- rank 컬럼 추가

update emp2 e set rank = ( -- rank() 등수를 rank 컬럼에 추가
select ranks from (select employee_id,rank()over(order by employee_id desc) ranks from employees) e2
where e.employee_id = e2.employee_id
);

select employee_id,rank from emp2
order by employee_id desc;

select * from emp2;
-- 컬럼의 순서 변경 (emp_name 뒤에 rank컬럼 배치) - 사이 컬럼들 숨김처리(modify invisible)
alter table emp2 modify EMAIL invisible;
alter table emp2 modify phone_number invisible;
alter table emp2 modify hire_date invisible;
alter table emp2 modify salary invisible;
alter table emp2 modify MANAGER_ID invisible;
alter table emp2 modify COMMISSION_PCT invisible;
alter table emp2 modify RETIRE_DATE invisible;
alter table emp2 modify DEPARTMENT_ID invisible;
alter table emp2 modify job_id invisible;
alter table emp2 modify CREATE_DATE invisible;
alter table emp2 modify UPDATE_DATE  invisible;

-- 사이 컬럼을 나타내기 (modify visible)
alter table emp2 modify EMAIL visible;
alter table emp2 modify phone_number visible;
alter table emp2 modify hire_date visible;
alter table emp2 modify salary visible;
alter table emp2 modify MANAGER_ID visible;
alter table emp2 modify COMMISSION_PCT visible;
alter table emp2 modify RETIRE_DATE visible;
alter table emp2 modify DEPARTMENT_ID visible;
alter table emp2 modify job_id visible;
alter table emp2 modify CREATE_DATE visible;
alter table emp2 modify UPDATE_DATE  visible;

select * from emp2;

desc emp2;
alter table emp2 drop column email;
alter table emp2 drop column phone_number;
alter table emp2 drop column HIRE_DATE;
alter table emp2 drop column SALARY;
alter table emp2 drop column COMMISSION_PCT;
alter table emp2 drop column RETIRE_DATE;
alter table emp2 drop column CREATE_DATE;
alter table emp2 drop column UPDATE_DATE;

alter table emp2 add department_name varchar2(80);

select * from emp2;
select * from departments;

select department_id,department_name from emp2;
select department_id,department_name from departments;

update emp2
set department_name = '배송부'
where department_id = 50
;

update emp2 e set e.department_name = ( -- emp2의 department_name을 수정
select department_name from(select department_id,department_name from departments) e2
where e.department_id = e2.department_id
);

select department_id,department_name from emp2;

-- 테이블 복사
create table stu as select * from students;

desc stu;
-- 컬럼 삭제
alter table stu drop column rank;
select * from stu;
-- 컬럼 추가
alter table stu add rank number(5);
-- 숨김 처리, 나타내기
alter table stu modify sdate visible;

update stu s set s.total = (
select total from(select name,total from students)s2
where s.name = s2.name
);

update stu set avg = (kor+eng+math)/3;

select * from stu;

update stu s set s.rank = (
select ranks from(select name,rank()over(order by total desc)ranks from stu)s2
where s.name=s2.name
);

select * from stu order by rank;
commit;

-- 날짜 함수
-- sysdate : 현재 날짜
select sysdate from dual;

create table datetable(
no number(4),
predate date,
today date,
nextdate date
);
-- 회원가입 1달,6달,1년치
insert into datetable values(
1,sysdate-30,sysdate,sysdate+180
);

select no,predate,today 가입일,nextdate 만료일 from datetable;

select * from member;

select id,name,mdate,round(sysdate-mdate) from member
where sysdate >= mdate+180;

-- 입사일 현재날짜와 입사일 몇일 지났는지
select emp_name,hire_date,round(sysdate-hire_date) from employees;
-- 날짜 round : 15일 전 내림, 15일 후 올림
select hire_date, round(hire_date,'month') from employees;
-- trunc : 일자를 1로 초기화
select hire_date,trunc(hire_date,'month') from employees;
-- 입사일~현재일 기준 달 수(몇 달이 지났나)
select hire_date,sysdate,round(months_between(sysdate,hire_date)) from employees;
-- add_months : 개월 수 더하기
select hire_date,add_months(hire_date,3) from employees;
-- next_day(sysdate, 'x요일') : 다음 x요일 날짜를 알려줌
select sysdate,next_day(sysdate,'수요일') from dual;
-- last_date : 그 달의 마지막 날짜를 알려줌
select hire_date,last_day(hire_date) from employees;

-- 타입 변경(형 변환함수) : TO_CHAR, TO_DATE, TO_NUMBER

select sysdate from dual;
select to_char(sysdate,'yy-mm-dd hh24:mi:ss') from dual; -- hh24 : 24시간으로 표현

select to_char(hire_date,'yyyy-mm-dd') from employees;

select to_char(to_date('24/01/01'),'yyyy-mm-dd') from dual;

select * from member where id='aaa' and pw='1111';

update member set id='abc',pw='1111',name='임민영',email='mylim52@naver.com',
gender='Male' where id='Trineman';

select * from member;

commit;

select * from member;