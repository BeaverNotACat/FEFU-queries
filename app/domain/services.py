from .models import FormPopulation, Parameter, User



# TODO refactor
class FormPopulationService:
    @staticmethod
    def create(data: dict) -> FormPopulation:
        return FormPopulation(**data)

    @staticmethod
    def create_list(data: list[dict]) -> list[FormPopulation]:
        return [FormPopulation(**row) for row in data]

    @staticmethod
    def add_parameter(form_population: FormPopulation, parameter: Parameter) -> None:
        form_population.parameters.append(parameter)


class ParameterService:
    @staticmethod
    def create(data: dict) -> Parameter:
        return Parameter(**data)

    @staticmethod
    def create_from_dict(data: dict[str, str]) -> list[Parameter]:
        return [Parameter(field=field, answer=answer) for field, answer in data.items()]


class UserService:
    @staticmethod
    def create(data: dict) -> User:
        return User(**data)
