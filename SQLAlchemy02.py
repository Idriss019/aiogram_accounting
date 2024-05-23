from sqlalchemy import create_engine, select, update, MetaData, Table, String, Integer, Column, Text, Date, Numeric, func, insert, desc, delete
from datetime import date

metadata = MetaData()
# Column('debt_credit', Boolean(), default=False, nullable=False),
engine = create_engine('sqlite:///bot_base.db')
engine.connect()

last_month = date.today().month
print("last_month :", last_month)

month_04_24 = Table('month_04_24', metadata,
                    Column('id', Integer(), primary_key=True),
                    Column('date', Date(), default=date.today(), nullable=True),
                    Column('debt', Numeric(10, 2), nullable=True),
                    Column('credit', Numeric(10, 2), nullable=True),
                    Column('section', String(30), nullable=True),
                    Column('description', Text(), nullable=True),
                    )

annual_report_24 = Table('annual_report_24', metadata,
                         Column('id', Integer(), primary_key=True),
                         Column('date', Date(), nullable=False),
                         Column('debt', Numeric(10, 2), nullable=True),
                         Column('credit', Numeric(10, 2), nullable=True),
                         Column('section', String(30), nullable=True),
                         )

annual_result_24 = Table('annual_result_24', metadata,
                         Column('id', Integer(), primary_key=True),
                         Column('date', Date(), nullable=False),
                         Column('debt', Numeric(10, 2), nullable=True),
                         Column('credit', Numeric(10, 2), nullable=True),
                         Column('total', Numeric(10, 2), nullable=True),
                         )

# Создание всех таблиц
# metadata.create_all(engine)

from sqlalchemy.orm import Session, sessionmaker
engine = create_engine("sqlite:///bot_base.db")
# Session = sessionmaker(bind=engine)
# session = Session()
#
# # session = Session()
# # session = sessionmaker(bind=engine)
# #session = Session(bind=engine)
#
# engine.connect()




class SqlAlchemy:
    # def __init__(self, path):
    #  self.engine = sessionmaker(bind=create_engine('sqlite:///%s' % path))
    # self.engine = Session()
    #  self.session = self.engine()

    def __init__(self, path):
        self.engine = create_engine('sqlite:///%s' % path)
        # self.engine = Session()
        # self.session = Session(bind=self.engine)
        self.conn = self.engine.connect()

    # def add_data(self, data_class):
    #   self.session.add(data_class)
    #   self.session.commit()

    # def add_data(self, data_class, **kwargs):
    #   ins = 
    #   self.engine.connect().execute(data_class.insert().values(**kwargs))
    #   self.session.commit()

    def add_data_last_of_month(self, *args):
        print(*args)
        self.conn.execute(insert(month_04_24), *args)
        self.conn.commit()
        print('ok')

    def add_data01(self, data_class, **kwargs):
        ins = data_class.insert().values(**kwargs)
        conn = self.engine.connect()
        print(ins.compile().params)
        conn.execute(ins)
        conn.commit()
        print('ok')

    def select_(self, data_class):
        # s = select(data_class)#data_class.select() #data_class.select(date)  # select([Fourth_month_24]) # data_class.select() #select([data_class])
        # print(data_class)
        # print(s)
        # conn = self.engine.connect()
        # r = conn.execute(s)
        # print(r.fetchall())
        # for row in s:
        #   print(row)
        conn = engine.connect()
        s = select(data_class)
        r = conn.execute(s)
        print(r.fetchall())

    def select_last_of_month(self, data_class):
        s = select(data_class.c.id).order_by(desc(data_class.c.id))
        r = self.conn.execute(s)
        print(r.fetchone())

    def delete_last_of_month(self, data_class):
        s = select(data_class.c.id).order_by(desc(data_class.c.id))
        r = self.conn.execute(s)
        id_ = r.fetchone()[0]
        print(id_, "qqqq")

        d = delete(month_04_24).where(month_04_24.c.id == id_)
        self.conn.execute(d)
        self.conn.commit()
        # print(r.fetchone())

    def update_last_of_month(self, id_, *args):
        action = update(month_04_24).where(
            month_04_24.c.id == id_
        ).values(*args)

        print('update :', action)
        self.conn.execute(action)
        self.conn.commit()

sqlbot = SqlAlchemy('bot_base.db')
dir = {'debt': '999', 'section': 'молоко', 'description': 'fddsf'}
dir2 = {'debt': '10', 'section': 'хозтовары', 'description': 'за привозку'}
# sqlbot.add_data_in_month(dir)

# sqlbot.delete_last_of_month(month_04_24)
dir_month = {
    '01': None,
    '02': None,
    '03': None,
    5: month_04_24

}
sqlbot.select_(dir_month[last_month])
# sqlbot.update_last_of_month(5, dir2)
# sqlbot.select_(Month_04_24)
# conn = engine.connect()
# s = select(['month_04_24'])
# r = conn.execute(s)
# print(r)

# for user in session.query(Month_04_24):
#     print(user.id)

# for row in r:
#     print(row)
# sqlbot.select_last_of_month(Month_04_24)
# a = Annual_result_24(date='09.09.2024', 
#                                  debt=99, 
#                                  credit=11, 
#                                  total=44)

# sqlbot.add_data(Month_04_24, class_='dfdfd',  obj1, obj2 = Sensors.query.order_by(Sensors.id.desc()).limit(2)
#                                   description="vbvbv",
#                                   # date=date.today(),
#                                   debt=100,
#                                   credit=111,
#                                   )

# sqlbot.select_(Month_04_24.Column)
# print(select(Month_04_24))

# s = select(Month_04_24).where(
#     Month_04_24.c.id == 3)

# conn = engine.connect()

# r = conn.execute(s).fetchall()
# print(r)

# s = select(Month_04_24)
# r = conn.execute(s)
# print(r.first())

# for row in r:
#     print(row)
# print(s)
# Внесение данных
# Фильрация данных
# Обновление даных
# Показ данных
# Удаление данныхTable


# from sqlalchemy.orm import declarative_base

# Base = declarative_base()

# class Annual_report01(Base):
#     __tablename__ = 'annual_report01'

#     id = Column(Integer, primary_key=True)
#     date = Column(String)
#     debt = Column(Integer)
#     credit = Column(Integer)
#     total = Column(Integer)

# session.add(Annual_report(date='40.04.2024', debt=35, credit=15, total=10,))
# session.commit()

# ins = Fourth_month_24.insert().values(class_='fffff',
#                                   description="asad",
#                                   date=date.today(), 
#                                   debt=99, 
#                                   credit=11, 
#                                   )

# conn = engine.connect()
# print(conn)
# conn.execute(ins)
# r = conn.execute(ins)
# print(session.commit())
# print(r.inserted_primary_key)
# conn.commit()

# conn = engine.connect()
#
# s = select([Month_04_24])
# r = conn.execute(s)
# print(r)


# Функция суммирования!!
# print(session.query(func.sum(Month_04_24.c.debt)).scalar())


# users = session.query(month_04_24).all()
#
# for user in users:
#     print(user.date, user.debt, user.credit, user.class_, user.description)

print(month_04_24.c.section)

conn = engine.connect()

# s = select(month_04_24).order_by
# s = select(month_04_24).where(month_04_24.c.id > 0)
s = select(month_04_24).order_by(desc(month_04_24.c.id))
r = conn.execute(s)
# print(r.fetchone())

print("dfdsgfdgd")