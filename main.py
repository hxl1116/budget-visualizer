import matplotlib.pyplot as plot
import numpy as np
import yaml


def get_budget_data():
    with open('data.yml') as yml_file:
        return yaml.safe_load(yml_file)
    

def process_takehome(takehome_data):
    return {
        'Taxes': takehome_data['taxes'],
        'Benefits': takehome_data['benefits'],
        'Retirement': takehome_data['retirement']
    }
    

def process_expenses(monthly, expense_data):
    return {
        'Food': round((expense_data['food'] / monthly) * 100, 2),
        'Housing': round((expense_data['housing'] / monthly) * 100, 2),
        'Utilities': round((expense_data['utilities'] / monthly) * 100, 2),
        'Transportation': round((expense_data['transportation'] / monthly) * 100, 2)
    }


def process_other(other_data):
    return {
        'Savings': other_data['savings']
    }


def main():
    budget_data = get_budget_data()['data']
    salary = budget_data['salary']

    takehome_data = process_takehome(budget_data['takehome'])
    expense_data = process_expenses((salary / 12), budget_data['expenses'])
    other_data = process_other(budget_data['other'])

    data = np.array(
        list(takehome_data.values()) + 
        list(expense_data.values()) + 
        list(other_data.values())
    )
    labels = list(takehome_data.keys()) + list(expense_data.keys()) + list(other_data.keys())

    plot.pie(data, labels=labels)
    plot.show()


if __name__ == '__main__':
    main()
