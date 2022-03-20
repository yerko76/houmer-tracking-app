from dataclasses import dataclass
from typing import Callable, cast

from app.domain.shared.gateway import HoumerDbGateway, PlaceDbGateway
from app.domain.stop.gateway import StopDbGateway
from app.domain.visit.gateway import VisitDbGateway
from app.adapters.database.repositories import houmer_repository, place_repository, visit_repository, stop_repository


@dataclass(frozen=True)
class Dependencies:
    houmer_db_gateway: HoumerDbGateway
    place_db_gateway: PlaceDbGateway
    visit_db_gateway: VisitDbGateway
    stop_db_gateway: StopDbGateway


def _build_dependencies() -> Callable[[], Dependencies]:
    deps = Dependencies(
        houmer_db_gateway=cast(HoumerDbGateway, houmer_repository),
        place_db_gateway=cast(PlaceDbGateway, place_repository),
        visit_db_gateway=cast(VisitDbGateway, visit_repository),
        stop_db_gateway=cast(StopDbGateway, stop_repository),
    )

    def fn() -> Dependencies:
        return deps

    return fn


get_dependencies = _build_dependencies()
