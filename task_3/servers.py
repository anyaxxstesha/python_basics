from task_3.data_sets import Data
from task_3.routers import Router


class Server:
    ip: int
    buffer: list[Data] | None
    router: Router

    ips = [0]

    def __init__(self, router) -> None:
        self.ip = self.ips[-1] + 1
        self.ips.append(self.ip)
        self.buffer = []
        self.router = router

    def send_data(self, data: Data) -> None:
        linked_server, *_ = list(filter(lambda s: s.ip == self.ip, self.router.linked_servers)) or (None,)
        if linked_server:
            self.router.buffer.append(data)

    def get_data(self) -> list[Data]:
        received_data = self.buffer
        if received_data:
            self.buffer = []
            return received_data
        return []

    def get_ip(self) -> int:
        return self.ip
