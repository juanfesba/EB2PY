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
class Car_CS(Enum):

   # CUSTOM USER CODE BEGIN: Increase or decrease the amount of finite elements as you wish!

   Car0 = auto()

   # CUSTOM USER CODE END

#Include this new Type in the Prelude.
P.AddCarrierSet("Car_CS",Car_CS)

@unique
class Door_CS(Enum):

   # CUSTOM USER CODE BEGIN: Increase or decrease the amount of finite elements as you wish!

   Door0 = auto()
   Door1 = auto()

   # CUSTOM USER CODE END

#Include this new Type in the Prelude.
P.AddCarrierSet("Door_CS",Door_CS)

@unique
class DoorState_CS(Enum):

   # CUSTOM USER CODE BEGIN: Increase or decrease the amount of finite elements as you wish!

   DoorState0 = auto()
   DoorState1 = auto()
   DoorState2 = auto()
   DoorState3 = auto()

   # CUSTOM USER CODE END

#Include this new Type in the Prelude.
P.AddCarrierSet("DoorState_CS",DoorState_CS)

@unique
class ParkingSpace_CS(Enum):

   # CUSTOM USER CODE BEGIN: Increase or decrease the amount of finite elements as you wish!

   ParkingSpace0 = auto()

   # CUSTOM USER CODE END

#Include this new Type in the Prelude.
P.AddCarrierSet("ParkingSpace_CS",ParkingSpace_CS)


#Translation of Context: ParkingLotCtx


