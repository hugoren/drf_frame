import simplejson as json
import operator
from django.template.defaulttags import register


@register.filter
def ts_filter(data, key):
    # REF: http://stackoverflow.com/questions/8000022/django-template-how-to-lookup-a-dictionary-value-with-a-variable

    # An example of data is something like:
    # {"connected": {"0": ["RET-56", "RET-55", "RET-52"], "1": ["RET-58", "RET-54"]}, "standalone": {"0": ["RET-53"]}}

    result = json.loads(data)[key]
    result = sorted(result.items(), key=operator.itemgetter(0))
    return result

@register.filter
def tsname_filter(data):
    # An example of data is something like:
    # ["RET-56", "RET-55", "RET-52"]

    result = ", ".join(map(str, data))
    return result
