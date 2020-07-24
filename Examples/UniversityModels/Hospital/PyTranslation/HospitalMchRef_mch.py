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
from HospitalMch_mch import *

#Machine Internal Context Dependencies
from HospitalCtxExt_ctx import *


#Translation of Machine: HospitalMchRef
#This machine refines the following machine: HospitalMch_class
#This machine sees the following context: HospitalCtxExt_class


class HospitalMchRef_class(HospitalMch_class):

   def __init__( self , HospitalCtxExt_userIn : HospitalCtxExt_class = HospitalCtxExt_class() ) -> None:

      #Assign Parameter to Context Extended Dependency Object
      self.__HospitalCtxExt : HospitalCtxExt_class = HospitalCtxExt_userIn
      if not(self.__HospitalCtxExt.Initialized_ContextGetMethod()):
         self.__HospitalCtxExt.checkedInit()

      #Variables
      self.HeadNurse : HospitalState_CS
      self.InSurgeryCnt : int
      self.MDCnt : int
      self.NurseCnt : int
      self.SurgeryCnt : int
      self.WaitingRoomCnt : int
      #EndVariables

      #INITIALISATION of variables
      self.WaitingRoomCnt = 0
      self.InSurgeryCnt = 0
      self.HeadNurse = self.HospitalCtxExt_get().HospitalCtx_get().Unavailable
      self.NurseCnt = 0
      self.MDCnt = 0
      self.SurgeryCnt = 0

      #Check ALL Invariants if enabled.
      if P.DESIGN_BY_CONTRACT_ENABLED() and not(self.checkAllInvariants()):
         raise Exception("Invariants violated after INITIALISATION.")

   #Internal Context Dependency Object Get Method

   def HospitalCtxExt_get(self) -> HospitalCtxExt_class:
      return self.__HospitalCtxExt

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
   def MDCnt(self) -> int:
      return self.__MDCnt

   @MDCnt.setter
   def MDCnt(self, MDCnt_userIn : int) -> None:
      self.__MDCnt : int = MDCnt_userIn

   @property
   def NurseCnt(self) -> int:
      return self.__NurseCnt

   @NurseCnt.setter
   def NurseCnt(self, NurseCnt_userIn : int) -> None:
      self.__NurseCnt : int = NurseCnt_userIn

   @property
   def SurgeryCnt(self) -> int:
      return self.__SurgeryCnt

   @SurgeryCnt.setter
   def SurgeryCnt(self, SurgeryCnt_userIn : int) -> None:
      self.__SurgeryCnt : int = SurgeryCnt_userIn

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
      return PySet({int_range for int_range in range(0, self.HospitalCtxExt_get().HospitalCtx_get().Capacity+1)}).PyContains(self.InSurgeryCnt)

   def inv10_invariantCheck(self) -> bool:
      return P.NAT().PyContains(self.NurseCnt)

   def inv11_invariantCheck(self) -> bool:
      return PySet({int_range for int_range in range(0, self.HospitalCtxExt_get().MaxMDCap+1)}).PyContains(self.MDCnt)

   def inv12_invariantCheck(self) -> bool:
      return P.NAT().PyContains(self.SurgeryCnt)

   def inv2_invariantCheck(self) -> bool:
      return self.HospitalCtxExt_get().HospitalCtx_get().HospitalState.PyContains(self.HeadNurse)

   def inv3_invariantCheck(self) -> bool:
      return PyPrelude.LogicImplication(self.InSurgeryCnt != 0, self.HeadNurse == self.HospitalCtxExt_get().HospitalCtx_get().Available)

   #Check ALL Invariants

   def checkAllInvariants(self) -> bool:
      checkedAns_local : bool = True
      allInvariants_local : List[str] = [ "inv0" , "inv1" , "inv10" , "inv11" , "inv12" , "inv2" , "inv3" ]

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

      self.InSurgeryCnt, self.MDCnt, self.SurgeryCnt = (self.InSurgeryCnt - 1), (self.MDCnt + 1), (self.SurgeryCnt + 1)

      #Check Invariants after the actions are executed.
      if P.DESIGN_BY_CONTRACT_ENABLED() and not(self.checkAllInvariants()):
         raise Exception("PostConditions of the Event could not be fulfilled.")


   #End Event

   #MDDeparture - Event

   def MDDeparture_eventGuards(self) -> bool:
      guard_ans : bool = True

      #Set Parameters as an Attribute.

      #Check Event PreConditions.
      if P.DESIGN_BY_CONTRACT_ENABLED():
         try:
            if True and (self.MDCnt > 0):
               guard_ans = True
            else:
               guard_ans = False
         except:
            guard_ans = False
      else:
         guard_ans = True

      return guard_ans

   def MDDeparture_eventActions(self) -> None:

      attempt_Count : int = 0
      while not(self.MDDeparture_eventGuards()):
         if attempt_Count == P.LOWMAXGENATTEMPTS():
            raise GuardsViolated("Guards of the Event could not be fulfilled.")
         attempt_Count += 1

      #Set Parameters as an Attribute.

      #Event Actions

      self.MDCnt = (self.MDCnt - 1)

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

   #PatientToSurgeryRef - Event

   def PatientToSurgeryRef_eventGuards(self, n_userIn : int) -> bool:
      guard_ans : bool = True

      #Set Parameters as an Attribute.
      self.n : int = n_userIn

      #Check Event PreConditions.
      if P.DESIGN_BY_CONTRACT_ENABLED():
         try:
            if True and (self.HeadNurse == self.HospitalCtxExt_get().HospitalCtx_get().Available) and (self.WaitingRoomCnt > 0) and (self.InSurgeryCnt < self.HospitalCtxExt_get().HospitalCtx_get().Capacity) and (self.MDCnt > 0) and (PySet({int_range for int_range in range(1, P.Minimum(PySet({3, self.NurseCnt}))+1)}).PyContains(self.n)):
               guard_ans = True
            else:
               guard_ans = False
         except:
            guard_ans = False
      else:
         guard_ans = True

      del(self.n)
      return guard_ans

   def PatientToSurgeryRef_eventActions(self, n_userIn : int = P.NoParam()) -> None:

      if n_userIn is None:
         n_userIn = P.PyRandValGen("int")

      attempt_Count : int = 0
      while not(self.PatientToSurgeryRef_eventGuards(n_userIn)):
         n_userIn = P.PyRandValGen("int")
         if attempt_Count == P.LOWMAXGENATTEMPTS():
            raise GuardsViolated("Guards of the Event could not be fulfilled.")
         attempt_Count += 1

      #Set Parameters as an Attribute.
      self.n = n_userIn

      #Event Actions

      self.WaitingRoomCnt, self.InSurgeryCnt, self.MDCnt, self.NurseCnt = (self.WaitingRoomCnt - 1), (self.InSurgeryCnt + 1), (self.MDCnt - 1), (self.NurseCnt - self.n)

      #Check Invariants after the actions are executed.
      if P.DESIGN_BY_CONTRACT_ENABLED() and not(self.checkAllInvariants()):
         raise Exception("PostConditions of the Event could not be fulfilled.")

      del(self.n)

   #End Event

   #NurseArrival - Event

   def NurseArrival_eventGuards(self) -> bool:
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

   def NurseArrival_eventActions(self) -> None:

      if not(self.NurseArrival_eventGuards()):
         raise GuardsViolated("Guards of the Event could not be fulfilled.")

      #Set Parameters as an Attribute.

      #Event Actions

      self.NurseCnt = (self.NurseCnt + 1)

      #Check Invariants after the actions are executed.
      if P.DESIGN_BY_CONTRACT_ENABLED() and not(self.checkAllInvariants()):
         raise Exception("PostConditions of the Event could not be fulfilled.")


   #End Event

   #MDArrival - Event

   def MDArrival_eventGuards(self) -> bool:
      guard_ans : bool = True

      #Set Parameters as an Attribute.

      #Check Event PreConditions.
      if P.DESIGN_BY_CONTRACT_ENABLED():
         try:
            if True and (self.MDCnt < self.HospitalCtxExt_get().MaxMDCap):
               guard_ans = True
            else:
               guard_ans = False
         except:
            guard_ans = False
      else:
         guard_ans = True

      return guard_ans

   def MDArrival_eventActions(self) -> None:

      attempt_Count : int = 0
      while not(self.MDArrival_eventGuards()):
         if attempt_Count == P.LOWMAXGENATTEMPTS():
            raise GuardsViolated("Guards of the Event could not be fulfilled.")
         attempt_Count += 1

      #Set Parameters as an Attribute.

      #Event Actions

      self.MDCnt = (self.MDCnt + 1)

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
            if True and (self.HeadNurse == self.HospitalCtxExt_get().HospitalCtx_get().Available) and (self.InSurgeryCnt == 0):
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

      self.HeadNurse = self.HospitalCtxExt_get().HospitalCtx_get().Unavailable

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
            if True and (self.HeadNurse == self.HospitalCtxExt_get().HospitalCtx_get().Unavailable):
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

      self.HeadNurse = self.HospitalCtxExt_get().HospitalCtx_get().Available

      #Check Invariants after the actions are executed.
      if P.DESIGN_BY_CONTRACT_ENABLED() and not(self.checkAllInvariants()):
         raise Exception("PostConditions of the Event could not be fulfilled.")


   #End Event

   #NurseDeparture - Event

   def NurseDeparture_eventGuards(self) -> bool:
      guard_ans : bool = True

      #Set Parameters as an Attribute.

      #Check Event PreConditions.
      if P.DESIGN_BY_CONTRACT_ENABLED():
         try:
            if True and (self.NurseCnt > 0):
               guard_ans = True
            else:
               guard_ans = False
         except:
            guard_ans = False
      else:
         guard_ans = True

      return guard_ans

   def NurseDeparture_eventActions(self) -> None:

      attempt_Count : int = 0
      while not(self.NurseDeparture_eventGuards()):
         if attempt_Count == P.LOWMAXGENATTEMPTS():
            raise GuardsViolated("Guards of the Event could not be fulfilled.")
         attempt_Count += 1

      #Set Parameters as an Attribute.

      #Event Actions

      self.NurseCnt = (self.NurseCnt - 1)

      #Check Invariants after the actions are executed.
      if P.DESIGN_BY_CONTRACT_ENABLED() and not(self.checkAllInvariants()):
         raise Exception("PostConditions of the Event could not be fulfilled.")


   #End Event

   #User/Debugging Functions

   def __str__(self) -> str:
      tmp_values : List[str] = list()

      #Print Internal Context Constants
      tmp_values.append(self.__HospitalCtxExt.__str__())

      #Print Variables
      tmp_values.append("###")
      tmp_values.append("Variables")

      tmp_values.append("HeadNurse ==> " + str(self.HeadNurse))
      tmp_values.append("InSurgeryCnt ==> " + str(self.InSurgeryCnt))
      tmp_values.append("MDCnt ==> " + str(self.MDCnt))
      tmp_values.append("NurseCnt ==> " + str(self.NurseCnt))
      tmp_values.append("SurgeryCnt ==> " + str(self.SurgeryCnt))
      tmp_values.append("WaitingRoomCnt ==> " + str(self.WaitingRoomCnt))

      return "\n".join(tmp_values)

   def __repr__(self) -> str:
      return self.__str__()

   def PyGuardsState(self) -> None:
      #This method will show which events (with no parameters) can be executed.
      tmp_values : List[str] = list()
      list_events_noparams : List[str] = ["PatientToRecovery", "MDDeparture", "PatientDeparture", "NurseArrival", "MDArrival", "HeadNurseDeparture", "PatientArrival", "HeadNurseArrival", "NurseDeparture"]
      list_events_params : List[Tuple[str,List[str]]] = [("PatientToSurgeryRef",["int"])]
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
      list_events_strs : List[str] = ["PatientToRecovery", "MDDeparture", "PatientDeparture", "PatientToSurgeryRef", "NurseArrival", "MDArrival", "HeadNurseDeparture", "PatientArrival", "HeadNurseArrival", "NurseDeparture"]
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
