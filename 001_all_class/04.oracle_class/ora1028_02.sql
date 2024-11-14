-- 검색
--select * from EMPLOYEES;
-- 테이블 생성
-- no, name, kor, eng, math, total, avg, rank
create table students(
no number(4),
name varchar2(20),
kor number(3),
eng number(3),
math number(3),
total number(3),
avg number(10),
rank number(4)
);
-- 데이터 입력
insert into students(no,name,kor,eng,math,total,avg,rank)
values(1,'홍길동',100,100,99,299,(299/3),1);

insert into students(no,name,kor,eng,math,total,avg,rank)
values(2,'유관순',100,90,99,289,(289/3),1);

-- 테이블 검색
select * from students;

commit; -- 저장

rollback; -- 전 commit까지 돌아가기

--drop table students; -- 테이블 삭제

select * from employees;

create table member(
id varchar2(20) primary key,
pw varchar(20),
name varchar(20),
phone varchar2(20)
);

insert into member (id,pw,name,phone) values(
'aaa','1111','홍길동','010-1111-1111'
);

select * from member;

commit;

insert into member values(
'bbb','1111','유관순','010-2222-2222'
); -- 전체 다 적을땐 컬럼명 생략가능

commit;
-- 입력
insert into member values(
'ccc','이순신'
); -- X 일부 출력 시 컬럼명 넣기

insert into member(id,name) values(
'ccc','이순신'
);

commit;

-- 검색
select * from member;
select id,phone from member; -- id,phone만 보기
select * from employees;
select emp_name, salary from employees;
select * from member;

update member set name='홍길자' where id='aaa'; -- 수정

select * from member;


delete member where id='ccc'; -- 삭제

-- 데이터 확정
commit;
rollback;
