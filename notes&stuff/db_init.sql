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
drop table if exists courses;
drop table if exists quizzes;
drop table if exists questions;
drop table if exists answers;

create table users (id serial primary key,
					first_name varchar(50) not null,
					last_name varchar(50) not null,
					login_id varchar(10) not null,
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