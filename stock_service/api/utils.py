from api.exceptions import ErrorResponse


def retrieve_last_two_days(stock_info):
    """
    Retrieve the last two days of stock info. Returns a tuple with the last_day (0)
    and previous_day (1).
    """
    if stock_info.get('Error Message', None):
        raise ErrorResponse(f"Error retrieving stock info: {stock_info['Error Message']}")
    try:
        stock_info = stock_info['Time Series (Daily)']
        days_info = list(stock_info.items())
        last_day = days_info[0]
        last_day = {
            'open': last_day[1]['1. open'],
            'high': last_day[1]['2. high'],
            'low': last_day[1]['3. low'],
            'close': last_day[1]['4. close'],
        }
        previous_day = days_info[1]
        previous_day = {
            'open': previous_day[1]['1. open'],
            'high': previous_day[1]['2. high'],
            'low': previous_day[1]['3. low'],
            'close': previous_day[1]['4. close'],
        }
        return last_day, previous_day
    except KeyError as e:
        raise Exception(f"Error parsing stock info: {e}, options are: {stock_info.keys()}")
