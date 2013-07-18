from django.shortcuts import redirect, render

from forms import PersonForm


def new(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('people:index')
    else:
        form = PersonForm()

    return render(request, 'people/person_new.html', {'form': form})
