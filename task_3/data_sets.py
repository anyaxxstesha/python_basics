class Data:
    data: str
    receiver_ip: int

    def __init__(self, data, receiver_ip) -> None:
        self.data = data
        self.receiver_ip = receiver_ip

    def __str__(self):
        return self.data

    def __repr__(self):
        return self.data
