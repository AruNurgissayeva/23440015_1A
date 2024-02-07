import pandas as pd


def clean(input1, input2, output):
    df_1 = pd.read_csv(input1)
    df_2 = pd.read_csv(input2)

    df_new = pd.merge(df_1, df_2, left_on='respondent_id', right_on='id')
    df_new.drop('id', axis=1, inplace=True)
    df_new.dropna(inplace=True)
    df_new = df_new[~df_new['job'].str.contains('insurance', na=False, case=False)]
    print(f'The shape of the cleaned data is: {df_new.shape}')
    df_new.to_csv(output, index=False)


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()

    parser.add_argument('input1', help='Data file 1 (CSV)')
    parser.add_argument('input2', help='Data file 2 (CSV')
    parser.add_argument('output', help='Cleaned data file (CSV)')
    args = parser.parse_args()

    clean(args.input1, args.input2, args.output)