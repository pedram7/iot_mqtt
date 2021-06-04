from statistics import mean, variance

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

avg_period_minutes = 2
data_freq = 2  # in sec


def make_html(datalist, output_path):
    maxrec = max(datalist)
    minrec = min(datalist)
    x = avg_period_minutes * 60 * data_freq
    if len(datalist) > x:
        avgrec = mean(datalist[-(x + 1):-1])
        vari = variance(datalist[-(-x + 1):-1])

    else:
        avgrec = mean(datalist)
        vari = variance(datalist)

    datalist = datalist[-17:-1]
    x = render_to_string('barchart.html',
                         {'datalist': datalist, 'min': minrec, 'max': maxrec, 'avg': avgrec, 'vari': vari})
    with open(output_path, 'wt') as f:
        f.write(x)
        f.flush()

# make_html([5, 12, 12, 54, 21, 64, 12, 3, 5, 67, 54, 23, 21, 8, 6, 42, 65, 34, 27, 89, 20, 10, 3, 15], 'output.html')
