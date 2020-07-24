#DEPENDENCIES

#Allow Path Access to the Prelude's Directory

import sys
if not(".." in sys.path):
   sys.path.append("..")

#Utilities Dependencies
from Py_Preludes import *

#Typing Dependencies
from typing import List


#Translation of Machine: CoffeeClubMch


class CoffeeClubMch_class():

   def __init__( self ) -> None:

      #Variables
      self.piggybank : int
      #EndVariables

      #INITIALISATION of variables
      self.piggybank = 0

      #Check ALL Invariants if enabled.
      if P.DESIGN_BY_CONTRACT_ENABLED() and not(self.checkAllInvariants()):
         raise Exception("Invariants violated after INITIALISATION.")

   #Variables Get/Set Methods

   @property
   def piggybank(self) -> int:
      return self.__piggybank

   @piggybank.setter
   def piggybank(self, piggybank_userIn : int) -> None:
      self.__piggybank : int = piggybank_userIn

   #End Variables Get Methods

   #Invariants Check Methods

   def inv1_invariantCheck(self) -> bool:
      return P.NAT().PyContains(self.piggybank)

   #Check ALL Invariants

   def checkAllInvariants(self) -> bool:
      checkedAns_local : bool = True
      allInvariants_local : List[str] = [ "inv1" ]

      for Invariant_local in allInvariants_local:
         InvariantMethod_local = getattr(self,Invariant_local + "_invariantCheck")
         checkedAns_local = checkedAns_local and InvariantMethod_local()

      return checkedAns_local

   #End Check ALL Invariants Method

   #Events

   #FeedBank - Event

   def FeedBank_eventGuards(self, amount_feed_userIn : int) -> bool:
      guard_ans : bool = True

      #Set Parameters as an Attribute.
      self.amount_feed : int = amount_feed_userIn

      #Check Event PreConditions.
      if P.DESIGN_BY_CONTRACT_ENABLED():
         try:
            if True and (PySet({int_range for int_range in range(1, 100+1)}).PyContains(self.amount_feed)):
               guard_ans = True
            else:
               guard_ans = False
         except:
            guard_ans = False
      else:
         guard_ans = True

      del(self.amount_feed)
      return guard_ans

   def FeedBank_eventActions(self, amount_feed_userIn : int = P.NoParam()) -> None:

      if amount_feed_userIn is None:
         amount_feed_userIn = P.PyRandValGen("int")

      attempt_Count : int = 0
      while not(self.FeedBank_eventGuards(amount_feed_userIn)):
         amount_feed_userIn = P.PyRandValGen("int")
         if attempt_Count == P.LOWMAXGENATTEMPTS():
            raise GuardsViolated("Guards of the Event could not be fulfilled.")
         attempt_Count += 1

      #Set Parameters as an Attribute.
      self.amount_feed = amount_feed_userIn

      #Event Actions

      self.piggybank = (self.piggybank + self.amount_feed)

      #Check Invariants after the actions are executed.
      if P.DESIGN_BY_CONTRACT_ENABLED() and not(self.checkAllInvariants()):
         raise Exception("PostConditions of the Event could not be fulfilled.")

      del(self.amount_feed)

   #End Event

   #RobBank - Event

   def RobBank_eventGuards(self, amount_rob_userIn : int) -> bool:
      guard_ans : bool = True

      #Set Parameters as an Attribute.
      self.amount_rob : int = amount_rob_userIn

      #Check Event PreConditions.
      if P.DESIGN_BY_CONTRACT_ENABLED():
         try:
            if True and (PySet({int_range for int_range in range(1, 50+1)}).PyContains(self.amount_rob)) and (self.amount_rob <= self.piggybank):
               guard_ans = True
            else:
               guard_ans = False
         except:
            guard_ans = False
      else:
         guard_ans = True

      del(self.amount_rob)
      return guard_ans

   def RobBank_eventActions(self, amount_rob_userIn : int = P.NoParam()) -> None:

      if amount_rob_userIn is None:
         amount_rob_userIn = P.PyRandValGen("int")

      attempt_Count : int = 0
      while not(self.RobBank_eventGuards(amount_rob_userIn)):
         amount_rob_userIn = P.PyRandValGen("int")
         if attempt_Count == P.LOWMAXGENATTEMPTS():
            raise GuardsViolated("Guards of the Event could not be fulfilled.")
         attempt_Count += 1

      #Set Parameters as an Attribute.
      self.amount_rob = amount_rob_userIn

      #Event Actions

      self.piggybank = (self.piggybank - self.amount_rob)

      #Check Invariants after the actions are executed.
      if P.DESIGN_BY_CONTRACT_ENABLED() and not(self.checkAllInvariants()):
         raise Exception("PostConditions of the Event could not be fulfilled.")

      del(self.amount_rob)

   #End Event

   #User/Debugging Functions

   def __str__(self) -> str:
      tmp_values : List[str] = list()

      #Print Variables
      tmp_values.append("###")
      tmp_values.append("Variables")

      tmp_values.append("piggybank ==> " + str(self.piggybank))

      return "\n".join(tmp_values)

   def __repr__(self) -> str:
      return self.__str__()

   def PyGuardsState(self) -> None:
      #This method will show which events (with no parameters) can be executed.
      tmp_values : List[str] = list()
      list_events_noparams : List[str] = []
      list_events_params : List[Tuple[str,List[str]]] = [("FeedBank",["int"]), ("RobBank",["int"])]
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
      list_events_strs : List[str] = ["FeedBank", "RobBank"]
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
