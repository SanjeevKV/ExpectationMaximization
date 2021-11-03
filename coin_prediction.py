from sklearn.mixture import GaussianMixture
import numpy as np
import api_handler as ah
import random


def get_datapoint(tosses):
    '''
    Returns the ratio of tosses that were heads
    '''
    return sum(tosses) / len(tosses)


def get_draw():
    '''
    Calls the api, gets the tosses
    And
    Returns a datapoint (Ratio of tosses that were heads)
    '''
    tosses = ah.get_tosses()
    return get_datapoint(tosses)


def prepare_data(n_draws=30):
    '''
    Returns an array of datapoints. Each datapoint corresponds to 1 draw
    '''
    data = []
    for i in range(n_draws):
        cur_draw = get_draw()
        print(f"Draw {i+1}: {cur_draw}")
        data.append([cur_draw])
    return np.array(data)


def prepare_fake_data(n_draws=30):
    '''
    Just a test function to check EM algorithm
    With this function, the mean values should be 0 and 1
    '''
    data = []
    for i in range(n_draws):
        data.append([random.choice([0, 1])])
    return np.array(data)


def exp_max(data, n_coins=2):
    '''
    Fits a gaussian mixture model and returns the means of components
    '''
    gm = GaussianMixture(n_components=n_coins, random_state=0).fit(data)
    return gm.means_, gm.covariances_


if __name__ == '__main__':
    data = prepare_data(n_draws=30)
    means, covariances = exp_max(data, 2)
    print(
        f"Likelihood of heads in two components: {means[0][0]}, {means[1][0]}")
    print(
        f"Variances of two components: {covariances[0][0][0]}, {covariances[1][0][0]}")
