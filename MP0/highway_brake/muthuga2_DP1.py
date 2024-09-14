from enum import Enum, auto
import copy
from typing import List

class PedestrianMode(Enum):
    Normal=auto()

class VehicleMode(Enum):
    Normal = auto()
    Brake = auto()
    Accel = auto()
    HardBrake = auto()

class State:
    x: float 
    y: float 
    theta: float 
    v: float 
    agent_mode: VehicleMode 

    def __init__(self, x, y, theta, v, agent_mode: VehicleMode):
        pass 

def decisionLogic(ego: State, other: State):
    output = copy.deepcopy(ego)

    # TODO: Edit this part of decision logic
    
    time_to_collision = other.dist / (ego.v)

    if time_to_collision <= 1.2 or other.dist <= 3.5:
        output.agent_node = VehicleMode.HardBrake
    if 1.2 < time_to_collision <= 2.5:
        output.agent_mode = VehicleMode.Brake
    if time_to_collision > 2.5:
        output.agent_mode = VehicleMode.Accel
       

    ###########################################

    # DO NOT CHANGE THIS
    assert other.dist > 2.0, "Too Close!"

    return output 