from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey
from database import Base
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    hashed_password = Column(String)
    role = Column(String)

    teacher_subject = relationship("Subject", back_populates="teacher")

class Grade(Base):
    __tablename__ = "grades"
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('users.id'))
    subject_id = Column(Integer, ForeignKey('subjects.id'))
    grade = Column(String)
    deadline = Column(Date)
    is_confirmed = Column(Boolean, default=False)

    student = relationship("User", back_populates="teacher_subject")
    subject = relationship("Subject", back_populates="teacher")

class Subject(Base):
    __tablename__ = "subjects"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    teacher_id = Column(Integer, ForeignKey('users.id'), index=True)
    teacher = relationship("User", back_populates="teacher_subject")

    grades = relationship("Grade", back_populates="subject_id")