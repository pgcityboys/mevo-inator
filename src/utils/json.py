def find_json_by_value(key: str, value: str, data: list[dict]):
    for i in data:
        if i[key] == value:
            return i
    raise KeyError(f"Value {value} does not exist")