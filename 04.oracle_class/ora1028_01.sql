-- 아이디에 c## 스크립트 해제
alter session set "_ORACLE_SCRIPT" = true;

-- 사용자 생성
create user ora_user identified by 1111;

-- 권한부여
grant connect,resource,dba to ora_user;

-- 권한해제
revoke connect,resource,dba to ora_user;