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
class DIRECTION_CS(Enum):

   # CUSTOM USER CODE BEGIN: Increase or decrease the amount of finite elements as you wish!

   DIRECTION0 = auto()
   DIRECTION1 = auto()

   # CUSTOM USER CODE END

#Include this new Type in the Prelude.
P.AddCarrierSet("DIRECTION_CS",DIRECTION_CS)

@unique
class LIGHTS_CS(Enum):

   # CUSTOM USER CODE BEGIN: Increase or decrease the amount of finite elements as you wish!

   LIGHTS0 = auto()
   LIGHTS1 = auto()
   LIGHTS2 = auto()

   # CUSTOM USER CODE END

#Include this new Type in the Prelude.
P.AddCarrierSet("LIGHTS_CS",LIGHTS_CS)


#Translation of Context: SimpleTwoWayCtx


class SimpleTwoWayCtx_class():

   def __init__(self) -> None:

      #Context Utils
      self.__Initialized_Context = False
      self.__Attributes_SetFlag : bool = True

      #CarrierSets
      self.DIRECTION : PySet[DIRECTION_CS] = P.PyCarrierSetGet("DIRECTION_CS")
      self.LIGHTS : PySet[LIGHTS_CS] = P.PyCarrierSetGet("LIGHTS_CS")
      #EndCarrierSets
      self.__Attributes_SetFlag = False

      #Constants
      self.EastWest : DIRECTION_CS
      self.Green : LIGHTS_CS
      self.NorthSouth : DIRECTION_CS
      self.Red : LIGHTS_CS
      self.Yellow : LIGHTS_CS
      #EndConstants


   #Initialized_Context Flag Attribute Get Method
   def Initialized_ContextGetMethod(self) -> bool:
      return self.__Initialized_Context

   #CarrierSets Get/Set Methods

   @property
   def DIRECTION(self) -> PySet[DIRECTION_CS]:
      return self.__DIRECTION

   @DIRECTION.setter
   def DIRECTION(self, DIRECTION_userIn : PySet[DIRECTION_CS]) -> None:
      if self.__Attributes_SetFlag == False: raise Exception("Changing the state of this Context is disabled.")
      self.__DIRECTION : PySet[DIRECTION_CS] = DIRECTION_userIn

   @property
   def LIGHTS(self) -> PySet[LIGHTS_CS]:
      return self.__LIGHTS

   @LIGHTS.setter
   def LIGHTS(self, LIGHTS_userIn : PySet[LIGHTS_CS]) -> None:
      if self.__Attributes_SetFlag == False: raise Exception("Changing the state of this Context is disabled.")
      self.__LIGHTS : PySet[LIGHTS_CS] = LIGHTS_userIn

   #End CarrierSets Get/Set Methods

   #Constants Get/Set Methods

   @property
   def EastWest(self) -> DIRECTION_CS:
      return self.__EastWest

   @EastWest.setter
   def EastWest(self, EastWest_userIn : DIRECTION_CS) -> None:
      if self.__Attributes_SetFlag == False: raise Exception("Changing the state of this Context is disabled.")
      self.__EastWest : DIRECTION_CS = EastWest_userIn

   @property
   def Green(self) -> LIGHTS_CS:
      return self.__Green

   @Green.setter
   def Green(self, Green_userIn : LIGHTS_CS) -> None:
      if self.__Attributes_SetFlag == False: raise Exception("Changing the state of this Context is disabled.")
      self.__Green : LIGHTS_CS = Green_userIn

   @property
   def NorthSouth(self) -> DIRECTION_CS:
      return self.__NorthSouth

   @NorthSouth.setter
   def NorthSouth(self, NorthSouth_userIn : DIRECTION_CS) -> None:
      if self.__Attributes_SetFlag == False: raise Exception("Changing the state of this Context is disabled.")
      self.__NorthSouth : DIRECTION_CS = NorthSouth_userIn

   @property
   def Red(self) -> LIGHTS_CS:
      return self.__Red

   @Red.setter
   def Red(self, Red_userIn : LIGHTS_CS) -> None:
      if self.__Attributes_SetFlag == False: raise Exception("Changing the state of this Context is disabled.")
      self.__Red : LIGHTS_CS = Red_userIn

   @property
   def Yellow(self) -> LIGHTS_CS:
      return self.__Yellow

   @Yellow.setter
   def Yellow(self, Yellow_userIn : LIGHTS_CS) -> None:
      if self.__Attributes_SetFlag == False: raise Exception("Changing the state of this Context is disabled.")
      self.__Yellow : LIGHTS_CS = Yellow_userIn

   #End Constants Get Methods

   #Axiom Check Methods

   def ax0_axiomCheck(self) -> bool:
      return self.LIGHTS.PyPartition([PySet({self.Red}), PySet({self.Green}), PySet({self.Yellow})])

   def ax1_axiomCheck(self) -> bool:
      return self.DIRECTION.PyPartition([PySet({self.NorthSouth}), PySet({self.EastWest})])

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
   def checkedInit(self, EastWest_userIn : DIRECTION_CS = P.NoParam(), Green_userIn : LIGHTS_CS = P.NoParam(), NorthSouth_userIn : DIRECTION_CS = P.NoParam(), Red_userIn : LIGHTS_CS = P.NoParam(), Yellow_userIn : LIGHTS_CS = P.NoParam() ) -> None:

      if EastWest_userIn is None:
         EastWest_userIn = P.PyRandValGen("DIRECTION_CS")
      if Green_userIn is None:
         Green_userIn = P.PyRandValGen("LIGHTS_CS")
      if NorthSouth_userIn is None:
         NorthSouth_userIn = P.PyRandValGen("DIRECTION_CS")
      if Red_userIn is None:
         Red_userIn = P.PyRandValGen("LIGHTS_CS")
      if Yellow_userIn is None:
         Yellow_userIn = P.PyRandValGen("LIGHTS_CS")

      if self.__Initialized_Context: raise Exception("Context already initialized!")
      self.__Initialized_Context = True

      #Enable Attributes Set Method
      self.__Attributes_SetFlag = True

      self.EastWest = EastWest_userIn
      self.Green = Green_userIn
      self.NorthSouth = NorthSouth_userIn
      self.Red = Red_userIn
      self.Yellow = Yellow_userIn

      if P.DESIGN_BY_CONTRACT_ENABLED():
         attempt_Count : int = 0
         while not(self.checkAllAxioms()):
            self.EastWest = P.PyRandValGen("DIRECTION_CS")
            self.Green = P.PyRandValGen("LIGHTS_CS")
            self.NorthSouth = P.PyRandValGen("DIRECTION_CS")
            self.Red = P.PyRandValGen("LIGHTS_CS")
            self.Yellow = P.PyRandValGen("LIGHTS_CS")
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
      tmp_values.append("SimpleTwoWayCtx Constants")

      tmp_values.append("EastWest ==> " + str(self.EastWest))
      tmp_values.append("Green ==> " + str(self.Green))
      tmp_values.append("NorthSouth ==> " + str(self.NorthSouth))
      tmp_values.append("Red ==> " + str(self.Red))
      tmp_values.append("Yellow ==> " + str(self.Yellow))

      return "\n".join(tmp_values)

   def __repr__(self) -> str:
      return self.__str__()
