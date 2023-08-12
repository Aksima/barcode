from django.conf import settings
from . import models, forms, views
from .entities import (
    APPLICATION_NAME,
    create_view_to_add_entity,
    create_view_to_edit_entity,
    create_view_to_list_entities,
    create_view_for_entity_detail
)
from django.urls import path

app_name = APPLICATION_NAME
urlpatterns = [
    path(
        'entity/<int:entity_id>/added/',
        views.entity_added,
        name='entity_added'
    ),
    path(
        'entity/<int:entity_id>/updated/',
        views.entity_updated,
        name='entity_updated'
    ),
    path(
        'payments/',
        views.payment_list,
        name='payments'
    ),
    path(
        'receipt/<int:payment_id>',
        views.receipt,
        name='receipt'
    ),
]
for model in [
    models.Coach,
    models.Member
]:
    name = model.__name__
    snake_case_name = model.MyMeta.name
    urlpatterns.extend((
        path(
            f'{snake_case_name}/add/',
            create_view_to_add_entity(
                model,
                getattr(forms, f'Add{name}Form')
            ),
            name=model.MyMeta.add_method
        ),
        path(
            f'{snake_case_name}/edit/<int:entity_id>/',
            create_view_to_edit_entity(
                model,
                getattr(forms, f'Edit{name}Form')
            ),
            name=model.MyMeta.edit_method
        ),
        path(
            f'{snake_case_name}/list/',
            create_view_to_list_entities(model),
            name=model.MyMeta.list_method
        ),
        path(
            f'{snake_case_name}/detail/<int:entity_id>/',
            create_view_for_entity_detail(
                model,
                lambda entity: {
                    'photo': f'{settings.MEDIA_URL}{entity.photo}'
                }
            ),
            name=snake_case_name
        ),
    ))
