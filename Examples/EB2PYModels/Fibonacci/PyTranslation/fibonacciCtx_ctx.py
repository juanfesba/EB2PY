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


#Translation of Context: fibonacciCtx


class fibonacciCtx_class():

   def __init__(self) -> None:

      #Context Utils
      self.__Initialized_Context = False
      self.__Attributes_SetFlag : bool = True

      #CarrierSets
      #EndCarrierSets
      self.__Attributes_SetFlag = False

      #Constants
      self.fibonacci : PyRel[int,int]
      #EndConstants


   #Initialized_Context Flag Attribute Get Method
   def Initialized_ContextGetMethod(self) -> bool:
      return self.__Initialized_Context

   #CarrierSets Get/Set Methods

   #End CarrierSets Get/Set Methods

   #Constants Get/Set Methods

   @property
   def fibonacci(self) -> PyRel[int,int]:
      return self.__fibonacci

   @fibonacci.setter
   def fibonacci(self, fibonacci_userIn : PyRel[int,int]) -> None:
      if self.__Attributes_SetFlag == False: raise Exception("Changing the state of this Context is disabled.")
      self.__fibonacci : PyRel[int,int] = fibonacci_userIn

   #End Constants Get Methods

   #Axiom Check Methods

   def ax0_axiomCheck(self) -> bool:
      return PyFamilies(PyFamilyTypes.TotalFunctions, P.NAT(), P.NAT()).PyContains(self.fibonacci)

   def ax1_axiomCheck(self) -> bool:
      return (self.fibonacci(0) == 0 and self.fibonacci(1) == 1)

   def ax2_axiomCheck(self) -> bool:
      return P.QuantifiedForAll( (lambda boundIdentifiers : PyPrelude.LogicImplication(boundIdentifiers[0] > 1, self.fibonacci(boundIdentifiers[0]) == (self.fibonacci((boundIdentifiers[0] - 1)) + self.fibonacci((boundIdentifiers[0] - 2))))) , [ (0,"int") ] ) 

   #End Axiom Check Methods

   #Check ALL Axioms

   def checkAllAxioms(self) -> bool:
      checkedAns_local : bool = True
      allAxioms_local : List[str] = [ "ax0" , "ax1" , "ax2" ]

      for Axiom_local in allAxioms_local:
         AxiomMethod_local = getattr(self,Axiom_local + "_axiomCheck")
         checkedAns_local = checkedAns_local and AxiomMethod_local()

      return checkedAns_local

   #End Check ALL Axioms

   #Checked Initialization Method
   def checkedInit(self, fibonacci_userIn : PyRel[int,int] = P.NoParam() ) -> None:

      if fibonacci_userIn is None:
         fibonacci_userIn = P.PyRandValGen("PyRel[int,int]")

      if self.__Initialized_Context: raise Exception("Context already initialized!")
      self.__Initialized_Context = True

      #Enable Attributes Set Method
      self.__Attributes_SetFlag = True

      self.fibonacci = fibonacci_userIn

      if P.DESIGN_BY_CONTRACT_ENABLED():
         attempt_Count : int = 0
         while not(self.checkAllAxioms()):
            self.fibonacci = P.PyRandValGen("PyRel[int,int]")
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
      tmp_values.append("fibonacciCtx Constants")

      tmp_values.append("fibonacci ==> " + str(self.fibonacci))

      return "\n".join(tmp_values)

   def __repr__(self) -> str:
      return self.__str__()
