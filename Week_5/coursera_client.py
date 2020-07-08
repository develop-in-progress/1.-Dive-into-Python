import time
import socket

"""
Клиент для отправки метрик на сервер
Протокол поддерживает два вида запросов к серверу со стороны клиента:
- отправка данных для сохранения их на сервере
- получения сохраненных данных
Общий формат запроса клиента:
<команда> <данные запроса><\n>
- <команда> - команда сервера (команда может принимать одно из двух значений: put — сохранить данные на сервере, get — вернуть сохраненные данные с сервера),
- <данные запроса> - данные запроса (их формат мы подробно разберем ниже в примере),
- <\n> - символ переноса строки.
"""


class ClientError(Exception):
    pass


class Client():
    def __init__(self, host, port, timeout=None):
        self.host = host
        self.port = port
        self.timeout = timeout
        self.conn = socket.create_connection((self.host, self.port), self.timeout)

    def _read(self):
        data = b''
        try:
            while not data.endswith(b'\n\n'):
                data += self.conn.recv(1024)
        except socker.error:
            raise ClientError

        status, payload = data.split(b'\n', 1)
        if status != b'ok':
            raise ClientError

        return payload

    def put(self, key, value, timestamp=None):
        """
        Метод put не возвращает ничего в случае успешной отправки и выбрасывает пользовательское исключение
        ClientError в случае не успешной."""
        # put palm.cpu 23.7 1150864247\n
        timestamp = timestamp or int(time.time())

        self.conn.sendall('put {} {} {}\n'.format(key, value, timestamp).encode())
        self._read()

    def get(self, key):
        self.conn.sendall('get {}\n'.format(key).encode())
        data = {}
        payload = self._read()
        if payload == b'\n':
            return data
        try:
            for i in payload.decode().strip().split('\n'):
                raw = i.split(' ')
                if len(raw) != 3:
                    raise ClientError
                if type(float(raw[1])) != float or type(int(raw[2])) != int:
                    raise ClientError
                if raw[0] not in data:
                    data[raw[0]] = []
                data[raw[0]].append((int(raw[2]), float(raw[1])))

        except (IndexError, KeyError):
            raise ClientError
        for key in data.keys():
            data[key].sort(key=lambda x: x[0])
        return data

    def _close(self):
        self.conn.close()
