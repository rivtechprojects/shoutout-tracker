import json


def load_json(file_path: str) -> dict:
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
    
    
def save_json(file_path: str, data: dict) -> None:
    with open(file_path, 'w') as f:
        json.dump(data, f)