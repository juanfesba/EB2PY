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


#Translation of Context: SortingCtx


class SortingCtx_class():

   def __init__(self) -> None:

      #Context Utils
      self.__Initialized_Context = False
      self.__Attributes_SetFlag : bool = True

      #CarrierSets
      #EndCarrierSets
      self.__Attributes_SetFlag = False

      #Constants
      self.m : int
      #EndConstants


   #Initialized_Context Flag Attribute Get Method
   def Initialized_ContextGetMethod(self) -> bool:
      return self.__Initialized_Context

   #CarrierSets Get/Set Methods

   #End CarrierSets Get/Set Methods

   #Constants Get/Set Methods

   @property
   def m(self) -> int:
      return self.__m

   @m.setter
   def m(self, m_userIn : int) -> None:
      if self.__Attributes_SetFlag == False: raise Exception("Changing the state of this Context is disabled.")
      self.__m : int = m_userIn

   #End Constants Get Methods

   #Axiom Check Methods

   def ax0_axiomCheck(self) -> bool:
      return P.NAT1().PyContains(self.m)

   #End Axiom Check Methods

   #Check ALL Axioms

   def checkAllAxioms(self) -> bool:
      checkedAns_local : bool = True
      allAxioms_local : List[str] = [ "ax0" ]

      for Axiom_local in allAxioms_local:
         AxiomMethod_local = getattr(self,Axiom_local + "_axiomCheck")
         checkedAns_local = checkedAns_local and AxiomMethod_local()

      return checkedAns_local

   #End Check ALL Axioms

   #Checked Initialization Method
   def checkedInit(self, m_userIn : int = P.NoParam() ) -> None:

      if m_userIn is None:
         m_userIn = P.PyRandValGen("int")

      if self.__Initialized_Context: raise Exception("Context already initialized!")
      self.__Initialized_Context = True

      #Enable Attributes Set Method
      self.__Attributes_SetFlag = True

      self.m = m_userIn

      if P.DESIGN_BY_CONTRACT_ENABLED():
         attempt_Count : int = 0
         while not(self.checkAllAxioms()):
            self.m = P.PyRandValGen("int")
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
      tmp_values.append("SortingCtx Constants")

      tmp_values.append("m ==> " + str(self.m))

      return "\n".join(tmp_values)

   def __repr__(self) -> str:
      return self.__str__()
