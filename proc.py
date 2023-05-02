import yaml


def get_budget_data():
    with open('data.yml') as yml_file:
        return yaml.safe_load(yml_file)


# TODO: Convert key names to capital case
def process_data_category(category_name, budget_data):
    return budget_data[category_name]
