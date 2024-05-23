from sqlalchemy import create_engine, select, update, MetaData, Table, String, Integer, Column, Text, Date, Numeric, \
    func, insert, desc, delete
from datetime import date

from icecream import ic

import pandas as pd

ic.configureOutput(includeContext=True)
ic.configureOutput(prefix='DEBUG => ')

# Создание всех таблиц
metadata = MetaData()
engine = create_engine('sqlite:///bot_base.db')
engine.connect()

month_01_24 = Table('month_01_24', metadata,
                    Column('id', Integer(), primary_key=True),
                    Column('date', Date(), default=date.today(), nullable=True),
                    Column('debt', Numeric(10, 2), nullable=True),
                    Column('credit', Numeric(10, 2), nullable=True),
                    Column('section', String(30), nullable=True),
                    Column('description', Text(), nullable=True),
                    )
month_02_24 = Table('month_02_24', metadata,
                    Column('id', Integer(), primary_key=True),
                    Column('date', Date(), default=date.today(), nullable=True),
                    Column('debt', Numeric(10, 2), nullable=True),
                    Column('credit', Numeric(10, 2), nullable=True),
                    Column('section', String(30), nullable=True),
                    Column('description', Text(), nullable=True),
                    )
month_03_24 = Table('month_03_24', metadata,
                    Column('id', Integer(), primary_key=True),
                    Column('date', Date(), default=date.today(), nullable=True),
                    Column('debt', Numeric(10, 2), nullable=True),
                    Column('credit', Numeric(10, 2), nullable=True),
                    Column('section', String(30), nullable=True),
                    Column('description', Text(), nullable=True),
                    )
month_04_24 = Table('month_04_24', metadata,
                    Column('id', Integer(), primary_key=True),
                    Column('date', Date(), default=date.today(), nullable=True),
                    Column('debt', Numeric(10, 2), nullable=True),
                    Column('credit', Numeric(10, 2), nullable=True),
                    Column('section', String(30), nullable=True),
                    Column('description', Text(), nullable=True),
                    )
month_05_24 = Table('month_05_24', metadata,
                    Column('id', Integer(), primary_key=True),
                    Column('date', Date(), default=date.today(), nullable=True),
                    Column('debt', Numeric(10, 2), nullable=True),
                    Column('credit', Numeric(10, 2), nullable=True),
                    Column('section', String(30), nullable=True),
                    Column('description', Text(), nullable=True),
                    )
month_06_24 = Table('month_06_24', metadata,
                    Column('id', Integer(), primary_key=True),
                    Column('date', Date(), default=date.today(), nullable=True),
                    Column('debt', Numeric(10, 2), nullable=True),
                    Column('credit', Numeric(10, 2), nullable=True),
                    Column('section', String(30), nullable=True),
                    Column('description', Text(), nullable=True),
                    )
month_07_24 = Table('month_07_24', metadata,
                    Column('id', Integer(), primary_key=True),
                    Column('date', Date(), default=date.today(), nullable=True),
                    Column('debt', Numeric(10, 2), nullable=True),
                    Column('credit', Numeric(10, 2), nullable=True),
                    Column('section', String(30), nullable=True),
                    Column('description', Text(), nullable=True),
                    )
month_08_24 = Table('month_08_24', metadata,
                    Column('id', Integer(), primary_key=True),
                    Column('date', Date(), default=date.today(), nullable=True),
                    Column('debt', Numeric(10, 2), nullable=True),
                    Column('credit', Numeric(10, 2), nullable=True),
                    Column('section', String(30), nullable=True),
                    Column('description', Text(), nullable=True),
                    )
month_09_24 = Table('month_09_24', metadata,
                    Column('id', Integer(), primary_key=True),
                    Column('date', Date(), default=date.today(), nullable=True),
                    Column('debt', Numeric(10, 2), nullable=True),
                    Column('credit', Numeric(10, 2), nullable=True),
                    Column('section', String(30), nullable=True),
                    Column('description', Text(), nullable=True),
                    )
month_10_24 = Table('month_10_24', metadata,
                    Column('id', Integer(), primary_key=True),
                    Column('date', Date(), default=date.today(), nullable=True),
                    Column('debt', Numeric(10, 2), nullable=True),
                    Column('credit', Numeric(10, 2), nullable=True),
                    Column('section', String(30), nullable=True),
                    Column('description', Text(), nullable=True),
                    )
