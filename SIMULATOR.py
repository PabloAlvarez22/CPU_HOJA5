import simpy
import random
from MAIN import MediaTime
from MAIN import MainProgram
CpuCores = 1
RandomNumber_seed = 100
PeriodTime = 10
CycleInstructions = 3
RamMB = 100
ProcessCC = 25
Environment = simpy.Environment()
RAM = simpy.Container(Environment, capacity=RamMB, init=RamMB)
CPU = simpy.Resource(Environment, capacity=CpuCores)
processingTime = []
random.seed(RandomNumber_seed)

