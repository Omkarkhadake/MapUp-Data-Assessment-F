import pandas as pd


def calculate_distance_matrix(df)->pd.DataFrame():
    distances_df = pd.DataFrame({'start_id': df['id_start'], 'end_id': df['id_end'], 'distance': df['distance']})

    distance_matrix = distances_df.pivot(index='start_id', columns='end_id', values='distance').fillna(0)

    distance_matrix = distance_matrix.add(distance_matrix.T, fill_value=0)

    cumulative_distance_matrix = np.triu(distance_matrix.values) + np.triu(distance_matrix.values, 1).T

    np.fill_diagonal(cumulative_distance_matrix, 0)

    cumulative_distance_df = pd.DataFrame(cumulative_distance_matrix, index=distance_matrix.index, columns=distance_matrix.columns)

    return cumulative_distance_df


def unroll_distance_matrix(df)->pd.DataFrame():
    lower_triangle = np.tril(distance_matrix.values, k=-1)

    indices = np.nonzero(lower_triangle)

    unrolled_df = pd.DataFrame({
        'id_start': distance_matrix.index[indices[0]],
        'id_end': distance_matrix.columns[indices[1]],
        'distance': lower_triangle[indices]
    })

    return unrolled_df


def find_ids_within_ten_percentage_threshold(df, reference_id)->pd.DataFrame():

    reference_rows = df[df['id_start'] == reference_value]

    reference_avg_distance = reference_rows['distance'].mean()

    lower_threshold = reference_avg_distance - 0.1 * reference_avg_distance
    upper_threshold = reference_avg_distance + 0.1 * reference_avg_distance

    within_threshold_ids = df[(df['distance'] >= lower_threshold) & (df['distance'] <= upper_threshold)]['id_start'].unique()

    sorted_within_threshold_ids = sorted(within_threshold_ids)

    return sorted_within_threshold_ids


def calculate_toll_rate(df)->pd.DataFrame():
    rate_coefficients = {
        'moto': 0.8,
        'car': 1.2,
        'rv': 1.5,
        'bus': 2.2,
        'truck': 3.6
    }
    for vehicle_type, rate_coefficient in rate_coefficients.items():
        df[vehicle_type] = df['distance'] * rate_coefficient

    return df


def calculate_time_based_toll_rates(df)->pd.DataFrame():
    """
    Calculate time-based toll rates for different time intervals within a day.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame
    """
    # Write your logic here

    return df
