from django_components import component


@component.register("profile")
class Calendar(component.Component):

    template_name = "profile/profile.html"

    # This component takes one parameter, a date string to show in the template
    def get_context_data(self):
        return {
            "date": "bingo",
        }
