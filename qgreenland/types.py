# NOTE: Will this cause a weird conflict?

type StepType = Literal['command', 'python', 'template']
# TODO: Make this into an interface that specifies only one top-level key
type Step = Dict[StepType, Dict[str, Any]]
