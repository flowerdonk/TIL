CREATE TABLE articles (
    title TEXT,
    content TEXT,
    user_id INTEGER
);

CREATE TABLE users (
    name TEXT,
    role_id INTEGER
);

CREATE TABLE roles (
    role TEXT
);

-- 데이터 베이스는 항상 보호받아야한다.
-- 실수로 날리는 쿼리
BEGIN;
  DELETE FROM zoo
  WHERE weight < 100;

ROLLBACK;
BEGIN;
  DELETE FROM zoo
  WHERE eat 'omnivore';
COMMIT;

SELECT COUNT(*)
FROM zoo;