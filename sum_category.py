import pandas as pd

def sum_category(df, list_columns, parent_pol=None):
    result = []
    parents = []
    for el in list_columns:
        result.append(df[el].sum())
    if parent_pol == None:
        result_df = pd.DataFrame(
            list(zip(list_columns, result)),
            columns =['category', 'count']
        )
    else:
        for el in result:
            parents.append(parent_pol)
        result_df = pd.DataFrame(
            list(zip(list_columns, result, parents)),
            columns =['category', 'count', 'parent']
        )
    return result_df
