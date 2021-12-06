from cms.utils.plugins import get_plugins
from django import template
from myblog.models import Post, BlogCategory
from utils.GLOBALS import get_setting

register = template.Library()

ASIDE_NUMBER_RECENT_POST_TO_DISPLAY = get_setting("ASIDE_NUMBER_RECENT_POST_TO_DISPLAY")

TRUNCWORDS_COUNT_ASIDE = get_setting('TRUNCWORDS_COUNT_ASIDE')

@register.simple_tag(name="media_plugins", takes_context=True)
def media_plugins(context, post):
    """
    Extract :py:class:`djangocms_blog.media.base.MediaAttachmentPluginMixin`
    plugins from the ``media`` placeholder of the provided post.
    They can be rendered with ``render_plugin`` templatetag:
    .. code-block: python
        {% media_plugins post as media_plugins %}
        {% for plugin in media_plugins %}{% render_plugin plugin %}{% endfor %}
    :param context: template context
    :type context: dict
    :param post: post instance
    :type post: :py:class:`djangocms_blog.models.Post`
    :return: list of :py:class:`djangocms_blog.media.base.MediaAttachmentPluginMixin` plugins
    :rtype: List[djangocms_blog.media.base.MediaAttachmentPluginMixin]
    """
    request = context["request"]
    if post.media.get_plugins().exists():
        return get_plugins(request, post.media, None)
    return []


@register.simple_tag(name="media_images", takes_context=True)
def media_images(context, post, main=True):
    """
    Extract images of the given size from all the
    :py:class:`djangocms_blog.media.base.MediaAttachmentPluginMixin`
    plugins in the ``media`` placeholder of the provided post.
    Support ``djangocms-video`` ``poster`` field in case the plugin
    does not implement ``MediaAttachmentPluginMixin`` API.
    Usage:
    .. code-block: python
        {% media_images post False as thumbs %}
        {% for thumb in thumbs %}<img src="{{ thumb }}/>{% endfor %}
    .. code-block: python
        {% media_images post as main_images %}
        {% for image in main_images %}<img src="{{ image }}/>{% endfor %}
    :param context: template context
    :type context: dict
    :param post: post instance
    :type post: :py:class:`djangocms_blog.models.Post`
    :param main: retrieve main image or thumbnail
    :type main: bool
    :return: list of images urls
    :rtype: list
    """
    plugins = media_plugins(context, post)
    if main:
        image_method = "get_main_image"
    else:
        image_method = "get_thumb_image"
    images = []
    for plugin in plugins:
        try:
            images.append(getattr(plugin, image_method)())
        except Exception:
            try:
                image = plugin.poster
                if image:
                    images.append(image.url)
            except AttributeError:
                pass
    return images



@register.simple_tag(name="get_all_posts", takes_context=True)
def get_all_posts(context):
    post = Post.objects.all()
    return post

@register.simple_tag(name="get_current_post", takes_context=True)
def get_current_post(context, index):
    post = Post.objects.all()[index]
    return post


@register.simple_tag(name='total_posts', takes_context=False) 
def total_posts():
    return Post.objects.count()

@register.simple_tag(name='get_recent_post', takes_context=True) 
def get_recent_post(context):
    #number_post=context['ASIDE_NUMBER_POST_TO_DISPLAY']
    number_post=ASIDE_NUMBER_RECENT_POST_TO_DISPLAY
    last_ten = Post.objects.all().order_by('-id')[:number_post]
    last_ten_in_ascending_order = reversed(last_ten)
    return last_ten_in_ascending_order


@register.simple_tag(name='get_num_recent_posts', takes_context=True) 
def get_num_recent_posts(context):
    try:
        return context['ASIDE_NUMBER_RECENT_POST_TO_DISPLAY']
    except Exception as ex:
         return ASIDE_NUMBER_RECENT_POST_TO_DISPLAY
 
    
@register.simple_tag(name='get_trunc_word_count_aside', takes_context=True) 
def get_trunc_word_count_aside(context):
    try:
        return context['TRUNCWORDS_COUNT_ASIDE']
    except Exception as ex:
         return TRUNCWORDS_COUNT_ASIDE
 
@register.simple_tag(name='get_categories', takes_context=False) 
def get_categories(context):
    categories =  BlogCategory.objects.all()
    return categories

@register.simple_tag(name='get_related_posts', takes_context=True) 
def get_related_posts(context, post):
    related_posts =  post.related.all()
    return related_posts

@register.simple_tag(name='get_modulo', takes_context=False) 
def get_modulo(index):
    return index % 2
