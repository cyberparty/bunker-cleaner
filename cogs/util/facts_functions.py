
def fact_spew(fileName, fileEncoding):
    factFile = open(str(fileName), "r", encoding=fileEncoding)
    facts = factFile.read().splitlines()
    factFile.close()
    return facts
