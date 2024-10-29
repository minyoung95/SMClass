--drop table member;
--drop table date_tab;
--drop table no_tab;
--drop table students;

-- create 테이블 생성, alter 테이블 수정, drop 테이블 삭제
-- number, char, varchar2, date
create table member(
no number(4),
id varchar2(20),
pw varchar2(20),
name varchar2(20),
phone varchar2(20),
mdate date
);

-- insert into values데이터 입력 (임시 저장소)
insert into member values(
1,'aaa','1111','홍길동','010-1111-1111','2024-10-29'
);
insert into member values(
2,'bbb','2222','유관순','010-2222-2222','2024-09-29'
);

-- select from 데이터 검색(* : 모든 컬럼 검색)
select * from member;

-- 확정 commit, 뒤로가기 rollback
commit; -- 1번에서 하면
rollback; -- 2번 입력 후 롤백 > 2번삭제 1번만 남음

-- delete (where 조건절) 데이터 삭제
delete member where no=2;

-- update set 데이터 수정
update member set name='홍길자' where no=1;

update member set name='김구';

create table students (
stuno number(4),
name varchar2(20),
kor number(3),
eng number(3),
math number(3),
total number(3),
sdate date
);

insert into students values(
1,'홍길동',100,100,100,100+100+100,sysdate -- sysdate 현재시간
);

commit;

select * from students;

-- 컬럼을 입력하면 그 컬럼만 검색
select name,sdate from students;

-- 특정 컬럼만 입력하기
insert into students (stuno,name) values(
2,'유관순'
);

select * from employees;

-- 테이블 생성하면서 내용 복사
create table emp2 as select * from employees;
select count(*) from emp2; -- 데이터 갯수

-- 테이블 생성하면서 구조 복사
create table emp3 as select * from employees where 1=2;
select * from emp3;


create table member2 as select * from member where 1=2; -- 구조만
-- 테이블이 존재 할 경우 데이터만 복사
insert into member2 select * from member;
select * from member2;
commit;

-- alter : 컬럼데이터 타입(유형), 길이 변경, 이름 변경

-- number(4) > number(10) : 같은 타입 길이변경
alter table member modify no number(10);
desc member;

-- 다른 타입으로 변경할 때 데이터 값이 바꿀 타입과 같거나 없어야함
alter table member modify no varchar2(10);
update member set no='';
select * from member;
commit;

-- 컬럼의 이름 변경
alter table member rename column no to memberNo;
desc member;


-- 테이블 구조
desc employees;

-- employees 테이블에서 사원번호, 사원이름, 입사일
select employee_id,emp_name,hire_date from employees;

-- 연산자 : 산술연산자, +,-,*,/

create table member (
	id VARCHAR2(50),
	pw varchar2(4),
	name VARCHAR2(50),
	email VARCHAR2(50),
	phone VARCHAR2(50),
	gender VARCHAR2(50),
	hobby varchar2(50),
	mdate DATE
);
select * from member;

create table students (
	no number(4),
	name VARCHAR2(50),
	kor number(3),
	eng number(3),
	math number(3),
	total number(3),
	avg number,
	rank number(3),
	sdate DATE
);

select * from students;
commit;

select kor,eng,(kor+eng) from students;
select kor,eng,(kor+eng),abs(kor-eng) from students; -- abs : 절댓값

select * from employees;
-- concat 
select concat(emp_name,email) from employees;
select emp_name||email from employees;

-- 달러환산
select salary*1384 from employees;

-- 문자로 변환, 천단위 표시
select to_char(salary*1384,'999,999,999') from employees;

create table stu(
no number(4),
name varchar2(20),
kor number(3)
);

insert into stu values(1,'홍길동',100);
insert into stu values(2,'유관순',99);

commit;

insert into stu values(3,'',0);
insert into stu values(4,null,null);

select * from stu;

-- null 값 검색 : is null
select * from stu where name is null;

select * from employees;
-- null 값 아닌것 출력 : is not null
select commission_pct from employees where commission_pct is not null;

select salary from employees;
select salary,salary*12 from employees;
select salary,salary*12,salary*1384*12 from employees;

-- 커미션이 없는 사원(null값이라 +,-,*,/ 안됨)
select salary,salary*12 as "연 봉",salary*12+(salary*12)*commission_pct*0.01 from employees;
-- as : 컬럼 별 명칭 사용(띄어쓰기,특수문자 쓸땐 "")
select salary,salary*12,salary*12+(salary*12)*nvl(commission_pct,0)*0.01 as real_yearSalary from employees;

-- uvl(n,0) 함수 : n 컬럼에 null값이 있으면 0으로 표시
select * from stu;
select no,name,kor,kor+100 from stu;
select no,name,kor,nvl(kor,0)+100 from stu;

