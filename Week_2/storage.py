import json
import tempfile
import argparse
import os

'''
Key-value хранилище, вызывается через терминал з параметрами --key, --val, 
записывает и возвращает данные по ключу
'''

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')


def read_data(path):
    if os.path.isfile(path):
        with open(path, 'r') as f:
            return json.load(f)
    else:
        with open(path, 'w') as f:
            f.read()
        return {}


def write_data(key, value):
    data = read_data(storage_path)
    try:
        if data[key]:
            data[key].append(value)
    except KeyError:
        data[key] = []
        data[key].append(value)
    with open(storage_path, 'w') as f:
        json.dump(data, f)


def get_data(key):
    data = read_data(storage_path)
    try:
        print(*data[key], sep=', ')
    except KeyError:
        print(None)


parser = argparse.ArgumentParser()
parser.add_argument('--key', help='input key')
parser.add_argument('--val', help='input val')
args = parser.parse_args()


def _main():
    if args.key and args.val:
        write_data(args.key, args.val)
    elif not args.val:
        get_data(args.key)


if not os.path.isfile(storage_path):
    with open(storage_path, 'w') as f:
        json.dump({}, f)

if __name__ == '__main__':
    _main()
