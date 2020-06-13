#!/usr/bin/python
# -*- coding: latin-1 -*-
import Grapher as gr
import MarketData as md


def main():
    while True:
        print("Options Disponibles:\n")
        print("1. Graphe de frontiere efficiente pour un portefeuille d'a tions:\n")
        print("2. Graphe de frontiere efficiente pour un portefeuille d'ations avec effet de levier:\n")
        choixGraph = input("saisir 1 ou 2:\n")
        num_portfolios = input("Nombre de portefeuils simulés:\n")
        risk_free_rate = input("Taux sans risque\n")
        if choixGraph == 2:
            Levier = input("Effet de levier\n")
        else:
            Levier = 0

        # demer le

        mesDonnes = md.MarketData()
        monGrapher = gr.Grapher(mesDonnes)
        # rendement couts(t) - cours(t-1)
        rendements = mesDonnes.table.pct_change()
        # Rendement moyens
        mean_returns = rendements.mean()
        # Matrice de variance covariance
        cov_matrix = rendements.cov()

        if choixGraph == 1:
            monGrapher.display1(mean_returns, cov_matrix, num_portfolios, risk_free_rate)
        else:
            monGrapher.display2(mean_returns, cov_matrix, risk_free_rate)


if __name__ == '__main__':
    main()
