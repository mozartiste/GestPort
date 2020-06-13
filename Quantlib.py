# coding=utf-8
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.optimize as sco

# *********************************************** #
# Inputs
# *********************************************** #
# weights : Vecteur des poids de chaque actif
# mean_returns : Vecteur des rendrements moyens de chaque actif
# cov_matrix : Matrice de variance covariance
# *********************************************** #
# Outputs
# *********************************************** #
# returns : rendement annualisé du portefeuille
# std : Volatilité du portefeuille
# *********************************************** #
AnnuBase = 252


def perfo_annualisee_portefeuille(weights, mean_returns, cov_matrix):
    returns = np.sum(mean_returns * weights) * AnnuBase
    std = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights))) * np.sqrt(AnnuBase)  # Volatilité
    return std, returns


# *********************************************** #
# Inputs
# *********************************************** #
# num_portfolios : Nombre de portefeuilles
# mean_returns : rendements moyens
# cov_matrix : matrice de variance covariance
# risk_free_rate : taux sans risque
# *********************************************** #
# Outputs
# *********************************************** #
# results : matrice des volatilités, rendements et ratio de sharpe par portefeuille
# weights_record : matrice des poids
# *********************************************** #
def portefeuilles_alea(num_portfolios, mean_returns, cov_matrix, risk_free_rate):
    numberOfAssets = len(cov_matrix)
    results = np.zeros((3, num_portfolios))
    weights_record = []
    for i in range(num_portfolios):
        weights = np.random.random(numberOfAssets)  # generation de numberOfAssets nombres aléatoirs
        weights /= np.sum(weights)  # reduction (sommes des poids =1)
        weights_record.append(weights)
        portfolio_std_dev, portfolio_return = perfo_annualisee_portefeuille(weights, mean_returns, cov_matrix)
        results[0, i] = portfolio_std_dev
        results[1, i] = portfolio_return
        results[2, i] = (portfolio_return - risk_free_rate) / portfolio_std_dev
    return results, weights_record



# to do ......................