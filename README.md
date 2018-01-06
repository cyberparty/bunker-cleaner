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
* Misc:
    * `!herken`: Displays a relic of a long-lost civilization. 
    * `!barney`: Reminds you who your god is.

**Requires:**
* [Python 3.6](https://www.python.org/downloads/release/python-360/)
* discord.py rewrite
	* `python3 -m pip install -U git+https://github.com/Rapptz/discord.py@rewrite#egg=discord.py[voice]`

**Running the bot:**
1. Download files into a directory.
2. Create a file called "key.txt" and put your bot key into it.
3. Invite your bot to the server.
4. Run main.py

**Issues:**
If you find any bugs or issues, please submit them on this repo for us to ignore.
