from .controllers import entities, payments
(
    entity_added,
    entity_updated,
    payment_list,
    receipt,
) = (
    entities.entity_added,
    entities.entity_updated,
    payments.payment_list,
    payments.receipt,
)
