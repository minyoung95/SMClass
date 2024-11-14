create table emp02(
empno number(4) primary key,
ename varchar2(30) not null,
job varchar2(9),
deptno number(2)
);
-- 중복불가 (unique)
insert into emp02 values(
1,'홍길동',null,null
);
insert into emp02 values(
2,'유관순',null,null
);
insert into emp02 values(
3,'이순신',null,null
);
insert into emp02 values(
null,'강감찬',null,null
);

select * from emp02;

delete emp02 where empno is null; -- null 삭제
commit;

alter table emp02 modify empno not null; -- 계약조건 변경(alter)
desc emp02;

-- not null, pk_emp02_empno:별칭
alter table emp02 add constraint pk_emp02_empno primary key(empno);
alter table emp02 drop constraint pk_emp02_empno;

create table mem(
id varchar2(30) primary key,
pw varchar2(30) not null,
name varchar2(100) default '무명', -- default : 아무값을 넣지 않았을 때 기본값
gender varchar2(6) check(gender in ('Male','Female')) -- 체크값만 넣을 수 있음
);

insert into mem values(
'aaa','1111','홍길동','Male'
);
insert into mem values(
'bbb','1111','유관순','Female' -- female 이면 check에 걸려서 입력이 안된다.
);
commit;

create table board2(
bno number(4) primary key,
btitle varchar2(1000) not null,
id varchar2(30),
-- constraint references : mem의 id(primary key)의 foreign key로 만들기
constraint fk_board2_id foreign key(id) references mem(id)
);

select * from mem;
delete mem where id = 'aaa'; -- 자식키에 해당 값이 있으면 삭제를 시킬 수 없음

 -- mem(id)에 abc라는 id가 없기때문에 제약조건에 걸림 (외래키로 등록 시 부모키에 해당 값이 없으면 에러)
insert into board2 values(
4,'제목4','abc'
);
-- 외래키 삭제
alter table board2 drop constraint fk_board2_id;

-- on delete cascade : 부모 키 삭제 시 외래키로 등록된 값들을 모두 삭제
alter table board2
add constraint fk_board2_id foreign key (id)
references mem(id) on delete cascade;
commit;

-- 부모테이블 bbb 삭제 시, 자식테이블의 bbb도 모두 삭제
delete mem where id ='bbb';
select * from board2;
-- no delete restricted(기본값) : 부모 키 삭제 시 외래키로 등록된 값이 있으면 삭제가 되지 않음.
-- on delete set null : 부모 키 삭제 시 외래키로 등록된 값들을 null값으로 바꿈

create table mem(
id varchar2(30) primary key,
pw varchar2(100) not null,
name varchar2(100),
deptno number(4)
);

insert into mem values('aaa','1111','홍길동',10);
insert into mem values('ccc','1111','이순신',30);
commit;

-- 10 총무부, 20 인사부, 30 마케팅
-- decode : 일치하는 경우
select id,pw,name,deptno,
decode(deptno,
10,'총무부',
20,'인사부',
30,'마케팅'
) from mem;

select * from employees;

select job_id from employees;

-- clerk 월급5%인상, rep:10%, man 15%
-- clerk , rep, man 출력
select emp_name,substr(job_id,4) j_id , salary,

decode(substr(job_id,4),
'CLERK',salary*1.05,
'REP',salary*1.1,
'MAN',salary*1.15
) sal

from employees 
where substr(job_id,4) in ('CLERK','REK','MAN');

select substr(job_id,4) j_id , salary,
decode (substr(job_id,4),
'CLERK',salary*1.05,
'REP', salary*1.1,
'MAN',salary*1.15
) sal
from employees
where substr(job_id,4) in ('CLERK','REP','MAN')
;

create table lavel_data (
	id VARCHAR2(50) primary key,
	lavel number(1) not null
);

commit;

select * from lavel_data;

-- 1: 100포, 2: 1000포, 3: 5000포, 4: 10000포, 5: 20000포인트
-- point
select id, lavel,
decode(lavel,
1,100,
2,1000,
3,5000,
4,10000,
5,20000
)||' point' point
from lavel_data order by lavel;

-- case : decode와 같은 기능이지만, 비교연산자 사용가능
select id,pw,name,deptno,
case
when deptno=10 then '총무부'
when deptno=20 then '인사부'
when deptno=30 then '마케팅'
end as deptName
from mem;

-- 1,2,3 : 5000 포인트, 4,5 : 20000 포인트
select id, lavel,
decode(lavel,
1,5000,
2,5000,
3,5000,
4,20000,
5,20000
)||' point' point
from lavel_data order by lavel;

select id, lavel,
case
when lavel >= 1 and lavel <= 3 then 5000
when lavel >= 4 then 20000
end as point
from lavel_data order by lavel;

