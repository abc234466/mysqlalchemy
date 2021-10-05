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

# import ipdb; ipdb.set_trace()
Session = sessionmaker(bind=engine)
session = Session()
session.add(user)

# auto flush magic!
# <User(name='xian', fullname='xian C.', nickname='{self.nickname}')>
print(session.query(User).filter_by(name='xian').first())

