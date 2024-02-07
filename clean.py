import sys
import pandas as pd


def clean_data(input1, input2, output):
    df_1 = pd.read_csv(input1)
    df_2 = pd.read_csv(input2)

    df_new = pd.merge(df_1, df_2, left_on='respondent_id', right_on='id')
    df_new.drop('id', axis=1, inplace=True)
    df_new.dropna(inplace=True)
    df_new = df_new[~df_new['job'].str.contains('insurance', na=False, case=False)]
    df_new.to_csv(output, index=False)


def main():
    if len(sys.argv) != 4:
        sys.exit(1)
    input1, input2, output = sys.argv[1], sys.argv[2], sys.argv[3]
    clean_data(input1, input2, output)


if __name__ == '__main__':
    main()
