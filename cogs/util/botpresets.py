"""
botpresets.py
Provides extra interfaces for the 'Bot' class when initialised in 'main.py'
Config is loaded here and database is called from this class.

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
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from discord.ext import commands
from cogs.util.db import DBConn
from json import load

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

    def reload_cfg(self):
        try:
            self.cfg = load_cfg()
            return True
        except:
            return False

    def run_with_token(self):
        token = self.cfg["Token"]
        self.run(token)
