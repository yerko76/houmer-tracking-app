
class VisitNotFoundError(Exception):
    def __init__(self, id_, msg="visit not found"):
        super().__init__(msg)
        self.visit_id = id_
        self.msg = msg

    def as_dict(self):
        return {"msg": self.msg, "visit_id": self.visit_id}
