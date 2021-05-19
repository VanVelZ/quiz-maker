alter table if exists courses
drop constraint if exists fk_teacher;

alter table if exists student_courses
drop constraint if exists fk_studentC;

alter table if exists quizzes
drop constraint if exists fk_courseQ;

alter table if exists answers
drop constraint if exists fk_questionanswer;

drop table if exists student_questions;
drop table if exists users;
drop table if exists student_courses;
drop table if exists answers;
drop table if exists questions;
drop table if exists quizzes;
drop table if exists courses;

create table users (id serial primary key,
					first_name varchar(50) not null,
					last_name varchar(50) not null,
					login_id varchar(10) not null unique,
					password varchar(50) not null,
					role_id int not null);
create table courses(id serial primary key,
					 "name" varchar(50) not null,
					 teacher_id int not null);
create table student_courses(id serial primary key,
							  student_id int not null,
							  course_id int not null);
create table quizzes(id serial primary key,
					"name" varchar(50) not null,
					course_id int not null);
create table questions(id serial primary key,
					   quiz_id int not null,
					   description varchar(100) not null);
create table answers(id serial primary key,
					 description varchar(100),
					 question_id int not null,
					 is_correct bool not null);
create table student_questions(id serial primary key,
							student_id int not null,
							question_id int not null,
							answer_id int not null);

insert into users values(default, 'Steve', 'Steven', '100000', 'password', 1);
insert into users values(default, 'Ben', 'Steven', '100001', 'password', 1);
insert into users values(default, 'George', 'Steven', '100002', 'password', 1);
insert into users values(default, 'Jeff', 'Steven', '100003', 'password', 1);
insert into users values(default, 'Beth', 'Steven', '100004', 'password', 1);

insert into users values(default, 'Mister', 'Teacher', '200000', 'password', 2);
insert into users values(default, 'Miss', 'Teacher', '200001', 'password', 2);
insert into users values(default, 'Some', 'One', '200002', 'password', 2);


insert into courses values(default, 'Physical Science', 6);
insert into courses values(default, 'Biology', 7);
insert into courses values(default, 'Computer Science', 6);
insert into courses values(default, 'Potatos 101', 8);

insert into student_courses values(default, 1, 1);
insert into student_courses values(default, 2, 1);
insert into student_courses values(default, 3, 1);
insert into student_courses values(default, 1, 2);
insert into student_courses values(default, 1, 3);
insert into student_courses values(default, 5, 4);
insert into student_courses values(default, 2, 4);
insert into student_courses values(default, 3, 4);
insert into student_courses values(default, 1, 4);

INSERT INTO quizzes values(default, 'Light Quiz', 1);
insert into questions values(default, 1, 'What is the speed of light?');
insert into answers  values(default, '671,000,000 mph', 1, true);
insert into answers  values(default, '100,000 mph', 1, false);
insert into answers  values(default, '671 mph', 1, false);
insert into answers  values(default, '6,000 mph', 1, false);

INSERT INTO quizzes values(default, 'Dark Quiz', 1);
insert into questions values(default, 2, 'What is the speed of Dark?');
insert into answers  values(default, '671,000,000 mph', 2, true);
insert into answers  values(default, '100,000 mph', 2, false);
insert into answers  values(default, '671 mph', 2, false);
insert into answers  values(default, '6,000 mph', 2, false);
insert into questions values(default, 2, 'Are you scared of the Dark?');
insert into answers  values(default, 'No', 3, false);
insert into answers  values(default, 'Definitely not', 3, false);
insert into answers  values(default, 'okay, maybe', 3, false);
insert into answers  values(default, 'still no', 3, true);
insert into questions values(default, 2, 'Perfect Dark was');
insert into answers  values(default, 'Better than Golden Eye', 4, false);
insert into answers  values(default, 'The best shooter of its time', 4, false);
insert into answers  values(default, 'Fun', 4, false);
insert into answers  values(default, 'All of the above', 4, true);

INSERT INTO quizzes values(default, 'Potato quiz', 4);
insert into questions values(default, 3, 'What is the speed of potato?');
insert into answers  values(default, '671,000,000 mph', 5, true);
insert into answers  values(default, '100,000 mph', 5, false);
insert into answers  values(default, '671 mph', 5, false);
insert into answers  values(default, '6,000 mph', 5, false);
insert into questions values(default, 3, 'What is a potato');
insert into answers  values(default, 'A fruit', 6, false);
insert into answers  values(default, 'Future French Fries', 6, true);
insert into answers  values(default, 'A legume', 6, false);
insert into answers  values(default, 'A vegetable', 6, false);

alter table courses
add constraint fk_teacher
foreign key (teacher_id)
references users(id)
on delete cascade;

alter table student_courses
add constraint fk_studentC
foreign key (student_id)
references users(id)
on delete cascade;

alter table student_courses
add constraint fk_courseS
foreign key (course_id)
references courses(id)
on delete cascade;

alter table quizzes
add constraint fk_courseQ
foreign key (course_id)
references courses(id)
on delete cascade;

alter table questions
add constraint fk_questionquiz
foreign key (quiz_id)
references quizzes(id)
on delete cascade;

alter table answers
add constraint fk_questionanswer
foreign key (question_id)
references questions(id)
on delete cascade;

alter table student_questions
add constraint fk_studentquiz
foreign key (student_id)
references users(id)
on delete cascade;

alter table student_questions
add constraint fk_studentquestions
foreign key (question_id)
references questions(id)
on delete cascade;

alter table student_questions
add constraint fk_studentanswers
foreign key (answer_id)
references answers(id)
on delete cascade;
