import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import Quantlib as ql


class Grapher:
    def __init__(self, marketData):
        self.dataObj = marketData
        self.returns = self.dataObj.table.pct_change()

    def display1(self, mean_returns, cov_matrix, num_portfolios, risk_free_rate):

        #todo#
        return 0

    def display2(self, mean_returns, cov_matrix, risk_free_rate):
        #todo#
        return 0
