import typing

from task_3.data_sets import Data
if typing.TYPE_CHECKING:
    from task_3.servers import Server


class Router:
    buffer: list[Data]
    linked_servers: list["Server"]

    def __init__(self) -> None:
        self.buffer = []
        self.linked_servers = []

    def link(self, server: "Server") -> None:
        self.linked_servers.append(server)

    def unlink(self, server: "Server") -> None:
        self.linked_servers.remove(server)

    def send_data(self) -> None:
        for data_set in self.buffer:
            server, *_ = filter(lambda s: s.ip == data_set.receiver_ip, self.linked_servers) or (None,)
            if server  and data_set not in server.buffer:
                server.buffer.append(data_set)
        self.buffer = []
