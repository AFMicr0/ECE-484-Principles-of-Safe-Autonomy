from enum import Enum, auto
import copy
from typing import List

class TLMode(Enum):
    GREEN=auto()
    YELLOW=auto()
    RED=auto()

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
    
    d_in = 20
    d_out = 15

    distance_to_light = other.x - ego.x

    if other.signal_mode == TLMode.RED:
        if d_out < distance_to_light < d_in:
            output.agent_mode = VehicleMode.Brake
        if d_out > distance_to_light:
            output.agent_mode = VehicleMode.Accel

    if other.signal_mode == TLMode.YELLOW:
        if d_in < distance_to_light:
            output.agent_mode = VehicleMode.Brake

    if other.signal_mode == TLMode.GREEN:
        output.agent_mode = VehicleMode.Accel


    ###########################################
    # DO NOT CHANGE THIS
    assert not (other.signal_mode == TLMode.RED and (ego.x>other.x-20 and ego.x<other.x-15)), "Run Red Light"  
    assert not (other.signal_mode == TLMode.RED and (ego.x>other.x-15 and ego.x<other.x) and ego.v<1), "Stop at Intersection"

    return output 