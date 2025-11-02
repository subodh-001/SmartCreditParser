def normalize_data(data):
    for key, value in data.items():
        if not value:
            data[key] = "Not found"
    return data
