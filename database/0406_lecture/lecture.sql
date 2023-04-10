CREATE TABLE lecture(
    lec_id INTEGER NOT NULL PRIMARY KEY,
    lec_name TEXT NOT NULL,
    professor TEXT NOT NULL,
    grade INTEGER,
    seat_available INTEGER,
    detail TEXT
);

CREATE TABLE professor(
    pf_name TEXT NOT NULL,
    pf_age INTEGER,
    major TEXT NOT NULL
);

CREATE TABLE student(
    st_id INTEGER NOT NULL PRIMARY KEY,
    st_name TEXT NOT NULL,
    st_age INTEGER,
    grade INTEGER NOT NULL
);

CREATE TABLE timetable(
    st_id INTEGER NOT NULL,
    lec_id INTEGER NOT NULL,
    lec_name TEXT NOT NULL
);

INSERT INTO professor
VALUES
    ('isaac', 25, 'SAFFY');

INSERT INTO student
VALUES
    (0944172, 'yujin', 18, 1),
    (0944173, 'heejin', 19, 2),
    (0944174, 'youngseo', 19, 2);

INSERT INTO lecture
VALUES
    (1, 'Django', 'isaac', 1, 28, '기초'),
    (2, 'DB', 'isaac', 2, 28, '응용'),
    (3, 'Project', 'isaac', 4, 28, '심화');
  
INSERT INTO timetable
VALUES
    (0944172, 2, 'DB'), --yujin
    (0944173, 3, 'Project'); --heejin

-- 수강신청 전체
BEGIN;
  SELECT T.lec_name, S.st_name, S.st_id FROM timetable AS T INNER JOIN student AS S ON T.st_id=S.st_id; 
ROLLBACK;

-- 특정 학생 수강신청 내역
BEGIN;
  SELECT T.lec_name, S.st_name, S.st_id FROM timetable AS T INNER JOIN student AS S ON T.st_id=S.st_id AND S.st_id=0944172; 
ROLLBACK;