-- kor 국어,영어,수학,합계,평균,등수,입력일 걸럼명 별칭 사용하여 출력
select * from students;

select no as 번호,name as 이름,kor as 국어,eng as 영어,math as 수학,total as 합계,avg as 평균,sdate as 입력일 
from students;

-- 사원번호,이름,이메일을 합쳐서 출력하기
select * from employees;
select concat(concat(employee_id,emp_name),email) from employees; -- concat 두개씩
select employee_id||emp_name||email from employees; -- 2개이상 ||
select emp_name||' is a '||job_id from employees; -- 사이에 글자 넣기

-- distinct : 중복 제거
select department_id from employees;
select distinct department_id from employees;
-- order by - asc(생략가능): 순차정렬, order by - desc : 역순정렬
select distinct department_id from employees order by department_id asc;
select distinct department_id from employees order by department_id desc;

-- job_id의 중복을 제거하여 출력
select distinct job_id from employees;

-- 문자열자르기 substr(0,2) 0,1 ,2 앞까지 출력
select substr(job_id,0,2) from employees;

-- 4번째 컬럼데이터를 가져와서 중복 제거
select distinct job_id from employees;
select distinct substr(job_id,4) from employees; --

-- where 절 : 조건비교연산자(=,<,>,<=,>=,!=)
select * from employees where manager_id = 124;
select * from employees where job_id = 'SH_CLERK';

select * from employees where employee_id > 100;

-- students 합계 250 이상, 국어 90 이상 출력
select * from students where total > 250 and kor > 90;

-- 영어 70이상 90이하
select * from students where eng >= 70 and eng <= 90; -- (70=<eng=<90 x)

-- 월급 5000이상 8000이하
select * from employees where salary >= 5000 and salary <= 8000;

-- 월급 7000 아닌 직원 검색(!=,<>,^=)
select * from employees where salary != 7000;

-- 부서 아이디가 50번인것, 50번이 아닌 직원 명 수(count(*)) 
select count(*) from employees where department_id = 50;
select count(*) from employees where department_id != 50;

-- null 값은 count에 포함되지 않는다. (전체수 알고싶을땐 null값이 없는 컬럼으로 찾기)
select count(*) from employees where department_id is null;

-- 급여 4000이하 사원번호,사원명,급여 만 출력
select employee_id as 사원번호,emp_name as 사원명,salary as 급여 from employees where salary <= 4000;

-- 숫자 비교연산자 가능, 날짜 비교연산자가 가능
select emp_name,hire_date from employees;

select emp_name,hire_date from employees where hire_date >= '2002/01/01';

-- 1999/12/31 이전에 입사한 사람을 출력하시오.
select emp_name,hire_date from employees where hire_date <= '1999/12/31';

-- 2001/01/01 부터 2004/12/31 까지 출력하시오.
select emp_name,hire_date from employees
where hire_date >= '20010101' and hire_date <= '2004/12/31';

-- 국어 90 또는 영어 90 이상 출력
select count(*) from students where kor >= 90 or eng >= 90;
select count(*) from students where kor >= 90 and eng >= 90;
select count(*) from students where kor >= 90;

-- 부서번호 80번, 직업이 man인 경우
select * from employees where department_id = 80  and substr(job_id,4) = 'MAN';

-- null 안나오게
select commission_pct from employees where commission_pct is not null;

-- 0.2,0.3,0.5
select commission_pct from employees 
where commission_pct =0.2 or commission_pct =0.3 or commission_pct =0.5;
select commission_pct from employees
where commission_pct in (0.2,0.3,0.5); -- in 연산자

-- 사원번호 110,120,130
select * from employees where employee_id in (110,120,130);
-- 사원번호 150-170
-- between a and b : =이 포함이 되어있음(이상, 이하)
select * from employees where employee_id >= 150 and employee_id <=170;
select * from employees where employee_id between 150 and 170;

select hire_date from employees;
select hire_date from employees where hire_date in ('20040217','20020607');

select hire_date from employees 
where hire_date between '20020617' and '20040217';

-- job man 출력
select * from employees where substr(job_id,4) ='MAN';

-- LIKE 연산자 : 포함되어 있는 글자 검색(%x : x로 끝나는 단어, x% : x로 시작하는 단어)
select * from employees where job_id like '%MAN';
select * from employees where job_id like 'ST%';

-- a가 들어가있는 이름 출력
select * from employees where emp_name not like '%a%';

-- 두번째 자리 t가 들어가있는 이름 출력(_x : _갯수 + x번째 자리)
select * from employees where emp_name like '_t%';
select * from employees where emp_name like '___v%';

-- 뒤에서 두번째 자리에 l이 있는 이름을 출력
select * from employees where emp_name like '%l_';

-- 첫번째 대문자 D 이름
select * from employees where emp_name like 'D%'
