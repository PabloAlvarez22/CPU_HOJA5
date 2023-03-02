import statistics
from random import randint
from decimal import Decimal
processingTime = []

class Simulating:
    def __init__(self, Key, Instructions, Memory):
        self.Key = Key
        self.Instructions = Instructions
        self.Memory = Memory

class MainProgram:
    def __init__(self, i ,Environment, CycleInstructions, RAM, CPU):
        self.i = i
        self.Environment = Environment
        self.CycleInstructions = CycleInstructions
        self.RAM = RAM
        self.CPU = CPU
        Environment.process(self.SimulationRunning())
    
    def Time(self):
        return self.Environment.now + 1
    
    def Redondear(self, n, decimals = 0):
        multiplier = 10 ** decimals
        return int(n * multiplier) / multiplier
    
    def SimulationRunning(self):
        InitialazingProgram= self.Time()
        Memory = randint(1, 10)
        Instructions = randint(1, 10)
        Simulation = Simulating(self.i, Instructions, Memory)
        print(f'Tiempo de procesamiento = {self.Time()} //// Instruccion realizada = {Simulation.Key} NUEVO PROCESO')
        with self.RAM.get(Simulation.Memory) as RAMRequest:
            yield RAMRequest
            print(f'Tiempo de procesamiento =  {self.Time()} //// Instruccion realizada = {Simulation.Key} PROCESO LISTO')
            Contador = 0
            while Simulation.Instructions > 0:
                with self.CPU.request() as CPURequest:
                    yield CPURequest
                    Contador += 1
                    print(f'Tiempo de procesamiento =  {self.Time()} //// Instruccion realizada = {Simulation.Key} (PROCESO NO. {Contador})')
                    Simulation.Instructions = max(
                        Simulation.Instructions - self.CycleInstructions, 0)
                    if Simulation.Instructions == 0:
                        print(f'Tiempo de procesamiento =  {self.Time()} //// Instruccion realizada = {Simulation.Key} PROCESO TERMINADO')
                    else:
                        New = randint(1, 2)
                        if New == 1:
                            print(f'Tiempo de procesamiento =  {self.Time()} //// Instruccion realizada = {Simulation.Key} ESPERANDO/COLA')
                            WaitingList = randint(1, 5)
                            yield self.Environment.timeout(WaitingList)
                        else:
                            print(f'Tiempo de procesamiento =  {self.Time()} //// Instruccion realizada = {Simulation.Key} PROCESO LISTO')
                    yield self.CPU.release(CPURequest)
        yield self.RAM.put(Simulation.Memory)        
        EndingProgram = self.Time()
        PrincipalTime = Decimal(EndingProgram) - Decimal(InitialazingProgram)
        processingTime.append(PrincipalTime)

def MediaTime():
    print("Promedio de tiempo de ejecución obtenido:")
    print(f"{statistics.mean(processingTime)}")
    print("Desviación Estándar obtenida:")
    print(f"{statistics.pstdev(processingTime)}")
    
