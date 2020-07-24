############ SEARCHARR ############

c = SearchArrCtx_class()
c.checkedInit(PyRel({(1,70),(2,60),(3,10),(4,30),(5,40),(6,20),(7,50),(8,90),(9,80)}),9,PySet({int_range for int_range in range(1, 101)}))
m = SearchArrMch_class(c)




############ SEARCHMAT ############ (mypy: PyRel)

c = SearchMatCtx_class()
c.checkedInit(PyRel({((1,1),104),((1,2),102),((1,3),115),((1,4),112),((2,1),106),((2,2),107),((2,3),105),((2,4),111),((3,1),109),((3,2),113),((3,3),110),((3,4),108),((4,1),103),((4,2),114),((4,3),101),((4,4),116)}),4,4,PySet({int_range for int_range in range(101, 116+1)}))
m = SearchMatMch_class(c)




############ COMMONNUMBER ############

P.setUSE_FINITE_SPECIAL_SETS(True)
c = CommonNumberCtx_class()
c.checkedInit(PyRel({(1,10),(2,20),(3,30),(4,40),(5,50),(6,60),(7,70),(8,80),(9,90)}),PyRel({(1,15),(2,25),(3,35),(4,70),(5,73),(6,75),(7,77),(8,85),(9,95)}),9,9)
m = CommonNumberMch_class(c)




############ ARRPART ############

c = ArrPartCtx_class()
c.checkedInit(10,5)
m = ArrPartMch_class(c)
# [4,10,7,1,6,8,9,3,5,2]
# [4,2,5,1,3,8,9,6,7,10] <== 5




############ SORTING ############

P.setUSE_FINITE_SPECIAL_SETS(True)
c = SortingCtx_class()
c.checkedInit(10)
m = SortingMch_class(c)
# [79, 34, 88, 13, 10, 40, 96, 14, 70, 39]
# [10, 13, 14, 34, 39, 40, 70, 79, 88, 96]




############ CAFETERIA ############

c = CafeteriaCtx_class()
c.checkedInit(99)
m = CafeteriaMch_class(c)
###
c = CafeteriaCtx_class()
c.checkedInit(99)
ce = CafeteriaCtxExt_class()
ce.checkedInit(c,1,0,0,1)
m = CafeteriaMchRef_class(ce)




############ HOSPITAL ############

c = HospitalCtx_class() ### Available Unavailable
c.checkedInit(Capacity_userIn=5)
m = HospitalMch_class(c)
###
P.setRAND_INT_RANGE((-1,5))
c = HospitalCtx_class()
c.checkedInit(Capacity_userIn=5)
ce = HospitalCtxExt_class()
ce.checkedInit(c,5)
m = HospitalMchRef_class(ce)
'''
@unique
class HospitalState_CS(Enum):

   # CUSTOM USER CODE BEGIN: Increase or decrease the amount of finite elements as you wish!

   Available = auto()
   Unavailable = auto()

   # CUSTOM USER CODE END
'''




############ PARKINGLOT ############ (mypy: PyRel)

c = ParkingLotCtx_class()  # Entrance,Exit ; Closed,Closing,Open,Opening.
c.checkedInit()
m = ParkingLotMch_class(c)
'''
@unique
class Car_CS(Enum):

   # CUSTOM USER CODE BEGIN: Increase or decrease the amount of finite elements as you wish!

   Car0 = auto()
   Car1 = auto()
   Car2 = auto()

   # CUSTOM USER CODE END
'''
'''
@unique
class Door_CS(Enum):

   # CUSTOM USER CODE BEGIN: Increase or decrease the amount of finite elements as you wish!

   Entrance = auto()
   Exit = auto()

   # CUSTOM USER CODE END
'''
'''
@unique
class DoorState_CS(Enum):

   # CUSTOM USER CODE BEGIN: Increase or decrease the amount of finite elements as you wish!

   Closed = auto()
   Closing = auto()
   Open = auto()
   Opening = auto()

   # CUSTOM USER CODE END
'''




############ BBIN ############

P.setUSE_FINITE_SPECIAL_SETS(True)
P.setRAND_INT_RANGE((-1,15))
c = bbinCtx_class()
c.checkedInit(PyRel({(1,10),(2,20),(3,30),(4,40),(5,50),(6,60),(7,70),(8,80),(9,90),(10,100),(11,110),(12,120),(13,130),(14,140)}),14,30)
m = bbinMch_class(c)
###
P.setUSE_FINITE_SPECIAL_SETS(True)
P.setRAND_INT_RANGE((-1,15))
c = bbinCtx_class()
c.checkedInit(PyRel({(1,10),(2,20),(3,30),(4,40),(5,50),(6,60),(7,70),(8,80),(9,90),(10,100),(11,110),(12,120),(13,130),(14,140)}),14,30)
m = bbinMchRef_class(c)




############ TRAFFICLIGHTSYSTEM ############

m = TrafficLightSystemMch_class()
#
c = TrafficLightSystemCtx_class() ### green red yellow
c.checkedInit()
#
m = TrafficLightSystemRef_class() #m.set_cars_eventActions(False,PySet({COLOURS_CS.red,COLOURS_CS.yellow}))
'''
@unique
class COLOURS_CS(Enum):

   # CUSTOM USER CODE BEGIN: Increase or decrease the amount of finite elements as you wish!

   green = auto()
   red = auto()
   yellow = auto()

   # CUSTOM USER CODE END
'''




############ COFFEECLUB ############ (mypy: PyRel)

P.setUSE_FINITE_SPECIAL_SETS(True) ### member0 member1 member2
m = CoffeeClubMch_class()
#
P.setUSE_FINITE_SPECIAL_SETS(True)
m = CoffeeClubRef_class()
'''
@unique
class MEMBER_CS(Enum):

   # CUSTOM USER CODE BEGIN: Increase or decrease the amount of finite elements as you wish!

   MEMBER0 = auto()
   MEMBER1 = auto()
   MEMBER2 = auto()

   # CUSTOM USER CODE END
'''



