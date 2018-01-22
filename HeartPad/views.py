from django.shortcuts import render


def home(request):
    return render(
        request,
        'Entry/home.html',
        {},
    )


def new_entry(request):
    return render(
        request,
        'Entry/new entry.html',
        {},
    )


def entry_list(request):
    return render(
        request,
        'Entry/entry list.html',
        {},
    )
