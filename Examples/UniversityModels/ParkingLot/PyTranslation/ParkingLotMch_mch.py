#DEPENDENCIES

#Allow Path Access to the Prelude's Directory

import sys
if not(".." in sys.path):
   sys.path.append("..")

#Utilities Dependencies
from Py_Preludes import *

#Typing Dependencies
from typing import List

#Machine Internal Context Dependencies
from ParkingLotCtx_ctx import *


#Translation of Machine: ParkingLotMch
#This machine sees the following context: ParkingLotCtx_class


class ParkingLotMch_class():

   def __init__( self , ParkingLotCtx_userIn : ParkingLotCtx_class = ParkingLotCtx_class() ) -> None:

      #Assign Parameter to Context Extended Dependency Object
      self.__ParkingLotCtx : ParkingLotCtx_class = ParkingLotCtx_userIn
      if not(self.__ParkingLotCtx.Initialized_ContextGetMethod()):
         self.__ParkingLotCtx.checkedInit()

      #Variables
      self.doors : PyRel[Door_CS,DoorState_CS]
      self.parking : PyRel[ParkingSpace_CS,Car_CS]
      #EndVariables

      #INITIALISATION of variables
      self.doors = PyRel({(self.ParkingLotCtx_get().Entrance, self.ParkingLotCtx_get().Closed), (self.ParkingLotCtx_get().Exit, self.ParkingLotCtx_get().Closed)})
      self.parking = PySet()

      #Check ALL Invariants if enabled.
      if P.DESIGN_BY_CONTRACT_ENABLED() and not(self.checkAllInvariants()):
         raise Exception("Invariants violated after INITIALISATION.")

   #Internal Context Dependency Object Get Method

   def ParkingLotCtx_get(self) -> ParkingLotCtx_class:
      return self.__ParkingLotCtx

   #Variables Get/Set Methods

   @property
   def doors(self) -> PyRel[Door_CS,DoorState_CS]:
      return self.__doors

   @doors.setter
   def doors(self, doors_userIn : PyRel[Door_CS,DoorState_CS]) -> None:
      self.__doors : PyRel[Door_CS,DoorState_CS] = doors_userIn

   @property
   def parking(self) -> PyRel[ParkingSpace_CS,Car_CS]:
      return self.__parking

   @parking.setter
   def parking(self, parking_userIn : PyRel[ParkingSpace_CS,Car_CS]) -> None:
      self.__parking : PyRel[ParkingSpace_CS,Car_CS] = parking_userIn

   #End Variables Get Methods

   #Invariants Check Methods

   def inv0_invariantCheck(self) -> bool:
      return PyFamilies(PyFamilyTypes.TotalFunctions, self.ParkingLotCtx_get().Door, self.ParkingLotCtx_get().DoorState).PyContains(self.doors)

   def inv1_invariantCheck(self) -> bool:
      return PyFamilies(PyFamilyTypes.PartialInjections, self.ParkingLotCtx_get().ParkingSpace, self.ParkingLotCtx_get().Car).PyContains(self.parking)

   #Check ALL Invariants

   def checkAllInvariants(self) -> bool:
      checkedAns_local : bool = True
      allInvariants_local : List[str] = [ "inv0" , "inv1" ]

      for Invariant_local in allInvariants_local:
         InvariantMethod_local = getattr(self,Invariant_local + "_invariantCheck")
         checkedAns_local = checkedAns_local and InvariantMethod_local()

      return checkedAns_local

   #End Check ALL Invariants Method

   #Events

   #FromClosing - Event

   def FromClosing_eventGuards(self, door1_userIn : Door_CS, state1_userIn : DoorState_CS) -> bool:
      guard_ans : bool = True

      #Set Parameters as an Attribute.
      self.door1 : Door_CS = door1_userIn
      self.state1 : DoorState_CS = state1_userIn

      #Check Event PreConditions.
      if P.DESIGN_BY_CONTRACT_ENABLED():
         try:
            if True and (self.ParkingLotCtx_get().Door.PyContains(self.door1)) and (self.doors(self.door1) == self.ParkingLotCtx_get().Closing) and (PySet({self.ParkingLotCtx_get().Opening, self.ParkingLotCtx_get().Closed}).PyContains(self.state1)):
               guard_ans = True
            else:
               guard_ans = False
         except:
            guard_ans = False
      else:
         guard_ans = True

      del(self.door1)
      del(self.state1)
      return guard_ans

   def FromClosing_eventActions(self, door1_userIn : Door_CS = P.NoParam(), state1_userIn : DoorState_CS = P.NoParam()) -> None:

      if door1_userIn is None:
         door1_userIn = P.PyRandValGen("Door_CS")
      if state1_userIn is None:
         state1_userIn = P.PyRandValGen("DoorState_CS")

      attempt_Count : int = 0
      while not(self.FromClosing_eventGuards(door1_userIn, state1_userIn)):
         door1_userIn = P.PyRandValGen("Door_CS")
         state1_userIn = P.PyRandValGen("DoorState_CS")
         if attempt_Count == P.LOWMAXGENATTEMPTS():
            raise GuardsViolated("Guards of the Event could not be fulfilled.")
         attempt_Count += 1

      #Set Parameters as an Attribute.
      self.door1 = door1_userIn
      self.state1 = state1_userIn

      #Event Actions

      self.doors = self.doors.PyOverriding(PyRel({(self.door1, self.state1)}))

      #Check Invariants after the actions are executed.
      if P.DESIGN_BY_CONTRACT_ENABLED() and not(self.checkAllInvariants()):
         raise Exception("PostConditions of the Event could not be fulfilled.")

      del(self.door1)
      del(self.state1)

   #End Event

   #UnparkCar - Event

   def UnparkCar_eventGuards(self, space_userIn : ParkingSpace_CS) -> bool:
      guard_ans : bool = True

      #Set Parameters as an Attribute.
      self.space : ParkingSpace_CS = space_userIn

      #Check Event PreConditions.
      if P.DESIGN_BY_CONTRACT_ENABLED():
         try:
            if True and (self.doors(self.ParkingLotCtx_get().Exit) == self.ParkingLotCtx_get().Open) and (self.parking.PyDomain().PyContains(self.space)):
               guard_ans = True
            else:
               guard_ans = False
         except:
            guard_ans = False
      else:
         guard_ans = True

      del(self.space)
      return guard_ans

   def UnparkCar_eventActions(self, space_userIn : ParkingSpace_CS = P.NoParam()) -> None:

      if space_userIn is None:
         space_userIn = P.PyRandValGen("ParkingSpace_CS")

      attempt_Count : int = 0
      while not(self.UnparkCar_eventGuards(space_userIn)):
         space_userIn = P.PyRandValGen("ParkingSpace_CS")
         if attempt_Count == P.LOWMAXGENATTEMPTS():
            raise GuardsViolated("Guards of the Event could not be fulfilled.")
         attempt_Count += 1

      #Set Parameters as an Attribute.
      self.space = space_userIn

      #Event Actions

      self.parking = self.parking.PyDifference(PyRel({(self.space, self.parking(self.space))}))

      #Check Invariants after the actions are executed.
      if P.DESIGN_BY_CONTRACT_ENABLED() and not(self.checkAllInvariants()):
         raise Exception("PostConditions of the Event could not be fulfilled.")

      del(self.space)

   #End Event

   #FromOpening - Event

   def FromOpening_eventGuards(self, door_userIn : Door_CS, state_userIn : DoorState_CS) -> bool:
      guard_ans : bool = True

      #Set Parameters as an Attribute.
      self.door : Door_CS = door_userIn
      self.state : DoorState_CS = state_userIn

      #Check Event PreConditions.
      if P.DESIGN_BY_CONTRACT_ENABLED():
         try:
            if True and (self.ParkingLotCtx_get().Door.PyContains(self.door)) and (self.doors(self.door) == self.ParkingLotCtx_get().Opening) and (PySet({self.ParkingLotCtx_get().Open, self.ParkingLotCtx_get().Closing}).PyContains(self.state)):
               guard_ans = True
            else:
               guard_ans = False
         except:
            guard_ans = False
      else:
         guard_ans = True

      del(self.door)
      del(self.state)
      return guard_ans

   def FromOpening_eventActions(self, door_userIn : Door_CS = P.NoParam(), state_userIn : DoorState_CS = P.NoParam()) -> None:

      if door_userIn is None:
         door_userIn = P.PyRandValGen("Door_CS")
      if state_userIn is None:
         state_userIn = P.PyRandValGen("DoorState_CS")

      attempt_Count : int = 0
      while not(self.FromOpening_eventGuards(door_userIn, state_userIn)):
         door_userIn = P.PyRandValGen("Door_CS")
         state_userIn = P.PyRandValGen("DoorState_CS")
         if attempt_Count == P.LOWMAXGENATTEMPTS():
            raise GuardsViolated("Guards of the Event could not be fulfilled.")
         attempt_Count += 1

      #Set Parameters as an Attribute.
      self.door = door_userIn
      self.state = state_userIn

      #Event Actions

      self.doors = self.doors.PyOverriding(PyRel({(self.door, self.state)}))

      #Check Invariants after the actions are executed.
      if P.DESIGN_BY_CONTRACT_ENABLED() and not(self.checkAllInvariants()):
         raise Exception("PostConditions of the Event could not be fulfilled.")

      del(self.door)
      del(self.state)

   #End Event

   #ParkCar - Event

   def ParkCar_eventGuards(self, c_userIn : Car_CS, s_userIn : ParkingSpace_CS) -> bool:
      guard_ans : bool = True

      #Set Parameters as an Attribute.
      self.c : Car_CS = c_userIn
      self.s : ParkingSpace_CS = s_userIn

      #Check Event PreConditions.
      if P.DESIGN_BY_CONTRACT_ENABLED():
         try:
            if True and (self.doors(self.ParkingLotCtx_get().Entrance) == self.ParkingLotCtx_get().Open) and (self.ParkingLotCtx_get().Car.PyDifference(self.parking.PyRange()).PyContains(self.c)) and (self.ParkingLotCtx_get().ParkingSpace.PyDifference(self.parking.PyDomain()).PyContains(self.s)):
               guard_ans = True
            else:
               guard_ans = False
         except:
            guard_ans = False
      else:
         guard_ans = True

      del(self.c)
      del(self.s)
      return guard_ans

   def ParkCar_eventActions(self, c_userIn : Car_CS = P.NoParam(), s_userIn : ParkingSpace_CS = P.NoParam()) -> None:

      if c_userIn is None:
         c_userIn = P.PyRandValGen("Car_CS")
      if s_userIn is None:
         s_userIn = P.PyRandValGen("ParkingSpace_CS")

      attempt_Count : int = 0
      while not(self.ParkCar_eventGuards(c_userIn, s_userIn)):
         c_userIn = P.PyRandValGen("Car_CS")
         s_userIn = P.PyRandValGen("ParkingSpace_CS")
         if attempt_Count == P.LOWMAXGENATTEMPTS():
            raise GuardsViolated("Guards of the Event could not be fulfilled.")
         attempt_Count += 1

      #Set Parameters as an Attribute.
      self.c = c_userIn
      self.s = s_userIn

      #Event Actions

      self.parking = self.parking.PyUnion(PyRel({(self.s, self.c)}))

      #Check Invariants after the actions are executed.
      if P.DESIGN_BY_CONTRACT_ENABLED() and not(self.checkAllInvariants()):
         raise Exception("PostConditions of the Event could not be fulfilled.")

      del(self.c)
      del(self.s)

   #End Event

   #StartOpening - Event

   def StartOpening_eventGuards(self, d_userIn : Door_CS) -> bool:
      guard_ans : bool = True

      #Set Parameters as an Attribute.
      self.d : Door_CS = d_userIn

      #Check Event PreConditions.
      if P.DESIGN_BY_CONTRACT_ENABLED():
         try:
            if True and (self.ParkingLotCtx_get().Door.PyContains(self.d)) and (self.doors(self.d) == self.ParkingLotCtx_get().Closed):
               guard_ans = True
            else:
               guard_ans = False
         except:
            guard_ans = False
      else:
         guard_ans = True

      del(self.d)
      return guard_ans

   def StartOpening_eventActions(self, d_userIn : Door_CS = P.NoParam()) -> None:

      if d_userIn is None:
         d_userIn = P.PyRandValGen("Door_CS")

      attempt_Count : int = 0
      while not(self.StartOpening_eventGuards(d_userIn)):
         d_userIn = P.PyRandValGen("Door_CS")
         if attempt_Count == P.LOWMAXGENATTEMPTS():
            raise GuardsViolated("Guards of the Event could not be fulfilled.")
         attempt_Count += 1

      #Set Parameters as an Attribute.
      self.d = d_userIn

      #Event Actions

      self.doors = self.doors.PyOverriding(PyRel({(self.d, self.ParkingLotCtx_get().Opening)}))

      #Check Invariants after the actions are executed.
      if P.DESIGN_BY_CONTRACT_ENABLED() and not(self.checkAllInvariants()):
         raise Exception("PostConditions of the Event could not be fulfilled.")

      del(self.d)

   #End Event

   #StartClosing - Event

   def StartClosing_eventGuards(self, door3_userIn : Door_CS) -> bool:
      guard_ans : bool = True

      #Set Parameters as an Attribute.
      self.door3 : Door_CS = door3_userIn

      #Check Event PreConditions.
      if P.DESIGN_BY_CONTRACT_ENABLED():
         try:
            if True and (self.ParkingLotCtx_get().Door.PyContains(self.door3)) and (self.doors(self.door3) == self.ParkingLotCtx_get().Open):
               guard_ans = True
            else:
               guard_ans = False
         except:
            guard_ans = False
      else:
         guard_ans = True

      del(self.door3)
      return guard_ans

   def StartClosing_eventActions(self, door3_userIn : Door_CS = P.NoParam()) -> None:

      if door3_userIn is None:
         door3_userIn = P.PyRandValGen("Door_CS")

      attempt_Count : int = 0
      while not(self.StartClosing_eventGuards(door3_userIn)):
         door3_userIn = P.PyRandValGen("Door_CS")
         if attempt_Count == P.LOWMAXGENATTEMPTS():
            raise GuardsViolated("Guards of the Event could not be fulfilled.")
         attempt_Count += 1

      #Set Parameters as an Attribute.
      self.door3 = door3_userIn

      #Event Actions

      self.doors = self.doors.PyOverriding(PyRel({(self.door3, self.ParkingLotCtx_get().Closing)}))

      #Check Invariants after the actions are executed.
      if P.DESIGN_BY_CONTRACT_ENABLED() and not(self.checkAllInvariants()):
         raise Exception("PostConditions of the Event could not be fulfilled.")

      del(self.door3)

   #End Event

   #User/Debugging Functions

   def __str__(self) -> str:
      tmp_values : List[str] = list()

      #Print Internal Context Constants
      tmp_values.append(self.__ParkingLotCtx.__str__())

      #Print Variables
      tmp_values.append("###")
      tmp_values.append("Variables")

      tmp_values.append("doors ==> " + str(self.doors))
      tmp_values.append("parking ==> " + str(self.parking))

      return "\n".join(tmp_values)

   def __repr__(self) -> str:
      return self.__str__()

   def PyGuardsState(self) -> None:
      #This method will show which events (with no parameters) can be executed.
      tmp_values : List[str] = list()
      list_events_noparams : List[str] = []
      list_events_params : List[Tuple[str,List[str]]] = [("FromClosing",["Door_CS", "DoorState_CS"]), ("UnparkCar",["ParkingSpace_CS"]), ("FromOpening",["Door_CS", "DoorState_CS"]), ("ParkCar",["Car_CS", "ParkingSpace_CS"]), ("StartOpening",["Door_CS"]), ("StartClosing",["Door_CS"])]
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
      list_events_strs : List[str] = ["FromClosing", "UnparkCar", "FromOpening", "ParkCar", "StartOpening", "StartClosing"]
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
