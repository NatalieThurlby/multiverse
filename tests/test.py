import pandas as pd
import patsy
import numpy as np
import statsmodels.formula.api as smf


def test_maps():
    """
    Loads in the MAPS synthetic data.
    Performs a basic multiverse analysis.
    Returns a table of results
    :return:
    """
    pd.set_option('display.max_columns', 20)

    # LOAD DATA:
    # TODO: At input stage, need to have types (e.g. ordinal, categorical) of all possible relevant columns.
    synthetic_data_path = 'docs/_data/maps-synthetic-data.csv'
    d_types = {'has_dep_diag': 'category',
               'comp_week': 'category'}
    synthetic_data = pd.read_csv(synthetic_data_path, index_col=0, dtype=d_types)

    variables = ['has_dep_diag', 'comp_week', 'mat_dep']
    synthetic_data = synthetic_data[variables]
    synthetic_data = synthetic_data.dropna()

    order_comp_week = ['Not at all', 'Less than 1 hour', '1-2 hours', '3 or more hours']
    synthetic_data['comp_week'] = synthetic_data['comp_week'].cat.reorder_categories(order_comp_week, ordered=True)

    print(synthetic_data.head())
    print(synthetic_data.dtypes)

    formula = 'has_dep_diag ~ comp_week + mat_dep'
    y, X = patsy.dmatrices(formula, data=synthetic_data, return_type='dataframe')

    print(f"y, {len(y)}")
    print(f"X, {len(X)}")

    mod = smf.OLS(y, X)  # Describe model
    res = mod.fit()  # Fit model
    print(res.summary())
    # design_matrix = patsy.dmatrices(formula, synthetic_data)
    # print(design_matrix)

    assert 0
    return None