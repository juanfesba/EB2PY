#DEPENDENCIES

#Allow Path Access to the Prelude's Directory

import sys
if not(".." in sys.path):
   sys.path.append("..")

#Utilities Dependencies
from Py_Preludes import *

#Typing Dependencies
from typing import List

#Enum Dependencies
from enum import Enum,auto,unique

#Context Extension Dependencies
from CafeteriaCtx_ctx import *


#CarrierSet Types Declarations


#Translation of Context: CafeteriaCtxExt
#This context extends the following context: CafeteriaCtx_class


class CafeteriaCtxExt_class():

   def __init__(self) -> None:

      #Context Utils
      self.__Initialized_Context = False
      self.__Attributes_SetFlag : bool = True

      #Context Extended Dependency Object
      self.__CafeteriaCtx : CafeteriaCtx_class

      #CarrierSets
      #EndCarrierSets
      self.__Attributes_SetFlag = False

      #Constants
      self.CashierAvailable : int
      self.CashierUnavailable : int
      self.NoPickup : int
      self.PickupReady : int
      #EndConstants


   #Context Extended Dependency Object Get Method

   def CafeteriaCtx_get(self) -> CafeteriaCtx_class:
      return self.__CafeteriaCtx

   #Initialized_Context Flag Attribute Get Method
   def Initialized_ContextGetMethod(self) -> bool:
      return self.__Initialized_Context

   #CarrierSets Get/Set Methods

   #End CarrierSets Get/Set Methods

   #Constants Get/Set Methods

   @property
   def CashierAvailable(self) -> int:
      return self.__CashierAvailable

   @CashierAvailable.setter
   def CashierAvailable(self, CashierAvailable_userIn : int) -> None:
      if self.__Attributes_SetFlag == False: raise Exception("Changing the state of this Context is disabled.")
      self.__CashierAvailable : int = CashierAvailable_userIn

   @property
   def CashierUnavailable(self) -> int:
      return self.__CashierUnavailable

   @CashierUnavailable.setter
   def CashierUnavailable(self, CashierUnavailable_userIn : int) -> None:
      if self.__Attributes_SetFlag == False: raise Exception("Changing the state of this Context is disabled.")
      self.__CashierUnavailable : int = CashierUnavailable_userIn

   @property
   def NoPickup(self) -> int:
      return self.__NoPickup

   @NoPickup.setter
   def NoPickup(self, NoPickup_userIn : int) -> None:
      if self.__Attributes_SetFlag == False: raise Exception("Changing the state of this Context is disabled.")
      self.__NoPickup : int = NoPickup_userIn

   @property
   def PickupReady(self) -> int:
      return self.__PickupReady

   @PickupReady.setter
   def PickupReady(self, PickupReady_userIn : int) -> None:
      if self.__Attributes_SetFlag == False: raise Exception("Changing the state of this Context is disabled.")
      self.__PickupReady : int = PickupReady_userIn

   #End Constants Get Methods

   #Axiom Check Methods

   def ax0_axiomCheck(self) -> bool:
      return self.CashierAvailable == 1

   def ax1_axiomCheck(self) -> bool:
      return self.CashierUnavailable == 0

   def ax2_axiomCheck(self) -> bool:
      return self.PickupReady == 1

   def ax3_axiomCheck(self) -> bool:
      return self.NoPickup == 0

   #End Axiom Check Methods

   #Check ALL Axioms

   def checkAllAxioms(self) -> bool:
      checkedAns_local : bool = True
      allAxioms_local : List[str] = [ "ax0" , "ax1" , "ax2" , "ax3" ]

      for Axiom_local in allAxioms_local:
         AxiomMethod_local = getattr(self,Axiom_local + "_axiomCheck")
         checkedAns_local = checkedAns_local and AxiomMethod_local()

      return checkedAns_local

   #End Check ALL Axioms

   #Checked Initialization Method
   def checkedInit(self , CafeteriaCtx_userIn : CafeteriaCtx_class = CafeteriaCtx_class(), CashierAvailable_userIn : int = P.NoParam(), CashierUnavailable_userIn : int = P.NoParam(), NoPickup_userIn : int = P.NoParam(), PickupReady_userIn : int = P.NoParam() ) -> None:

      if CashierAvailable_userIn is None:
         CashierAvailable_userIn = P.PyRandValGen("int")
      if CashierUnavailable_userIn is None:
         CashierUnavailable_userIn = P.PyRandValGen("int")
      if NoPickup_userIn is None:
         NoPickup_userIn = P.PyRandValGen("int")
      if PickupReady_userIn is None:
         PickupReady_userIn = P.PyRandValGen("int")

      if self.__Initialized_Context: raise Exception("Context already initialized!")
      self.__Initialized_Context = True

      #Enable Attributes Set Method
      self.__Attributes_SetFlag = True

      #Assign Parameter to Context Extended Dependency Object
      self.__CafeteriaCtx = CafeteriaCtx_userIn
      if not(self.__CafeteriaCtx.Initialized_ContextGetMethod()):
         self.__CafeteriaCtx.checkedInit()

      self.CashierAvailable = CashierAvailable_userIn
      self.CashierUnavailable = CashierUnavailable_userIn
      self.NoPickup = NoPickup_userIn
      self.PickupReady = PickupReady_userIn

      if P.DESIGN_BY_CONTRACT_ENABLED():
         attempt_Count : int = 0
         while not(self.checkAllAxioms()):
            self.CashierAvailable = P.PyRandValGen("int")
            self.CashierUnavailable = P.PyRandValGen("int")
            self.NoPickup = P.PyRandValGen("int")
            self.PickupReady = P.PyRandValGen("int")
            if attempt_Count == P.HIGHMAXGENATTEMPTS():
               raise Exception("Initialization could not satisfy the Axioms!")
            attempt_Count += 1

      #Disable Attributes Set Method
      self.__Attributes_SetFlag = False

   #User/Debugging Functions

   def __str__(self) -> str:
      tmp_values : List[str] = list()

      #Print Constants
      tmp_values.append("###")
      tmp_values.append("CafeteriaCtxExt Constants")

      tmp_values.append("CashierAvailable ==> " + str(self.CashierAvailable))
      tmp_values.append("CashierUnavailable ==> " + str(self.CashierUnavailable))
      tmp_values.append("NoPickup ==> " + str(self.NoPickup))
      tmp_values.append("PickupReady ==> " + str(self.PickupReady))

      #Print Extended Context Constants
      tmp_values.append(self.__CafeteriaCtx.__str__())

      return "\n".join(tmp_values)

   def __repr__(self) -> str:
      return self.__str__()
