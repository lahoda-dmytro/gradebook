from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey
from database import Base
from sqlalchemy.orm import relationship

class Group(Base):
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    students = relationship('Student', back_populates='group')

class Speciality(Base):
    __tablename__ = 'specialities'
    id = Column(Integer, primary_key=True)
    code = Column(String, unique=True)
    name = Column(String)

class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    number = Column(Integer, unique=True) # num of course

class Student(Base):
    __tablename__ = 'students'
    zalik_book = Column(String, primary_key=True) #num of zalik book
    first_name = Column(String)
    last_name = Column(String)
    patronymic = Column(String)
    email = Column(String, unique=True)
    phone = Column(String)
    group_id = Column(Integer, ForeignKey('groups.id'))
    speciality_id = Column(Integer, ForeignKey('specialities.id'))
    course_id = Column(Integer, ForeignKey('courses.id'))

    group = relationship('Group', back_populates='students')
    grades = relationship('Grade', back_populates='student')

class DeanWorker(Base):
    __tablename__ = 'dean_workers'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    patronymic = Column(String)
    email = Column(String, unique=True)
    phone = Column(String)
    role = Column(String) #"teacher", "admin", "dean"

    subjects = relationship('Subject', back_populates='teacher')


class Grade(Base):
    __tablename__ = "grades"
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.zalik_book'))
    subject_id = Column(Integer, ForeignKey('subjects.id'))
    grade = Column(String)
    is_confirmed = Column(Boolean, default=False)
    date = Column(Date) # date of grade was created

    student = relationship("Student", back_populates="grades")
    subject = relationship("Subject", back_populates="grades")

class Subject(Base):
    __tablename__ = "subjects"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    type = Column(String)
    deadline = Column(Date) # date to confirm grades
    teacher_id = Column(Integer, ForeignKey('dean_workers.id'))
    course_id = Column(Integer, ForeignKey('courses.id'))
    speciality_id = Column(Integer, ForeignKey('specialities.id'))

    teacher = relationship("DeanWorker", back_populates="subject")
    grades = relationship("Grade", back_populates="subject")