_site_information = {}


def get_site_information():
    if not _site_information:
        load_site_information()
    return _site_information


def set_site_information(**kwargs):
    _site_information.update(kwargs)


def load_site_information():
    from .models import SiteInformation
    qs = SiteInformation.objects.all()
    if qs:
        site_info_model_instance = qs[0]
    else:
        site_info_model_instance = SiteInformation.objects.create()
    site_info = {
        'site_name': site_info_model_instance.name,
        'site_register': site_info_model_instance.register,
        'site_register_url': site_info_model_instance.register_url
    }
    set_site_information(**site_info)