class ParkingLotCtx_class():

   def __init__(self) -> None:

      #Context Utils
      self.__Initialized_Context = False
      self.__Attributes_SetFlag : bool = True

      #CarrierSets
      self.Car : PySet[Car_CS] = P.PyCarrierSetGet("Car_CS")
      self.Door : PySet[Door_CS] = P.PyCarrierSetGet("Door_CS")
      self.DoorState : PySet[DoorState_CS] = P.PyCarrierSetGet("DoorState_CS")
      self.ParkingSpace : PySet[ParkingSpace_CS] = P.PyCarrierSetGet("ParkingSpace_CS")
      #EndCarrierSets
      self.__Attributes_SetFlag = False

      #Constants
      self.Closed : DoorState_CS
      self.Closing : DoorState_CS
      self.Entrance : Door_CS
      self.Exit : Door_CS
      self.Open : DoorState_CS
      self.Opening : DoorState_CS
      #EndConstants


   #Initialized_Context Flag Attribute Get Method
   def Initialized_ContextGetMethod(self) -> bool:
      return self.__Initialized_Context

   #CarrierSets Get/Set Methods

   @property
   def Car(self) -> PySet[Car_CS]:
      return self.__Car

   @Car.setter
   def Car(self, Car_userIn : PySet[Car_CS]) -> None:
      if self.__Attributes_SetFlag == False: raise Exception("Changing the state of this Context is disabled.")
      self.__Car : PySet[Car_CS] = Car_userIn

   @property
   def Door(self) -> PySet[Door_CS]:
      return self.__Door

   @Door.setter
   def Door(self, Door_userIn : PySet[Door_CS]) -> None:
      if self.__Attributes_SetFlag == False: raise Exception("Changing the state of this Context is disabled.")
      self.__Door : PySet[Door_CS] = Door_userIn

   @property
   def DoorState(self) -> PySet[DoorState_CS]:
      return self.__DoorState

   @DoorState.setter
   def DoorState(self, DoorState_userIn : PySet[DoorState_CS]) -> None:
      if self.__Attributes_SetFlag == False: raise Exception("Changing the state of this Context is disabled.")
      self.__DoorState : PySet[DoorState_CS] = DoorState_userIn

   @property
   def ParkingSpace(self) -> PySet[ParkingSpace_CS]:
      return self.__ParkingSpace

   @ParkingSpace.setter
   def ParkingSpace(self, ParkingSpace_userIn : PySet[ParkingSpace_CS]) -> None:
      if self.__Attributes_SetFlag == False: raise Exception("Changing the state of this Context is disabled.")
      self.__ParkingSpace : PySet[ParkingSpace_CS] = ParkingSpace_userIn

   #End CarrierSets Get/Set Methods

   #Constants Get/Set Methods

   @property
   def Closed(self) -> DoorState_CS:
      return self.__Closed

   @Closed.setter
   def Closed(self, Closed_userIn : DoorState_CS) -> None:
      if self.__Attributes_SetFlag == False: raise Exception("Changing the state of this Context is disabled.")
      self.__Closed : DoorState_CS = Closed_userIn

   @property
   def Closing(self) -> DoorState_CS:
      return self.__Closing

   @Closing.setter
   def Closing(self, Closing_userIn : DoorState_CS) -> None:
      if self.__Attributes_SetFlag == False: raise Exception("Changing the state of this Context is disabled.")
      self.__Closing : DoorState_CS = Closing_userIn

   @property
   def Entrance(self) -> Door_CS:
      return self.__Entrance

   @Entrance.setter
   def Entrance(self, Entrance_userIn : Door_CS) -> None:
      if self.__Attributes_SetFlag == False: raise Exception("Changing the state of this Context is disabled.")
      self.__Entrance : Door_CS = Entrance_userIn

   @property
   def Exit(self) -> Door_CS:
      return self.__Exit

   @Exit.setter
   def Exit(self, Exit_userIn : Door_CS) -> None:
      if self.__Attributes_SetFlag == False: raise Exception("Changing the state of this Context is disabled.")
      self.__Exit : Door_CS = Exit_userIn

   @property
   def Open(self) -> DoorState_CS:
      return self.__Open

   @Open.setter
   def Open(self, Open_userIn : DoorState_CS) -> None:
      if self.__Attributes_SetFlag == False: raise Exception("Changing the state of this Context is disabled.")
      self.__Open : DoorState_CS = Open_userIn

   @property
   def Opening(self) -> DoorState_CS:
      return self.__Opening

   @Opening.setter
   def Opening(self, Opening_userIn : DoorState_CS) -> None:
      if self.__Attributes_SetFlag == False: raise Exception("Changing the state of this Context is disabled.")
      self.__Opening : DoorState_CS = Opening_userIn

   #End Constants Get Methods

   #Axiom Check Methods

   def ax0_axiomCheck(self) -> bool:
      return self.DoorState.PyPartition([PySet({self.Open}), PySet({self.Opening}), PySet({self.Closing}), PySet({self.Closed})])

   def ax1_axiomCheck(self) -> bool:
      return self.Door.PyPartition([PySet({self.Entrance}), PySet({self.Exit})])

   def ax2_axiomCheck(self) -> bool:
      return self.Car.PyFinite()

   def ax3_axiomCheck(self) -> bool:
      return self.ParkingSpace.PyFinite()

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
   def checkedInit(self, Closed_userIn : DoorState_CS = P.NoParam(), Closing_userIn : DoorState_CS = P.NoParam(), Entrance_userIn : Door_CS = P.NoParam(), Exit_userIn : Door_CS = P.NoParam(), Open_userIn : DoorState_CS = P.NoParam(), Opening_userIn : DoorState_CS = P.NoParam() ) -> None:

      if Closed_userIn is None:
         Closed_userIn = P.PyRandValGen("DoorState_CS")
      if Closing_userIn is None:
         Closing_userIn = P.PyRandValGen("DoorState_CS")
      if Entrance_userIn is None:
         Entrance_userIn = P.PyRandValGen("Door_CS")
      if Exit_userIn is None:
         Exit_userIn = P.PyRandValGen("Door_CS")
      if Open_userIn is None:
         Open_userIn = P.PyRandValGen("DoorState_CS")
      if Opening_userIn is None:
         Opening_userIn = P.PyRandValGen("DoorState_CS")

      if self.__Initialized_Context: raise Exception("Context already initialized!")
      self.__Initialized_Context = True

      #Enable Attributes Set Method
      self.__Attributes_SetFlag = True

      self.Closed = Closed_userIn
      self.Closing = Closing_userIn
      self.Entrance = Entrance_userIn
      self.Exit = Exit_userIn
      self.Open = Open_userIn
      self.Opening = Opening_userIn

      if P.DESIGN_BY_CONTRACT_ENABLED():
         attempt_Count : int = 0
         while not(self.checkAllAxioms()):
            self.Closed = P.PyRandValGen("DoorState_CS")
            self.Closing = P.PyRandValGen("DoorState_CS")
            self.Entrance = P.PyRandValGen("Door_CS")
            self.Exit = P.PyRandValGen("Door_CS")
            self.Open = P.PyRandValGen("DoorState_CS")
            self.Opening = P.PyRandValGen("DoorState_CS")
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
      tmp_values.append("ParkingLotCtx Constants")

      tmp_values.append("Closed ==> " + str(self.Closed))
      tmp_values.append("Closing ==> " + str(self.Closing))
      tmp_values.append("Entrance ==> " + str(self.Entrance))
      tmp_values.append("Exit ==> " + str(self.Exit))
      tmp_values.append("Open ==> " + str(self.Open))
      tmp_values.append("Opening ==> " + str(self.Opening))

      return "\n".join(tmp_values)

   def __repr__(self) -> str:
      return self.__str__()
