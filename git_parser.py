'''
git a commit from the github or from the company server and set the commit in the
Excel file
'''
from datetime import date, timedelta,datetime
# from pydriller import Repository
# from pydriller.domain.commit import ModificationType
# import xlsxwriter as xw

Repository = None
ModificationType = None
xw = None

import pandas as pd
from pathlib import Path


def show_commit(args):

    # Create a output file
    if args.output_file:
        # The user choosed a new local path through the flag (-o)

        output_data_file_path = Path(args.output_file, "outputExcel_file.xlsx")
        workbook = xw.Workbook(output_data_file_path)
        print(f"Excel file created in: {output_data_file_path}")
    else:
        # Set in a same arg_parser.py path
        output_data_file_path = "outputExcel_file.xlsx"
        workbook = xw.Workbook(output_data_file_path)
        print("Excel file created in: local_python_file_path/outputExcel_file.xlsx")

    # Set worksheet name
    worksheet = workbook.add_worksheet(name="parser_git_commit")

    # Add worksheet font format
    bold = workbook.add_format({'bold': True})
    italic = workbook.add_format(dict(italic=True))

    if args.show_lats_days:
        # The user defined to show only commits from the last 'X' days through the flag (-d)
        today = datetime.now().today()
        first_day = today - timedelta(days=args.show_lats_days)
        print(first_day)
        print(today)

    else:
        # Show all the commits
        first_day = None
        today = None


    print("Please wait...")
    row_number = 0
    col_number = 0

    # Set the titles in the firs row in the Excel file
    worksheet.write(row_number, col_number, 'hash commit', bold)
    worksheet.write(row_number, col_number + 1, 'Commit subject', bold)
    worksheet.write(row_number, col_number + 2, 'Commit Date', bold)
    worksheet.write(row_number, col_number + 3, 'File Name', bold)

    for commit in Repository(path_to_repo=args.repository, since=first_day, to=today).traverse_commits():
        row_number += 1

        worksheet.write(row_number, col_number, commit.hash[:12])
        worksheet.write(row_number, col_number + 1, commit.msg)
        worksheet.write(row_number, col_number + 2, str(commit.author_date))
        worksheet.write(row_number, col_number + 3, ','.join([mf.filename for mf in commit.modified_files]), italic)

    workbook.close()
    print("finish...")

    # open the xlsx file and put the data in dataframe
    df_dataframe = pd.read_excel(output_data_file_path)

    # print the dataframe
    print(df_dataframe)





