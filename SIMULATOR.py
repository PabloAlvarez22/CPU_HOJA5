import simpy
import random
from MAIN import MediaTime
from MAIN import MainProgram
CpuCores = 2
RandomNumber_seed = 100
PeriodTime = 1
CycleInstructions = 3
RamMB = 100
ProcessCC = 25
Environment = simpy.Environment()
RAM = simpy.Container(Environment, capacity=RamMB, init=RamMB)
CPU = simpy.Resource(Environment, capacity=CpuCores)
processingTime = []
random.seed(RandomNumber_seed)

def ProgramSimulation():        
    print("Inicio de la Simulación del CPU")
    i = 0
    while i  < ProcessCC:
        i  += 1
        NewTime = random.expovariate(1.0 / PeriodTime)
        yield Environment.timeout(NewTime)
        MainProgram(i ,Environment, CycleInstructions, RAM, CPU)
Environment.process(ProgramSimulation())
Environment.run()
MediaTime()
print("Programa Finalizado")