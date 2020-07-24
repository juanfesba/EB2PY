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


#CarrierSet Types Declarations

@unique
class HospitalState_CS(Enum):

   # CUSTOM USER CODE BEGIN: Increase or decrease the amount of finite elements as you wish!

   HospitalState0 = auto()
   HospitalState1 = auto()

   # CUSTOM USER CODE END

#Include this new Type in the Prelude.
P.AddCarrierSet("HospitalState_CS",HospitalState_CS)


#Translation of Context: HospitalCtx


class HospitalCtx_class():

   def __init__(self) -> None:

      #Context Utils
      self.__Initialized_Context = False
      self.__Attributes_SetFlag : bool = True

      #CarrierSets
      self.HospitalState : PySet[HospitalState_CS] = P.PyCarrierSetGet("HospitalState_CS")
      #EndCarrierSets
      self.__Attributes_SetFlag = False

      #Constants
      self.Available : HospitalState_CS
      self.Capacity : int
      self.Unavailable : HospitalState_CS
      #EndConstants


   #Initialized_Context Flag Attribute Get Method
   def Initialized_ContextGetMethod(self) -> bool:
      return self.__Initialized_Context

   #CarrierSets Get/Set Methods

   @property
   def HospitalState(self) -> PySet[HospitalState_CS]:
      return self.__HospitalState

   @HospitalState.setter
   def HospitalState(self, HospitalState_userIn : PySet[HospitalState_CS]) -> None:
      if self.__Attributes_SetFlag == False: raise Exception("Changing the state of this Context is disabled.")
      self.__HospitalState : PySet[HospitalState_CS] = HospitalState_userIn

   #End CarrierSets Get/Set Methods

   #Constants Get/Set Methods

   @property
   def Available(self) -> HospitalState_CS:
      return self.__Available

   @Available.setter
   def Available(self, Available_userIn : HospitalState_CS) -> None:
      if self.__Attributes_SetFlag == False: raise Exception("Changing the state of this Context is disabled.")
      self.__Available : HospitalState_CS = Available_userIn

   @property
   def Capacity(self) -> int:
      return self.__Capacity

   @Capacity.setter
   def Capacity(self, Capacity_userIn : int) -> None:
      if self.__Attributes_SetFlag == False: raise Exception("Changing the state of this Context is disabled.")
      self.__Capacity : int = Capacity_userIn

   @property
   def Unavailable(self) -> HospitalState_CS:
      return self.__Unavailable

   @Unavailable.setter
   def Unavailable(self, Unavailable_userIn : HospitalState_CS) -> None:
      if self.__Attributes_SetFlag == False: raise Exception("Changing the state of this Context is disabled.")
      self.__Unavailable : HospitalState_CS = Unavailable_userIn

   #End Constants Get Methods

   #Axiom Check Methods

   def ax0_axiomCheck(self) -> bool:
      return P.NAT1().PyContains(self.Capacity)

   def ax1_axiomCheck(self) -> bool:
      return self.HospitalState.PyPartition([PySet({self.Available}), PySet({self.Unavailable})])

   #End Axiom Check Methods

   #Check ALL Axioms

   def checkAllAxioms(self) -> bool:
      checkedAns_local : bool = True
      allAxioms_local : List[str] = [ "ax0" , "ax1" ]

      for Axiom_local in allAxioms_local:
         AxiomMethod_local = getattr(self,Axiom_local + "_axiomCheck")
         checkedAns_local = checkedAns_local and AxiomMethod_local()

      return checkedAns_local

   #End Check ALL Axioms

   #Checked Initialization Method
   def checkedInit(self, Available_userIn : HospitalState_CS = P.NoParam(), Capacity_userIn : int = P.NoParam(), Unavailable_userIn : HospitalState_CS = P.NoParam() ) -> None:

      if Available_userIn is None:
         Available_userIn = P.PyRandValGen("HospitalState_CS")
      if Capacity_userIn is None:
         Capacity_userIn = P.PyRandValGen("int")
      if Unavailable_userIn is None:
         Unavailable_userIn = P.PyRandValGen("HospitalState_CS")

      if self.__Initialized_Context: raise Exception("Context already initialized!")
      self.__Initialized_Context = True

      #Enable Attributes Set Method
      self.__Attributes_SetFlag = True

      self.Available = Available_userIn
      self.Capacity = Capacity_userIn
      self.Unavailable = Unavailable_userIn

      if P.DESIGN_BY_CONTRACT_ENABLED():
         attempt_Count : int = 0
         while not(self.checkAllAxioms()):
            self.Available = P.PyRandValGen("HospitalState_CS")
            self.Capacity = P.PyRandValGen("int")
            self.Unavailable = P.PyRandValGen("HospitalState_CS")
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
      tmp_values.append("HospitalCtx Constants")

      tmp_values.append("Available ==> " + str(self.Available))
      tmp_values.append("Capacity ==> " + str(self.Capacity))
      tmp_values.append("Unavailable ==> " + str(self.Unavailable))

      return "\n".join(tmp_values)

   def __repr__(self) -> str:
      return self.__str__()
