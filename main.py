from proc import get_budget_data
from dotenv import dotenv_values

import matplotlib.pyplot as plot
import numpy as np

DATA_FILENAME = 'DATA_FILENAME'

config = dotenv_values('.env')


# TODO: Compile budget data points
def get_chart_data():
    return np.array(0)


# TODO: Compile budget data labels
def get_chart_labels():
    return list('placeholder')


def main():
    budget_data = get_budget_data(config[DATA_FILENAME])

    # TODO: Update when func implemented
    placeholder_data = get_chart_data()
    placeholder_labels = get_chart_labels()

    plot.pie(placeholder_data, labels=placeholder_labels)
    plot.show()


if __name__ == '__main__':
    main()
