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
class COLOURS_CS(Enum):

   # CUSTOM USER CODE BEGIN: Increase or decrease the amount of finite elements as you wish!

   COLOURS0 = auto()
   COLOURS1 = auto()
   COLOURS2 = auto()

   # CUSTOM USER CODE END

#Include this new Type in the Prelude.
P.AddCarrierSet("COLOURS_CS",COLOURS_CS)


#Translation of Context: TrafficLightSystemCtx


class TrafficLightSystemCtx_class():

   def __init__(self) -> None:

      #Context Utils
      self.__Initialized_Context = False
      self.__Attributes_SetFlag : bool = True

      #CarrierSets
      self.COLOURS : PySet[COLOURS_CS] = P.PyCarrierSetGet("COLOURS_CS")
      #EndCarrierSets
      self.__Attributes_SetFlag = False

      #Constants
      self.green : COLOURS_CS
      self.red : COLOURS_CS
      self.yellow : COLOURS_CS
      #EndConstants


   #Initialized_Context Flag Attribute Get Method
   def Initialized_ContextGetMethod(self) -> bool:
      return self.__Initialized_Context

   #CarrierSets Get/Set Methods

   @property
   def COLOURS(self) -> PySet[COLOURS_CS]:
      return self.__COLOURS

   @COLOURS.setter
   def COLOURS(self, COLOURS_userIn : PySet[COLOURS_CS]) -> None:
      if self.__Attributes_SetFlag == False: raise Exception("Changing the state of this Context is disabled.")
      self.__COLOURS : PySet[COLOURS_CS] = COLOURS_userIn

   #End CarrierSets Get/Set Methods

   #Constants Get/Set Methods

   @property
   def green(self) -> COLOURS_CS:
      return self.__green

   @green.setter
   def green(self, green_userIn : COLOURS_CS) -> None:
      if self.__Attributes_SetFlag == False: raise Exception("Changing the state of this Context is disabled.")
      self.__green : COLOURS_CS = green_userIn

   @property
   def red(self) -> COLOURS_CS:
      return self.__red

   @red.setter
   def red(self, red_userIn : COLOURS_CS) -> None:
      if self.__Attributes_SetFlag == False: raise Exception("Changing the state of this Context is disabled.")
      self.__red : COLOURS_CS = red_userIn

   @property
   def yellow(self) -> COLOURS_CS:
      return self.__yellow

   @yellow.setter
   def yellow(self, yellow_userIn : COLOURS_CS) -> None:
      if self.__Attributes_SetFlag == False: raise Exception("Changing the state of this Context is disabled.")
      self.__yellow : COLOURS_CS = yellow_userIn

   #End Constants Get Methods

   #Axiom Check Methods

   def ax0_axiomCheck(self) -> bool:
      return self.COLOURS.PyPartition([PySet({self.red}), PySet({self.yellow}), PySet({self.green})])

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
   def checkedInit(self, green_userIn : COLOURS_CS = P.NoParam(), red_userIn : COLOURS_CS = P.NoParam(), yellow_userIn : COLOURS_CS = P.NoParam() ) -> None:

      if green_userIn is None:
         green_userIn = P.PyRandValGen("COLOURS_CS")
      if red_userIn is None:
         red_userIn = P.PyRandValGen("COLOURS_CS")
      if yellow_userIn is None:
         yellow_userIn = P.PyRandValGen("COLOURS_CS")

      if self.__Initialized_Context: raise Exception("Context already initialized!")
      self.__Initialized_Context = True

      #Enable Attributes Set Method
      self.__Attributes_SetFlag = True

      self.green = green_userIn
      self.red = red_userIn
      self.yellow = yellow_userIn

      if P.DESIGN_BY_CONTRACT_ENABLED():
         attempt_Count : int = 0
         while not(self.checkAllAxioms()):
            self.green = P.PyRandValGen("COLOURS_CS")
            self.red = P.PyRandValGen("COLOURS_CS")
            self.yellow = P.PyRandValGen("COLOURS_CS")
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
      tmp_values.append("TrafficLightSystemCtx Constants")

      tmp_values.append("green ==> " + str(self.green))
      tmp_values.append("red ==> " + str(self.red))
      tmp_values.append("yellow ==> " + str(self.yellow))

      return "\n".join(tmp_values)

   def __repr__(self) -> str:
      return self.__str__()
