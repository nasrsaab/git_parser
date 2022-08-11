# Git parser is my first task in Nvidia company.
This script in Python that connect with any Repo in world,
and parse the Repo and take all the commits and sort him in Excel file.
In first column write the Hash commit after that write the commit massege,
and date, and in the end write all the files name that related with the same Hash commit.

To run this project you need to do that:
1. Download the git parser Repo to you pc
2. Open cmd or any command line
3. python3 setup.py install
4. python3 module.py -h (for help)
5. python3 module.py -r  RepoName.git   -o c:\outputExcelFile.xlsx  -d 15

-r = Repo URL (Imperative)
-o = output file path (Optional)
-d = last X days (Optional)

