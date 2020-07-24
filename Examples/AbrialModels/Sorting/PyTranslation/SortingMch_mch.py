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
from SortingCtx_ctx import *


#Translation of Machine: SortingMch
#This machine sees the following context: SortingCtx_class


class SortingMch_class():

   def __init__( self , SortingCtx_userIn : SortingCtx_class = SortingCtx_class() ) -> None:

      #Assign Parameter to Context Extended Dependency Object
      self.__SortingCtx : SortingCtx_class = SortingCtx_userIn
      if not(self.__SortingCtx.Initialized_ContextGetMethod()):
         self.__SortingCtx.checkedInit()

      #Variables
      self.d : int
      self.f : PyRel[int,int]
      self.j : int
      self.k : int
      self.l : int
      #EndVariables

      #INITIALISATION of variables
      self.f = PyFamilies(PyFamilyTypes.TotalInjections, PySet({int_range for int_range in range(1, self.SortingCtx_get().m+1)}), P.NAT()).PyChoice()
      self.k = 1
      self.l = 1
      self.j = 1
      self.d = 1

      #Check ALL Invariants if enabled.
      if P.DESIGN_BY_CONTRACT_ENABLED() and not(self.checkAllInvariants()):
         raise Exception("Invariants violated after INITIALISATION.")

   #Internal Context Dependency Object Get Method

   def SortingCtx_get(self) -> SortingCtx_class:
      return self.__SortingCtx

   #Variables Get/Set Methods

   @property
   def d(self) -> int:
      return self.__d

   @d.setter
   def d(self, d_userIn : int) -> None:
      self.__d : int = d_userIn

   @property
   def f(self) -> PyRel[int,int]:
      return self.__f

   @f.setter
   def f(self, f_userIn : PyRel[int,int]) -> None:
      self.__f : PyRel[int,int] = f_userIn

   @property
   def j(self) -> int:
      return self.__j

   @j.setter
   def j(self, j_userIn : int) -> None:
      self.__j : int = j_userIn

   @property
   def k(self) -> int:
      return self.__k

   @k.setter
   def k(self, k_userIn : int) -> None:
      self.__k : int = k_userIn

   @property
   def l(self) -> int:
      return self.__l

   @l.setter
   def l(self, l_userIn : int) -> None:
      self.__l : int = l_userIn

   #End Variables Get Methods

   #Invariants Check Methods

   def inv0_invariantCheck(self) -> bool:
      return PyFamilies(PyFamilyTypes.TotalInjections, PySet({int_range for int_range in range(1, self.SortingCtx_get().m+1)}), P.NAT()).PyContains(self.f)

   def inv1_invariantCheck(self) -> bool:
      return PySet({0, 1}).PyContains(self.d)

   def inv2_invariantCheck(self) -> bool:
      return PySet({int_range for int_range in range(1, self.SortingCtx_get().m+1)}).PyContains(self.k)

   def inv3_invariantCheck(self) -> bool:
      return P.QuantifiedForAll( (lambda boundIdentifiers : PyPrelude.LogicImplication((PySet({int_range for int_range in range(1, (self.k - 1)+1)}).PyContains(boundIdentifiers[1]) and PySet({int_range for int_range in range(1, self.SortingCtx_get().m+1)}).PyContains(boundIdentifiers[0]) and boundIdentifiers[1] < boundIdentifiers[0]), self.f(boundIdentifiers[1]) < self.f(boundIdentifiers[0]))) , [ (0,"int") , (1,"int") ] ) 

   def inv4_invariantCheck(self) -> bool:
      return PySet({int_range for int_range in range(self.k, self.SortingCtx_get().m+1)}).PyContains(self.j)

   def inv5_invariantCheck(self) -> bool:
      return PySet({int_range for int_range in range(self.k, self.j+1)}).PyContains(self.l)

   def inv6_invariantCheck(self) -> bool:
      return P.QuantifiedForAll( (lambda boundIdentifiers : PyPrelude.LogicImplication(PySet({int_range for int_range in range(self.k, self.j+1)}).PyDifference(PySet({self.l})).PyContains(boundIdentifiers[0]), self.f(self.l) < self.f(boundIdentifiers[0]))) , [ (0,"int") ] ) 

   #Check ALL Invariants

   def checkAllInvariants(self) -> bool:
      checkedAns_local : bool = True
      allInvariants_local : List[str] = [ "inv0" , "inv1" , "inv2" , "inv3" , "inv4" , "inv5" , "inv6" ]

      for Invariant_local in allInvariants_local:
         InvariantMethod_local = getattr(self,Invariant_local + "_invariantCheck")
         checkedAns_local = checkedAns_local and InvariantMethod_local()

      return checkedAns_local

   #End Check ALL Invariants Method

   #Events

   #aprog - Event

   def aprog_eventGuards(self) -> bool:
      guard_ans : bool = True

      #Set Parameters as an Attribute.

      #Check Event PreConditions.
      if P.DESIGN_BY_CONTRACT_ENABLED():
         try:
            if True and (self.d != 0) and (self.k == self.SortingCtx_get().m):
               guard_ans = True
            else:
               guard_ans = False
         except:
            guard_ans = False
      else:
         guard_ans = True

      return guard_ans

   def aprog_eventActions(self) -> None:

      attempt_Count : int = 0
      while not(self.aprog_eventGuards()):
         if attempt_Count == P.LOWMAXGENATTEMPTS():
            raise GuardsViolated("Guards of the Event could not be fulfilled.")
         attempt_Count += 1

      #Set Parameters as an Attribute.

      #Event Actions

      self.d = 0

      #Check Invariants after the actions are executed.
      if P.DESIGN_BY_CONTRACT_ENABLED() and not(self.checkAllInvariants()):
         raise Exception("PostConditions of the Event could not be fulfilled.")


   #End Event

   #progr - Event

   def progr_eventGuards(self) -> bool:
      guard_ans : bool = True

      #Set Parameters as an Attribute.

      #Check Event PreConditions.
      if P.DESIGN_BY_CONTRACT_ENABLED():
         try:
            if True and ((self.d != 0 and self.k < self.SortingCtx_get().m and self.j == self.SortingCtx_get().m)):
               guard_ans = True
            else:
               guard_ans = False
         except:
            guard_ans = False
      else:
         guard_ans = True

      return guard_ans

   def progr_eventActions(self) -> None:

      attempt_Count : int = 0
      while not(self.progr_eventGuards()):
         if attempt_Count == P.LOWMAXGENATTEMPTS():
            raise GuardsViolated("Guards of the Event could not be fulfilled.")
         attempt_Count += 1

      #Set Parameters as an Attribute.

      #Event Actions

      self.k, self.j, self.l, self.f = (self.k + 1), (self.k + 1), (self.k + 1), self.f.PyOverriding(PyRel({(self.k, self.f(self.l))})).PyOverriding(PyRel({(self.l, self.f(self.k))}))

      #Check Invariants after the actions are executed.
      if P.DESIGN_BY_CONTRACT_ENABLED() and not(self.checkAllInvariants()):
         raise Exception("PostConditions of the Event could not be fulfilled.")


   #End Event

   #prog2 - Event

   def prog2_eventGuards(self) -> bool:
      guard_ans : bool = True

      #Set Parameters as an Attribute.

      #Check Event PreConditions.
      if P.DESIGN_BY_CONTRACT_ENABLED():
         try:
            if True and ((self.d != 0 and self.k < self.SortingCtx_get().m and self.j < self.SortingCtx_get().m and self.f(self.l) > self.f((self.j + 1)))):
               guard_ans = True
            else:
               guard_ans = False
         except:
            guard_ans = False
      else:
         guard_ans = True

      return guard_ans

   def prog2_eventActions(self) -> None:

      attempt_Count : int = 0
      while not(self.prog2_eventGuards()):
         if attempt_Count == P.LOWMAXGENATTEMPTS():
            raise GuardsViolated("Guards of the Event could not be fulfilled.")
         attempt_Count += 1

      #Set Parameters as an Attribute.

      #Event Actions

      self.j, self.l = (self.j + 1), (self.j + 1)

      #Check Invariants after the actions are executed.
      if P.DESIGN_BY_CONTRACT_ENABLED() and not(self.checkAllInvariants()):
         raise Exception("PostConditions of the Event could not be fulfilled.")


   #End Event

   #prog1 - Event

   def prog1_eventGuards(self) -> bool:
      guard_ans : bool = True

      #Set Parameters as an Attribute.

      #Check Event PreConditions.
      if P.DESIGN_BY_CONTRACT_ENABLED():
         try:
            if True and ((self.d != 0 and self.k < self.SortingCtx_get().m and self.j < self.SortingCtx_get().m and self.f(self.l) <= self.f((self.j + 1)))):
               guard_ans = True
            else:
               guard_ans = False
         except:
            guard_ans = False
      else:
         guard_ans = True

      return guard_ans

   def prog1_eventActions(self) -> None:

      attempt_Count : int = 0
      while not(self.prog1_eventGuards()):
         if attempt_Count == P.LOWMAXGENATTEMPTS():
            raise GuardsViolated("Guards of the Event could not be fulfilled.")
         attempt_Count += 1

      #Set Parameters as an Attribute.

      #Event Actions

      self.j = (self.j + 1)

      #Check Invariants after the actions are executed.
      if P.DESIGN_BY_CONTRACT_ENABLED() and not(self.checkAllInvariants()):
         raise Exception("PostConditions of the Event could not be fulfilled.")


   #End Event

   #User/Debugging Functions

   def __str__(self) -> str:
      tmp_values : List[str] = list()

      #Print Internal Context Constants
      tmp_values.append(self.__SortingCtx.__str__())

      #Print Variables
      tmp_values.append("###")
      tmp_values.append("Variables")

      tmp_values.append("d ==> " + str(self.d))
      tmp_values.append("f ==> " + str(self.f))
      tmp_values.append("j ==> " + str(self.j))
      tmp_values.append("k ==> " + str(self.k))
      tmp_values.append("l ==> " + str(self.l))

      return "\n".join(tmp_values)

   def __repr__(self) -> str:
      return self.__str__()

   def PyGuardsState(self) -> None:
      #This method will show which events (with no parameters) can be executed.
      tmp_values : List[str] = list()
      list_events_noparams : List[str] = ["aprog", "progr", "prog2", "prog1"]
      list_events_params : List[Tuple[str,List[str]]] = []
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
      list_events_strs : List[str] = ["aprog", "progr", "prog2", "prog1"]
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
