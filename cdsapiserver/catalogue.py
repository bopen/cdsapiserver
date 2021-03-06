from fastapi import APIRouter

router = APIRouter(
    prefix="/collections",
    tags=["catalogue"],
)


@router.get("/")
async def collections():
    return [
        {
            "id": "1234567890",
            "title": "Example Collection Description Response",
            "description": "This is an example of a Collection Description in JSON format",
            "links": [
                {
                    "href": "http://data.example.org/collections.json",
                    "rel": "self",
                    "type": "application/json",
                    "title": "this document",
                },
                {
                    "href": "http://data.example.org/collections.html",
                    "rel": "alternate",
                    "type": "text/html",
                    "title": "this document as HTML",
                },
                {
                    "href": "http://schemas.example.org/1.0/foobar.xsd",
                    "rel": "describedby",
                    "type": "application/xml",
                    "title": "XML schema for Acme Corporation data",
                },
            ],
            "extent": {
                "spatial": [7.01, 50.63, 7.22, 50.78],
                "temporal": ["2010-02-15T12:34:56Z", "2018-03-18T12:11:00Z"],
            },
        }
    ]
