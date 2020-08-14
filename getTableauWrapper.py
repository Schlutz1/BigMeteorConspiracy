# Simple wrapper for tableau functions

from pandleau import *
import datetime
import os

path_tableau = "./tableau/"
path_logs = "./logs/"


def makeConversion(df, filename) :
    """convert dataframe to .hyper extract"""

    if not os.path.isdir(path_tableau):
        os.mkdir(path_tableau)

    df_tmp = pandleau(df)

    # remove if file exists, write out new file
    file_out = os.path.join(path_tableau, "{0}.hyper".format(filename))

    if os.path.isfile(file_out):
        os.remove(file_out)

    df_tmp.to_tableau(file_out, add_index=False)

    print("PYTHON: {0}".format(datetime.datetime.now().strftime("%d/%m/%Y %H:%M")))

    
def cleanLogs():
    """clean log files function"""

    if not os.path.isdir(path_logs):
        os.mkdir(path_logs)

    files_logs = [
        f for f in os.listdir("./")
        if os.path.isfile(os.path.join("./", f)) and ".log" in f
        or "hyper_db_" in f
    ]

    for file in files_logs:
        os.rename(file, os.path.join(path_logs, file))

    print("\nPYTHON: Directory cleaned")
    print("PYTHON: {0}".format(datetime.datetime.now().strftime("%d/%m/%Y %H:%M")))
