select * from member;

update member set id='abc',pw='1111',name='임민영',email='mylim52@naver.com'
where id='abc';
commit;

select sysdate-1,sysdate,sysdate+1 from dual;

-- round : 15일 기준 월초 버림, 월말 올림
select hire_date,round(hire_date,'Month') from employees;
-- trunc : 버림 (000223 > 000201)
select hire_date,trunc(hire_date,'month') from employees;

select trunc(sysdate,'month') from dual; -- 기준을 잡은 달 1일
select add_months(trunc(sysdate,'month'),1) from dual; -- 1달 + (add_months)

-- 요금제 변경하면 다음달 1일부터 혜택
select sysdate,add_months(trunc(sysdate,'month'),1) from dual;

-- 입사일 기준 다음달부터 1일부터 혜택
select hire_date,add_months(trunc(hire_date,'month'),1) from employees;

-- 입사일 기준 1년 후 날짜 출력
select hire_date,hire_date+365,add_months(hire_date,12) from employees; 

-- 입사일 기준 1년 후 날짜와, 1년 후 그 달의 마지막 날짜(last_day) 출력
select hire_date,hire_date+365,add_months(last_day(hire_date),12) from employees;

-- 입력일 기준 1년 후 마지막 날짜가 8월 31일, 9월 30일,10월 31일인 학생들 모두 출력
select sdate from students;
select name,add_months(last_day(sdate),12) sdate2 from students
where add_months(last_day(sdate),12) in ('25/08/31','25/09/30','25/10/31')
order by sdate2;

-- sysdate : 년 월 일 // extract : 특정 년,월,일,시,분,초 만 분리해서 가져올수있음
select extract(year from sysdate) from dual;
select extract(month from sysdate) from dual;
select extract(day from sysdate) from dual;

-- systimestamp : 년 월 일, 시 분 초
select systimestamp from dual;
select extract(hour from systimestamp) from dual;
select extract(minute from systimestamp) from dual;
select extract(second from systimestamp) from dual;

select sdate, extract(month from sysdate), extract(year from last_day(sdate+365))
from students
where extract(month from last_day(sdate+365)) in (8,9,10);

-- substr(시작 위치,갯수)
select sysdate,substr(sysdate,4,2) from dual;

select sdate from students where substr(sdate,4,2) in (8,9,10)
order by sdate;

-- 날짜,숫자 > 문자 : to_char, 문자 > 날짜 : to_date, 문자 > 숫자 : to_number
-- 날짜 형 변환 날짜 포맷을 변경 (24/10/31 >> )
-- date 타입 > char 타입으로 변경하여 포맷 (to_char)
select sysdate from dual;
select sysdate,to_char(sysdate,'yyyy-mm-dd')from dual;
select sysdate,to_char(sysdate,'yyyy-mm-dd hh24:mi:ss day')from dual; -- hh24 : 0~24시
select sysdate,to_char(sysdate,'yyyy-mm-dd pm hh:mi:ss day')from dual; -- am/pm hh : 오전/오후 0~12시 
select sysdate,to_char(sysdate,'yy-mm-dd hh24:mi:ss dy')from dual; -- yy :24, dy: 목
select sysdate,to_char(sysdate,'yy-Mon-dd hh24:mi:ss')from dual; -- Mon : 10월

select hire_date,to_char(hire_date,'yyyy-mm-dd hh:mi:ss')from employees;

-- student 테이블 sdate를 2024/01/01 형태로 출력
select sdate,to_char(sdate,'yyyy/mm/dd') from students;

-- 숫자 > 문자(to_char) : 천단위 표시 (000 : 빈자리는 0으로 채워짐, 999 : 빈자리 공백)
select salary*1382.86*12 from employees;
select to_char(salary*1382.86*12,'000,000,999,999') from employees;

select to_char(12,'000') from dual; -- 012 (자릿수 채울때 사용)
select to_char(100000,'L999,999') from dual; -- L:국가통화기호 표시, $:$표시

select to_char(123456,'000000000'), to_char(123456,'999,999,999') from dual;

create table chartable2(
no number(4),
kor number(10),
kor_char number(10),
kor_mark number(10)
);

insert into chartable values(
1,10000,to_char(10000,'00000000'),to_char(10000,'0,000,000')
);

select * from chartable;



select kor+kor_mark from chartable; -- 숫자형 타입과 문자 천단위 표시는 사칙연산 불가
select kor+kor_char from chartable; -- 숫자형 타입과 문자형(숫자)타입은 사칙연산 가능

insert into chartable values(
1,10000,10000,10000
);
-- 숫자타입은 앞에 0을 넣어도 생략된다. : 문자열타입만 가능
-- 천단위 표시는 숫자형타입에 쓸수 없음
insert into chartable2 values(
4,4000000,004000000,'4,000,000' 
);
commit;
rollback;

select * from chartable2;

-- 2일 이후의 날짜를 출력 (문자를 날짜로 변환 후 +2)
select to_date('20241031')+2 from dual;

-- 숫자 > 날짜
select to_date(20231031) from dual;
-- 문자 > 날짜
select sysdate-to_date('20231101') from dual;


select '20,000' from dual;
-- 천단위 문자형 > 천단위 제외 숫자형
select to_number('20,000','999,999') from dual;
-- 천단위 문자형 >

