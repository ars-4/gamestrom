from pyuploadcare.dj.forms import ImageField as IfPu
from core.models import Person
from django.forms import ModelForm


class PersonForm(ModelForm):
    profile_picture = IfPu(label='')
    # {{ form.media }}
    # { % with title=form.media %}
    # { % endwith %}

    class Meta:
        model = Person
        fields = ['profile_picture']
