import json

#JsonDB driver. Implements quote management functionality, and loading and saving to disk
class JsonDB:

    #Constructor
    def __init__(self,filename):
        self.filename=filename
        #Try to read the existing file
        try:
            file=open(self.filename,"r")
            self.js=json.load(file)
        #If that fails, try creating a new empty one, without overwriting the old one
        except Exception:
            with open(self.filename,"x") as new_file:
                self.js={"users":{},"count":0,"nextID":0}
                json.dump(self.js,new_file)
        finally:
            file.close()

    #Save the current database into disk
    def save(self):
        with open(self.filename,"w") as file:
            json.dump(self.js,file)

    #Get an user from the database, can create it if it doesn't exist
    def get_user(self,userID,createIfNeeded=False):
        userID=str(userID)
        
        if createIfNeeded and userID not in self.js["users"]:
            self.js["users"][userID]=[]
        try:
            return self.js["users"][userID]
        except Exception:
            return None
        
    #Get a valid ID, and increment it
    def get_new_ID(self):
        return self.js["nextID"]

    #Update internal counters, for a new inserted quote
    def update_quote_created(self):
        self.js["nextID"]+=1
        self.js["count"]+=1

    #Update internal counters, for an existing quote deleted
    def update_quote_deleted(self):
        self.js["count"]-=1
        
    
    #Add a quote to an user
    def add_quote(self,text,userID):
        user=self.get_user(userID,True)
        quoteID=str(self.get_new_ID())

        user.insert(0,{"ID":quoteID,"text":text})
        self.update_quote_created()
        self.save()

    #Get a quote from an user, given its index (default is most recent one)
    def get_quote_user_index(self,userID,index=0):
        userID=str(userID)

        user=self.get_user(userID)
        if user is not None:
            try:
                return user[index]
            except Exception:
                pass
        return None

    #Get a quote from the db, given its ID
    def get_quote_ID(self,quoteID):
        for user_quotes in self.js["users"].values():
            for quote in user_quotes:
                if quote["ID"]==quoteID:
                    return quote
        return None

    #Remove a quote by ID, return the deleted quote (None if not found)
    def remove_quote_ID(self,quoteID):
        for user_quotes in self.js["users"].values():
            for (index,quote) in enumerate(user_quotes):
                if quote["ID"]==quoteID:
                    rv=quote
                    del user_quotes[index]
                    self.update_quote_deleted()
                    self.save()
                    return rv
        return None
