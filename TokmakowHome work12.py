import pytest
import requests


def test_request_with_invalid_date():
    date = "31-06-2024"
    url = f"https://api.nasa.gov/planetary/apod?api_key=jUsYymkf0vV58o8oJUSsls07GhfVpBW1HmURrBla&date={date}"
    response = requests.get(url)
expected_result = range(400, 500)

result = response.status_code  # одно число
return result in expected_result

