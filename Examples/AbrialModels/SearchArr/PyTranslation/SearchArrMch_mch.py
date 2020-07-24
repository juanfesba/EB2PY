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
from SearchArrCtx_ctx import *


#Translation of Machine: SearchArrMch
#This machine sees the following context: SearchArrCtx_class


class SearchArrMch_class():

   def __init__( self , SearchArrCtx_userIn : SearchArrCtx_class = SearchArrCtx_class() ) -> None:

      #Assign Parameter to Context Extended Dependency Object
      self.__SearchArrCtx : SearchArrCtx_class = SearchArrCtx_userIn
      if not(self.__SearchArrCtx.Initialized_ContextGetMethod()):
         self.__SearchArrCtx.checkedInit()

      #Variables
      self.d : int
      self.i : int
      self.k : int
      self.x : int
      #EndVariables

      #INITIALISATION of variables
      self.x = self.SearchArrCtx_get().f.PyRange().PyChoice()
      self.d = 1
      self.i = 1
      self.k = 0

      #Check ALL Invariants if enabled.
      if P.DESIGN_BY_CONTRACT_ENABLED() and not(self.checkAllInvariants()):
         raise Exception("Invariants violated after INITIALISATION.")

   #Internal Context Dependency Object Get Method

   def SearchArrCtx_get(self) -> SearchArrCtx_class:
      return self.__SearchArrCtx

   #Variables Get/Set Methods

   @property
   def d(self) -> int:
      return self.__d

   @d.setter
   def d(self, d_userIn : int) -> None:
      self.__d : int = d_userIn

   @property
   def i(self) -> int:
      return self.__i

   @i.setter
   def i(self, i_userIn : int) -> None:
      self.__i : int = i_userIn

   @property
   def k(self) -> int:
      return self.__k

   @k.setter
   def k(self, k_userIn : int) -> None:
      self.__k : int = k_userIn

   @property
   def x(self) -> int:
      return self.__x

   @x.setter
   def x(self, x_userIn : int) -> None:
      self.__x : int = x_userIn

   #End Variables Get Methods

   #Invariants Check Methods

   def inv0_invariantCheck(self) -> bool:
      return self.SearchArrCtx_get().f.PyDomain().PyContains(self.i)

   def inv1_invariantCheck(self) -> bool:
      return self.SearchArrCtx_get().f.PyRange().PyContains(self.x)

   def inv2_invariantCheck(self) -> bool:
      return PySet({0, 1}).PyContains(self.d)

   def inv3_invariantCheck(self) -> bool:
      return PySet({int_range for int_range in range(0, (self.SearchArrCtx_get().n - 1)+1)}).PyContains(self.k)

   def inv4_invariantCheck(self) -> bool:
      return self.SearchArrCtx_get().f[PySet({int_range for int_range in range(1, self.k+1)})].PyNotContains(self.x)

   #Check ALL Invariants

   def checkAllInvariants(self) -> bool:
      checkedAns_local : bool = True
      allInvariants_local : List[str] = [ "inv0" , "inv1" , "inv2" , "inv3" , "inv4" ]

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
            if True and (self.d != 0) and (self.SearchArrCtx_get().f((self.k + 1)) == self.x):
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

      self.i, self.d = (self.k + 1), 0

      #Check Invariants after the actions are executed.
      if P.DESIGN_BY_CONTRACT_ENABLED() and not(self.checkAllInvariants()):
         raise Exception("PostConditions of the Event could not be fulfilled.")


   #End Event

   #progress - Event

   def progress_eventGuards(self) -> bool:
      guard_ans : bool = True

      #Set Parameters as an Attribute.

      #Check Event PreConditions.
      if P.DESIGN_BY_CONTRACT_ENABLED():
         try:
            if True and ((self.d != 0 and self.SearchArrCtx_get().f((self.k + 1)) != self.x)):
               guard_ans = True
            else:
               guard_ans = False
         except:
            guard_ans = False
      else:
         guard_ans = True

      return guard_ans

   def progress_eventActions(self) -> None:

      attempt_Count : int = 0
      while not(self.progress_eventGuards()):
         if attempt_Count == P.LOWMAXGENATTEMPTS():
            raise GuardsViolated("Guards of the Event could not be fulfilled.")
         attempt_Count += 1

      #Set Parameters as an Attribute.

      #Event Actions

      self.k = (self.k + 1)

      #Check Invariants after the actions are executed.
      if P.DESIGN_BY_CONTRACT_ENABLED() and not(self.checkAllInvariants()):
         raise Exception("PostConditions of the Event could not be fulfilled.")


   #End Event

   #User/Debugging Functions

   def __str__(self) -> str:
      tmp_values : List[str] = list()

      #Print Internal Context Constants
      tmp_values.append(self.__SearchArrCtx.__str__())

      #Print Variables
      tmp_values.append("###")
      tmp_values.append("Variables")

      tmp_values.append("d ==> " + str(self.d))
      tmp_values.append("i ==> " + str(self.i))
      tmp_values.append("k ==> " + str(self.k))
      tmp_values.append("x ==> " + str(self.x))

      return "\n".join(tmp_values)

   def __repr__(self) -> str:
      return self.__str__()

   def PyGuardsState(self) -> None:
      #This method will show which events (with no parameters) can be executed.
      tmp_values : List[str] = list()
      list_events_noparams : List[str] = ["aprog", "progress"]
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
      list_events_strs : List[str] = ["aprog", "progress"]
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
