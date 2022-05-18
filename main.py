import random
import math


class Simulation:

    def __init__(self, lam, mu):
        self.num_jobs = 0
        self.curr_time = 0.0
        self.lam = lam
        self.mu = mu

        self.total_customer = 0
        self.total_arrive_time = 0.0
        self.total_leave_time = 0.0

        self.jobs_mul_time = 0.0

        self.total_service_time = 0.0

    def next(self):
        prob = random.uniform(0, 1)
        interval = -math.log(prob) / (self.lam + self.mu)

        self.jobs_mul_time += self.num_jobs * interval
        self.curr_time += interval

        if self.is_arrive():
            self.num_jobs += 1
            self.total_customer += 1
            self.total_arrive_time += self.curr_time
        elif self.num_jobs > 0:
            self.num_jobs -= 1
            self.total_leave_time += self.curr_time
            self.total_service_time += interval

        return self.curr_time

    def is_arrive(self):
        if random.uniform(0, 1) < self.lam / (self.lam + self.mu):
            return True
        else:
            return False

    def is_empty(self):
        return self.num_jobs == 0

    def mean_stay_time(self):
        return (self.total_leave_time - self.total_arrive_time) / self.total_customer

    def mean_length(self):
        return self.jobs_mul_time / self.curr_time

    def mean_wait_time(self):
        return (self.total_leave_time - self.total_arrive_time - self.total_service_time) / self.total_customer


if __name__ == '__main__':
    mean_stay_time = 0.0
    mean_len = 0.0
    mean_wait_time = 0.0

    duration = 50000.0
    lam = 1.0
    mu = 1.1
    count = 10
    for i in range(0, count):
        simulation = Simulation(lam, mu)
        while True:
            curr_time = simulation.next()
            if curr_time > duration and simulation.is_empty():
                break
        mean_stay_time += simulation.mean_stay_time()
        mean_len += simulation.mean_length()
        mean_wait_time += simulation.mean_wait_time()

    mean_stay_time /= count
    mean_len /= count
    mean_wait_time /= count

    print(f"mean stay time: {mean_stay_time}")
    print(f"mean len: {mean_len}")
    print(f"mean wait time: {mean_wait_time}")
