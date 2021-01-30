from share.cached import get_site_information
from django.conf import settings


def website_information(request):
    """
    Return website information.
    """

    return get_site_information()


def timezones(request):
    return {'timezones': settings.TIMEZONES}