select * from students;
-- avg: 90점 이상 A, 80점 이상 B, 70점 이상 C, 60점 이상 D, 나머지 F
select name, round(avg,2),
case
when avg >=90 then 'A'
when avg >=80 then 'B'
when avg >=70 then 'C'
when avg >=60 then 'D'
when avg <60 then 'F'
end as result
from students order by round(avg,2) desc;

create table stu as select * from students; -- 테이블 전체 복사
-- 컬럼추가
select * from stu;
alter table stu add result varchar2(2);

-- 컬럼에 데이터 값 추가하기 update set
update stu set result = (
case
when avg >=90 then 'A'
when avg >=80 then 'B'
when avg >=70 then 'C'
when avg >=60 then 'D'
when avg <60 then 'F'
end
);

-- rank() over : 순위 정하기 (중복 순위가 있을 경우 다음 순위가 뒤로 밀림 ex 1,2,2,4)
select no,name,total,rank()over(order by total desc) from stu;
-- dense_rank() over (중복 순위가 있어도 다음 순위가 순서대로 ex 1,2,2,3)
select no,name,total,dense_rank()over(order by total desc) from stu;

select * from stu;
-- 순위를 rank 컬럼에 추가하시오
update stu a set rank = (
select ranks from(select no,rank()over(order by total desc)as ranks from stu
) b 
where b.no = a.no -- 같게 만들어줌? (2)
);
-- 두개의 차트의 순서? 형태가 다르기때문에 (1)
select no,rank from stu;
select no,rank()over(order by total desc) as ranks from stu;

-- case
-- salary 5000 이하 15%인상, 5000~8000 10%인상, 8000이상 5% 인상
select emp_name,salary,
case
when salary <5000 then salary*1.15
when salary >=5000 and salary <=8000 then salary*1.1
when salary >8000 then salary*1.05
end salary2
from employees;

-- like : 대문자 D가 포함되어 있으면 10% 인상, M이 포함 되어있으면 5%인상, 그 외 그대로
select emp_name, salary,
case
when emp_name like '%D%' then salary*1.1
when emp_name like '%M%' then salary*1.05
else salary -- 나머지
end y_salary
from employees;

select * from employees;

select department_id, commission_pct from employees
where commission_pct is not null;

-- 커미션이 있는 사원 수를 출력하시오.
select count(*) from employees where commission_pct is not null;

-- 부서별 사원수를 출력하시오.
select department_id,count(*) from employees
group by department_id
order by department_id;

-- 부서 번호,부서별 평균월급, 사원 수 출력
select department_id,round(avg(salary),2),count(salary) from employees
group by department_id;

-- having : 조건절에 그룹함수 비교연산 having
-- 부서별 평균월급이 7000보다 높은 사람의 인원 수
select department_id,avg(salary),count(salary) from employees
group by department_id
having avg(salary) >=7000;

-- 부서별 평균 월급이 5000 이하인 부서별 인원수
-- 그룹 함수는 having 조건문을 사용, where절에는 사용 불가
select department_id,avg(salary),count(salary) from employees
group by department_id
having avg(salary)<=5000;

-- 전체 평균월급보다 적게 받는 사원 수
select department_id,avg(salary),count(*) from employees
where salary < (select avg(salary) from employees)
group by department_id;

-- 부서별 평균월급 보다 적게 받는 사원
select department_id,emp_name,salary from employees a
where salary <
(
select salarys from(
select department_id, avg(salary) salarys from employees
group by department_id
) b
where a.department_id = b.department_id
);

-- ★부서별 평균 월급보다 적게 받는 사원수★
select department_id,count(*) from employees a
where salary <
(
select salarys from(
select department_id, avg(salary) salarys from employees
group by department_id
) b
where a.department_id = b.department_id
)
group by department_id
order by department_id;

-- 부서별 월급 최대,최솟값을 출력, 최대급여가 5000이상인 부서만
select department_id,max(salary),min(salary) from employees
group by department_id
having max(salary) >= 5000
order by department_id;

-- 학번,이름,전화번호,주소,성별,학년,학기,국어,영어,수학,합계,평규는, 등수

-- 1001,홍길동,010,서울,남자,1,1,100,100,100,300,1
-- 1001,홍길동,010,서울,남자,1,2,90,90,90,270,8
-- 1001,홍길동,010,서울,남자,1,3,95,95,95,285,15
-- 1001,홍길동,010,서울,남자,1,4,100,100,99,299,2
-- 1001,홍길동,010,서울,남자,2,1,100,100,100,300,1
-- 1001,홍길동,010,서울,남자,2,2,90,90,90,270,8
-- 1001,홍길동,010,서울,남자,3,3,95,95,95,285,15
-- 1001,홍길동,010,서울,남자,4,4,100,100,99,299,2
-- 1001,홍길동,010,서울,남자,3,1,100,100,100,300,1
-- 1001,홍길동,010,서울,남자,3,2,90,90,90,270,8
-- 1001,홍길동,010,서울,남자,3,3,95,95,95,285,15
-- 1001,홍길동,010,서울,남자,3,4,100,100,99,299,2

