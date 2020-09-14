import os
import tempfile
import argparse
import json

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')


def get_data():
    with open(storage_path, 'r') as f:
        raw_data = f.read()
        if raw_data:
            return json.loads(raw_data)
        return {}


def add_data(key, value):
    data = get_data()
    if key in data:
        data[key].append(value)
    else:
        data[key] = [value]
    with open(storage_path, 'w') as f:
        f.write(json.dumps(data))


def get_value(key):
    data = get_data()
    return data.get(key)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--key', required=True)
    parser.add_argument('--val')

    args = parser.parse_args()

    if args.key and args.val:
        add_data(args.key, args.val)
    else:
        print(get_value(args.key))


