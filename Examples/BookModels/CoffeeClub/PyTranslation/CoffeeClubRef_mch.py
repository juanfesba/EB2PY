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
from CoffeeClubMch_mch import *

#Machine Internal Context Dependencies
from CoffeeClubCtx_ctx import *


#Translation of Machine: CoffeeClubRef
#This machine refines the following machine: CoffeeClubMch_class
#This machine sees the following context: CoffeeClubCtx_class


class CoffeeClubRef_class(CoffeeClubMch_class):

   def __init__( self , CoffeeClubCtx_userIn : CoffeeClubCtx_class = CoffeeClubCtx_class() ) -> None:

      #Assign Parameter to Context Extended Dependency Object
      self.__CoffeeClubCtx : CoffeeClubCtx_class = CoffeeClubCtx_userIn
      if not(self.__CoffeeClubCtx.Initialized_ContextGetMethod()):
         self.__CoffeeClubCtx.checkedInit()

      #Variables
      self.accounts : PyRel[MEMBER_CS,int]
      self.coffeeprice : int
      self.members : PySet[MEMBER_CS]
      self.piggybank : int
      #EndVariables

      #INITIALISATION of variables
      self.piggybank = 0
      self.members = PySet()
      self.accounts = PySet()
      self.coffeeprice = P.NAT1().PyChoice()

      #Check ALL Invariants if enabled.
      if P.DESIGN_BY_CONTRACT_ENABLED() and not(self.checkAllInvariants()):
         raise Exception("Invariants violated after INITIALISATION.")

   #Internal Context Dependency Object Get Method

   def CoffeeClubCtx_get(self) -> CoffeeClubCtx_class:
      return self.__CoffeeClubCtx

   #Variables Get/Set Methods

   @property
   def accounts(self) -> PyRel[MEMBER_CS,int]:
      return self.__accounts

   @accounts.setter
   def accounts(self, accounts_userIn : PyRel[MEMBER_CS,int]) -> None:
      self.__accounts : PyRel[MEMBER_CS,int] = accounts_userIn

   @property
   def coffeeprice(self) -> int:
      return self.__coffeeprice

   @coffeeprice.setter
   def coffeeprice(self, coffeeprice_userIn : int) -> None:
      self.__coffeeprice : int = coffeeprice_userIn

   @property
   def members(self) -> PySet[MEMBER_CS]:
      return self.__members

   @members.setter
   def members(self, members_userIn : PySet[MEMBER_CS]) -> None:
      self.__members : PySet[MEMBER_CS] = members_userIn

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

   def inv10_invariantCheck(self) -> bool:
      return self.members.PyIsSubset(self.CoffeeClubCtx_get().MEMBER)

   def inv11_invariantCheck(self) -> bool:
      return PyFamilies(PyFamilyTypes.TotalFunctions, self.members, P.NAT()).PyContains(self.accounts)

   def inv12_invariantCheck(self) -> bool:
      return P.NAT1().PyContains(self.coffeeprice)

   #Check ALL Invariants

   def checkAllInvariants(self) -> bool:
      checkedAns_local : bool = True
      allInvariants_local : List[str] = [ "inv1" , "inv10" , "inv11" , "inv12" ]

      for Invariant_local in allInvariants_local:
         InvariantMethod_local = getattr(self,Invariant_local + "_invariantCheck")
         checkedAns_local = checkedAns_local and InvariantMethod_local()

      return checkedAns_local

   #End Check ALL Invariants Method

   #Events

   #SetPrice - Event

   def SetPrice_eventGuards(self, new_price_userIn : int) -> bool:
      guard_ans : bool = True

      #Set Parameters as an Attribute.
      self.new_price : int = new_price_userIn

      #Check Event PreConditions.
      if P.DESIGN_BY_CONTRACT_ENABLED():
         try:
            if True and (PySet({int_range for int_range in range(1, 30+1)}).PyContains(self.new_price)):
               guard_ans = True
            else:
               guard_ans = False
         except:
            guard_ans = False
      else:
         guard_ans = True

      del(self.new_price)
      return guard_ans

   def SetPrice_eventActions(self, new_price_userIn : int = P.NoParam()) -> None:

      if new_price_userIn is None:
         new_price_userIn = P.PyRandValGen("int")

      attempt_Count : int = 0
      while not(self.SetPrice_eventGuards(new_price_userIn)):
         new_price_userIn = P.PyRandValGen("int")
         if attempt_Count == P.LOWMAXGENATTEMPTS():
            raise GuardsViolated("Guards of the Event could not be fulfilled.")
         attempt_Count += 1

      #Set Parameters as an Attribute.
      self.new_price = new_price_userIn

      #Event Actions

      self.coffeeprice = self.new_price

      #Check Invariants after the actions are executed.
      if P.DESIGN_BY_CONTRACT_ENABLED() and not(self.checkAllInvariants()):
         raise Exception("PostConditions of the Event could not be fulfilled.")

      del(self.new_price)

   #End Event

   #BuyCoffee - Event

   def BuyCoffee_eventGuards(self, member_buy_userIn : MEMBER_CS) -> bool:
      guard_ans : bool = True

      #Set Parameters as an Attribute.
      self.member_buy : MEMBER_CS = member_buy_userIn

      #Check Event PreConditions.
      if P.DESIGN_BY_CONTRACT_ENABLED():
         try:
            if True and (self.accounts(self.member_buy) >= self.coffeeprice) and (self.members.PyContains(self.member_buy)):
               guard_ans = True
            else:
               guard_ans = False
         except:
            guard_ans = False
      else:
         guard_ans = True

      del(self.member_buy)
      return guard_ans

   def BuyCoffee_eventActions(self, member_buy_userIn : MEMBER_CS = P.NoParam()) -> None:

      if member_buy_userIn is None:
         member_buy_userIn = P.PyRandValGen("MEMBER_CS")

      attempt_Count : int = 0
      while not(self.BuyCoffee_eventGuards(member_buy_userIn)):
         member_buy_userIn = P.PyRandValGen("MEMBER_CS")
         if attempt_Count == P.LOWMAXGENATTEMPTS():
            raise GuardsViolated("Guards of the Event could not be fulfilled.")
         attempt_Count += 1

      #Set Parameters as an Attribute.
      self.member_buy = member_buy_userIn

      #Event Actions

      self.accounts = self.accounts.PyOverriding(PyRel({(self.member_buy, (self.accounts(self.member_buy) - self.coffeeprice))}))

      #Check Invariants after the actions are executed.
      if P.DESIGN_BY_CONTRACT_ENABLED() and not(self.checkAllInvariants()):
         raise Exception("PostConditions of the Event could not be fulfilled.")

      del(self.member_buy)

   #End Event

   #NewMember - Event

   def NewMember_eventGuards(self, new_member_userIn : MEMBER_CS) -> bool:
      guard_ans : bool = True

      #Set Parameters as an Attribute.
      self.new_member : MEMBER_CS = new_member_userIn

      #Check Event PreConditions.
      if P.DESIGN_BY_CONTRACT_ENABLED():
         try:
            if True and (self.CoffeeClubCtx_get().MEMBER.PyDifference(self.members).PyContains(self.new_member)):
               guard_ans = True
            else:
               guard_ans = False
         except:
            guard_ans = False
      else:
         guard_ans = True

      del(self.new_member)
      return guard_ans

   def NewMember_eventActions(self, new_member_userIn : MEMBER_CS = P.NoParam()) -> None:

      if new_member_userIn is None:
         new_member_userIn = P.PyRandValGen("MEMBER_CS")

      attempt_Count : int = 0
      while not(self.NewMember_eventGuards(new_member_userIn)):
         new_member_userIn = P.PyRandValGen("MEMBER_CS")
         if attempt_Count == P.LOWMAXGENATTEMPTS():
            raise GuardsViolated("Guards of the Event could not be fulfilled.")
         attempt_Count += 1

      #Set Parameters as an Attribute.
      self.new_member = new_member_userIn

      #Event Actions

      self.accounts, self.members = self.accounts.PyOverriding(PyRel({(self.new_member, 0)})), self.members.PyUnion(PySet({self.new_member}))

      #Check Invariants after the actions are executed.
      if P.DESIGN_BY_CONTRACT_ENABLED() and not(self.checkAllInvariants()):
         raise Exception("PostConditions of the Event could not be fulfilled.")

      del(self.new_member)

   #End Event

   #Contribute - Event

   def Contribute_eventGuards(self, contribution_userIn : int, member_userIn : MEMBER_CS) -> bool:
      guard_ans : bool = True

      #Set Parameters as an Attribute.
      self.contribution : int = contribution_userIn
      self.member : MEMBER_CS = member_userIn

      #Check Event PreConditions.
      if P.DESIGN_BY_CONTRACT_ENABLED():
         try:
            if True and (PySet({int_range for int_range in range(1, 70+1)}).PyContains(self.contribution)) and (self.members.PyContains(self.member)):
               guard_ans = True
            else:
               guard_ans = False
         except:
            guard_ans = False
      else:
         guard_ans = True

      del(self.contribution)
      del(self.member)
      return guard_ans

   def Contribute_eventActions(self, contribution_userIn : int = P.NoParam(), member_userIn : MEMBER_CS = P.NoParam()) -> None:

      if contribution_userIn is None:
         contribution_userIn = P.PyRandValGen("int")
      if member_userIn is None:
         member_userIn = P.PyRandValGen("MEMBER_CS")

      attempt_Count : int = 0
      while not(self.Contribute_eventGuards(contribution_userIn, member_userIn)):
         contribution_userIn = P.PyRandValGen("int")
         member_userIn = P.PyRandValGen("MEMBER_CS")
         if attempt_Count == P.LOWMAXGENATTEMPTS():
            raise GuardsViolated("Guards of the Event could not be fulfilled.")
         attempt_Count += 1

      #Set Parameters as an Attribute.
      self.contribution = contribution_userIn
      self.member = member_userIn

      #Event Actions

      self.accounts, self.piggybank = self.accounts.PyOverriding(PyRel({(self.member, (self.accounts(self.member) + self.contribution))})), (self.piggybank + self.contribution)

      #Check Invariants after the actions are executed.
      if P.DESIGN_BY_CONTRACT_ENABLED() and not(self.checkAllInvariants()):
         raise Exception("PostConditions of the Event could not be fulfilled.")

      del(self.contribution)
      del(self.member)

   #End Event

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

      #Print Internal Context Constants
      tmp_values.append(self.__CoffeeClubCtx.__str__())

      #Print Variables
      tmp_values.append("###")
      tmp_values.append("Variables")

      tmp_values.append("accounts ==> " + str(self.accounts))
      tmp_values.append("coffeeprice ==> " + str(self.coffeeprice))
      tmp_values.append("members ==> " + str(self.members))
      tmp_values.append("piggybank ==> " + str(self.piggybank))

      return "\n".join(tmp_values)

   def __repr__(self) -> str:
      return self.__str__()

   def PyGuardsState(self) -> None:
      #This method will show which events (with no parameters) can be executed.
      tmp_values : List[str] = list()
      list_events_noparams : List[str] = []
      list_events_params : List[Tuple[str,List[str]]] = [("SetPrice",["int"]), ("BuyCoffee",["MEMBER_CS"]), ("NewMember",["MEMBER_CS"]), ("Contribute",["int", "MEMBER_CS"]), ("FeedBank",["int"]), ("RobBank",["int"])]
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
      list_events_strs : List[str] = ["SetPrice", "BuyCoffee", "NewMember", "Contribute", "FeedBank", "RobBank"]
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
