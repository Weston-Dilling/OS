import sys
from Simulator import Simulator

if __name__ == "__main__":
    
    lamb = 1
    end = 10000
    avg_service_time = 0.06

    for scheduler in range(5):
        if scheduler == 0:
            print("Running FCFS")
            while lamb < 31:
                sim = Simulator(scheduler, lamb, avg_service_time, 0, end)
                sim.run()
                sim.generateReport()
                lamb += 1
            lamb = 1

        elif scheduler == 1:
            print("Running SRTF")
            while lamb < 31:
                sim = Simulator(scheduler, lamb, avg_service_time, 0, end)
                sim.run()
                sim.generateReport()
                lamb += 1
            lamb = 1

        elif scheduler == 2:
            print("Running HRRN")
            while lamb < 31:
                sim = Simulator(scheduler, lamb, avg_service_time, 0, end)
                sim.run()
                sim.generateReport()
                lamb += 1
            lamb = 1

        elif scheduler == 3:
            print("Running RR, quant:", 0.01)
            while lamb < 31:
                sim = Simulator(scheduler, lamb, avg_service_time, .01, end)
                sim.run()
                sim.generateReport()
                lamb += 1
            lamb = 1

        elif scheduler == 4:
            print("Running RR, quant:", 0.2)
            while lamb < 31:
                sim = Simulator(scheduler-1, lamb, avg_service_time, .2, end)
                sim.run()
                sim.generateReport()
                lamb += 1
            lamb = 1

        else:
            print("Invalid input.")
        scheduler += 1