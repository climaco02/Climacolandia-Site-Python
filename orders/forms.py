from django import forms

class MakeOrderForm(forms.Form):
	type_sweet = forms.CharField(required=True)
	description = forms.CharField(required=True)

	def is_valid(self):
		valid = True

		if not super(MakeOrderForm, self).is_valid():
			self.add_error('Por favor, preencha todos os campos')
			valid = False

		return valid

	def add_error(self, error_message):
		errors_in_form = self._errors.setdefault(forms.forms.NON_FIELD_ERRORS, forms.utils.ErrorList())
		errors_in_form.append(error_message)
