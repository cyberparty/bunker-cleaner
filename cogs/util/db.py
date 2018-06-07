import aiomysql

"""
SQL Database Driver.
It's just as painful for me as it is for you.
"""

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
