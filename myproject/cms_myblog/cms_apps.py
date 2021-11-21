from aldryn_apphooks_config.app_base import CMSConfigApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import gettext_lazy as _


from .cms_appconfig import BlogConfig
from utils.GLOBALS import get_setting

URLCONF = "myblog.urls"

@apphook_pool.register
class BlogAppHook(CMSConfigApp):

  app_name = "myblog" #namespace
  #_urls = [get_setting("URLCONF")]
  name = _("MyBlog Application") #human readable name
  app_config = BlogConfig


  def get_urls(self, page=None, language=None, **kwargs):
      return [URLCONF]
