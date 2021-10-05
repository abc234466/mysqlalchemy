from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('sqlite:///:memory:', echo=True)  # Lazy connecting


Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    nickname = Column(String)
    fullname = Column(String)
    createdAt = Column(DateTime)
    updatedAt = Column(DateTime)

    def __repr__(self) -> str:
        return f"<User(name='{self.name}', fullname='{self.fullname}'," \
                " nickname='{self.nickname}')>"


Base.metadata.create_all(engine)

user = User(name='xian', fullname='xian C.', nickname='cookie')

Session = sessionmaker(bind=engine)
session = Session()
session.add(user)

# auto flush magic!
# <User(name='xian', fullname='xian C.', nickname='{self.nickname}')>
print(session.query(User).filter_by(name='xian2').first())
query_user = session.query(User).filter_by(name='xian').first()


# If change the name, then call session.dirty
query_user.name = 'xian_C'
print(session.dirty)
"""
IdentitySet([<User(name='xian_C', fullname='xian C.',
             nickname='{self.nickname}')>])
"""

# We can add multiple data at the same time, then call session.new
session.add_all([
    User(name='willy', fullname='willy B.', nickname='will'),
    User(name='lisa', fullname='lisa A.', nickname='li'),
])


print(session.new)
"""
IdentitySet(
    [<User(name='willy', fullname='willy B.', nickname='{self.nickname}')>,
     <User(name='lisa', fullname='lisa A.', nickname='{self.nickname}')>]
)
"""
