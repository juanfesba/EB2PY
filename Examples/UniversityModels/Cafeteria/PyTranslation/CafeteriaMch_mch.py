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
from CafeteriaCtx_ctx import *


#Translation of Machine: CafeteriaMch
#This machine sees the following context: CafeteriaCtx_class


class CafeteriaMch_class():

   def __init__( self , CafeteriaCtx_userIn : CafeteriaCtx_class = CafeteriaCtx_class() ) -> None:

      #Assign Parameter to Context Extended Dependency Object
      self.__CafeteriaCtx : CafeteriaCtx_class = CafeteriaCtx_userIn
      if not(self.__CafeteriaCtx.Initialized_ContextGetMethod()):
         self.__CafeteriaCtx.checkedInit()

      #Variables
      self.AvailableDishCnt : int
      self.ClientsEatingCnt : int
      self.ClientsInQueueCnt : int
      #EndVariables

      #INITIALISATION of variables
      self.ClientsInQueueCnt = 0
      self.AvailableDishCnt = 0
      self.ClientsEatingCnt = 0

      #Check ALL Invariants if enabled.
      if P.DESIGN_BY_CONTRACT_ENABLED() and not(self.checkAllInvariants()):
         raise Exception("Invariants violated after INITIALISATION.")

   #Internal Context Dependency Object Get Method

   def CafeteriaCtx_get(self) -> CafeteriaCtx_class:
      return self.__CafeteriaCtx

   #Variables Get/Set Methods

   @property
   def AvailableDishCnt(self) -> int:
      return self.__AvailableDishCnt

   @AvailableDishCnt.setter
   def AvailableDishCnt(self, AvailableDishCnt_userIn : int) -> None:
      self.__AvailableDishCnt : int = AvailableDishCnt_userIn

   @property
   def ClientsEatingCnt(self) -> int:
      return self.__ClientsEatingCnt

   @ClientsEatingCnt.setter
   def ClientsEatingCnt(self, ClientsEatingCnt_userIn : int) -> None:
      self.__ClientsEatingCnt : int = ClientsEatingCnt_userIn

   @property
   def ClientsInQueueCnt(self) -> int:
      return self.__ClientsInQueueCnt

   @ClientsInQueueCnt.setter
   def ClientsInQueueCnt(self, ClientsInQueueCnt_userIn : int) -> None:
      self.__ClientsInQueueCnt : int = ClientsInQueueCnt_userIn

   #End Variables Get Methods

   #Invariants Check Methods

   def inv0_invariantCheck(self) -> bool:
      return P.NAT().PyContains(self.ClientsInQueueCnt)

   def inv1_invariantCheck(self) -> bool:
      return P.NAT().PyContains(self.AvailableDishCnt)

   def inv2_invariantCheck(self) -> bool:
      return PySet({int_range for int_range in range(0, self.CafeteriaCtx_get().MaxChairCnt+1)}).PyContains(self.ClientsEatingCnt)

   #Check ALL Invariants

   def checkAllInvariants(self) -> bool:
      checkedAns_local : bool = True
      allInvariants_local : List[str] = [ "inv0" , "inv1" , "inv2" ]

      for Invariant_local in allInvariants_local:
         InvariantMethod_local = getattr(self,Invariant_local + "_invariantCheck")
         checkedAns_local = checkedAns_local and InvariantMethod_local()

      return checkedAns_local

   #End Check ALL Invariants Method

   #Events

   #AddDishes - Event

   def AddDishes_eventGuards(self, ad_userIn : int) -> bool:
      guard_ans : bool = True

      #Set Parameters as an Attribute.
      self.ad : int = ad_userIn

      #Check Event PreConditions.
      if P.DESIGN_BY_CONTRACT_ENABLED():
         try:
            if True and (PySet({int_range for int_range in range(1, 40+1)}).PyContains(self.ad)):
               guard_ans = True
            else:
               guard_ans = False
         except:
            guard_ans = False
      else:
         guard_ans = True

      del(self.ad)
      return guard_ans

   def AddDishes_eventActions(self, ad_userIn : int = P.NoParam()) -> None:

      if ad_userIn is None:
         ad_userIn = P.PyRandValGen("int")

      attempt_Count : int = 0
      while not(self.AddDishes_eventGuards(ad_userIn)):
         ad_userIn = P.PyRandValGen("int")
         if attempt_Count == P.LOWMAXGENATTEMPTS():
            raise GuardsViolated("Guards of the Event could not be fulfilled.")
         attempt_Count += 1

      #Set Parameters as an Attribute.
      self.ad = ad_userIn

      #Event Actions

      self.AvailableDishCnt = (self.AvailableDishCnt + self.ad)

      #Check Invariants after the actions are executed.
      if P.DESIGN_BY_CONTRACT_ENABLED() and not(self.checkAllInvariants()):
         raise Exception("PostConditions of the Event could not be fulfilled.")

      del(self.ad)

   #End Event

   #ExitCafeteria - Event

   def ExitCafeteria_eventGuards(self, ce_userIn : int) -> bool:
      guard_ans : bool = True

      #Set Parameters as an Attribute.
      self.ce : int = ce_userIn

      #Check Event PreConditions.
      if P.DESIGN_BY_CONTRACT_ENABLED():
         try:
            if True and (PySet({int_range for int_range in range(1, self.ClientsEatingCnt+1)}).PyContains(self.ce)):
               guard_ans = True
            else:
               guard_ans = False
         except:
            guard_ans = False
      else:
         guard_ans = True

      del(self.ce)
      return guard_ans

   def ExitCafeteria_eventActions(self, ce_userIn : int = P.NoParam()) -> None:

      if ce_userIn is None:
         ce_userIn = P.PyRandValGen("int")

      attempt_Count : int = 0
      while not(self.ExitCafeteria_eventGuards(ce_userIn)):
         ce_userIn = P.PyRandValGen("int")
         if attempt_Count == P.LOWMAXGENATTEMPTS():
            raise GuardsViolated("Guards of the Event could not be fulfilled.")
         attempt_Count += 1

      #Set Parameters as an Attribute.
      self.ce = ce_userIn

      #Event Actions

      self.ClientsEatingCnt = (self.ClientsEatingCnt - self.ce)

      #Check Invariants after the actions are executed.
      if P.DESIGN_BY_CONTRACT_ENABLED() and not(self.checkAllInvariants()):
         raise Exception("PostConditions of the Event could not be fulfilled.")

      del(self.ce)

   #End Event

   #ArriveInQueue - Event

   def ArriveInQueue_eventGuards(self, ca_userIn : int) -> bool:
      guard_ans : bool = True

      #Set Parameters as an Attribute.
      self.ca : int = ca_userIn

      #Check Event PreConditions.
      if P.DESIGN_BY_CONTRACT_ENABLED():
         try:
            if True and (PySet({int_range for int_range in range(1, 50+1)}).PyContains(self.ca)):
               guard_ans = True
            else:
               guard_ans = False
         except:
            guard_ans = False
      else:
         guard_ans = True

      del(self.ca)
      return guard_ans

   def ArriveInQueue_eventActions(self, ca_userIn : int = P.NoParam()) -> None:

      if ca_userIn is None:
         ca_userIn = P.PyRandValGen("int")

      attempt_Count : int = 0
      while not(self.ArriveInQueue_eventGuards(ca_userIn)):
         ca_userIn = P.PyRandValGen("int")
         if attempt_Count == P.LOWMAXGENATTEMPTS():
            raise GuardsViolated("Guards of the Event could not be fulfilled.")
         attempt_Count += 1

      #Set Parameters as an Attribute.
      self.ca = ca_userIn

      #Event Actions

      self.ClientsInQueueCnt = (self.ClientsInQueueCnt + self.ca)

      #Check Invariants after the actions are executed.
      if P.DESIGN_BY_CONTRACT_ENABLED() and not(self.checkAllInvariants()):
         raise Exception("PostConditions of the Event could not be fulfilled.")

      del(self.ca)

   #End Event

   #ServeClients - Event

   def ServeClients_eventGuards(self, c_userIn : int, d_userIn : int) -> bool:
      guard_ans : bool = True

      #Set Parameters as an Attribute.
      self.c : int = c_userIn
      self.d : int = d_userIn

      #Check Event PreConditions.
      if P.DESIGN_BY_CONTRACT_ENABLED():
         try:
            if True and (PySet({int_range for int_range in range(1, P.Minimum(PySet({self.ClientsInQueueCnt, self.AvailableDishCnt, (self.CafeteriaCtx_get().MaxChairCnt - self.ClientsEatingCnt)}))+1)}).PyContains(self.c)) and (PySet({int_range for int_range in range(1, self.c+1)}).PyContains(self.d)):
               guard_ans = True
            else:
               guard_ans = False
         except:
            guard_ans = False
      else:
         guard_ans = True

      del(self.c)
      del(self.d)
      return guard_ans

   def ServeClients_eventActions(self, c_userIn : int = P.NoParam(), d_userIn : int = P.NoParam()) -> None:

      if c_userIn is None:
         c_userIn = P.PyRandValGen("int")
      if d_userIn is None:
         d_userIn = P.PyRandValGen("int")

      attempt_Count : int = 0
      while not(self.ServeClients_eventGuards(c_userIn, d_userIn)):
         c_userIn = P.PyRandValGen("int")
         d_userIn = P.PyRandValGen("int")
         if attempt_Count == P.LOWMAXGENATTEMPTS():
            raise GuardsViolated("Guards of the Event could not be fulfilled.")
         attempt_Count += 1

      #Set Parameters as an Attribute.
      self.c = c_userIn
      self.d = d_userIn

      #Event Actions

      self.ClientsInQueueCnt, self.AvailableDishCnt, self.ClientsEatingCnt = (self.ClientsInQueueCnt - self.c), (self.AvailableDishCnt - self.d), (self.ClientsEatingCnt + self.c)

      #Check Invariants after the actions are executed.
      if P.DESIGN_BY_CONTRACT_ENABLED() and not(self.checkAllInvariants()):
         raise Exception("PostConditions of the Event could not be fulfilled.")

      del(self.c)
      del(self.d)

   #End Event

   #LeaveQueue - Event

   def LeaveQueue_eventGuards(self, cl_userIn : int) -> bool:
      guard_ans : bool = True

      #Set Parameters as an Attribute.
      self.cl : int = cl_userIn

      #Check Event PreConditions.
      if P.DESIGN_BY_CONTRACT_ENABLED():
         try:
            if True and (PySet({int_range for int_range in range(1, self.ClientsInQueueCnt+1)}).PyContains(self.cl)):
               guard_ans = True
            else:
               guard_ans = False
         except:
            guard_ans = False
      else:
         guard_ans = True

      del(self.cl)
      return guard_ans

   def LeaveQueue_eventActions(self, cl_userIn : int = P.NoParam()) -> None:

      if cl_userIn is None:
         cl_userIn = P.PyRandValGen("int")

      attempt_Count : int = 0
      while not(self.LeaveQueue_eventGuards(cl_userIn)):
         cl_userIn = P.PyRandValGen("int")
         if attempt_Count == P.LOWMAXGENATTEMPTS():
            raise GuardsViolated("Guards of the Event could not be fulfilled.")
         attempt_Count += 1

      #Set Parameters as an Attribute.
      self.cl = cl_userIn

      #Event Actions

      self.ClientsInQueueCnt = (self.ClientsInQueueCnt - self.cl)

      #Check Invariants after the actions are executed.
      if P.DESIGN_BY_CONTRACT_ENABLED() and not(self.checkAllInvariants()):
         raise Exception("PostConditions of the Event could not be fulfilled.")

      del(self.cl)

   #End Event

   #User/Debugging Functions

   def __str__(self) -> str:
      tmp_values : List[str] = list()

      #Print Internal Context Constants
      tmp_values.append(self.__CafeteriaCtx.__str__())

      #Print Variables
      tmp_values.append("###")
      tmp_values.append("Variables")

      tmp_values.append("AvailableDishCnt ==> " + str(self.AvailableDishCnt))
      tmp_values.append("ClientsEatingCnt ==> " + str(self.ClientsEatingCnt))
      tmp_values.append("ClientsInQueueCnt ==> " + str(self.ClientsInQueueCnt))

      return "\n".join(tmp_values)

   def __repr__(self) -> str:
      return self.__str__()

   def PyGuardsState(self) -> None:
      #This method will show which events (with no parameters) can be executed.
      tmp_values : List[str] = list()
      list_events_noparams : List[str] = []
      list_events_params : List[Tuple[str,List[str]]] = [("AddDishes",["int"]), ("ExitCafeteria",["int"]), ("ArriveInQueue",["int"]), ("ServeClients",["int", "int"]), ("LeaveQueue",["int"])]
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
      list_events_strs : List[str] = ["AddDishes", "ExitCafeteria", "ArriveInQueue", "ServeClients", "LeaveQueue"]
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
