#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3

conn = sqlite3.connect("test.db")

cursor = conn.cursor()

try:
    # 创建一个表
    # cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')

    # 插入数据
    # cursor.execute('insert into user (id, name) values ("1", "wanghx")')

    cursor.execute('select * from user where id=?', '1')

    value = cursor.fetchall()

    print(value)

    print(cursor.rowcount)
except Exception as e:
    print('Error',e)
finally:
    # 要保证指针和链接要关闭
    cursor.close()
    # 只要提交了事务，插入语句才会生效
    # conn.commit()
    conn.close()
