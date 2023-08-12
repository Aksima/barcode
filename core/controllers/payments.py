from typing import Optional
from dataclasses import dataclass
from django.conf import settings
from django.shortcuts import get_object_or_404, render
from ..entities.training import Training, COMPLETED
from ..entities.payment import Payment
from ..entities.assignment import Assignment


@dataclass
class Record:
    name: str
    date: str
    counter: int
    payment_id: Optional[int]


def payment_list(request):
    payments = getattr(Payment, 'objects').values('assignment__id')
    distinct_assignments = set(
        payment['assignment__id'] for payment in payments
    )
    groups = {}
    for assignment_id in distinct_assignments:
        payments = getattr(Payment, 'objects').filter(
            assignment__id=assignment_id
        )
        trainings = getattr(Training, 'objects').filter(
            assignment__id=assignment_id,
            status=COMPLETED
        )
        timeline = [
            *((
                payment.dt,
                'Оплата',
                payment.volume,
                payment.id
            ) for payment in payments),
            *((
                training.dt,
                training.label,
                -1,
                None
            ) for training in trainings)
        ]
        timeline.sort()
        records = []
        counter = 0
        for item in timeline:
            counter += item[2]
            records.append(
                Record(
                    item[1],
                    item[0],
                    counter,
                    item[3]
                )
            )
        assignment = getattr(Assignment, 'objects').get(pk=assignment_id)
        groups[str(assignment)] = records
    return render(
        request,
        'gto/payments.html',
        {'groups': groups}
    )


def receipt(request, payment_id):
    payment = get_object_or_404(Payment, pk=payment_id)
    return render(
        request,
        'gto/receipt.html',
        {
            'link': f'{settings.MEDIA_URL}{payment.receipt}',
            'image_width': payment.image_width,
            'image_height': payment.image_height
        }
    )
