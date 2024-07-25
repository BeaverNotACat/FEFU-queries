from app.application.gateway import FormPopulationReader, FormPopulationSaver
from app.domain.models import UserEmail, FormId, FormPopulation
from app.adapters.database.models import FormPopulationODM

class FormPopulationGateway(FormPopulationReader, FormPopulationSaver):
    def get_filtered_form_populations_list(
        self, user_email: UserEmail, form_id: FormId
    ) -> list[FormPopulation]:
        FormPopulation.find(FormPopulation.user_email == user_email).find(FormPopulation.form_id == form_id).to_list()
        
        return FormPopulation()

    
