from typing import Optional

from fastapi import APIRouter, Request
from pydantic import BaseModel


class Link(BaseModel):
    href: str
    rel: str
    type: Optional[str]
    hreflang: Optional[str]
    title: Optional[str]
    length: Optional[int]


class CollectionSummary(BaseModel):
    id: str
    title: Optional[str]
    description: Optional[str]
    attribution: Optional[str]
    links: list[Link]
    # extent: List[Extent] = []
    itemType: Optional[str]
    # crs: List[str] = []


class Collection(CollectionSummary):
    data_type: str  # 'Gridded'
    # variables: list[str]
    # licences: list[Licence]


class Collections(BaseModel):
    collections: list[CollectionSummary]
    links: list[Link]


router = APIRouter(
    prefix="/collections",
    tags=["catalogue"],
)


@router.get("/", response_model=Collections)
async def collections(request: Request) -> Collections:
    base = request.url_for("collections")
    return Collections(
        collections=[
            {
                "id": "reanalysis-era5-pressure-levels",
                "title": "ERA5 hourly data on pressure levels from 1979 to present",
                "description": "ERA5 is the fifth generation ECMWF reanalysis for the global climate…",
                "itemType": "dataset",
                "links": [
                    {
                        "href": f"{base}reanalysis-era5-pressure-levels",
                        "rel": "self",
                        "type": "application/json",
                    },
                ],
                "extent": {
                    "spatial": [-180, -90, 180, 90],
                    "temporal": ["1979-01-11T00:00:00Z", ".."],
                },
            }
        ],
        links=[
            {
                "href": base,
                "rel": "self",
                "type": "application/json",
            },
        ],
    )
