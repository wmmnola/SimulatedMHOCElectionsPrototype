__author__ = 'Wade'

import random
import math

def distFrom(p1,p2):
    return math.sqrt(((p1.x-p2.x)**2)+((p1.y-p2.y)**2)+((p1.z-p2.z)**2))

class Point(object):
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z



class Voter(object):
    def __init__(self,economics,social,democracy):
        self.Democracy = democracy
        self.Economics = economics
        self.Social = social
        self.mypoint = Point(economics,social,democracy)

    def vote(self,parties):
        points = {}
        distances = {}
        for x in parties:
            points[x] = Point(parties[x][0],parties[x][0],parties[x][0])
        for i in points:
            distances[i] = distFrom(self.mypoint,points[i])
        keys = list(distances.keys())
        values = list(distances.values())


        minimum =  min(float(s) for s in values)
        return keys[values.index(minimum)]








voters = []
parties = {"Right":[0,0,0],"Center":[50,50,50],"Left":[100,100,100]}
print("The Right's Party Score %s" % (parties["Right"][0]))
for x in range(0,1000):
    dem = random.randint(0,100)
    soc = random.randint(0,100)
    econ = random.randint(0,100)
    voters.append(Voter(econ,soc,dem))
votes = []
Tallied = {}
for x in voters:
    votes.append(x.vote(parties))
for x in parties:
    Tallied[x] = votes.count(x)
print("Votes: ")
print(Tallied)


