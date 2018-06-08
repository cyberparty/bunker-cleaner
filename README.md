## bunker-cleaner
Just a bot tailored towards the needs of the BUNKER server's users.

**Current features:**
* Quotation system:
    * `!grab [user]`: Grabs last message of specified user and stores it. If no user is specified, it will grab the most recent message.
    * `!quote [user]`: Sends the last grabbed quote of the specified user.
    * `!list [user]`: Lists all the quotes the specified user has, and each quote's ID.
    * `!say [quote id]`: Says the quote with the specified quote ID, which can be found out using `!list`.
    * `!ungrab [quote id]`: Removes specified quote from database.
    * `!random`: Sends a random quote of all the stored quotes.
* Facts:
    * `!cat`: Gives you a random cat fact.
    * `!shark`: Gives you a random shark fact.
* Role colour:
    * `!col [colour]`: Creates and assigns a role to the sender based on a hex colour value they provide
        * Requires bot to have role management permissions, and to possess a role higher than the assignee.
* Admin:
    * `!sql [sql]`: Execute SQL command to interact with the bot's database via Discord.
    * `!reload_cfg`: Reload config file.
* Misc:
    * `!herken`: Displays a relic of a long-lost civilization. 
    * `!barney`: Reminds you who your god is.
    * `!ready`: I have no idea.

**Requires:**
* [Python 3.6+](https://www.python.org/downloads/release/python-360/)
* discord.py rewrite
	* `python3 -m pip install -U git+https://github.com/Rapptz/discord.py@rewrite#egg=discord.py[voice]`
* aiomysql
	* `python3 -m pip install aiomysql`
	* PyMySQL is a dependency of aiomysql, but the above command should automatically install it alongside aiomysql.
* MySQL Server

**Running the bot:**
1. Download files into a directory.
2. Place your bot token into the "Token" field in cfg/cfg.json
3. Run the SQL script. (docs/db.sql)
	* This script will create a database labeled 'bunkerbot' on localhost unless otherwise defined in cfg/cfg.json. **If you modify the database name, make sure the name defined in db.sql reflects this change, otherwise the bot will not be able to locate the database.**
4. Invite your bot to the server.
5. Run main.py

**Issues:**
If you find any bugs or issues, please submit them on this repo for us to ignore.
