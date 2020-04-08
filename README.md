# Running the River
A Monte Carlo simulation of the card game "running the river," used to determine the
most optimal card count.

To run the simulation: `$ python3 controller.py [trials] > results/stats.txt` \
To run a convergence test: `$ python3 controller.py -c [depth]`

Data from convergence testing suggests that the simulation results converge
reasonably after at least 10^5 trials