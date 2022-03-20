
class HoumerNotFoundError(Exception):
    def __init__(self, id_, msg="houmer not found"):
        super().__init__(msg)
        self.houmer_id = id_
        self.msg = msg

    def as_dict(self):
        return {"msg": self.msg, "houmer_id": self.houmer_id}
