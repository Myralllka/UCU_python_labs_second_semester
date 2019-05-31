from simulation import *


num_of_minutes = int(input("Enter the total minutes number: "))
num_of_agents = int(input("Enter the total agents number: "))
service_time = int(input("Enter the total service time: "))
between_time = int(input("Enter the between time: "))
a = TicketCounterSimulation(num_of_agents,
                            num_of_minutes,
                            between_time,
                            service_time)
a.run()
a.print_results()
