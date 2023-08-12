from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

APPLICATION_NAME = 'gto'
NAMESPACE = APPLICATION_NAME + ':'
MALE = 'M'
FEMALE = 'F'
GENDERS = [
    (MALE, 'мужчина'),
    (FEMALE, 'женщина'),
]
SUFFIX_FOR_GENDER = {
    MALE: 'ый',
    FEMALE: 'ая'
}


def pluralize(name: str):
    for suffix in ['s', 'ss', 'ch', 'sh', 'x', 'z']:
        if name.endswith(suffix):
            return f'{name}es'
    return f'{name}s'


def get_declension(
        case_nominative_single,
        case_genitive_single,
        case_genitive_plural
):
    def f(number):
        if number / 10 % 10 != 1:
            ones = number % 10
            if ones == 1:
                return case_nominative_single
            if ones in [2, 3, 4]:
                return case_genitive_single
        return case_genitive_plural

    return f


def with_names_for_methods(meta_info_class):
    name = meta_info_class.name
    meta_info_class.qualified_name = NAMESPACE + name
    meta_info_class.add_method = 'add_' + name
    meta_info_class.qualified_add_method = \
        NAMESPACE + meta_info_class.add_method
    meta_info_class.edit_method = 'edit_' + name
    meta_info_class.qualified_edit_method = \
        NAMESPACE + meta_info_class.edit_method
    meta_info_class.list_method = pluralize(name)
    meta_info_class.qualified_list_method = \
        NAMESPACE + meta_info_class.list_method
    return meta_info_class


def create_view_to_add_entity(
        entity_class,
        form_to_add_entity
):
    def add_entity(request):
        if request.method == 'POST':
            form = form_to_add_entity(
                request.POST,
                request.FILES
            )
            if form.is_valid():
                entity = form.save()
                return HttpResponseRedirect(
                    reverse(
                        f'gto:entity_added',
                        args=(entity.account.id,)
                    )
                )
        else:
            form = form_to_add_entity()
        return render(
            request,
            'gto/add.html',
            {
                'form': form,
                'continuation':
                    entity_class.MyMeta.qualified_add_method,
                'verbose_name_genitive':
                    entity_class.MyMeta.verbose_name_genitive
            }
        )

    return add_entity


def create_view_to_edit_entity(
        entity_class,
        form_to_edit_entity
):
    def edit_entity(request, entity_id):
        if request.method == 'POST':
            entity = get_object_or_404(
                entity_class,
                pk=entity_id
            )
            form = form_to_edit_entity(
                request.POST,
                request.FILES,
                instance=entity
            )
            if form.is_valid():
                entity = form.save()
                return HttpResponseRedirect(
                    reverse(
                        'gto:entity_updated',
                        args=(entity.account.id,)
                    )
                )
        else:
            entity = get_object_or_404(
                entity_class,
                pk=entity_id
            )
            form = form_to_edit_entity(instance=entity)
        return render(
            request,
            'gto/edit.html',
            {
                'form': form,
                'continuation':
                    entity_class.MyMeta.qualified_edit_method,
                'entity_id': entity_id
            }
        )

    return edit_entity


def create_view_to_list_entities(entity_class):
    def list_entities(request):
        verbose_name_plural = \
            getattr(entity_class, '_meta').verbose_name_plural
        verbose_name_plural_genitive = \
            entity_class.MyMeta.verbose_name_plural_genitive
        entities = entity_class.objects.all()
        return render(
            request,
            f'gto/list.html',
            {
                'verbose_name_plural': verbose_name_plural,
                'verbose_name_plural_genitive':
                    verbose_name_plural_genitive,
                'entities': entities
            }
        )

    return list_entities


def create_view_for_entity_detail(entity_class, annotator=None):
    def entity_detail(request, entity_id):
        nonlocal annotator
        entity = get_object_or_404(entity_class, pk=entity_id)
        snake_case_name = entity_class.MyMeta.name
        if annotator is None:
            extra_details = {}
        else:
            extra_details = annotator(entity)
        return render(
            request,
            f'gto/{snake_case_name}_detail.html',
            {'entity': entity, **extra_details}
        )

    return entity_detail