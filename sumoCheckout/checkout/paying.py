import random
import logging

from .signature import send_signed_request

""" This is a very simple script working on Binance Pay API

Set your KEY and SECRET in signature.py, then you are ready to go.

"""

logging.basicConfig(level=logging.DEBUG)

# Query Order
# 
# POST /binancepay/openapi/order/query
# https://developers.binance.com/docs/binance-pay/api-order-query
# def query_order():
#   response = send_signed_request(
#     'POST', 
#     '/binancepay/openapi/order/query',
#     {
#       'merchantId': '523839444',
#       'merchantTradeNo': '121055692278489088'
#     }
#   )
#   print(response)

# query_order()


# Create Order

# POST /binancepay/openapi/order
# https://developers.binance.com/docs/binance-pay/api-order-create
def create_order():
  id=str(random.randint(0,1999999999))
  print(id)
  response = send_signed_request(
    'POST',
    #'/binancepay/openapi/order',
    # {
    #   'merchantId': '523839444',
    #   'merchantTradeNo': id,
    #   'tradeType': 'WEB',
    #   'totalFee': '0.01',
    #   'currency': 'USDT',
    #   'productType': 'Application',
    #   'productName': 'Sumo',
    #   'productDetail': 'Application to install',
    #   'returnUrl': 'https://e14f-197-49-33-90.ngrok-free.app/callback'
    # }
    '/binancepay/openapi/v3/order',
      {
        "env": {
          "terminalType": "WEB"
        },
        "merchantTradeNo": id,
        "orderAmount": 0.01,
        "currency": "USDT",
        "description": "Sumo Files",
        "goodsDetails": [
          {
            "goodsType": "02",
            "goodsCategory": "Z000",
            "referenceGoodsId": "12345678",
            "goodsName": "SUMO",
            "goodsDetail": "Sump application files"
          }
        ],
        'returnUrl': 'https://e14f-197-49-33-90.ngrok-free.app/callback',
        'cancelUrl': 'https://e14f-197-49-33-90.ngrok-free.app/fail'
    }
    
  )
  print(response)
  return response

#create_order()

# You are free to test on more endpoints with send_signed_request
# https://developers.binance.com/docs/binance-pay/api-order-create