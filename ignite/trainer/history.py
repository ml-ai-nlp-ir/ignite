import numpy as np


class History(list):
    def __init__(self):
        super(History, self).__init__()

    def clear(self):
        del self[:]

    def simple_moving_average(self, window_size, transform=lambda x: x):
        """
        Calculate the simple moving average over the last `window_size` elements in the history

        Parameters
        ----------
        window_size : int
            The historical window on which to calculate the moving average.

        transform : Callable
            an optional transform to convert historical data into a nummber (default is identity)
        """
        return np.ma.average(list(map(transform, self[-window_size:])))

    def weighted_moving_average(self, window_size, weights, transform=lambda x: x):
        """
        Calculate a weighted moving average over the last `window_size` elements in the history

        Parameters
        ----------
        window_size : int
            The historical window on which to calculate the moving average.
        weights: Iterable
            The importance that each element has in the computation of the average.
        transform : Callable
            an optional transform to convert historical data into a nummber (default is identity)
        """
        return np.ma.average(list(map(transform, self[-window_size:])), weights=weights)

    def exponential_moving_average(self, window_size, alpha, transform=lambda x: x):
        """
        Calculate a weighted moving average over the last `window_size` elements in the history

        Parameters
        ----------
        window_size : int
            The historical window on which to calculate the moving average.
        alpha: float
            The constant smoothing factor between 0 and 1. A higher `alpha` discounts older observations faster.
        transform : Callable
            an optional transform to convert historical data into a nummber (default is identity)
        """

        weights = [(1 - alpha)**i for i in list(range(window_size))[::-1]]
        return self.weighted_moving_average(window_size, weights, transform)