-- 부서명 departments
select * from departments;

select * from employees;

-- donald Oconnell 의 부서명
select emp_name,department_id from employees
where emp_name = 'Donald OConnell';

select department_id,department_name from departments
where department_id=50;

-- ★★join을 사용하여 두개의 쿼리를 1개의 쿼리로 구성★★
-- 1. cross join,2. inner join,3. outer join,4. self join
-- 1. cross join : 특별한 키워드 없이 두개의 테이블을 검색
select * from employees;
select * from departments;
select count(*) from employees, departments; -2889
select * from employees, departments;

--2. inner join (equi join : 두 테이블에서 공통적으로 존재하는 컬럼을 연결)
select emp_name,a.department_id,department_name from employees a,departments b
where a.department_id = b.department_id(+); -- (+) :null 값도 포함

select * from member; -- id 존재
select * from board; -- id 존재
select bno,btitle,bcontent,a.id,email,phone from member a,board b
where a.id = b.id;

-- inner join : 사원번호, 사원명,job_id,job_title 출력
select * from jobs;
select * from employees;
select employee_id,emp_name,a.job_id,job_title from employees a, jobs b
where a.job_id = b.job_id and a.job_id = 'SH_CLERK';

-- 사원번호, 사원명, 부서번호, 부서명, job_id, job_title 을 출력
select * from departments;
select employee_id,emp_name,a.department_id,department_name,a.job_id,job_title
from employees a, departments b, jobs c
where a.department_id = b.department_id and a.job_id = c.job_id;

-- member 닉네임 , board 게시글
select * from member;
select * from board;
select bno,btitle,bcontent,a.name,bgroup,bstep,bindent,bhit,bdate,bfile
from member a, board b
where a.id = b.id;

-- 사원번호, 사원명, 월급, 부서번호, 부서명
-- 월급 평균 월급보다 적은 사원을 출력하시오.

select employee_id,emp_name,a.department_id,department_name
from employees a, departments b
where a.department_id = b.department_id 
and salary < (select avg(salary) from employees);

-- ★★부서별 평균 월급보다 적은 사원★★
select employee_id,emp_name,salary,a.department_id,department_name
from employees a, departments b
where a.department_id = b.department_id
and salary <
(
select salarys from(
select department_id, avg(salary) salarys from employees
group by department_id
) c
where a.department_id = c.department_id
);

-- job_id CLERK인 사원의 사원명, 사원번호, 부서명, 부서번호, 직급번호, 직급명 출력
select * from employees;
select * from departments;
select * from jobs;

select emp_name, employee_id, department_name, a.department_id, a.job_id, job_title
from employees a, departments b, jobs c
where a.department_id = b.department_id and a.job_id = c.job_id
and substr(a.job_id,4)in ('CLERK','MAN');

-- 2. inner join (non-equi join)
create table salgrade(
grade varchar2(10),
losal number(6),
hisal number(6)
);

insert into salgrade values(
'E등급',2000,4000
);
insert into salgrade values(
'D등급',4001,6000
);
insert into salgrade values(
'C등급',6001,8000
);
insert into salgrade values(
'B등급',8001,10000
);
insert into salgrade values(
'A등급',10001,100000
);
select * from salgrade;
commit;
-- salary 옆에 등급(salgrade)을 넣으려고 하는데 같은 컬럼이 없음
-- non-equi join 사용
select salary from employees;

select emp_name,salary,grade
from employees,salgrade
where salary between losal and hisal; -- 조건 (값의 범위를 비교)

-- non-equi join 활용하여 students total A,B,C,D,F 등급 출력
create table stu_grade(
grade varchar2(10),
lototal number(5,2), -- 59.99
hitotal number(5,2)
);
insert into stu_grade values(
'A등급',90,100
);

select * from stu_grade;
select * from students;
select name, round(avg,2), grade from students,stu_grade
where avg between lototal and hitotal
order by grade;

select * from stu;
-- stu의 result non-equi join을 사용하여 입력
update stu a set result = (
select results from(
select no,grade as results 
from stu,stu_grade
where avg between lototal and hitotal) b
where a.no = b.no
);

select name,avg,grade grades from stu,stu_grade
where avg between lototal and hitotal;


-- self join: 자신의 테이블 2개를 join 결과값 출력
select employee_id,emp_name,manager_id from employees;

select employee_id,emp_name from employees
where employee_id = 124;

select a.employee_id,a.emp_name,a.manager_id,b.emp_name
-- 원래 b.emp_name(196)이 a.emp_name(196)과 똑같이 나온다
from employees a, employees b
where a.manager_id = b.employee_id and a.manager_id = 124;
-- a의 매니저아이디(124) > b의 사원아이디(196>124) > b의 사원명(124와 대칭되는)을 찾을수 있게 해줌

select * from students;