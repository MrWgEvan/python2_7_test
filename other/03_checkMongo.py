# coding:utf-8

import codecs,pymongo


class checkMongo():


    def checkOut(self,host,port,dbName,collectionName,fileName):
        host = host
        port = port
        dbName = dbName
        collectionName = collectionName
        c2 = pymongo.MongoClient(host=host, port=port)
        db = c2[dbName]
        db_collection = db[collectionName]
        text = db_collection.find({})
        with codecs.open(ur'{}.txt'.format(fileName), 'wb', encoding='utf-8') as f:
            for item in text:
                f.write(item['title']+ '\n')
                f.write(item['content'] + '\n')




    def main_check(self):
        host = "127.0.0.1"
        port = 27017
        dbName = "biquge"
        collectionName = "shengxu"
        fileName = u"圣墟"
        self.checkOut(host,port,dbName,collectionName,fileName)
        print ("写出完成！！！")


if __name__ == '__main__':
    c = checkMongo()
    c.main_check()