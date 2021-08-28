import pathlib
from pathlib import Path
import argparse
import re
import pandas as pd


def init_database(fol_path):
    df = pd.DataFrame(columns=['Year', 'Conf', 'Title', 'Link', 'Authors', 'Keywords'])
    for tsv_path in Path(fol_path).glob('*.tsv'):
        # load the conference name and year 
        tsv_name = tsv_path.name[10:-4]
        year, conf = int(tsv_name[-4:]),  tsv_name[:-4]

        # load the tsv file
        tsv = pd.read_csv(tsv_path, sep='\t').fillna('-')
        
        # modify the columns
        tsv.drop(tsv.columns[0], axis=1, inplace=True)
        tsv.insert(0, 'Year', year)
        tsv.insert(1, 'Conf', conf)

        # add to the df
        df = df.append(tsv, ignore_index=True)
        del tsv

    df.info()
    print('\nFinished to read all paper lists...')
    return df


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--path', dest='path', type=str, default='./paperlist',
                        help='the path of folder containing tsv files.')
    args = parser.parse_args()

    # set a data frame using pandas
    df = init_database(args.path)

    # search papers
    #print(df.loc[df["Title"].str.contains("Quantiz|pruning", case=False), df.columns[0:3]])
    print(df.loc[df["Title"].str.contains(r'^(?=.*pruning)(?=.*quantiz)', case=False), df.columns[0:3]])