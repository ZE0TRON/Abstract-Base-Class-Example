from abc import ABCMeta, abstractmethod
class SocialProfile():
    __metaclass__=ABCMeta

    @abstractmethod
    def followedby_number(self):
        nothing=0
        #Need to have a func in that name to become a child class of this class
    @abstractmethod
    def follow_number(self):
        nothing=0
    @abstractmethod
    def follow(self,other):
        #yeah same shit
        nothing=0
    @abstractmethod
    def followed(self,other):
        #same shit
        nothing=0
    def __init__(self,name,sname,age,followedBy=[],youFollow=[]):
        self._name=name
        self._sname=sname
        self._age=age
        self._followedBy=followedBy
        self._youFollow=youFollow
    def get_name(self):
        return self._name
    def get_sname(self):
        return self._sname
    def get_age(self):
        return self._age
class Facebook(SocialProfile):
    def __init__(self,name,sname,age,school,followedBy=[],youFollow=[],lastPostLike=0,numberPhotos=0):
        super(Facebook,self).__init__(name,sname,age,followedBy,youFollow)
        self._school=school
        self._lastPostLike=lastPostLike
        self._numberPhotos=numberPhotos
    def followedby_number(self):
        return len(self._followedBy)
    def follow_number(self):
        return len(self._youFollow)
    def follow(self,other):
        self._youFollow.append(other.get_name()+" "+other.get_sname()+" ")
        other.followed(self)
    def followed(self,other):
        print self.get_name()
        self._followedBy.append(other.get_name()+" "+other.get_sname()+" ")
    def print_friendship(self):
        print self._youFollow
        print self._followedBy
class HackerRank(SocialProfile):
    def __init__(self,name,sname,age,school,rank,followedBy=[],youFollow=[],lastSubPoint=0):
        super(HackerRank,self).__init__(name,sname,age,followedBy,youFollow)
        self._school=school
        self._lastSubPoint=lastSubPoint
        self._rank=rank
    def followedby_number(self):
        return len(self._followedBy)
    def follow_number(self):
        return len(self._youFollow)
    def follow(self,other):
        self._youFollow.append(other.get_name()+" "+other.get_sname()+" ")
        other.followed(self)
    def followed(self,other):
        self._followedBy.append(other.get_name()+" "+other.get_sname()+" ")
    def submit(self,score):
        if(self._lastSubPoint<score):
            self._rank-=1
        elif(self._lastSubPoint==score):
            self._rank=self._rank
        else:
            self._rank+=1
        self._lastSubPoint=score
    def get_rank(self):
        return self._rank
    def print_friendship(self):
        print self._youFollow
        print self._followedBy
#############################################################
bilge=HackerRank("Bilge","Cimen",18,"Hacettepe University",10)
bugra=Facebook("Bugra","Tuncer",18,"Hacettepe University")
emir=HackerRank("Emir","Ilhan",20,"Hacettepe University",9)
koray=Facebook("Koray","Ikiz",18,"Hacettepe University")
bilge.follow(emir)
bugra.follow(koray)
emir.follow(bilge)
koray.follow(bugra)
bilge.submit(1)
bilge.submit(5)
bilge.submit(4)
bilge.submit(5)
print bilge.follow_number()
print bilge.followedby_number()
print bugra.follow_number()
print bugra.followedby_number()
print bilge.get_rank()
bilge.print_friendship()
bugra.print_friendship()
koray.print_friendship()
