import requests

def get_json(url, params=None, headers=None, timeout=1):
    try:
        data = requests.get(url, params=params, headers=headers, timeout=timeout)
        data.raise_for_status()
        return data.json()
    except requests.exceptions.Timeout:
        print("The requests took too long.")
    except requests.exceptions.ConnectionError:
        print("Could not connect to the server.")
    except requests.exceptions.HTTPError as error:
        print(f"The server said NO: {error.response.status_code}")
    except requests.exceptions.JSONDecodeError:
        print("The answer was not JSON")
    except requests.exceptions.RequestException as error:
        print(f"Someting else went wrong: {type(error).__name__}")
    return None