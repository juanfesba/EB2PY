#DEPENDENCIES

#Allow Path Access to the Prelude's Directory

import sys
if not(".." in sys.path):
   sys.path.append("..")

#Utilities Dependencies
from Py_Preludes import *

#Typing Dependencies
from typing import List

#Machine Refinement Dependencies
from SquareRootMchRef_mch import *

#Machine Internal Context Dependencies
from SquareRootCtx_ctx import *


#Translation of Machine: SquareRootMchRefRef
#This machine refines the following machine: SquareRootMchRef_class
#This machine sees the following context: SquareRootCtx_class


class SquareRootMchRefRef_class(SquareRootMchRef_class):

   def __init__( self , SquareRootCtx_userIn : SquareRootCtx_class = SquareRootCtx_class() ) -> None:

      #Assign Parameter to Context Extended Dependency Object
      self.__SquareRootCtx : SquareRootCtx_class = SquareRootCtx_userIn
      if not(self.__SquareRootCtx.Initialized_ContextGetMethod()):
         self.__SquareRootCtx.checkedInit()

      #Variables
      self.high : int
      self.low : int
      self.sqrt : int
      #EndVariables

      #INITIALISATION of variables
      self.sqrt = P.NAT().PyChoice()
      self.low = P.BecomesSuchThat((lambda boundIdentifiers : (P.NAT().PyContains(boundIdentifiers) and (boundIdentifiers * boundIdentifiers) <= self.SquareRootCtx_get().num)) , "int") 
      self.high = P.BecomesSuchThat((lambda boundIdentifiers : (P.NAT().PyContains(boundIdentifiers) and self.SquareRootCtx_get().num < (boundIdentifiers * boundIdentifiers))) , "int") 

      #Check ALL Invariants if enabled.
      if P.DESIGN_BY_CONTRACT_ENABLED() and not(self.checkAllInvariants()):
         raise Exception("Invariants violated after INITIALISATION.")

   #Internal Context Dependency Object Get Method

   def SquareRootCtx_get(self) -> SquareRootCtx_class:
      return self.__SquareRootCtx

   #Variables Get/Set Methods

   @property
   def high(self) -> int:
      return self.__high

   @high.setter
   def high(self, high_userIn : int) -> None:
      self.__high : int = high_userIn

   @property
   def low(self) -> int:
      return self.__low

   @low.setter
   def low(self, low_userIn : int) -> None:
      self.__low : int = low_userIn

   @property
   def sqrt(self) -> int:
      return self.__sqrt

   @sqrt.setter
   def sqrt(self, sqrt_userIn : int) -> None:
      self.__sqrt : int = sqrt_userIn

   #End Variables Get Methods

   #Invariants Check Methods

   def inv0_invariantCheck(self) -> bool:
      return P.NAT().PyContains(self.sqrt)

   def inv1_invariantCheck(self) -> bool:
      return P.NAT().PyContains(self.low)

   def inv2_invariantCheck(self) -> bool:
      return P.NAT().PyContains(self.high)

   def inv3_invariantCheck(self) -> bool:
      return (self.low + 1) <= self.high

   def inv4_invariantCheck(self) -> bool:
      return (self.low * self.low) <= self.SquareRootCtx_get().num

   def inv5_invariantCheck(self) -> bool:
      return self.low < (self.high * self.high)

   #Check ALL Invariants

   def checkAllInvariants(self) -> bool:
      checkedAns_local : bool = True
      allInvariants_local : List[str] = [ "inv0" , "inv1" , "inv2" , "inv3" , "inv4" , "inv5" ]

      for Invariant_local in allInvariants_local:
         InvariantMethod_local = getattr(self,Invariant_local + "_invariantCheck")
         checkedAns_local = checkedAns_local and InvariantMethod_local()

      return checkedAns_local

   #End Check ALL Invariants Method

   #Events

   #Improve2 - Event

   def Improve2_eventGuards(self, m2_userIn : int) -> bool:
      guard_ans : bool = True

      #Set Parameters as an Attribute.
      self.m2 : int = m2_userIn

      #Check Event PreConditions.
      if P.DESIGN_BY_CONTRACT_ENABLED():
         try:
            if True and ((self.low + 1) != self.high) and (P.NAT().PyContains(self.m2)) and ((self.low < self.m2 and self.m2 < self.high)) and ((self.m2 * self.m2) > self.SquareRootCtx_get().num):
               guard_ans = True
            else:
               guard_ans = False
         except:
            guard_ans = False
      else:
         guard_ans = True

      del(self.m2)
      return guard_ans

   def Improve2_eventActions(self, m2_userIn : int = P.NoParam()) -> None:

      if m2_userIn is None:
         m2_userIn = P.PyRandValGen("int")

      attempt_Count : int = 0
      while not(self.Improve2_eventGuards(m2_userIn)):
         m2_userIn = P.PyRandValGen("int")
         if attempt_Count == P.LOWMAXGENATTEMPTS():
            raise GuardsViolated("Guards of the Event could not be fulfilled.")
         attempt_Count += 1

      #Set Parameters as an Attribute.
      self.m2 = m2_userIn

      #Event Actions

      self.high = self.m2

      #Check Invariants after the actions are executed.
      if P.DESIGN_BY_CONTRACT_ENABLED() and not(self.checkAllInvariants()):
         raise Exception("PostConditions of the Event could not be fulfilled.")

      del(self.m2)

   #End Event

   #SquareRootRef - Event

   def SquareRootRef_eventGuards(self) -> bool:
      guard_ans : bool = True

      #Set Parameters as an Attribute.

      #Check Event PreConditions.
      if P.DESIGN_BY_CONTRACT_ENABLED():
         try:
            if True and ((self.low + 1) == self.high):
               guard_ans = True
            else:
               guard_ans = False
         except:
            guard_ans = False
      else:
         guard_ans = True

      return guard_ans

   def SquareRootRef_eventActions(self) -> None:

      attempt_Count : int = 0
      while not(self.SquareRootRef_eventGuards()):
         if attempt_Count == P.LOWMAXGENATTEMPTS():
            raise GuardsViolated("Guards of the Event could not be fulfilled.")
         attempt_Count += 1

      #Set Parameters as an Attribute.

      #Event Actions

      self.sqrt = self.low

      #Check Invariants after the actions are executed.
      if P.DESIGN_BY_CONTRACT_ENABLED() and not(self.checkAllInvariants()):
         raise Exception("PostConditions of the Event could not be fulfilled.")


   #End Event

   #Improve1 - Event

   def Improve1_eventGuards(self, m1_userIn : int) -> bool:
      guard_ans : bool = True

      #Set Parameters as an Attribute.
      self.m1 : int = m1_userIn

      #Check Event PreConditions.
      if P.DESIGN_BY_CONTRACT_ENABLED():
         try:
            if True and ((self.low + 1) != self.high) and (P.NAT().PyContains(self.m1)) and ((self.low < self.m1 and self.m1 < self.high)) and ((self.m1 * self.m1) <= self.SquareRootCtx_get().num):
               guard_ans = True
            else:
               guard_ans = False
         except:
            guard_ans = False
      else:
         guard_ans = True

      del(self.m1)
      return guard_ans

   def Improve1_eventActions(self, m1_userIn : int = P.NoParam()) -> None:

      if m1_userIn is None:
         m1_userIn = P.PyRandValGen("int")

      attempt_Count : int = 0
      while not(self.Improve1_eventGuards(m1_userIn)):
         m1_userIn = P.PyRandValGen("int")
         if attempt_Count == P.LOWMAXGENATTEMPTS():
            raise GuardsViolated("Guards of the Event could not be fulfilled.")
         attempt_Count += 1

      #Set Parameters as an Attribute.
      self.m1 = m1_userIn

      #Event Actions

      self.low = self.m1

      #Check Invariants after the actions are executed.
      if P.DESIGN_BY_CONTRACT_ENABLED() and not(self.checkAllInvariants()):
         raise Exception("PostConditions of the Event could not be fulfilled.")

      del(self.m1)

   #End Event

   #User/Debugging Functions

   def __str__(self) -> str:
      tmp_values : List[str] = list()

      #Print Internal Context Constants
      tmp_values.append(self.__SquareRootCtx.__str__())

      #Print Variables
      tmp_values.append("###")
      tmp_values.append("Variables")

      tmp_values.append("high ==> " + str(self.high))
      tmp_values.append("low ==> " + str(self.low))
      tmp_values.append("sqrt ==> " + str(self.sqrt))

      return "\n".join(tmp_values)

   def __repr__(self) -> str:
      return self.__str__()

   def PyGuardsState(self) -> None:
      #This method will show which events (with no parameters) can be executed.
      tmp_values : List[str] = list()
      list_events_noparams : List[str] = ["SquareRootRef"]
      list_events_params : List[Tuple[str,List[str]]] = [("Improve2",["int"]), ("Improve1",["int"])]
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
      list_events_strs : List[str] = ["Improve2", "SquareRootRef", "Improve1"]
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