############ SIMPLETWOWAY ############

c = SimpleTwoWayCtx_class() ### EastWest,NorthSouth ; Green Red Yellow;
c.checkedInit()
#
c = SimpleTwoWayCtxExt_class()
c.checkedInit(OTHERDIR_userIn = PyRel({(DIRECTION_CS.EastWest,DIRECTION_CS.NorthSouth),(DIRECTION_CS.NorthSouth,DIRECTION_CS.EastWest)}))
'''
@unique
class DIRECTION_CS(Enum):

   # CUSTOM USER CODE BEGIN: Increase or decrease the amount of finite elements as you wish!

   EastWest = auto()
   NorthSouth = auto()

   # CUSTOM USER CODE END
'''
'''
@unique
class LIGHTS_CS(Enum):

   # CUSTOM USER CODE BEGIN: Increase or decrease the amount of finite elements as you wish!

   Green = auto()
   Red = auto()
   Yellow = auto()

   # CUSTOM USER CODE END
'''



############ SQUAREROOT ############ (mypy: boundidentifiers)

P.setUSE_FINITE_SPECIAL_SETS(True)
P.setFINITE_SPECIAL_SETS_LIMIT(90)
c = SquareRootCtx_class()
c.checkedInit(49)
m = SquareRootMch_class(c)
#
P.setRAND_INT_RANGE((0,30))
P.setUSE_FINITE_SPECIAL_SETS(True)
P.setFINITE_SPECIAL_SETS_LIMIT(90)
c = SquareRootCtx_class()
c.checkedInit(49)
m = SquareRootMchRef_class(c)
#
P.setRAND_INT_RANGE((0,30))
P.setUSE_FINITE_SPECIAL_SETS(True)
P.setFINITE_SPECIAL_SETS_LIMIT(90)
c = SquareRootCtx_class()
c.checkedInit(49)
m = SquareRootMchRefRef_class(c)




############ FIBONACCI ############

   def fibonacci_func(self, pyset_fibb : PySet) -> PySet:
      ans : Set = set()
      for fibb in pyset_fibb:
         if fibb==0:
            ans.add(0)
         elif fibb==1:
            ans.add(1)
         else:
            ans.add(self.fibonacci(fibb-1) + self.fibonacci(fibb-2))
      return PySet(ans)

def fibonacci_range(check_num : int) -> bool:
   if check_num == 0 or check_num == 1:
      return True
   previous = 1
   last = 2
   while(last<check_num):
      previous,last = last,previous+last
   return last==check_num

class PyFIB_Iter(PyBaseIter):

   def __iter__(self) -> Iterator:
      self.boundary : int = 100
      self.previous : int = -1
      self.last : int = 1
      return self
   
   def __next__(self) -> int:
      if P.USE_FINITE_SPECIAL_SETS():
         self.previous,self.last = self.last,self.previous+self.last
         if self.last > self.boundary:
            raise StopIteration
         return self.last
         
      raise Exception("You cannot traverse an infinite set.")

P.setUSE_FINITE_SPECIAL_SETS(True)
P.setRAND_INT_RANGE((-2,20))
c = fibonacciCtx_class()
c.checkedInit(PyCondRel(getattr(c,"fibonacci_func"),PyNAT(),PyCondSet(fibonacci_range,PyFIB_Iter())))




############ DJKSTRA ############ (mypy: PyRel)

P.setUSE_FINITE_SPECIAL_SETS(True)
graph_rel = PyRel({ (CITIES_CS.CALI,(CITIES_CS.LA,4)) , (CITIES_CS.CALI,(CITIES_CS.BOGOTA,1)) , (CITIES_CS.LA,(CITIES_CS.BOGOTA,2)) , (CITIES_CS.LA,(CITIES_CS.SANFRANCISCO,1)) , (CITIES_CS.BOGOTA,(CITIES_CS.LA,2)) , (CITIES_CS.BOGOTA,(CITIES_CS.MADRID,3)) , (CITIES_CS.MADRID,(CITIES_CS.BERLIN,1)) , (CITIES_CS.SANFRANCISCO,(CITIES_CS.TOKYO,3)) , (CITIES_CS.SANFRANCISCO,(CITIES_CS.MADRID,2)) , (CITIES_CS.BERLIN,(CITIES_CS.TOKYO,2)) })

def sort_function(heap_rel_set):
   ans : Set = set()
   for heap_rel in heap_rel_set:
      rel_to_sort = list(heap_rel.FiniteInclusion())
      rel_to_sort.sort(key=lambda key_rel : key_rel[1][1])
      new_rel = set()
      for index in range(len(rel_to_sort)):
         element = rel_to_sort[index]
         new_rel.add((index,(element[1])))
      ans.add(PyRel(new_rel))
   return PySet(ans)

P.setDESIGN_BY_CONTRACT_ENABLED(False)
c = DjkstraCtx_class()
c.checkedInit(source_userIn = CITIES_CS.CALI,
      graph_userIn = graph_rel,
      sort_func_userIn = PyCondRel(sort_function))
P.setDESIGN_BY_CONTRACT_ENABLED(True)
m = DjkstraMch_class(c)
'''
@unique
class CITIES_CS(Enum):

   # CUSTOM USER CODE BEGIN: Increase or decrease the amount of finite elements as you wish!

   BERLIN = auto()
   BOGOTA = auto()
   CALI = auto()
   LA = auto()
   MADRID = auto()
   SANFRANCISCO = auto()
   TOKYO = auto()

   # CUSTOM USER CODE END
'''