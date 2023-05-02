from proc import get_budget_data

import matplotlib.pyplot as plot
import numpy as np


# TODO: Compile budget data points
def get_chart_data():
    return np.array()


# TODO: Compile budget data labels
def get_chart_labels():
    return list()


def main():
    budget_data = get_budget_data()

    # TODO: Update when func implemented
    placeholder_data = get_chart_data()
    placeholder_labels = get_chart_labels()

    plot.pie(placeholder_data, labels=placeholder_labels)
    plot.show()


if __name__ == '__main__':
    main()
