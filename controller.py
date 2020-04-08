import numpy as np
import sys

from game import Game


# Calculate the statistics from a trial
def calc_stats(result):
    mean = np.mean(result)
    stddev = np.std(result)
    return [mean, stddev]


# Run a simulation with a specific number of trials and return the result
def run_simulation(trials):
    results_5 = np.empty(trials)
    results_6 = np.empty(trials)
    results_7 = np.empty(trials)

    for i in range(trials):
        results_5[i] = Game(5).play()
        results_6[i] = Game(6).play()
        results_7[i] = Game(7).play()

    results_out = np.stack((results_5, results_6, results_7), axis=1)
    return results_out


# Run a convergence test to a specified depth. The depth represents the order of magnitude of the largest tested
# simulation
def run_convergence_test(depth):
    converge_mean_5 = np.empty(depth);
    converge_mean_6 = np.empty(depth);
    converge_mean_7 = np.empty(depth);

    converge_std_5 = np.empty(depth);
    converge_std_6 = np.empty(depth);
    converge_std_7 = np.empty(depth);

    for i in range(depth):
        results = run_simulation(10**i)

        converge_mean_5[i] = calc_stats(results[:, 0])[0]
        converge_mean_6[i] = calc_stats(results[:, 1])[0]
        converge_mean_7[i] = calc_stats(results[:, 2])[0]

        converge_std_5[i] = calc_stats(results[:, 0])[1]
        converge_std_6[i] = calc_stats(results[:, 1])[1]
        converge_std_7[i] = calc_stats(results[:, 2])[1]

    convergence_mean_out = np.stack((converge_mean_5, converge_mean_6, converge_mean_7), axis=1)
    convergence_std_out = np.stack((converge_std_5, converge_std_6, converge_std_7), axis=1)

    return [convergence_mean_out, convergence_std_out]


# Save and print results from a simulation
def save_results(trials, all_results):
    # Return the results
    np.savetxt("results/results.csv", all_results, fmt='%.3f', delimiter=',')

    print("Ran " + str(trials) + " trials")

    stats_5 = calc_stats(all_results[:, 0])
    print("The five-card test resulted in a mean of " + str(stats_5[0]) + " and a std. dev. of " + str(stats_5[1]))

    stats_6 = calc_stats(all_results[:, 1])
    print("The six-card test resulted in a mean of " + str(stats_6[0]) + " and a std. dev. of " + str(stats_6[1]))

    stats_7 = calc_stats(all_results[:, 2])
    print("The seven-card test resulted in a mean of " + str(stats_7[0]) + " and a std. dev. of " + str(stats_7[1]))


# Save and print results from a convergence test
def save_convergence(depth, convergence_mean_results, convergence_std_results):
    # Save the results
    np.savetxt("results/convergence_mean.csv", convergence_mean_results, fmt='%.3f', delimiter=',')
    np.savetxt("results/convergence_std.csv", convergence_std_results, fmt='%.3f', delimiter=',')


# Number of trials to run
run_convergence = False if (sys.argv[1]!="-c") else True

if run_convergence:
    convergence_depth = int(sys.argv[2])
    convergence_results = run_convergence_test(convergence_depth)
    save_convergence(convergence_depth, convergence_results[0], convergence_results[1])
else:
    desired_trials = int(sys.argv[1])
    simulation_results = run_simulation(desired_trials)
    save_results(desired_trials, simulation_results)

