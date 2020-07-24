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
from HospitalCtx_ctx import *


#Translation of Machine: HospitalMch
#This machine sees the following context: HospitalCtx_class


class HospitalMch_class():

   def __init__( self , HospitalCtx_userIn : HospitalCtx_class = HospitalCtx_class() ) -> None:

      #Assign Parameter to Context Extended Dependency Object
      self.__HospitalCtx : HospitalCtx_class = HospitalCtx_userIn
      if not(self.__HospitalCtx.Initialized_ContextGetMethod()):
         self.__HospitalCtx.checkedInit()

      #Variables
      self.HeadNurse : HospitalState_CS
      self.InSurgeryCnt : int
      self.WaitingRoomCnt : int
      #EndVariables

      #INITIALISATION of variables
      self.WaitingRoomCnt = 0
      self.InSurgeryCnt = 0
      self.HeadNurse = self.HospitalCtx_get().Unavailable

      #Check ALL Invariants if enabled.
      if P.DESIGN_BY_CONTRACT_ENABLED() and not(self.checkAllInvariants()):
         raise Exception("Invariants violated after INITIALISATION.")

   #Internal Context Dependency Object Get Method

   def HospitalCtx_get(self) -> HospitalCtx_class:
      return self.__HospitalCtx

   #Variables Get/Set Methods

   @property
   def HeadNurse(self) -> HospitalState_CS:
      return self.__HeadNurse

   @HeadNurse.setter
   def HeadNurse(self, HeadNurse_userIn : HospitalState_CS) -> None:
      self.__HeadNurse : HospitalState_CS = HeadNurse_userIn

   @property
   def InSurgeryCnt(self) -> int:
      return self.__InSurgeryCnt

   @InSurgeryCnt.setter
   def InSurgeryCnt(self, InSurgeryCnt_userIn : int) -> None:
      self.__InSurgeryCnt : int = InSurgeryCnt_userIn

   @property
   def WaitingRoomCnt(self) -> int:
      return self.__WaitingRoomCnt

   @WaitingRoomCnt.setter
   def WaitingRoomCnt(self, WaitingRoomCnt_userIn : int) -> None:
      self.__WaitingRoomCnt : int = WaitingRoomCnt_userIn

   #End Variables Get Methods

   #Invariants Check Methods

   def inv0_invariantCheck(self) -> bool:
      return P.NAT().PyContains(self.WaitingRoomCnt)

   def inv1_invariantCheck(self) -> bool:
      return PySet({int_range for int_range in range(0, self.HospitalCtx_get().Capacity+1)}).PyContains(self.InSurgeryCnt)

   def inv2_invariantCheck(self) -> bool:
      return self.HospitalCtx_get().HospitalState.PyContains(self.HeadNurse)

   def inv3_invariantCheck(self) -> bool:
      return PyPrelude.LogicImplication(self.InSurgeryCnt != 0, self.HeadNurse == self.HospitalCtx_get().Available)

   #Check ALL Invariants

   def checkAllInvariants(self) -> bool:
      checkedAns_local : bool = True
      allInvariants_local : List[str] = [ "inv0" , "inv1" , "inv2" , "inv3" ]

      for Invariant_local in allInvariants_local:
         InvariantMethod_local = getattr(self,Invariant_local + "_invariantCheck")
         checkedAns_local = checkedAns_local and InvariantMethod_local()

      return checkedAns_local

   #End Check ALL Invariants Method

   #Events

   #PatientToRecovery - Event

   def PatientToRecovery_eventGuards(self) -> bool:
      guard_ans : bool = True

      #Set Parameters as an Attribute.

      #Check Event PreConditions.
      if P.DESIGN_BY_CONTRACT_ENABLED():
         try:
            if True and (self.InSurgeryCnt > 0):
               guard_ans = True
            else:
               guard_ans = False
         except:
            guard_ans = False
      else:
         guard_ans = True

      return guard_ans

   def PatientToRecovery_eventActions(self) -> None:

      attempt_Count : int = 0
      while not(self.PatientToRecovery_eventGuards()):
         if attempt_Count == P.LOWMAXGENATTEMPTS():
            raise GuardsViolated("Guards of the Event could not be fulfilled.")
         attempt_Count += 1

      #Set Parameters as an Attribute.

      #Event Actions

      self.InSurgeryCnt = (self.InSurgeryCnt - 1)

      #Check Invariants after the actions are executed.
      if P.DESIGN_BY_CONTRACT_ENABLED() and not(self.checkAllInvariants()):
         raise Exception("PostConditions of the Event could not be fulfilled.")


   #End Event

   #PatientToSurgery - Event

   def PatientToSurgery_eventGuards(self) -> bool:
      guard_ans : bool = True

      #Set Parameters as an Attribute.

      #Check Event PreConditions.
      if P.DESIGN_BY_CONTRACT_ENABLED():
         try:
            if True and (self.HeadNurse == self.HospitalCtx_get().Available) and (self.WaitingRoomCnt > 0) and (self.InSurgeryCnt < self.HospitalCtx_get().Capacity):
               guard_ans = True
            else:
               guard_ans = False
         except:
            guard_ans = False
      else:
         guard_ans = True

      return guard_ans

   def PatientToSurgery_eventActions(self) -> None:

      attempt_Count : int = 0
      while not(self.PatientToSurgery_eventGuards()):
         if attempt_Count == P.LOWMAXGENATTEMPTS():
            raise GuardsViolated("Guards of the Event could not be fulfilled.")
         attempt_Count += 1

      #Set Parameters as an Attribute.

      #Event Actions

      self.WaitingRoomCnt, self.InSurgeryCnt = (self.WaitingRoomCnt - 1), (self.InSurgeryCnt + 1)

      #Check Invariants after the actions are executed.
      if P.DESIGN_BY_CONTRACT_ENABLED() and not(self.checkAllInvariants()):
         raise Exception("PostConditions of the Event could not be fulfilled.")


   #End Event

   #PatientDeparture - Event

   def PatientDeparture_eventGuards(self) -> bool:
      guard_ans : bool = True

      #Set Parameters as an Attribute.

      #Check Event PreConditions.
      if P.DESIGN_BY_CONTRACT_ENABLED():
         try:
            if True and (self.WaitingRoomCnt != 0):
               guard_ans = True
            else:
               guard_ans = False
         except:
            guard_ans = False
      else:
         guard_ans = True

      return guard_ans

   def PatientDeparture_eventActions(self) -> None:

      attempt_Count : int = 0
      while not(self.PatientDeparture_eventGuards()):
         if attempt_Count == P.LOWMAXGENATTEMPTS():
            raise GuardsViolated("Guards of the Event could not be fulfilled.")
         attempt_Count += 1

      #Set Parameters as an Attribute.

      #Event Actions

      self.WaitingRoomCnt = (self.WaitingRoomCnt - 1)

      #Check Invariants after the actions are executed.
      if P.DESIGN_BY_CONTRACT_ENABLED() and not(self.checkAllInvariants()):
         raise Exception("PostConditions of the Event could not be fulfilled.")


   #End Event

   #HeadNurseDeparture - Event

   def HeadNurseDeparture_eventGuards(self) -> bool:
      guard_ans : bool = True

      #Set Parameters as an Attribute.

      #Check Event PreConditions.
      if P.DESIGN_BY_CONTRACT_ENABLED():
         try:
            if True and (self.HeadNurse == self.HospitalCtx_get().Available) and (self.InSurgeryCnt == 0):
               guard_ans = True
            else:
               guard_ans = False
         except:
            guard_ans = False
      else:
         guard_ans = True

      return guard_ans

   def HeadNurseDeparture_eventActions(self) -> None:

      attempt_Count : int = 0
      while not(self.HeadNurseDeparture_eventGuards()):
         if attempt_Count == P.LOWMAXGENATTEMPTS():
            raise GuardsViolated("Guards of the Event could not be fulfilled.")
         attempt_Count += 1

      #Set Parameters as an Attribute.

      #Event Actions

      self.HeadNurse = self.HospitalCtx_get().Unavailable

      #Check Invariants after the actions are executed.
      if P.DESIGN_BY_CONTRACT_ENABLED() and not(self.checkAllInvariants()):
         raise Exception("PostConditions of the Event could not be fulfilled.")


   #End Event

   #PatientArrival - Event

   def PatientArrival_eventGuards(self) -> bool:
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

   def PatientArrival_eventActions(self) -> None:

      if not(self.PatientArrival_eventGuards()):
         raise GuardsViolated("Guards of the Event could not be fulfilled.")

      #Set Parameters as an Attribute.

      #Event Actions

      self.WaitingRoomCnt = (self.WaitingRoomCnt + 1)

      #Check Invariants after the actions are executed.
      if P.DESIGN_BY_CONTRACT_ENABLED() and not(self.checkAllInvariants()):
         raise Exception("PostConditions of the Event could not be fulfilled.")


   #End Event

   #HeadNurseArrival - Event

   def HeadNurseArrival_eventGuards(self) -> bool:
      guard_ans : bool = True

      #Set Parameters as an Attribute.

      #Check Event PreConditions.
      if P.DESIGN_BY_CONTRACT_ENABLED():
         try:
            if True and (self.HeadNurse == self.HospitalCtx_get().Unavailable):
               guard_ans = True
            else:
               guard_ans = False
         except:
            guard_ans = False
      else:
         guard_ans = True

      return guard_ans

   def HeadNurseArrival_eventActions(self) -> None:

      attempt_Count : int = 0
      while not(self.HeadNurseArrival_eventGuards()):
         if attempt_Count == P.LOWMAXGENATTEMPTS():
            raise GuardsViolated("Guards of the Event could not be fulfilled.")
         attempt_Count += 1

      #Set Parameters as an Attribute.

      #Event Actions

      self.HeadNurse = self.HospitalCtx_get().Available

      #Check Invariants after the actions are executed.
      if P.DESIGN_BY_CONTRACT_ENABLED() and not(self.checkAllInvariants()):
         raise Exception("PostConditions of the Event could not be fulfilled.")


   #End Event

   #User/Debugging Functions

   def __str__(self) -> str:
      tmp_values : List[str] = list()

      #Print Internal Context Constants
      tmp_values.append(self.__HospitalCtx.__str__())

      #Print Variables
      tmp_values.append("###")
      tmp_values.append("Variables")

      tmp_values.append("HeadNurse ==> " + str(self.HeadNurse))
      tmp_values.append("InSurgeryCnt ==> " + str(self.InSurgeryCnt))
      tmp_values.append("WaitingRoomCnt ==> " + str(self.WaitingRoomCnt))

      return "\n".join(tmp_values)

   def __repr__(self) -> str:
      return self.__str__()

   def PyGuardsState(self) -> None:
      #This method will show which events (with no parameters) can be executed.
      tmp_values : List[str] = list()
      list_events_noparams : List[str] = ["PatientToRecovery", "PatientToSurgery", "PatientDeparture", "HeadNurseDeparture", "PatientArrival", "HeadNurseArrival"]
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
      list_events_strs : List[str] = ["PatientToRecovery", "PatientToSurgery", "PatientDeparture", "HeadNurseDeparture", "PatientArrival", "HeadNurseArrival"]
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
