from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, JSON
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True)
    username = Column(String)
    current_timer_settings = Column(JSON, default=lambda: {
        'pomodoro': 25,
        'short_break': 5,
        'long_break': 15
    })

    @classmethod
    async def get_or_create(cls, session, user_id, username=None):
        user = await session.get(cls, user_id)
        if not user:
            user = cls(user_id=user_id, username=username)
            session.add(user)
            await session.commit()
        return user

class Project(Base):
    __tablename__ = 'projects'
    project_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    name = Column(String)
    user = relationship('User')

    @classmethod
    async def get_user_projects(cls, session, user_id):
        result = await session.execute(
            cls.__table__.select().where(cls.user_id == user_id)
        )
        return result.scalars().all()

class Task(Base):
    __tablename__ = 'tasks'
    task_id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey('projects.project_id'))
    title = Column(String)
    status = Column(String, default='active')
    project = relationship('Project')

    @classmethod
    async def get_active_tasks(cls, session, user_id):
        result = await session.execute(
            cls.__table__.join(Project, cls.project_id == Project.project_id)
            .select().where(Project.user_id == user_id, cls.status == 'active')
        )
        return result.scalars().all()

    @classmethod
    async def get_focused_task(cls, session, user_id):
        # Для MVP: возвращаем первую активную задачу
        tasks = await cls.get_active_tasks(session, user_id)
        return tasks[0] if tasks else None

class Tree(Base):
    __tablename__ = 'trees'
    tree_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    growth_stage = Column(Integer, default=1)  # 1: 🌱, 2: 🌿, 3: 🌳
    last_updated = Column(DateTime)
    user = relationship('User')

class UserStats(Base):
    __tablename__ = 'user_stats'
    user_id = Column(Integer, ForeignKey('users.user_id'), primary_key=True)
    total_pomodoros = Column(Integer, default=0)
    xp = Column(Integer, default=0)
    user = relationship('User')

class Group(Base):
    __tablename__ = 'groups'
    group_id = Column(Integer, primary_key=True)
    name = Column(String)
    is_public = Column(Integer, default=0)
    invite_code = Column(String, unique=True, nullable=True)

    @classmethod
    async def get_by_code(cls, session, code):
        result = await session.execute(
            cls.__table__.select().where(cls.invite_code == code)
        )
        return result.scalar_one_or_none()

class GroupMember(Base):
    __tablename__ = 'group_members'
    user_id = Column(Integer, ForeignKey('users.user_id'), primary_key=True)
    group_id = Column(Integer, ForeignKey('groups.group_id'), primary_key=True)

class TimerSession(Base):
    __tablename__ = 'timer_sessions'
    session_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    start_time = Column(DateTime, default=datetime.utcnow)
    end_time = Column(DateTime)
    type = Column(String)  # pomodoro, break
    user = relationship('User')
