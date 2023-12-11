import pandas as pd


def generate_car_matrix(df)->pd.DataFrame:
 matrix_df = df.pivot(index='id_1', columns='id_2', values='car').fillna(0)

    for index in matrix_df.index:
        if index in matrix_df.columns:
            matrix_df.loc[index, index] = 0

    return matrix_df



def get_type_count(df)->dict:
    """
    df['car_type'] = pd.cut(df['car'], bins=[-float('inf'), 15, 25, float('inf')],
                            labels=['low', 'medium', 'high'], right=False)

    type_count = df['car_type'].value_counts().to_dict()

    sorted_type_count = dict(sorted(type_count.items()))

    return sorted_type_count


def get_bus_indexes(df)->list:
    bus_mean = df['bus'].mean()

    bus_indexes = df[df['bus'] > 2 * bus_mean].index.tolist()

    bus_indexes.sort()

    return bus_indexes


def filter_routes(df)->list:
    route_avg_truck = df.groupby('route')['truck'].mean()

    selected_routes = route_avg_truck[route_avg_truck > 7].index.tolist()

    selected_routes.sort()

    return selected_routes


def multiply_matrix(matrix)->pd.DataFrame:
    modified_matrix = result_matrix.applymap(lambda x: x * 0.75 if x > 20 else x * 1.25)

    modified_matrix = modified_matrix.round(1)

    return modified_matrix


def time_check(df)->pd.Series:

    df['start_datetime'] = pd.to_datetime(df['startDay'] + ' ' + df['startTime'], format='%Y-%m-%d %I:%M %p', errors='coerce')
    df['end_datetime'] = pd.to_datetime(df['endDay'] + ' ' + df['endTime'], format='%Y-%m-%d %I:%M %p', errors='coerce')

    df['duration'] = df['end_datetime'] - df['start_datetime']

    completeness_check = df.groupby(['id', 'id_2']).apply(lambda group: (
        (group['duration'].min() >= pd.Timedelta(hours=24)) and
        (group['duration'].max() <= pd.Timedelta(days=7))
    ))

    return completeness_check
