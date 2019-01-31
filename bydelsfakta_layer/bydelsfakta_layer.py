def generate_metadata(district: str,
                      heading,
                      help="Dette er en beskrivelse for hvordan dataene leses",
                      data=list,
                      series=None
                      ):
    if series is None:
        series = [{"heading": "Default heading", "subheading": " Default subheading"}]

    return {
        "meta": {
            "scope": "bydel",
            "heading": heading + " i {district}".format(district=district),
            "help": help,
            "series": series,
            "xAxis": {
                "format": "%",
                "title": False
            },
            "publishedDate": "2019-06-01",
            "dataSource": {
                "url": "http://ssb.no/data/1234124/",
                "label": "Statistisk sentralbyrå"
            },
            "files": [
                {
                    "url": "http://data.oslo.kommune.no/data/1234123/data.xls",
                    "type": "Excel"
                },
                {
                    "url": "http://data.oslo.kommune.no/data/1234123/data.csv",
                    "type": "csv"
                }
            ]
        },

        "data": data
    }