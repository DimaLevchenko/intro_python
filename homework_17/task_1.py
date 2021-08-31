# Дано два кортежа, напишите функцию которая соединит их в один dict:
# Input:
# coin = ('Bitcoin', 'Ether', 'Ripple', 'Litecoin')
# code = ('BTC', 'ETH', 'XRP', 'LTC')
# Output:
# {'Bitcoin': 'BTC', 'Ether': 'ETH', 'Ripple': 'XRP', 'Litecoin': 'LTC'}
coin = ('Bitcoin', 'Ether', 'Ripple', 'Litecoin')
code = ('BTC', 'ETH', 'XRP', 'LTC')


def to_dict(tup1, tup2):
    di = {k: v for k, v in zip(tup1, tup2)}
    return di


to_dict(coin, code)
