from Queue.arrays import Array
from Queue.linkedqueue import LinkedQueue
from simpeople import TicketAgent, Passenger
import random


# random.seed(4500)

class TicketCounterSimulation:
    # Create a simulation object.
    def __init__(self, num_agents, num_minutes, between_time, service_time):
        # Parameters supplied by the user.
        self._arrive_prob = 1.0 / between_time
        self._service_time = service_time
        self._num_minutes = num_minutes

        # Simulation components.
        self._passenger_q = LinkedQueue()
        self._the_agents = Array(num_agents)
        for i in range(num_agents):
            self._the_agents[i] = TicketAgent(i)
        # Computed during the simulation.
        self._total_wait_time = 0
        self._num_passengers = 0

    # Print the simulation results.
    def print_results(self):
        num_served = self._num_passengers - len(self._passenger_q)
        avg_wait = float(self._total_wait_time) / num_served
        print("")
        print("Number of passengers served = ", num_served)
        print("Number of passengers remaining in line = %d" %
              len(self._passenger_q))
        print("The average wait time was %4.2f minutes." % avg_wait)

    # Run the simulation using the parameters supplied earlier.
    def run(self):
        for cur_time in range(self._num_minutes + 1):
            self._handle_arrive(cur_time)
            self._handle_begin_service(cur_time)
            self._handle_end_service(cur_time)

    # The remaining methods that have yet to be implemented.
    def _handle_arrive(self, cur_time):  # Handles simulation rule #1.
        if random.random() <= self._arrive_prob:
            new_passenger = Passenger(self._num_passengers, cur_time)
            self._passenger_q.add(new_passenger)
            print('Time {}: Passenger {} arrived.'.format(
                    cur_time, self._num_passengers + 1))
            self._num_passengers += 1

    def _handle_begin_service(self, cur_time):  # Handles simulation rule #2.
        for each in self._the_agents:
            if each.is_free() and not self._passenger_q.is_empty():
                tmp_passenger = self._passenger_q.pop()
                each.start_service(tmp_passenger,
                                   cur_time + self._service_time)
                self._total_wait_time += (cur_time -
                                          tmp_passenger.time_arrived)
                print('Time {}: Agent {} started serving passenger {}.'.format(
                        cur_time, each.id_num + 1, tmp_passenger.id_num + 1))

    def _handle_end_service(self, cur_time):  # Handles simulation rule #3.
        for each in self._the_agents:
            if each.is_finished(cur_time):
                res_passenger = each.stop_service()
                print('Time {}: Agent {} stopped serving passenger {}.'.format(
                        cur_time, each.id_num + 1, res_passenger.id_num + 1))
