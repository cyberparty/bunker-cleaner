from discord.ext import commands
from cogs.util.db import DBConn
from json import load

"""
Provides extra interfaces for the 'Bot' class when initialised in 'main.py'
Config is loaded here and database is called from this class.
"""

cfg_file = "./cfg/cfg.json"


def load_cfg():
    with open(cfg_file) as f:
        return load(f)


class CBot(commands.AutoShardedBot):

    def __init__(self, **kwargs):
        self.cfg = load_cfg()
        super().__init__(command_prefix=self.get_cfg_pref(),
                         description=self.get_cfg_des(),
                         **kwargs)
        self.db = DBConn
        DBConn.config = self.cfg["Database"]

    def get_cfg_pref(self):
        return self.cfg["Attributes"]["Prefix"]

    def get_cfg_des(self):
        return self.cfg["Attributes"]["Description"]

    def run_with_token(self):
        token = self.cfg["Token"]
        self.run(token)
