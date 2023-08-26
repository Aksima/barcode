from .entities import coach, member, training

(
    AddCoachForm,
    EditCoachForm,
    AddMemberForm,
    EditMemberForm,
    AddTrainingForm,
    EditTrainingForm,
) = (
    coach.AddCoachForm,
    coach.EditCoachForm,
    member.AddMemberForm,
    member.EditMemberForm,
    training.AddTrainingForm,
    training.EditTrainingForm,
)
