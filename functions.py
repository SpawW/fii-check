#!/usr/bin/env python3
import time
import sys
import json
import re
from unicodedata import normalize
import progressbar

def escape(text):
    return re.escape(text)

def unique(listData):

    unique_list = []
    for x in listData:
        if x not in unique_list:
            unique_list.append(x)
    return unique_list


def remover_acentos(txt):
    """Remove special schars

    Arguments:
        txt {string} -- string to remove special chars

    Returns:
        string -- txt without special chars
    """
    return normalize('NFKD', txt).encode('ASCII', 'ignore').decode('ASCII').lower()


def stringPoolCheck(text, pool, poolName, trusted):
    """Check if words from a array of strings exists in a text

    Arguments:
        text {string} -- full text to search words
        pool {object} -- json object with structure: { 'x': { "good": [array], "bad": [array], "tags": [array]}, ...{} }
        poolName {[type]} -- [description]
        trusted {[type]} -- [description]

    Returns:
        [type] -- [description]
    """
    cloudTags = []
    text = remover_acentos(text.lower())
    trusted = remover_acentos(trusted.lower())
    for word in pool["good"]:
        if len(word.strip()) > 1 and word in text:
            # if "desenvolvimento de novo software" in text:
            #     print(["texto",text])
            badFound = False
            if word not in trusted:
                for badWord in pool["bad"]:
                    if len(badWord.strip()) > 1 and "#" not in badWord and badWord in text:
                        badFound = True
                        # return []
                        break
                if badFound:  # If found a bad word abort analisys
                    # if "banda larga" in text:
                    #     print ([badWord,trusted,text,pool,"bad bad robot"])
                    return []
            # print (["aqui",pool])
            for tag in pool["tags"]:
                cloudTags.append(tag)
            # print([pool["tags"],word])
    return cloudTags


"""
str2bool: get a text parameter and return a boolean value
"""


def str2bool(v):
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')


"""
toFloat: Convert a string value to a float and change pontuation
"""


def toFloat(value):
    return float(value.replace('.', '').replace(',', '.'))


def valueExistsDF(uasg, df, field):
    i = 0
    for index, row in df.iterrows():
        # print(uasg,process,row)
        if (row[field] == uasg):
            return i
        i += 1
    return False


def valueExists(uasg, report):
    i = 0
    for row in report:
        # print(uasg,process,row)
        if (row[0] == uasg):
            return i
        i += 1
    return False


def requests_retry_session(
    retries=3,
    backoff_factor=0.3,
    status_forcelist=(500, 502, 504),
    session=None,
):
    session = session or requests.Session()
    retry = Retry(
        total=retries,
        read=retries,
        connect=retries,
        backoff_factor=backoff_factor,
        status_forcelist=status_forcelist,
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    return session


def normalText():
    print('\033[0;37;40m', end='')
    # print('\033[30m', end = '')


def msgOk(msg):
    print("\033[1;32;40m {} ".format(msg))
    normalText()


def msgError(msg):
    print("\033[0;31;47m {} ".format(msg,))
    normalText()

def msgWarning(msg):
    print(f"\033[1;33;47m ==> \033[1;33;40m {msg} ")
    normalText()

def msgDebug(msg):
    print(f"\033[0;35;47m ==> \033[1;32;40m {msg} ")
    normalText()

def updateCSV(csvFileName, fields, func, csvDelimiter=";"):
    from tempfile import NamedTemporaryFile
    import shutil
    import csv

    tempfile = NamedTemporaryFile(mode='w', delete=False)
    # msgDebug(tempfile.name)
    # fields = ['ID', 'Name', 'Course', 'Year']
    with open(csvFileName, 'r') as csvfile, tempfile:
        # print(csvFileName)
        reader = csv.DictReader(csvfile, fieldnames=fields, delimiter=csvDelimiter)
        writer = csv.DictWriter(tempfile, fieldnames=fields, delimiter=csvDelimiter)
        for row in reader:
            row = func(row)
            # print(row)
            writer.writerow(row)
    shutil.move(tempfile.name, csvFileName)


def bar_create(message):
    global widgets, bar
    widgets = [f"{message} ", progressbar.AnimatedMarker()]
    bar = progressbar.ProgressBar(widgets=widgets).start()
    
def bar_update(value):
    bar.update(value)