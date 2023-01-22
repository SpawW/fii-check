#!/usr/bin/env python3

import requests
import json

START_MOMENT = '02/01/2023 00:00'
fii_list = 'output/fii-list.csv'


def getFiiData(ticker):
    cookies = {
        'wisepops_session':
        '%7B%22arrivalOnSite%22%3A%222023-01-22T19%3A18%3A45.718Z%22%2C%22mtime%22%3A1674415129448%2C%22pageviews%22%3A2%2C%22popups%22%3A%7B%7D%2C%22bars%22%3A%7B%7D%2C%22countdowns%22%3A%7B%7D%2C%22src%22%3A%22https%3A%2F%2Fwww.google.com%2F%22%2C%22utm%22%3A%7B%7D%2C%22testIp%22%3Anull%7D',
        '__hssrc': '1',
        'wisepops':
        '%7B%22csd%22%3A1%2C%22popups%22%3A%7B%7D%2C%22sub%22%3A0%2C%22ucrn%22%3A22%2C%22cid%22%3A%2252100%22%2C%22v%22%3A4%2C%22bandit%22%3A%7B%22recos%22%3A%7B%7D%7D%7D',
        'wisepops_visits':
        '%5B%222023-01-22T19%3A18%3A45.718Z%22%2C%222023-01-22T19%3A18%3A36.638Z%22%5D',
        '_gcl_au': '1.1.1916320422.1674415119',
        '_ga_B7T95936E1': 'GS1.1.1674415119.1.1.1674415129.50.0.0',
        '_ga': 'GA1.3.1029974601.1674415120',
        '_gid': 'GA1.3.411319576.1674415120',
        'ln_or': 'eyIxNzg4ODE4IjoiZCJ9',
        'blueID': '7f1eca09-b5f0-46d2-aa24-e88b9b2e1e5e',
        '__hstc':
        '189907700.6bedf10feb49a4598ffc40598c3f6ef9.1674415121662.1674415121662.1674415121662.1',
        'hubspotutk': '6bedf10feb49a4598ffc40598c3f6ef9',
        '__hssc': '189907700.2.1674415121662',
        '_hjSessionUser_464057':
        'eyJpZCI6ImQyY2FkNjU5LTUxMDQtNTZhOC1iYWRiLWZkYzVjODM5MzNhYyIsImNyZWF0ZWQiOjE2NzQ0MTUxMjE2MzcsImV4aXN0aW5nIjp0cnVlfQ==',
        '_hjFirstSeen': '1',
        '_hjIncludedInSessionSample': '0',
        '_hjSession_464057':
        'eyJpZCI6IjI2MGY1ZTg5LTA4ZGMtNGQwZi1hM2UwLWZmYWZmYmRkM2Y0ZiIsImNyZWF0ZWQiOjE2NzQ0MTUxMjE3MjgsImluU2FtcGxlIjpmYWxzZX0=',
        '_hjIncludedInPageviewSample': '1',
        '_hjAbsoluteSessionInProgress': '0',
        'messagesUtk': '4dd4a52156fe4293a8b1b9b3adf7bde7',
        '__hs_opt_out': 'no',
        '__hs_initial_opt_in': 'true',
        '_gat_UA-85692343-14': '1',
    }

    headers = {
        'User-Agent':
        'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/109.0',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.5',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Content-Type': 'application/json',
        'Referer': 'https://www.suno.com.br/fundos-imobiliarios/arct11/',
        'Origin': 'https://www.suno.com.br',
        'Connection': 'keep-alive',
        # 'Cookie': 'wisepops_session=%7B%22arrivalOnSite%22%3A%222023-01-22T19%3A18%3A45.718Z%22%2C%22mtime%22%3A1674415129448%2C%22pageviews%22%3A2%2C%22popups%22%3A%7B%7D%2C%22bars%22%3A%7B%7D%2C%22countdowns%22%3A%7B%7D%2C%22src%22%3A%22https%3A%2F%2Fwww.google.com%2F%22%2C%22utm%22%3A%7B%7D%2C%22testIp%22%3Anull%7D; __hssrc=1; wisepops=%7B%22csd%22%3A1%2C%22popups%22%3A%7B%7D%2C%22sub%22%3A0%2C%22ucrn%22%3A22%2C%22cid%22%3A%2252100%22%2C%22v%22%3A4%2C%22bandit%22%3A%7B%22recos%22%3A%7B%7D%7D%7D; wisepops_visits=%5B%222023-01-22T19%3A18%3A45.718Z%22%2C%222023-01-22T19%3A18%3A36.638Z%22%5D; _gcl_au=1.1.1916320422.1674415119; _ga_B7T95936E1=GS1.1.1674415119.1.1.1674415129.50.0.0; _ga=GA1.3.1029974601.1674415120; _gid=GA1.3.411319576.1674415120; ln_or=eyIxNzg4ODE4IjoiZCJ9; blueID=7f1eca09-b5f0-46d2-aa24-e88b9b2e1e5e; __hstc=189907700.6bedf10feb49a4598ffc40598c3f6ef9.1674415121662.1674415121662.1674415121662.1; hubspotutk=6bedf10feb49a4598ffc40598c3f6ef9; __hssc=189907700.2.1674415121662; _hjSessionUser_464057=eyJpZCI6ImQyY2FkNjU5LTUxMDQtNTZhOC1iYWRiLWZkYzVjODM5MzNhYyIsImNyZWF0ZWQiOjE2NzQ0MTUxMjE2MzcsImV4aXN0aW5nIjp0cnVlfQ==; _hjFirstSeen=1; _hjIncludedInSessionSample=0; _hjSession_464057=eyJpZCI6IjI2MGY1ZTg5LTA4ZGMtNGQwZi1hM2UwLWZmYWZmYmRkM2Y0ZiIsImNyZWF0ZWQiOjE2NzQ0MTUxMjE3MjgsImluU2FtcGxlIjpmYWxzZX0=; _hjIncludedInPageviewSample=1; _hjAbsoluteSessionInProgress=0; messagesUtk=4dd4a52156fe4293a8b1b9b3adf7bde7; __hs_opt_out=no; __hs_initial_opt_in=true; _gat_UA-85692343-14=1',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }

    json_data = {
        'ticker': ticker,
        'range': '1M',
    }

    response = requests.post(
        'https://www.suno.com.br/fundos-imobiliarios/api/quotations/filter/',
        cookies=cookies,
        headers=headers,
        json=json_data,
    )

    JSON = json.loads(response.text)
    # print(JSON["quotationsDataArrayResponse"])
    for day in JSON["quotationsDataArrayResponse"]:
        if (day[0] == START_MOMENT):
            # print(ticker, day)
            start = day[1]
        end = day[1]
    tmp = getDividend(ticker)
    return f"{ticker};{start};{end};{tmp[0]};{tmp[1]};{tmp[2]}"


def getDividend(ticker):
    headers = {
        'User-Agent':
        'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/109.0',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'en-US,en;q=0.5',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://www.infomoney.com.br/',
        'Origin': 'https://www.infomoney.com.br',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
    }

    params = {
        'Ticker': ticker,
    }

    response = requests.get(
        'https://fii-api.infomoney.com.br/api/v1/fii/provento/historico',
        params=params,
        headers=headers)

    JSON = json.loads(response.text)
    hyield = [0, 0, 0]
    for month in JSON:
        hyield[0] = hyield[0] + month['rendimento']
        hyield[1] = hyield[1] + month['yield']
        hyield[2] = month['yield']
    # return {'money': hyield[0],'percent': hyield[1]}
    hyield[0] = round(hyield[0], 2)
    hyield[1] = round(hyield[1], 2)
    hyield[2] = round(hyield[2], 2)
    return hyield

print(f"FII;FIRST_DAY;LAST_DAY;YEAR_MONEY;YEAR_PERCENT;LAST_DIVIDEND")
errorList=""
with open(fii_list) as f:
    for line in f:
        line = line.replace("\n", "")
        try:
            print(getFiiData(line))
        except:
            errorList = errorList+(f"{line};;;;;\n") 
        if 'str' in line:
            break

print(errorList)

# print(getFiiData('ARCT11'))
# print(getFiiData('BARI11'))

# print(getDividend('ARCT11'))

# value = JSON["quotationsDataArrayResponse"][day]
# print("Key and Value pair are ({}) = ({})".format(day, value))
# pass
# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"ticker":"ARCT11","range":"1M"}'
#response = requests.post(
#    'https://www.suno.com.br/fundos-imobiliarios/api/quotations/filter/',
#    cookies=cookies,
#    headers=headers,
#    data=data,
#)