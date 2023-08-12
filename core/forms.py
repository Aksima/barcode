from .entities import coach, member

(
    AddCoachForm,
    EditCoachForm,
    AddMemberForm,
    EditMemberForm,
) = (
    coach.AddCoachForm,
    coach.EditCoachForm,
    member.AddMemberForm,
    member.EditMemberForm,
)
