import requests

def fetch_posts():
    try:
        response=requests.get("https://jsonplaceholder.typicode.com/posts", timeout=5)


        if response.status_code==200:
            data=response.json()
            print(f"API request succeeded: {response.status_code}")
            return data
        else:
            return None
    except requests.exceptions.ConnectionError:
        return None

    except requests.exceptions.Timeout:
        return None

    except requests.exceptions.JSONDecodeError:
        return None
