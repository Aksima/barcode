from django.shortcuts import render


def entity_added(request, entity_id):
    return render(
        request,
        'gto/entity_added.html',
        {'entity_id': entity_id}
    )


def entity_updated(request, entity_id):
    return render(
        request,
        'gto/entity_updated.html',
        {'entity_id': entity_id}
    )
