from abc import abstractmethod
class Musician:
    def __init__(self,name):
        self.name=name

    def __repr__(self) -> str:
        rep= self.__class__.__name__+" instance. Name = "+ str(self.name)
        return rep
    def get_instrument(self):
        return self.instrument 
    def __str__(self):
        return f"My name is {self.name} and I play {self.get_instrument()}"
    @abstractmethod
    def play_solo():
        pass


class Guitarist (Musician):
    instrument="guitar"
    def play_solo(self):
        return "face melting guitar solo"

class Bassist(Musician):
    instrument="bass"
    def play_solo(self):
        return "bom bom buh bom"

class Drummer (Musician):
    instrument="drums"
    def play_solo(self):
        return "rattle boom crash"


class Band(Musician):
    instances=[]
    def __init__(self,name,members):
        super().__init__(name)
        self.members=members
        Band.instances.append(self)

        
    def play_solos(self):
        newArr=[]
        for i in self.members:
            newArr.append(i.play_solo())
        return newArr
    def __repr__(self) -> str:
        return super().__repr__()
    def __str__(self) -> str:
        return super().__str__()
    @classmethod
    def to_list(cls):
        return cls.instances

