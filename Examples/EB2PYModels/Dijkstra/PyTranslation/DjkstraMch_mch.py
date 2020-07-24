#DEPENDENCIES

#Allow Path Access to the Prelude's Directory

import sys
if not(".." in sys.path):
   sys.path.append("..")

#Utilities Dependencies
from Py_Preludes import *

#Typing Dependencies
from typing import List

#Machine Internal Context Dependencies
from DjkstraCtx_ctx import *


#Translation of Machine: DjkstraMch
#This machine sees the following context: DjkstraCtx_class


class DjkstraMch_class():

   def __init__( self , DjkstraCtx_userIn : DjkstraCtx_class = DjkstraCtx_class() ) -> None:

      #Assign Parameter to Context Extended Dependency Object
      self.__DjkstraCtx : DjkstraCtx_class = DjkstraCtx_userIn
      if not(self.__DjkstraCtx.Initialized_ContextGetMethod()):
         self.__DjkstraCtx.checkedInit()

      #Variables
      self.d : int
      self.distances : PyRel[CITIES_CS,int]
      self.finished : bool
      self.heap : PyRel[int,Tuple[CITIES_CS,int]]
      self.new_distances : PyRel[CITIES_CS,int]
      self.visited : PySet[CITIES_CS]
      #EndVariables

      #INITIALISATION of variables
      self.visited = PySet()
      self.finished = False
      self.distances = PyRel({(self.DjkstraCtx_get().CALI, 0), (self.DjkstraCtx_get().BOGOTA, 9999), (self.DjkstraCtx_get().LA, 9999), (self.DjkstraCtx_get().SANFRANCISCO, 9999), (self.DjkstraCtx_get().MADRID, 9999), (self.DjkstraCtx_get().BERLIN, 9999), (self.DjkstraCtx_get().TOKYO, 9999)})
      self.heap = PyRel({(0, (self.DjkstraCtx_get().source, 0))})
      self.new_distances = PySet()
      self.d = 0

      #Check ALL Invariants if enabled.
      if P.DESIGN_BY_CONTRACT_ENABLED() and not(self.checkAllInvariants()):
         raise Exception("Invariants violated after INITIALISATION.")

   #Internal Context Dependency Object Get Method

   def DjkstraCtx_get(self) -> DjkstraCtx_class:
      return self.__DjkstraCtx

   #Variables Get/Set Methods

   @property
   def d(self) -> int:
      return self.__d

   @d.setter
   def d(self, d_userIn : int) -> None:
      self.__d : int = d_userIn

   @property
   def distances(self) -> PyRel[CITIES_CS,int]:
      return self.__distances

   @distances.setter
   def distances(self, distances_userIn : PyRel[CITIES_CS,int]) -> None:
      self.__distances : PyRel[CITIES_CS,int] = distances_userIn

   @property
   def finished(self) -> bool:
      return self.__finished

   @finished.setter
   def finished(self, finished_userIn : bool) -> None:
      self.__finished : bool = finished_userIn

   @property
   def heap(self) -> PyRel[int,Tuple[CITIES_CS,int]]:
      return self.__heap

   @heap.setter
   def heap(self, heap_userIn : PyRel[int,Tuple[CITIES_CS,int]]) -> None:
      self.__heap : PyRel[int,Tuple[CITIES_CS,int]] = heap_userIn

   @property
   def new_distances(self) -> PyRel[CITIES_CS,int]:
      return self.__new_distances

   @new_distances.setter
   def new_distances(self, new_distances_userIn : PyRel[CITIES_CS,int]) -> None:
      self.__new_distances : PyRel[CITIES_CS,int] = new_distances_userIn

   @property
   def visited(self) -> PySet[CITIES_CS]:
      return self.__visited

   @visited.setter
   def visited(self, visited_userIn : PySet[CITIES_CS]) -> None:
      self.__visited : PySet[CITIES_CS] = visited_userIn

   #End Variables Get Methods

   #Invariants Check Methods

   def inv0_invariantCheck(self) -> bool:
      return self.DjkstraCtx_get().CITIES.PyPowerSet().PyContains(self.visited)

   def inv1_invariantCheck(self) -> bool:
      return P.BOOL().PyContains(self.finished)

   def inv2_invariantCheck(self) -> bool:
      return PyFamilies(PyFamilyTypes.PartialFunctions, P.NAT(), self.DjkstraCtx_get().CITIES.PyCartesianProduct(P.NAT())).PyContains(self.heap)

   def inv3_invariantCheck(self) -> bool:
      return PyFamilies(PyFamilyTypes.TotalFunctions, self.DjkstraCtx_get().CITIES, P.NAT()).PyContains(self.distances)

   def inv4_invariantCheck(self) -> bool:
      return PyPrelude.LogicImplication(self.finished == True, len(self.visited) == len(self.DjkstraCtx_get().CITIES))

   def inv5_invariantCheck(self) -> bool:
      return self.distances(self.DjkstraCtx_get().source) == 0

   def inv6_invariantCheck(self) -> bool:
      return P.QuantifiedForAll( (lambda boundIdentifiers : PyPrelude.LogicImplication((self.heap.PyDomain().PyContains(boundIdentifiers[1]) and self.heap.PyDomain().PyContains(boundIdentifiers[0]) and boundIdentifiers[1] < boundIdentifiers[0]), P.Minimum(PySet({self.heap(boundIdentifiers[1])}).PyRange()) <= P.Minimum(PySet({self.heap(boundIdentifiers[0])}).PyRange()))) , [ (0,"int") , (1,"int") ] ) 

   def inv7_invariantCheck(self) -> bool:
      return PyFamilies(PyFamilyTypes.PartialFunctions, self.DjkstraCtx_get().CITIES, P.NAT()).PyContains(self.new_distances)

   def inv8_invariantCheck(self) -> bool:
      return P.NAT().PyContains(self.d)

   #Check ALL Invariants

   def checkAllInvariants(self) -> bool:
      checkedAns_local : bool = True
      allInvariants_local : List[str] = [ "inv0" , "inv1" , "inv2" , "inv3" , "inv4" , "inv5" , "inv6" , "inv7" , "inv8" ]

      for Invariant_local in allInvariants_local:
         InvariantMethod_local = getattr(self,Invariant_local + "_invariantCheck")
         checkedAns_local = checkedAns_local and InvariantMethod_local()

      return checkedAns_local

   #End Check ALL Invariants Method

   #Events

   #PopNonVisited - Event

   def PopNonVisited_eventGuards(self) -> bool:
      guard_ans : bool = True

      #Set Parameters as an Attribute.

      #Check Event PreConditions.
      if P.DESIGN_BY_CONTRACT_ENABLED():
         try:
            if True and (self.finished == False) and (len(self.visited) != len(self.DjkstraCtx_get().CITIES)) and (len(self.heap) > 0) and (PySet({self.heap(P.Minimum(self.heap.PyDomain()))}).PyDomain().PyIsSubset(self.visited)) and (len(self.new_distances) == 0):
               guard_ans = True
            else:
               guard_ans = False
         except:
            guard_ans = False
      else:
         guard_ans = True

      return guard_ans

   def PopNonVisited_eventActions(self) -> None:

      attempt_Count : int = 0
      while not(self.PopNonVisited_eventGuards()):
         if attempt_Count == P.LOWMAXGENATTEMPTS():
            raise GuardsViolated("Guards of the Event could not be fulfilled.")
         attempt_Count += 1

      #Set Parameters as an Attribute.

      #Event Actions

      self.heap = self.heap.PyDomainSubstraction(PySet({P.Minimum(self.heap.PyDomain())}))

      #Check Invariants after the actions are executed.
      if P.DESIGN_BY_CONTRACT_ENABLED() and not(self.checkAllInvariants()):
         raise Exception("PostConditions of the Event could not be fulfilled.")


   #End Event

   #PopVisited - Event

   def PopVisited_eventGuards(self) -> bool:
      guard_ans : bool = True

      #Set Parameters as an Attribute.

      #Check Event PreConditions.
      if P.DESIGN_BY_CONTRACT_ENABLED():
         try:
            if True and (self.finished == False) and (len(self.visited) != len(self.DjkstraCtx_get().CITIES)) and (len(self.heap) > 0) and (PySet({self.heap(P.Minimum(self.heap.PyDomain()))}).PyDomain().PyNotSubset(self.visited)) and (len(self.new_distances) == 0):
               guard_ans = True
            else:
               guard_ans = False
         except:
            guard_ans = False
      else:
         guard_ans = True

      return guard_ans

   def PopVisited_eventActions(self) -> None:

      attempt_Count : int = 0
      while not(self.PopVisited_eventGuards()):
         if attempt_Count == P.LOWMAXGENATTEMPTS():
            raise GuardsViolated("Guards of the Event could not be fulfilled.")
         attempt_Count += 1

      #Set Parameters as an Attribute.

      #Event Actions

      self.visited, self.new_distances, self.heap, self.d = self.visited.PyUnion(PySet({self.heap(P.Minimum(self.heap.PyDomain()))}).PyDomain()), self.DjkstraCtx_get().graph[PySet({self.heap(P.Minimum(self.heap.PyDomain()))}).PyDomain()], self.heap.PyDomainSubstraction(PySet({P.Minimum(self.heap.PyDomain())})), P.Minimum(PySet({self.heap(P.Minimum(self.heap.PyDomain()))}).PyRange())

      #Check Invariants after the actions are executed.
      if P.DESIGN_BY_CONTRACT_ENABLED() and not(self.checkAllInvariants()):
         raise Exception("PostConditions of the Event could not be fulfilled.")


   #End Event

   #HeapPush - Event

   def HeapPush_eventGuards(self, city_userIn : CITIES_CS) -> bool:
      guard_ans : bool = True

      #Set Parameters as an Attribute.
      self.city : CITIES_CS = city_userIn

      #Check Event PreConditions.
      if P.DESIGN_BY_CONTRACT_ENABLED():
         try:
            if True and (len(self.new_distances) > 0) and (self.new_distances.PyDomain().PyContains(self.city)) and (self.distances(self.city) > (self.d + self.new_distances(self.city))) and (len(self.visited) != len(self.DjkstraCtx_get().CITIES)):
               guard_ans = True
            else:
               guard_ans = False
         except:
            guard_ans = False
      else:
         guard_ans = True

      del(self.city)
      return guard_ans

   def HeapPush_eventActions(self, city_userIn : CITIES_CS = P.NoParam()) -> None:

      if city_userIn is None:
         city_userIn = P.PyRandValGen("CITIES_CS")

      attempt_Count : int = 0
      while not(self.HeapPush_eventGuards(city_userIn)):
         city_userIn = P.PyRandValGen("CITIES_CS")
         if attempt_Count == P.LOWMAXGENATTEMPTS():
            raise GuardsViolated("Guards of the Event could not be fulfilled.")
         attempt_Count += 1

      #Set Parameters as an Attribute.
      self.city = city_userIn

      #Event Actions

      self.new_distances, self.distances, self.heap = self.new_distances.PyDifference(PyRel({(self.city, self.new_distances(self.city))})), self.distances.PyOverriding(PyRel({(self.city, (self.d + self.new_distances(self.city)))})), self.DjkstraCtx_get().sort_func(self.heap.PyUnion(PyRel({(len(self.heap), (self.city, (self.d + self.new_distances(self.city))))})))

      #Check Invariants after the actions are executed.
      if P.DESIGN_BY_CONTRACT_ENABLED() and not(self.checkAllInvariants()):
         raise Exception("PostConditions of the Event could not be fulfilled.")

      del(self.city)

   #End Event

   #HeapNoPush - Event

   def HeapNoPush_eventGuards(self, city_userIn : CITIES_CS) -> bool:
      guard_ans : bool = True

      #Set Parameters as an Attribute.
      self.city : CITIES_CS = city_userIn

      #Check Event PreConditions.
      if P.DESIGN_BY_CONTRACT_ENABLED():
         try:
            if True and (len(self.new_distances) > 0) and (self.new_distances.PyDomain().PyContains(self.city)) and (self.distances(self.city) <= (self.d + self.new_distances(self.city))) and (len(self.visited) != len(self.DjkstraCtx_get().CITIES)):
               guard_ans = True
            else:
               guard_ans = False
         except:
            guard_ans = False
      else:
         guard_ans = True

      del(self.city)
      return guard_ans

   def HeapNoPush_eventActions(self, city_userIn : CITIES_CS = P.NoParam()) -> None:

      if city_userIn is None:
         city_userIn = P.PyRandValGen("CITIES_CS")

      attempt_Count : int = 0
      while not(self.HeapNoPush_eventGuards(city_userIn)):
         city_userIn = P.PyRandValGen("CITIES_CS")
         if attempt_Count == P.LOWMAXGENATTEMPTS():
            raise GuardsViolated("Guards of the Event could not be fulfilled.")
         attempt_Count += 1

      #Set Parameters as an Attribute.
      self.city = city_userIn

      #Event Actions

      self.new_distances = self.new_distances.PyDifference(PyRel({(self.city, self.new_distances(self.city))}))

      #Check Invariants after the actions are executed.
      if P.DESIGN_BY_CONTRACT_ENABLED() and not(self.checkAllInvariants()):
         raise Exception("PostConditions of the Event could not be fulfilled.")

      del(self.city)

   #End Event

   #Finish - Event

   def Finish_eventGuards(self) -> bool:
      guard_ans : bool = True

      #Set Parameters as an Attribute.

      #Check Event PreConditions.
      if P.DESIGN_BY_CONTRACT_ENABLED():
         try:
            if True and (len(self.visited) == len(self.DjkstraCtx_get().CITIES)) and (self.finished == False):
               guard_ans = True
            else:
               guard_ans = False
         except:
            guard_ans = False
      else:
         guard_ans = True

      return guard_ans

   def Finish_eventActions(self) -> None:

      attempt_Count : int = 0
      while not(self.Finish_eventGuards()):
         if attempt_Count == P.LOWMAXGENATTEMPTS():
            raise GuardsViolated("Guards of the Event could not be fulfilled.")
         attempt_Count += 1

      #Set Parameters as an Attribute.

      #Event Actions

      self.finished = True

      #Check Invariants after the actions are executed.
      if P.DESIGN_BY_CONTRACT_ENABLED() and not(self.checkAllInvariants()):
         raise Exception("PostConditions of the Event could not be fulfilled.")


   #End Event

   #User/Debugging Functions

   def __str__(self) -> str:
      tmp_values : List[str] = list()

      #Print Internal Context Constants
      tmp_values.append(self.__DjkstraCtx.__str__())

      #Print Variables
      tmp_values.append("###")
      tmp_values.append("Variables")

      tmp_values.append("d ==> " + str(self.d))
      tmp_values.append("distances ==> " + str(self.distances))
      tmp_values.append("finished ==> " + str(self.finished))
      tmp_values.append("heap ==> " + str(self.heap))
      tmp_values.append("new_distances ==> " + str(self.new_distances))
      tmp_values.append("visited ==> " + str(self.visited))

      return "\n".join(tmp_values)

   def __repr__(self) -> str:
      return self.__str__()

   def PyGuardsState(self) -> None:
      #This method will show which events (with no parameters) can be executed.
      tmp_values : List[str] = list()
      list_events_noparams : List[str] = ["PopNonVisited", "PopVisited", "Finish"]
      list_events_params : List[Tuple[str,List[str]]] = [("HeapPush",["CITIES_CS"]), ("HeapNoPush",["CITIES_CS"])]
      tmp_values.append("State of the Guards of every event!")
      for event_name in list_events_noparams:
         guards_to_check = getattr(self,event_name + "_eventGuards")
         tmp_values.append(event_name + " ==> " + str(guards_to_check()))
      for event_name,params_type in list_events_params:
         if len(params_type)>1:
            tmp_values.append(event_name + " ==> Undetermined")
            continue
         guards_to_check = getattr(self,event_name + "_eventGuards")
         guards_state = False
         for possible_any in P.ObtainSetFromType(params_type[0]):
            try:
               guards_state = guards_to_check(possible_any)
            except:
               continue
            if guards_state:
               tmp_values.append(event_name + " ==> " + str(guards_state) + ", e.g. with param = " + str(possible_any))
               break
         if not guards_state:
            tmp_values.append(event_name + " ==> " + str(guards_state))
      print("\n".join(tmp_values))

   def PyAutoExecute(self) -> None:
      #This method will try to find an event to execute.
      list_events_strs : List[str] = ["PopNonVisited", "PopVisited", "HeapPush", "HeapNoPush", "Finish"]
      amount_of_events : int = len(list_events_strs)
      attempt_count : int = 0
      while(attempt_count < P.MaxAutoExecuteAttempts()):
         event_iter : int = randint(0,amount_of_events-1)
         event_name : str = list_events_strs[event_iter]
         try:
            event_to_attempt = getattr(self,event_name + "_eventActions")
            event_to_attempt()
            print(event_name + " succesfully executed!!!")
            print(self)
            return
         except GuardsViolated:
            attempt_count += 1
      print("No event could be AutoExecuted")
