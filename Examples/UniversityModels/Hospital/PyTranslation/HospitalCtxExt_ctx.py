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
from HospitalCtx_ctx import *


#CarrierSet Types Declarations


#Translation of Context: HospitalCtxExt
#This context extends the following context: HospitalCtx_class


class HospitalCtxExt_class():

   def __init__(self) -> None:

      #Context Utils
      self.__Initialized_Context = False
      self.__Attributes_SetFlag : bool = True

      #Context Extended Dependency Object
      self.__HospitalCtx : HospitalCtx_class

      #CarrierSets
      #EndCarrierSets
      self.__Attributes_SetFlag = False

      #Constants
      self.MaxMDCap : int
      #EndConstants


   #Context Extended Dependency Object Get Method

   def HospitalCtx_get(self) -> HospitalCtx_class:
      return self.__HospitalCtx

   #Initialized_Context Flag Attribute Get Method
   def Initialized_ContextGetMethod(self) -> bool:
      return self.__Initialized_Context

   #CarrierSets Get/Set Methods

   #End CarrierSets Get/Set Methods

   #Constants Get/Set Methods

   @property
   def MaxMDCap(self) -> int:
      return self.__MaxMDCap

   @MaxMDCap.setter
   def MaxMDCap(self, MaxMDCap_userIn : int) -> None:
      if self.__Attributes_SetFlag == False: raise Exception("Changing the state of this Context is disabled.")
      self.__MaxMDCap : int = MaxMDCap_userIn

   #End Constants Get Methods

   #Axiom Check Methods

   def ax10_axiomCheck(self) -> bool:
      return P.NAT1().PyContains(self.MaxMDCap)

   #End Axiom Check Methods

   #Check ALL Axioms

   def checkAllAxioms(self) -> bool:
      checkedAns_local : bool = True
      allAxioms_local : List[str] = [ "ax10" ]

      for Axiom_local in allAxioms_local:
         AxiomMethod_local = getattr(self,Axiom_local + "_axiomCheck")
         checkedAns_local = checkedAns_local and AxiomMethod_local()

      return checkedAns_local

   #End Check ALL Axioms

   #Checked Initialization Method
   def checkedInit(self , HospitalCtx_userIn : HospitalCtx_class = HospitalCtx_class(), MaxMDCap_userIn : int = P.NoParam() ) -> None:

      if MaxMDCap_userIn is None:
         MaxMDCap_userIn = P.PyRandValGen("int")

      if self.__Initialized_Context: raise Exception("Context already initialized!")
      self.__Initialized_Context = True

      #Enable Attributes Set Method
      self.__Attributes_SetFlag = True

      #Assign Parameter to Context Extended Dependency Object
      self.__HospitalCtx = HospitalCtx_userIn
      if not(self.__HospitalCtx.Initialized_ContextGetMethod()):
         self.__HospitalCtx.checkedInit()

      self.MaxMDCap = MaxMDCap_userIn

      if P.DESIGN_BY_CONTRACT_ENABLED():
         attempt_Count : int = 0
         while not(self.checkAllAxioms()):
            self.MaxMDCap = P.PyRandValGen("int")
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
      tmp_values.append("HospitalCtxExt Constants")

      tmp_values.append("MaxMDCap ==> " + str(self.MaxMDCap))

      #Print Extended Context Constants
      tmp_values.append(self.__HospitalCtx.__str__())

      return "\n".join(tmp_values)

   def __repr__(self) -> str:
      return self.__str__()