month_11_24 = Table('month_11_24', metadata,
                    Column('id', Integer(), primary_key=True),
                    Column('date', Date(), default=date.today(), nullable=True),
                    Column('debt', Numeric(10, 2), nullable=True),
                    Column('credit', Numeric(10, 2), nullable=True),
                    Column('section', String(30), nullable=True),
                    Column('description', Text(), nullable=True),
                    )
month_12_24 = Table('month_12_24', metadata,
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

# команда для запуска создания
# metadata.create_all(engine)

# определения теккущего месяца


last_month = date.today().month
ic(last_month)

dir_month = {
    1: month_01_24,
    2: month_02_24,
    3: month_03_24,
    4: month_04_24,
    5: month_05_24,
    6: month_06_24,
    7: month_07_24,
    8: month_08_24,
    9: month_09_24,
    10: month_10_24,
    11: month_11_24,
    12: month_12_24,
}


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

    # внесение даных в последний месяц
    def add_last_month(self, *args):
        data = self.conn.execute(insert(dir_month[last_month]), *args)
        self.conn.commit()
        return data.inserted_primary_key[0]

    # def add_data_last_of_month01(self, *args):
    #     print(*args)
    #     self.conn.execute(insert(month_04_24), *args)
    #     self.conn.commit()
    #     print('ok')
    #
    # def add_data01(self, data_class, **kwargs):
    #     ins = data_class.insert().values(**kwargs)
    #     conn = self.engine.connect()
    #     print(ins.compile().params)
    #     conn.execute(ins)
    #     conn.commit()
    #     print('ok')

    # def select_(self, data_class):
    #     # s = select(data_class)#data_class.select() #data_class.select(date)  # select([Fourth_month_24]) # data_class.select() #select([data_class])
    #     # print(data_class)
    #     # print(s)
    #     # conn = self.engine.connect()
    #     # r = conn.execute(s)
    #     # print(r.fetchall())
    #     # for row in s:
    #     #   print(row)
    #
    #     conn = engine.connect()
    #     s = select(data_class)
    #     r = conn.execute(s)
    #     print(r.fetchall())
    #
    # def select_last_of_month(self, data_class):
    #     s = select(data_class.c.id).order_by(desc(data_class.c.id))
    #     r = self.conn.execute(s)
    #     print(r.fetchone())

    def select_last_sum_section_of_debt(self, section_):
        s = select(func.sum(dir_month[last_month].c.debt)).where(dir_month[last_month].c.section == section_)
        r = self.conn.execute(s)
        return r.fetchone()[0]

    def select_last_sum_section_of_credit(self, section_):
        s = select(func.sum(dir_month[last_month].c.credit)).where(dir_month[last_month].c.section == section_)
        r = self.conn.execute(s)
        return r.fetchone()[0]

    def select_last_debt(self):
        s = select(func.sum(dir_month[last_month].c.debt))
        r = self.conn.execute(s)
        return int(r.fetchone()[0])

    def select_last_credit(self):
        s = select(func.sum(dir_month[last_month].c.credit))
        r = self.conn.execute(s)
        return int(r.fetchone()[0])

    # def select_annual_report_24_debt(self, month_number_: str):
    #     date_month = date(date.today().year, int(month_number_), 1)
    #     date_month_end = date(date.today().year, int(month_number_)+1, 1)
    #     s = select(annual_report_24.c.section, annual_report_24.c.debt).where((annual_report_24.c.date >= date_month) & (annual_report_24.c.date < date_month_end))
    #     r = self.conn.execute(s)
    #     return r.fetchall()

    def select_annual_report_24_debt(self, month_number_: str, section_):
        date_month = date(date.today().year, int(month_number_), 1)
        date_month_end = date(date.today().year, int(month_number_)+1, 1)
        s = select(func.sum(annual_report_24.c.debt)).where((annual_report_24.c.date >= date_month) & (annual_report_24.c.date < date_month_end) & (annual_report_24.c.section == section_))
        r = self.conn.execute(s)
        return r.fetchone()

    def select_annual_report_24_credit(self, month_number_: str, section_):
        date_month = date(date.today().year, int(month_number_), 1)
        date_month_end = date(date.today().year, int(month_number_)+1, 1)
        s = select(func.sum(annual_report_24.c.credit)).where((annual_report_24.c.date >= date_month) & (annual_report_24.c.date < date_month_end) & (annual_report_24.c.section == section_))
        r = self.conn.execute(s)
        return r.fetchone()

    # def select_annual_report_24_credit(self, month_number_: str):
    #     date_month = date(date.today().year, int(month_number_), 1)
    #     date_month_end = date(date.today().year, int(month_number_)+1, 1)
    #     s = select(annual_report_24.c.section, annual_report_24.c.credit).where((annual_report_24.c.date > date_month) & (annual_report_24.c.date < date_month_end))
    #     r = self.conn.execute(s)
    #     return r.fetchall()

    def select_annual_result_24(self, month_number_: str):
        s = select(annual_result_24).where(annual_result_24.c.date == date(date.today().year, int(month_number_), 1))
        r = self.conn.execute(s)
        return r.fetchone()

    def select_all_month_01_24(self):
        s = select(month_01_24)
        r = self.conn.execute(s)
        return r.fetchall()

    def select_all_month_02_24(self):
        s = select(month_02_24)
        r = self.conn.execute(s)
        return r.fetchall()

    def select_all_month_03_24(self):
        s = select(month_03_24)
        r = self.conn.execute(s)
        return r.fetchall()

    def select_all_month_04_24(self):
        s = select(month_04_24)
        r = self.conn.execute(s)
        return r.fetchall()

    def select_all_month_05_24(self):
        s = select(month_05_24)
        r = self.conn.execute(s)
        return r.fetchall()

    def select_all_month_06_24(self):
        s = select(month_06_24)
        r = self.conn.execute(s)
        return r.fetchall()

    def select_all_month_07_24(self):
        s = select(month_07_24)
        r = self.conn.execute(s)
        return r.fetchall()

    def select_all_month_08_24(self):
        s = select(month_08_24)
        r = self.conn.execute(s)
        return r.fetchall()

    def select_all_month_09_24(self):
        s = select(month_09_24)
        r = self.conn.execute(s)
        return r.fetchall()

    def select_all_month_10_24(self):
        s = select(month_10_24)
        r = self.conn.execute(s)
        return r.fetchall()

    def select_all_month_11_24(self):
        s = select(month_11_24)
        r = self.conn.execute(s)
        return r.fetchall()

    def select_all_month_12_24(self):
        s = select(month_12_24)
        r = self.conn.execute(s)
        return r.fetchall()

    def select_all_annual_report_24(self):
        s = select(annual_report_24)
        r = self.conn.execute(s)
        return r.fetchall()

    def select_all_annual_result_24(self):
        s = select(annual_result_24)
        r = self.conn.execute(s)
        return r.fetchall()

    def delete_last_month(self, id_):
        d = delete(dir_month[last_month]).where(dir_month[last_month].c.id == id_)
        self.conn.execute(d)
        self.conn.commit()
        # ic(id_)


        # print(r.fetchone())

    # def delete_last_month01(self, data_class):
    #     s = select(data_class.c.id).order_by(desc(data_class.c.id))
    #     r = self.conn.execute(s)
    #     id_ = r.fetchone()[0]
    #     print(id_, "qqqq")
    #
    #     d = delete(month_04_24).where(month_04_24.c.id == id_)
    #     self.conn.execute(d)
    #     self.conn.commit()
    #     # print(r.fetchone())
    def update_last_of_month(self, id_, *args):
        action = update(dir_month[last_month]).where(dir_month[last_month].c.id == id_).values(*args)
        self.conn.execute(action)
        self.conn.commit()

    # def update_last_of_month(self, id_, *args):
    #     action = update(month_04_24).where(
    #         month_04_24.c.id == id_
    #     ).values(*args)
    #
    #     print('update :', action)
    #     self.conn.execute(action)
    #     self.conn.commit()


sqlbot = SqlAlchemy('bot_base.db')
dir = {'debt': '999', 'section': 'молоко', 'description': 'fddsf'}
dir2 = {'debt': '10', 'section': 'хозтовары', 'description': 'за привозку'}

#ic(sqlbot.add_last_month(dir2))

#sqlbot.add_data_last_of_month01(dir)
#sqlbot.delete_last_of_month(month_04_24)
# sqlbot.delete_last_month(15)

list_debt = ['мясо', 'молоко', 'техника',   "хозтовары"]
# for i in list_debt:
    # ic(sqlbot.select_annual_report_24_debt('04', i))

list_credit = ['хозтовары', 'молоко', 'техника', 'зарплата', ]
# for i in list_credit:
#     ic(sqlbot.select_annual_report_24_credit('04', i))
    # ic(sqlbot.select_last_sum_section_of_credit(i))
# ic(sqlbot.select_last_debt())
# ic(sqlbot.select_last_credit())
# ic(sqlbot.select_last_debt() - sqlbot.select_last_credit())

# ic(sqlbot.select_all_month_05_24()[0])

# df = pd.read_sql(sql, sqlbot.select_all_month_05_24())
# item = [i[0] for i in sqlbot.select_all_month_05_24()]
# ic(item)

# Установка индекса из столбца 'id'   Устанавливая параметр inplace=True, мы изменяем исходный dataframe с новым индексом.
# df.set_index('id', inplace=True)

# df.to_excel('excel01.xlsx', sheet_name='Total')

# # Создаем эксель файл
# writer = pd.ExcelWriter('excel01.xlsx')
#
# # Записываем датафреймы в разные листы
# df.to_excel(writer, sheet_name='Лист1', index=False)
# df.to_excel(writer, sheet_name='Лист2', index=False)
#
# # Сохраняем файл
# writer._save()
dataframe_01 = pd.DataFrame(sqlbot.select_all_month_01_24())
dataframe_02 = pd.DataFrame(sqlbot.select_all_month_02_24())
dataframe_03 = pd.DataFrame(sqlbot.select_all_month_03_24())
dataframe_04 = pd.DataFrame(sqlbot.select_all_month_04_24())
dataframe_05 = pd.DataFrame(sqlbot.select_all_month_05_24())
dataframe_06 = pd.DataFrame(sqlbot.select_all_month_06_24())
dataframe_07 = pd.DataFrame(sqlbot.select_all_month_07_24())
dataframe_08 = pd.DataFrame(sqlbot.select_all_month_08_24())
dataframe_09 = pd.DataFrame(sqlbot.select_all_month_09_24())
dataframe_10 = pd.DataFrame(sqlbot.select_all_month_10_24())
dataframe_11 = pd.DataFrame(sqlbot.select_all_month_11_24())
dataframe_12 = pd.DataFrame(sqlbot.select_all_month_12_24())
dataframe_annual_report = pd.DataFrame(sqlbot.select_all_annual_report_24())
dataframe_annual_result = pd.DataFrame(sqlbot.select_all_annual_result_24())


def create_excelfile():
    # Создаем эксель файл
    with pd.ExcelWriter('result_year_24.xlsx',
            engine="xlsxwriter",
            mode='w') as writer:

        # Записываем датафреймы в разные листы
        dataframe_01.to_excel(writer, sheet_name="01", index=False)
        dataframe_02.to_excel(writer, sheet_name="02", index=False)
        dataframe_03.to_excel(writer, sheet_name="03", index=False)
        dataframe_04.to_excel(writer, sheet_name="04", index=False)
        dataframe_05.to_excel(writer, sheet_name="05", index=False)
        dataframe_06.to_excel(writer, sheet_name="06", index=False)
        dataframe_07.to_excel(writer, sheet_name="07", index=False)
        dataframe_08.to_excel(writer, sheet_name="08", index=False)
        dataframe_09.to_excel(writer, sheet_name="09", index=False)
        dataframe_10.to_excel(writer, sheet_name="10", index=False)
        dataframe_11.to_excel(writer, sheet_name="11", index=False)
        dataframe_12.to_excel(writer, sheet_name="12", index=False)
        dataframe_annual_report.to_excel(writer, sheet_name="Год. отчет", index=False)
        dataframe_annual_result.to_excel(writer, sheet_name="Год. результат", index=False)

        # Сохраняем файл
        # writer._save()


create_excelfile()
# sqlbot.select_(dir_month[last_month])
# ic(sqlbot.select_annual_report_24_debt('04', 'молоко'))

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

# print(month_04_24.c.section)
#
# conn = engine.connect()
#
# # s = select(month_04_24).order_by
# # s = select(month_04_24).where(month_04_24.c.id > 0)
# s = select(month_04_24).order_by(desc(month_04_24.c.id))
# r = conn.execute(s)
# print(r.fetchone())
