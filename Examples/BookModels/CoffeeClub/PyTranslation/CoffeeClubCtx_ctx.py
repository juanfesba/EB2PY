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
class MEMBER_CS(Enum):

   # CUSTOM USER CODE BEGIN: Increase or decrease the amount of finite elements as you wish!

   MEMBER0 = auto()
   MEMBER1 = auto()

   # CUSTOM USER CODE END

#Include this new Type in the Prelude.
P.AddCarrierSet("MEMBER_CS",MEMBER_CS)


#Translation of Context: CoffeeClubCtx


class CoffeeClubCtx_class():

   def __init__(self) -> None:

      #Context Utils
      self.__Initialized_Context = False
      self.__Attributes_SetFlag : bool = True

      #CarrierSets
      self.MEMBER : PySet[MEMBER_CS] = P.PyCarrierSetGet("MEMBER_CS")
      #EndCarrierSets
      self.__Attributes_SetFlag = False

      #Constants
      #EndConstants


   #Initialized_Context Flag Attribute Get Method
   def Initialized_ContextGetMethod(self) -> bool:
      return self.__Initialized_Context

   #CarrierSets Get/Set Methods

   @property
   def MEMBER(self) -> PySet[MEMBER_CS]:
      return self.__MEMBER

   @MEMBER.setter
   def MEMBER(self, MEMBER_userIn : PySet[MEMBER_CS]) -> None:
      if self.__Attributes_SetFlag == False: raise Exception("Changing the state of this Context is disabled.")
      self.__MEMBER : PySet[MEMBER_CS] = MEMBER_userIn

   #End CarrierSets Get/Set Methods

   #Constants Get/Set Methods

   #End Constants Get Methods

   #Axiom Check Methods

   def ax0_axiomCheck(self) -> bool:
      return self.MEMBER.PyFinite()

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
   def checkedInit(self ) -> None:


      if self.__Initialized_Context: raise Exception("Context already initialized!")
      self.__Initialized_Context = True

      #Enable Attributes Set Method
      self.__Attributes_SetFlag = True


      if P.DESIGN_BY_CONTRACT_ENABLED():
         attempt_Count : int = 0
         while not(self.checkAllAxioms()):
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
      tmp_values.append("CoffeeClubCtx Constants")


      return "\n".join(tmp_values)

   def __repr__(self) -> str:
      return self.__str__()
