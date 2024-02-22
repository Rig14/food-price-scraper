import json
import os


def construct_request(categorys: list[int] | int) -> str:
    """Construct a request json string for the Selver API."""
    # get the file path
    file_path = os.path.join(os.path.dirname(__file__), "request.json")

    with open(file_path, "r", encoding="UTF-8") as f:
        # read the request file
        request = f.read()
        request = json.loads(request)
        # fill in the category ids
        request["query"]["bool"]["filter"]["bool"]["must"][2]["terms"][
            "category_ids"
        ] = (categorys if isinstance(categorys, list) else [categorys])
        # return the json string
        request = json.dumps(request)
        return request
