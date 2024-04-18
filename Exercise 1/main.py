# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


#Check a single document against an existing collection of previsouly seen documents for exact duplicates.
def check_exct(doc, docs):
    docHash = hash(doc[1])
    for x in docs:
        if hash(x[1]) == docHash:
            return True
    return False

#Check a single document against an existing collection of previsouly seen documents for near duplicates
def check_simhash(doc, docs):
    #TODO: Implement near duplicate detection
    return False #TODO: Return True if the document is a duplicate

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    crawl = [['D1', 'This is just some document'], ['D2', 'This is another piece of text'],
             ['D3', 'This is another piece of text'], ['D4', 'This is just some documents'],
             ['D5', 'Totally different stuff']]


    # Process raw crawled website content
    def process(crawl):
        docs = []
        for doc in crawl:
            if check_exct(doc, docs):  # Can be exchanged for check_simhash()
                print('DUPLICATE: ' + doc[0])
            else:
                docs.append(doc)


    process(crawl)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
