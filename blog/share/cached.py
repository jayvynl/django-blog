_site_information = {}


def get_site_information():
    if not _site_information:
        load_site_information()
    return _site_information


def set_site_information(**kwargs):
    _site_information.update(kwargs)


def load_site_information():
    from .models import SiteInformation
    site_info_model_instance = SiteInformation.objects.get_or_create(id=1)
    site_info = {
        'site_name': site_info_model_instance.name,
        'site_register': site_info_model_instance.register,
        'site_register_url': site_info_model_instance.register_url
    }
    set_site_information(**site_info)
