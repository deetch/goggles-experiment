Coords = {
    1: {"label": "x", "isValue": True},
    2: {"label": "width", "isValue": True},
    3: {"label": "y", "isValue": True},
    4: {"label": "height", "isValue": True}
}

Info = {
    15690847: {
        "label": "UIStuff",
        "isValue": False,
        "contents": {
            1: {
                "label": "Coords",
                "isValue": False,
                "contents": Coords
            },
            2: {
                "label": "some int",
                "isValue": True
            },
            3: {
                "label": "image for result type",
                "isValue": False,
                "contents": {
                    1: {"label": "image to show", "isValue": True},
                    2: {"label": "urllist", "isValue": False, "contents": {}},
                    3: {"label": "site where the image originates", "isValue": True}
                }
            },
            6: {
                "label": "language",
                "isValue": True
            }
        }
    },
    15693652: {
        "label": "Search query for request",
        "isValue": False,
        "contents": {
            2: {"label": "url", "isValue": True}
        }
    },
    16045192: {
        "label": "direct result",
        "isValue": False,
        "contents": {
            1: {"label": "result string", "isValue": True},
            3: {"label": "result description", "isValue": True}
        }
    }
}

ReplyItem = {
    1: {
        "label": "Info",
        "isValue": False,
        "contents": Info
    } 
}

parse_dict = {
    1: {
        "label": "Reply",
        "isValue": False,
        "contents": {
            1: {
                "label": "ReplyItem",
                "isValue": False,
                #"contents": ReplyItem
                "contents": Info
            },
            15705729: {
                "label": "unknown",
                "isValue": True,
            }
        }
    }
}

