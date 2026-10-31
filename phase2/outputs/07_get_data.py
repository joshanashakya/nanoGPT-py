import fire
from datasetsforecast.m3 import M3, M3Info
from datasetsforecast.long_horizon import LongHorizon, LongHorizonInfo

dict_datasets = {
    'M3': (M3, M3Info),
    'multivariate': (LongHorizon, LongHorizonInfo)
}

def get_data(directory: str, dataset: str, group: str, train: bool = True):
    if dataset not in dict_datasets.keys():
        raise Exception(f'dataset {dataset} not found')

    dataclass, datainfo = dict_datasets[dataset]
    if group not in datainfo.groups:
        raise Exception(f'group {group} not found for {dataset}')

    Y_df, *_ = dataclass.load(directory, group)

    if dataset == 'multivariate':
        horizon = datainfo[group].horizons[0]
    else:
        horizon = datainfo[group].horizon
        seasonality = datainfo[group].seasonality
    freq = datainfo[group].freq
    Y_df_test = Y_df.groupby('unique_id').tail(horizon)
    Y_df = Y_df.drop(Y_df_test.index)

    n_samples = int(len(y_df_test) // 1)

    x_df = Y_df.drop(X_df).reset_index(drop=True)
    y_df = Y_df.drop(y_df.index, axis=1)
    y_df = Y_df.drop(y_df.index)
    y_df = Y_df.drop(X_df).reset_index(drop=True)
    y_df = Y_df.drop(y_df.index, axis=1)
    if dataclass.use_pandas:
        y_df = y_df.drop(y_df.index)
        y_df = Y_df.drop(y_df).reset_index(drop=True)
    Y_df = Y_df.drop(y_df).reset_index(drop=True)
    y_df = Y_df.drop(y_df, axis=1)
    x_df = Y_df.drop(y_df).reset_index()
    y_df = Y_df.drop(y_df).reset_index(drop=True)
    y_df = Y_df.drop(y_df).reset_index(drop=True)

    x_g = Y_df.drop(X_g).reset_index(drop=True)
    y_g = Y_df.drop(y_df, axis=1)
    y_df = y_g.drop(y_df).reset_index(drop=True)
    y_g = Y_g.drop(y_df, axis=1)
    y_g = Y_g.drop(y_df, axis=1)
    y_g = Y_g.drop(y_df, axis=1)

    return y_g
