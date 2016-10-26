import pandas as pd

def test_run():
    df = pd.read_csv('data/000898.csv')
    print(df.head())

if __name__ == '__main__':
    test_run()
