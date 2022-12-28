from typing import Optional

import requests
from api.exceptions import ErrorResponse


class AlphavantageApiClient:
    BASE_URL = "https://www.alphavantage.co"
    QUERY_URL = f"{BASE_URL}/query"

    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or "X86NOH6II01P7R24"

    def get_stock_info(self, query_params={}):
        _query_params = {
            "function": "TIME_SERIES_DAILY_ADJUSTED",
            "outputsize": "compact",
            "apikey": self.api_key,
        }
        _query_params.update(query_params)
        response = requests.get(
            url=self.QUERY_URL,
            params=_query_params,
            timeout=(2, 10)
        )
        if response.status_code == 200:
            return response.json()
        else:
            raise ErrorResponse(f"Invalid response (code {response.status_code} from foreign API: {response.text}")
