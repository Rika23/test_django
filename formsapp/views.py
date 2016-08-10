from django.shortcuts import render
from formsapp.models import Form
from .forms import ItemForm
from django.forms.formsets import formset_factory

def index(request):
    data = {
     'form-TOTAL_FORMS': u'1',
     'form-INITIAL_FORMS': u'0',
     'form-MAX_NUM_FORMS': u'',
    }
    
    DataFormSet = formset_factory(ItemForm)
    f = Form.objects.first()
    if not f:
        f = Form.objects.create(data={})
    init_data = [{'value' : v} for k,v in f.data.items()]
    if request.method == 'POST':
        data_formset = DataFormSet(request.POST)

        if data_formset.is_valid():
            i = 0
            for data_form in data_formset:
                value = data_form.cleaned_data.get('value')
                f.data[str(i).decode("utf-8")] = value
                i += 1
            f.save()
    else:
        data_formset = DataFormSet( initial=init_data)

    context = {
        'data_formset': data_formset,
    }

    return render(request, 'formsapp/index.html', context)
