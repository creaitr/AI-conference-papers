import pathlib
from pathlib import Path
import argparse
import time
import re
import pandas as pd


def init_database(path):
    # init a dataframe
    df = pd.DataFrame(columns=['Year', 'Conf', 'Title', 'Link', 'Authors', 'Keywords'])

    # check the input
    if '.tsv' in path:
        file_list = [Path(path)]
    else:
        file_list = list(Path(path).glob('*.tsv'))
    print(f"{len(file_list)} tsv files are listed...")

    # main loop
    for tsv_path in file_list:
        # load the tsv file
        tsv = pd.read_csv(tsv_path, sep='\t').fillna('-')
        
        # For the crawled tsv files
        if tsv.columns[0] == 'No.':
            # load the conference name and year 
            tsv_name = tsv_path.name[10:-4]
            year, conf = int(tsv_name[-4:]),  tsv_name[:-4]
            
            # modify the columns
            tsv.drop(tsv.columns[0], axis=1, inplace=True)
            tsv.insert(0, 'Year', year)
            tsv.insert(1, 'Conf', conf)

        # add to the df
        df = df.append(tsv, ignore_index=True)
        del tsv

    print(f'Finished to read all paper lists ({df.shape[0]} entries)...')
    return df


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--path', dest='path', type=str, default='./paperlist',
                        help='the path of a folder containing tsv files or a file formmated in tsv.')
    parser.add_argument('-c', '--conf', dest='conf', type=str, default=None,
                        help='a list of conferences, e.g., iclr\\|nips')
    parser.add_argument('-y', '--year', dest='year', type=str, default=None, nargs='+',
                        help='a list of year queries, e.g., \>\\=2020 \<2021')
    parser.add_argument('-t', '--title', dest='title', type=str, default=None,
                        help='a list of words with & or |, e.g., convolution\|quantization. ')
    parser.add_argument('-k', '--keyword', dest='keyword', type=str, default=None,
                        help='a list of words with & or |, e.g., compreesion\&detection')
    args = parser.parse_args()

    # set a data frame using pandas
    df = init_database(args.path)

    # set search conditions
    print('Search conditions:')
    conds = []
    # Conferences
    if args.conf != None:
        print(f'  - Conferences: {args.conf}')
        conds.append('(df[\"Conf\"].str.contains(args.conf, case=False))')
    # Year
    if args.conf != None:
        print('  - Years:', end='')
        for query in args.year:
            print(f' {query}', end='')
            conds.append(f'(df[\"Year\"]{query})')
        print()
    # Title or Keyword
    if args.title != None:
        print(f'  - Title: {args.title}')
        if '&' in args.title:
            query = ''.join([f'(?=.*{w})' for w in args.title.split('&')])
            query = f'r\'^{query}\''
        else:
            query = f'\'{args.title}\''
        conds.append(f'(df[\"Title\"].str.contains({query}, case=False))')
    elif args.keyword != None:
        print(f'  - Keywords: {args.keyword}')
        if '&' in args.keyword:
            query = ''.join([f'(?=.*{w})' for w in args.keyword.split('&')])
            query = f'r\'^{query}\''
        else:
            query = f'\'{args.keyword}\''
        conds.append(f'(df[\"Keywords\"].str.contains({query}, case=False))')
    
    # search papers
    if len(conds) == 0:
        print('  - None')
        result = df
    else:
        cond = eval(' & '.join(conds))
        result = df.loc[cond, :]
        result = result.reset_index(drop=True)

    # save the results
    result_name = f'result_{time.strftime("%Y%m%d-%H%M%S")}.tsv'
    result.to_csv(result_name, sep='\t')
    print(f'The searched {result.shape[0]} papers are saved at {result_name}!')
