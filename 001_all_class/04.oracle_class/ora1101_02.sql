desc board;
-- 테이블 create 할 때, foreign key 생성
create table board2(
bno number(4) primary key,
btitle varchar2(1000) not null,
bcontent clob,
id varchar2(30),
constraint fk_board2_id foreign key(id) references bmember(id)
);

desc board2;



-- 닉네임 : id_fk, foreign key : id, bmember테이블의 primary key : id 등록
alter table board add constraint id_fk foreign key(id) references bmember(id);

select * from board;
select * from bmember;

-- abc 글을 등록하면, 등록이 안됨
insert into board values(
board_seq.nextval,'제목6','내용6','abc',board_seq.currval,0,0,0,sysdate.''
);

-- foreign key 삭제
alter table board drop constraint;

-- bmember 테이블 id, foreign key로 board, board2에 등록
-- foreign key(외래키), primary key(기본기)
-- 원본의 primary key 데이터를 지우려면, foreign key의 데이터를 모두 삭제해야 삭제가 됨
-- or foreign key를 해제해야 삭제 가능

delete bmember where id='aaa'; -- 삭제 안됨 // 삭제됨 
delete board where id='aaa'; -- 먼저 삭제하면

alter table board drop constraint fk_id;
-- primary key가 삭제되면, foreign key로 등록된 모든 글을 삭제 (on delete cascade)
alter table board add constraint fk_id foreign key(id) references bmember(id) on delete cascade;

-- on delete restricted
-- 기본값 : 입력하지 않을 시, 자식데이터가 있을경우 부모데이터가 삭제가 되지 않음
alter table board add constraint id_fk foreign key(id) references bmember(id);
-- 자식테이블에 aaa로 쓴 데이터를 삭제해야 id를 삭제할 수 있음
delete board where bno=5;
delete bmember where id='aaa';

-- on delete cascade : 부모데이터 삭제시, 자식데이터 모두 삭제
alter table board add constraint id_fk foreign key(id) references bmember(id) on delete cascade;
-- 부모데이터 삭제 시 자식데이터의 모든 글이 삭제됨
delete bmember where id='aaa';

-- on delete set null
-- 부모데이터 삭제시, 자식데이터 null
alter table board add constraint id_fk foreign key(id) references bmember(id) on delete set null;
-- 부모데이터 삭제 시 자식데이터의 해당컬럼만 null 변경, 데이터는 그대로 존재
delete bmember where id='aaa';

alter table board drop constraint id_fk;
-- 1.


-- check 구문
create table emp01(
empno number(4) primary key,
ename varchar2(30) not null,
salary number(7,2) check(salary between 2000 and 20000),
gender varchar2(10) check(gender in('Male','Female'))
);

-- check 되어있는 컬럼에 데이터 추가
insert into emp01 values(
1,'홍길동',2500,'Male'
);
-- salary 범위 벗어나면 에러, Male,Female 이외 단어 입력시 에러
insert into emp01 values(
2,'유관순',20000,'Female'
);

-- default :insert 값이 입력되지 않을 시, 문자, 숫자, 날짜 설정가능
create table emp02(
empno number(4) primary key,
ename varchar2(30) default '무명',
income number(4) default 0,
salary number(7,2) check(salary between 2000 and 20000),
gender varchar2(10) check(gender in('Male','Female')),
edate date default sysdate
);

insert into emp02 (empno,salary,gender) values(
1,5000,'Male'
); -- ename, income, edate는 디폴트값으로 들어감

select * from emp02;
commit;

drop table datetable;

create table mem(
id varchar2(30) primary key,
pw varchar2(30) not null,
name varchar2(30) default '무명',
age number(3) default 0,
birth date,
gender varchar2(6) check (gender in('Male','Female')),
hobby varchar2(50) default 'game',
mdate date default sysdate
);

insert into mem values(
'aaa','1111','홍길동','24','2000/05/05','Male','golf',sysdate
);
insert into mem values(
'bbb','1111','유관순','23','2001/07/25','Female','game',sysdate
);
insert into mem values(
'ccc','1111','이순신','23','2001/07/25','Male','game',sysdate
);


commit;

select count(*) from mem;
select * from mem;
desc mem;

insert into mem(id,pw,name,age,birth,gender,hobby) values('ddd','1111','강감찬',22,'20220312','Male','game');
rollback;

-- employees 테이블 부서번호 50인 부서인원,부서번호,부서명
select count(*),department_id from employees
where department_id=50
group by department_id;

select a.department_id,department_name
from employees a, department b
where a.department_id = b.department_id

-- 부서별 수, 부서번호, 이름
select count(*), a.department_id,department_name from employees a, departments b
where a.department_id = b.department_id
group by a.department_id,department_name;

select * from students;
insert into students values(
students_seq.nextval,'김유신',99,98,96,99+98+96,(99+98+96)/3,1,sysdate
);
rollback;