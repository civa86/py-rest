from sqlalchemy import Column, Integer, String, Boolean, DateTime
from services.database import Base


class Todo(Base):
    __tablename__ = 'todo'
    id = Column(Integer, primary_key=True)
    task = Column(String(255))
    done = Column(Boolean())
    created_at = Column(DateTime())

    def __init__(self, task=None, done=False):
        self.task = task
        self.done = done

    def __repr__(self):
        return '<Todo #ID: %r>' % (self.id)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'task': self.task,
            'done': self.done,
            'created_at': self.created_at
        }
