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
from bbinMch_mch import *

#Machine Internal Context Dependencies
from bbinCtx_ctx import *


#Translation of Machine: bbinMchRef
#This machine refines the following machine: bbinMch_class
#This machine sees the following context: bbinCtx_class


class bbinMchRef_class(bbinMch_class):

   def __init__( self , bbinCtx_userIn : bbinCtx_class = bbinCtx_class() ) -> None:

      #Assign Parameter to Context Extended Dependency Object
      self.__bbinCtx : bbinCtx_class = bbinCtx_userIn
      if not(self.__bbinCtx.Initialized_ContextGetMethod()):
         self.__bbinCtx.checkedInit()

      #Variables
      self.p : int
      self.q : int
      self.r : int
      #EndVariables

      #INITIALISATION of variables
      self.p = 1
      self.q = self.bbinCtx_get().n
      self.r = PySet({int_range for int_range in range(1, self.bbinCtx_get().n+1)}).PyChoice()

      #Check ALL Invariants if enabled.
      if P.DESIGN_BY_CONTRACT_ENABLED() and not(self.checkAllInvariants()):
         raise Exception("Invariants violated after INITIALISATION.")

   #Internal Context Dependency Object Get Method

   def bbinCtx_get(self) -> bbinCtx_class:
      return self.__bbinCtx

   #Variables Get/Set Methods

   @property
   def p(self) -> int:
      return self.__p

   @p.setter
   def p(self, p_userIn : int) -> None:
      self.__p : int = p_userIn

   @property
   def q(self) -> int:
      return self.__q

   @q.setter
   def q(self, q_userIn : int) -> None:
      self.__q : int = q_userIn

   @property
   def r(self) -> int:
      return self.__r

   @r.setter
   def r(self, r_userIn : int) -> None:
      self.__r : int = r_userIn

   #End Variables Get Methods

   #Variant Method
   def PyMachineVariant(self) -> int:
      return (self.q - self.p)

   #Invariants Check Methods

   def inv1_invariantCheck(self) -> bool:
      return PySet({int_range for int_range in range(1, self.bbinCtx_get().n+1)}).PyContains(self.p)

   def inv2_invariantCheck(self) -> bool:
      return PySet({int_range for int_range in range(1, self.bbinCtx_get().n+1)}).PyContains(self.q)

   def inv3_invariantCheck(self) -> bool:
      return PySet({int_range for int_range in range(self.p, self.q+1)}).PyContains(self.r)

   def inv4_invariantCheck(self) -> bool:
      return self.bbinCtx_get().f[PySet({int_range for int_range in range(self.p, self.q+1)})].PyContains(self.bbinCtx_get().v)

   #Check ALL Invariants

   def checkAllInvariants(self) -> bool:
      checkedAns_local : bool = True
      allInvariants_local : List[str] = [ "inv1" , "inv2" , "inv3" , "inv4" ]

      for Invariant_local in allInvariants_local:
         InvariantMethod_local = getattr(self,Invariant_local + "_invariantCheck")
         checkedAns_local = checkedAns_local and InvariantMethod_local()

      return checkedAns_local

   #End Check ALL Invariants Method

   #Events

   #found - Event

   def found_eventGuards(self) -> bool:
      guard_ans : bool = True

      #Set Parameters as an Attribute.

      #Check Event PreConditions.
      if P.DESIGN_BY_CONTRACT_ENABLED():
         try:
            if True and (self.bbinCtx_get().f(self.r) == self.bbinCtx_get().v):
               guard_ans = True
            else:
               guard_ans = False
         except:
            guard_ans = False
      else:
         guard_ans = True

      return guard_ans

   def found_eventActions(self) -> None:

      attempt_Count : int = 0
      while not(self.found_eventGuards()):
         if attempt_Count == P.LOWMAXGENATTEMPTS():
            raise GuardsViolated("Guards of the Event could not be fulfilled.")
         attempt_Count += 1

      #Set Parameters as an Attribute.

      #Event Actions

      #Check Invariants after the actions are executed.


   #End Event

   #dec - Event

   def dec_eventGuards(self) -> bool:
      guard_ans : bool = True

      #Set Parameters as an Attribute.

      #Check Event PreConditions.
      if P.DESIGN_BY_CONTRACT_ENABLED():
         try:
            if True and (self.bbinCtx_get().f(self.r) > self.bbinCtx_get().v):
               guard_ans = True
            else:
               guard_ans = False
         except:
            guard_ans = False
      else:
         guard_ans = True

      return guard_ans

   #Convergent Event!
   def dec_eventActions(self) -> None:

      attempt_Count : int = 0
      while not(self.dec_eventGuards()):
         if attempt_Count == P.LOWMAXGENATTEMPTS():
            raise GuardsViolated("Guards of the Event could not be fulfilled.")
         attempt_Count += 1

      #Set Parameters as an Attribute.

      #Event Actions

      #Convergent Event: Value of the variant before the actions.
      tmp_variant_value : int = self.PyMachineVariant()

      self.q, self.r = (self.r - 1), PySet({int_range for int_range in range(self.p, (self.r - 1)+1)}).PyChoice()

      #Convergent Event: Check that the Variant decreased.
      if tmp_variant_value <= self.PyMachineVariant():
         raise Exception("The Variant did not decrease!")

      #Check Invariants after the actions are executed.
      if P.DESIGN_BY_CONTRACT_ENABLED() and not(self.checkAllInvariants()):
         raise Exception("PostConditions of the Event could not be fulfilled.")


   #End Event

   #inc - Event

   def inc_eventGuards(self) -> bool:
      guard_ans : bool = True

      #Set Parameters as an Attribute.

      #Check Event PreConditions.
      if P.DESIGN_BY_CONTRACT_ENABLED():
         try:
            if True and (self.bbinCtx_get().f(self.r) < self.bbinCtx_get().v):
               guard_ans = True
            else:
               guard_ans = False
         except:
            guard_ans = False
      else:
         guard_ans = True

      return guard_ans

   #Convergent Event!
   def inc_eventActions(self) -> None:

      attempt_Count : int = 0
      while not(self.inc_eventGuards()):
         if attempt_Count == P.LOWMAXGENATTEMPTS():
            raise GuardsViolated("Guards of the Event could not be fulfilled.")
         attempt_Count += 1

      #Set Parameters as an Attribute.

      #Event Actions

      #Convergent Event: Value of the variant before the actions.
      tmp_variant_value : int = self.PyMachineVariant()

      self.p, self.r = (self.r + 1), PySet({int_range for int_range in range((self.r + 1), self.q+1)}).PyChoice()

      #Convergent Event: Check that the Variant decreased.
      if tmp_variant_value <= self.PyMachineVariant():
         raise Exception("The Variant did not decrease!")

      #Check Invariants after the actions are executed.
      if P.DESIGN_BY_CONTRACT_ENABLED() and not(self.checkAllInvariants()):
         raise Exception("PostConditions of the Event could not be fulfilled.")


   #End Event

   #User/Debugging Functions

   def __str__(self) -> str:
      tmp_values : List[str] = list()

      #Print Internal Context Constants
      tmp_values.append(self.__bbinCtx.__str__())

      #Print Variables
      tmp_values.append("###")
      tmp_values.append("Variables")

      tmp_values.append("p ==> " + str(self.p))
      tmp_values.append("q ==> " + str(self.q))
      tmp_values.append("r ==> " + str(self.r))

      return "\n".join(tmp_values)

   def __repr__(self) -> str:
      return self.__str__()

   def PyGuardsState(self) -> None:
      #This method will show which events (with no parameters) can be executed.
      tmp_values : List[str] = list()
      list_events_noparams : List[str] = ["found", "dec", "inc"]
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
      list_events_strs : List[str] = ["found", "dec", "inc"]
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
