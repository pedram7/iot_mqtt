from statistics import mean

from django.template.loader import render_to_string, get_template
from django.template import Template, Context
from django.conf import settings
import django

settings.configure(TEMPLATE_DIRS=[".", ], TEMPLATES=[
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['.'],  # if you want the templates from a file
        'APP_DIRS': False,  # we have no apps
    },
])
django.setup()


def make_html(datalist, output_path):
    maxrec = max(datalist)
    minrec = min(datalist)
    avgrec = mean(datalist)
    datalist = datalist[-9:-1]
    x = render_to_string('barchart.html',
                         {'datalist': datalist, 'min': minrec, 'max': maxrec, 'avg': avgrec})
    with open(output_path, 'wt') as f:
        f.write(x)
        f.flush()


make_html([5, 12, 12, 54, 21, 64, 12, 3, 5, 67, 54, 23, 21, 8, 6, 42, 65, 34, 27, 89, 20, 10, 3, 15], 'new_html.html')
