import pandas as pd

def read_file_csv(filename):
    df = pd.read_csv(filename)
    print(df)
    return df
    
def create_data_lookup(filename):
    df = read_file_csv(filename)
    data = df.to_numpy()
    N = len(data)
    DM = data[:, -N:]
    return {
        "NAME": df["NAME"],
        "LAT": df["LAT"],
        "LNG": df["LNG"],
        "DEMAND": df["DEMAND"],
        "VISITED TIME": df["VISITED TIME"],
        "DISTANCE_MATRIX": DM,
        "DM": DM
    }
    