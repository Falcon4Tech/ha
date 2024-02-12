import requests
import time
import hashlib
import hmac
import uuid
import json
import config

api_key = config.API_KEY
secret_key = config.SECRET_KEY

url = "https://api.bybit.com"
recv_window = str(5000)

def HTTP_Request(endPoint, method, payload, Info, httpClient):
    time_stamp = str(int(time.time() * 10 ** 3))
    signature = genSignature(payload, time_stamp)
    headers = {
        'X-BAPI-API-KEY': api_key,
        'X-BAPI-SIGN': signature,
        'X-BAPI-SIGN-TYPE': '2',
        'X-BAPI-TIMESTAMP': time_stamp,
        'X-BAPI-RECV-WINDOW': recv_window,
        'Content-Type': 'application/json'
    }
    if method == "POST":
        response = httpClient.request(method, url + endPoint, headers=headers, data=payload)
    else:
        response = httpClient.request(method, url + endPoint + "?" + payload, headers=headers)
    return response.text

def genSignature(payload, time_stamp):
    param_str = time_stamp + api_key + recv_window + payload
    hash_value = hmac.new(bytes(secret_key, "utf-8"), param_str.encode("utf-8"), hashlib.sha256)
    return hash_value.hexdigest()

def get_average_value():
    endpoint = "/v5/market/mark-price-kline"
    method = "GET"
    params = 'symbol=BTCUSDT&interval=60&limit=1'
    re = HTTP_Request(endpoint, method, params, "Kline", requests.Session())
    obj = json.loads(re)
    obj = obj['result']
    nested_list = obj.get("list", [])

    sum_values = 0
    count_values = 0

    for sublist in nested_list:
        for value in sublist[1:]:
            sum_values += float(value)
            count_values += 1

    average_value = sum_values / count_values if count_values != 0 else 0
    return round(average_value, 2)

def get_sum_wallet():
    account_types = ['FUND', 'SPOT', 'CONTRACT', 'INVESTMENT']
    sum_wallet = 0
    endpoint = "/v5/asset/transfer/query-account-coins-balance"
    method = "GET"

    for account_type in account_types:
        params = f'accountType={account_type}&coin=BTC,USDT'
        re = HTTP_Request(endpoint, method, params, "Balance", requests.Session())
        obj = json.loads(re)

        if obj['retMsg'] == "success":
            balances = obj['result']['balance']
            
            for balance_item in balances:
                coin = balance_item.get('coin')
                balance_str = balance_item.get('walletBalance', '0')

                if coin == 'BTC':
                    sum_wallet += float(balance_str)
                elif coin == 'USDT':
                    sum_wallet += float(balance_str) / get_average_value()

    return round(sum_wallet, 6)

def main():
    average_value = get_average_value()
    sum_wallet = get_sum_wallet()

    response_data = {
        "price": average_value,
        "sum": sum_wallet
    }
    json_response = json.dumps(response_data)
    print(json_response)

if __name__ == "__main__":
    main()