select department_id from employees where department_id is not null; -- null 제외 찾기
select commission_pct from employees where commission_pct is null; -- null 만 찾기

-- 월급 * 커미션 nvl(x,0) : null 값 0으로 표시
select salary, salary+salary*nvl(commission_pct,0) from employees;

select nvl(department_id,0) from employees;
-- nvl(x,y) x,y의 타입이 같아야 적용할 수 있음 >> department_id 를 문자형으로 바꾼다.
select nvl(to_char(department_id),'ceo') from employees;

-- 그룹함수
-- sum 합계, avg 평균, count 갯수, min 최솟값, max 최댓값
select sum(salary) from employees;
select to_char(sum(salary),'999,999,999') from employees; -- 천 단위 표시

select avg(salary) from employees;
select round(avg(salary),4) from employees; -- 소숫점 넷째자리 반올림 round(x,4)
select trunc(avg(salary),4) from employees; -- 소숫점 넷째자리 버림
-- max,min : 최댓값, 최솟값
select max(salary) from employees;
select min(salary) from employees;

-- 평균값보다 높게 임금을 받는사람 명 수(count)
select count(salary) from employees 
where salary >= (select avg(salary) from employees);

-- 단일함수(emp_name), 그룹합수(avg)는 같이 쓸 수 없음
select emp_name,avg(salary) from employees;

-- students 테이블 모든 학생의 kor점수 합계,평균,최대,최솟값 출력 (median : 중간값)
select sum(kor),round(avg(kor),2),max(kor),min(kor),median(kor) from students;

-- 부서번호가 50 사원들의 월급의 합, 평균, 최대, 최솟값 출력
select sum(salary),round(avg(salary),2),max(salary),min(salary) from employees
where department_id = 50;

-- 부서별 최댓값
select department_id,max(salary) from employees
group by department_id; -- 단일함수 그룹화(group by)

-- 전체평균
select avg(salary) from employees;
-- 부서별 평균
select department_id,round(avg(salary),2),max(salary),min(salary) from employees
group by department_id
order by department_id;

-- 평균월급보다 높은 사람 수
select count(salary) from employees 
where salary >= (select avg(salary) from employees);

-- 수학함수 : abs-절댓값, ceil-올림, floor-버림, round-반올림, trunc-절삭, mod-나머지
-- power - 제곱, sqrt - 제곱근

select power(3,3) from dual;

-- 문자,숫자형 타입 > 날짜형타입 변경가능
-- 숫자,날짜형 타입 > 문자형타입 변경가능
-- 문자형 타입 > 숫자형타입 변경가능
select 20240101,to_date(20240101) from dual; -- 숫자 > 날짜
select '20240101', to_number('20240101') from dual; -- 문자 > 숫자
select sysdate,to_number(sysdate) from dual; -- 날짜 > 숫자 (x)
select to_number(to_date('20240101')) from dual; -- 문자 > 날짜 > 숫자 (x)
-- sysdate (24/01/01) or yyyy-mm-dd : 중간 / 나 -가 있으면 숫자로 변경 불가
select sysdate,to_number(to_char(sysdate,'yyyymmdd')) from dual;
-- 년 월 일에 "" 넣어주면 변경 가능
select sysdate,to_char(sysdate,'yyyy"년"mm"월"dd"일" day') from dual;

--- 문자형 함수☆
select emp_name,email from employees;

-- 문자형 타입을 +기호를 사용하여 합치려면 에러
select emp_name+email from employees;
-- ||, concat함수
select emp_name || email from employees; -- 속도 더 빠름, 많이씀
select concat(emp_name,email) from employees;

-- lower : 소문자 치환, upper: 대문자 치환, initcap: 첫글자 대문자 치환
select * from member where lower(name)='bryan';

--lpad : 왼쪽 자릿수 채우기, rpad : 오른쪽 자릿수 채우기
select 'john',lpad('john',10,'#') from dual;
select 'john',rpad('john',10,'~') from dual;

--trim : 빈 공백 없애기, ltrim, rtrim : 왼쪽,오른쪽 공백 없애기
select length('     aaa  '),length(trim('     aaa  ')) from dual; -- 길이 10개, 3개

--replace : 치환
select '    a  b c   ',trim('    a  b c   '),replace('    a  b c   ',' ','') from dual;

--substr(x,n)(시작위치,갯수) : 자르기(x번째부터 n개) 
select 'abcdefg',substr('abcdefg',0,3) from dual;

-- 입사일이 3월 인 사원을 출력
select emp_name,hire_date from employees where substr(hire_date,4,2)=3;
-- 입사일 3,8,10
select emp_name,hire_date from employees where substr(hire_date,4,2)in (3,8,10);

-- translate 치환
select 'axyz',translate('axyzxkzzxbcy','xyk','ab') from dual; -- x > a, y > b로 바꿈, k > 삭제

-- length() : 문자열 길이
-- students 테이블 name길이가 5자 이상인 학생
select name,length(name) from students where length(name) > 5;

-- 사원의 월급의 합과 평균
select sum(salary),round(avg(salary),2) from employees;

-- 영어점수의 합, 평균, 최대, 최솟값
select sum(eng),round(avg(eng),2),max(eng),min(eng) from students;

--
select name,to_char(sdate,'"등록일 : "yyyy"년"mm"월"dd"일"')as 등록일 from students ;
