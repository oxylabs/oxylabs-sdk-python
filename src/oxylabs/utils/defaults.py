SYNC_BASE_URL = "https://realtime.oxylabs.io/v1/queries"
ASYNC_BASE_URL = "https://data.oxylabs.io/v1/queries"

PROXY_BASE_URL = "realtime.oxylabs.io"
PROXY_PORT = 60000
NON_UNIVERSAL_DOMAINS = {"google", "bing", "amazon", "wayfair"}


DEFAULT_REQUEST_TIMEOUT = 160
DEFAULT_POLL_INTERVAL = 5
DEFAULT_REQUEST_TIMEOUT_ASYNC = 105
DEFAULT_JOB_COMPLETION_TIMEOUT = 50


def set_default_tbm_context(context):
    """
    Sets the default tbm value if the provided value is None.

    Args:
        context (list): The context list of dictionaries to be checked and updated.

    Returns:
        list: The updated context list.
    """
    if context is None:
        context = []

    default_tbm = "isch"
    for item in context:
        if item.get("key") == "tbm":
            item["value"] = item.get("value", default_tbm)
            break
    else:
        context.append({"key": "tbm", "value": default_tbm})
    return context
