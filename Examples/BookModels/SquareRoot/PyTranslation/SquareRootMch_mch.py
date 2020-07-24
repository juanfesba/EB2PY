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
from SquareRootCtx_ctx import *


#Translation of Machine: SquareRootMch
#This machine sees the following context: SquareRootCtx_class


class SquareRootMch_class():

   def __init__( self , SquareRootCtx_userIn : SquareRootCtx_class = SquareRootCtx_class() ) -> None:

      #Assign Parameter to Context Extended Dependency Object
      self.__SquareRootCtx : SquareRootCtx_class = SquareRootCtx_userIn
      if not(self.__SquareRootCtx.Initialized_ContextGetMethod()):
         self.__SquareRootCtx.checkedInit()

      #Variables
      self.sqrt : int
      #EndVariables

      #INITIALISATION of variables
      self.sqrt = P.NAT().PyChoice()

      #Check ALL Invariants if enabled.
      if P.DESIGN_BY_CONTRACT_ENABLED() and not(self.checkAllInvariants()):
         raise Exception("Invariants violated after INITIALISATION.")

   #Internal Context Dependency Object Get Method

   def SquareRootCtx_get(self) -> SquareRootCtx_class:
      return self.__SquareRootCtx

   #Variables Get/Set Methods

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

   #Check ALL Invariants

   def checkAllInvariants(self) -> bool:
      checkedAns_local : bool = True
      allInvariants_local : List[str] = [ "inv0" ]

      for Invariant_local in allInvariants_local:
         InvariantMethod_local = getattr(self,Invariant_local + "_invariantCheck")
         checkedAns_local = checkedAns_local and InvariantMethod_local()

      return checkedAns_local

   #End Check ALL Invariants Method

   #Events

   #SquareRoot - Event

   def SquareRoot_eventGuards(self) -> bool:
      guard_ans : bool = True

      #Set Parameters as an Attribute.

      #Check Event PreConditions.
      if P.DESIGN_BY_CONTRACT_ENABLED():
         try:
            if True:
               guard_ans = True
            else:
               guard_ans = False
         except:
            guard_ans = False
      else:
         guard_ans = True

      return guard_ans

   def SquareRoot_eventActions(self) -> None:

      if not(self.SquareRoot_eventGuards()):
         raise GuardsViolated("Guards of the Event could not be fulfilled.")

      #Set Parameters as an Attribute.

      #Event Actions

      self.sqrt = P.BecomesSuchThat((lambda boundIdentifiers : (P.NAT().PyContains(boundIdentifiers) and (boundIdentifiers * boundIdentifiers) <= self.SquareRootCtx_get().num and self.SquareRootCtx_get().num < ((boundIdentifiers + 1) * (boundIdentifiers + 1)))) , "int") 

      #Check Invariants after the actions are executed.
      if P.DESIGN_BY_CONTRACT_ENABLED() and not(self.checkAllInvariants()):
         raise Exception("PostConditions of the Event could not be fulfilled.")


   #End Event

   #User/Debugging Functions

   def __str__(self) -> str:
      tmp_values : List[str] = list()

      #Print Internal Context Constants
      tmp_values.append(self.__SquareRootCtx.__str__())

      #Print Variables
      tmp_values.append("###")
      tmp_values.append("Variables")

      tmp_values.append("sqrt ==> " + str(self.sqrt))

      return "\n".join(tmp_values)

   def __repr__(self) -> str:
      return self.__str__()

   def PyGuardsState(self) -> None:
      #This method will show which events (with no parameters) can be executed.
      tmp_values : List[str] = list()
      list_events_noparams : List[str] = ["SquareRoot"]
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
      list_events_strs : List[str] = ["SquareRoot"]
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
