import numpy as np
import sys

from game import Game



# Number of trials to run
trials = int(sys.argv[1])

results_5 = np.empty(trials)
results_6 = np.empty(trials)
results_7 = np.empty(trials)

for i in range(trials):
    results_5[i] = Game(5).play()
    results_6[i] = Game(6).play()
    results_7[i] = Game(7).play()

results_out = np.stack((results_5, results_6, results_7), axis=1)


def calcStats(result):
    mean = np.mean(result)
    stddev = np.std(result)
    return [mean, stddev]


# Return the results
np.savetxt("results/results.csv", results_out, fmt='%d', delimiter=',')

print("Ran " + str(trials) + " trials")

stats_5 = calcStats(results_5)
print("The five-card test resulted in a mean of " + str(stats_5[0]) + " and a std. dev. of " + str(stats_5[1]))

stats_6 = calcStats(results_6)
print("The six-card test resulted in a mean of " + str(stats_6[0]) + " and a std. dev. of " + str(stats_6[1]))

stats_7 = calcStats(results_7)
print("The seven-card test resulted in a mean of " + str(stats_7[0]) + " and a std. dev. of " + str(stats_7[1]))
