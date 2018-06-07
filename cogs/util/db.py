"""
db.py
SQL Database Driver.
It's just as painful for me as it is for you.

Copyright (C) 2018 Joseph Cole <jc@cyberparty.me>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
"""

import aiomysql


class DBConn(object):

    config = None

    def __init__(self):
        self.db = None
        self.cur = None

    async def __aenter__(self):
        self.db = await self.get_db_conn()
        self.cur = await self.db.cursor(aiomysql.DictCursor)
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.cur.close()
        self.db.close()

    async def get_db_conn(self):
        conn = await aiomysql.connect(**DBConn.config)
        return conn

    async def __call__(self, sql:str, data):
        await self.cur.execute(sql, data)
        await self.db.commit()
        r = await self.cur.fetchall()

        if r:
            return r
        else:
            return None
