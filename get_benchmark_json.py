from pymongo import MongoClient
import argparse
import pprint
import json
from bson.objectid import ObjectId
import re
'''
client = MongoClient('mongodb://qaubd1:27017')
db = client.prf
collection = db.builds
a = collection.find().limit(1)
for i in a:
   print(i)
'''

def getMongodb():
    client = MongoClient('mongodb://qaubd1:27017')
    db = client.prf
    return db

def getMongoConnections(connection):
    db = getMongodb()
    conn = ''
    if connection == 'builds':
        conn = db.builds
    elif connection == 'benchmarks':
        conn = db.benchmarks
    elif connection == 'results':
        conn = db.results

    return conn

def getBuilds(buildId):
    conn = getMongoConnections('builds')
    try:
        results = conn.find({'_id': buildId, 'name': {'$regex': '(?i)(.*)zvm\-dev(.*)'}}, {'name': 1}).limit(1)
    except:
        pass
    return results

def getBmarkID(bgroup, bname=None):
    conn = getMongoConnections('benchmarks')
    try:
        if bname is not None:
            results = conn.find({'bmark_group': {'$regex': '(?i)(.*)' + (bgroup) + '(.*)'},
                             'bmark_name': {'$regex': '(?i)(.*)' + (bname) + '(.*)'}},
                            {'_id': 1, 'bmark_group': 1, 'bmark_name': 1})
        elif bname is None and bgroup is not None:
            results = conn.find({'bmark_group': {'$regex': '(?i)(.*)' + (bgroup) + '(.*)'}},
                                {'_id': 1, 'bmark_group': 1, 'bmark_name': 1})
        else:
            results = conn.find({},{'_id': 1, 'bmark_group': 1, 'bmark_name': 1})
    except:
        pass

    return results

def getResult(bmarkId, limit):
    conn = getMongoConnections('results')
    try:
        results = conn.find({'bmark_id': bmarkId}).limit(limit).sort([('t_stamp', -1)])
    except:
        pass
    return results

# def main(bgroup="stashing", bname="tradebeans", limit=10):
def main(bgroup="Hybrid-lite_Benchmarks", bname='MyBenchMark', limit=3):
# def main(bgroup="Datomic_Benchmark", bname=None, limit=5):
# def main(bgroup="Chronicle_Wire", bname=None, limit=3):
# def main(bgroup=None, bname=None, limit=3):
    regression = {}
    regressions = []
    a = []

    argparser = argparse.ArgumentParser()
    argparser.add_argument('--bgroup', type=str, default=bgroup)
    argparser.add_argument('--bname', type=str, default=bname)
    argparser.add_argument('--limit', type=int, default=limit)
    args = argparser.parse_args()

    bmarkId = getBmarkID(args.bgroup, args.bname)
    for id in bmarkId:
        print(id['bmark_name'])
        results = getResult(id['_id'], args.limit)
        for result in results:
            buildName =''
            build = getBuilds(result['build_id'])
            buildresult = []
            for buildN in build:
                for i, j in result['results'].items():
                    buildresult.append({i:j})
                    buildName = buildN["name"]
            regression[buildName] = (buildresult)
            header = f'{id["bmark_group"]}|{id["bmark_name"]}'
        regressions.append({header:regression})
        # regressions.append({id['bmark_group']: {id['bmark_name']: regression}})
        # print(regression)
    # pprint.pprint(regressions)
    return (regressions)

if __name__ == '__main__':
    regressions = main()
    pprint.pprint(regressions)
    with open('regressions.json', 'w') as outfile:
        json.dump(regressions, outfile)



