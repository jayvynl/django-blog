from shares.cached import get_site_information


def website_information(request):
    """
    Return website information.
    """

    return get_site_information()
