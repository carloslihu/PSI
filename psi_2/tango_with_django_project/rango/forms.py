from django import forms
from rango.models import Page, Category


class CategoryForm(forms.ModelForm):
	name = forms.CharField(max_length=128, help_text="Please enter the category name.")
	views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
	likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
	slug = forms.CharField(widget=forms.HiddenInput(), required=False)
	# An inline class to provide additional information on the form.
	class Meta:
		# Provide an association between the ModelForm and a model
		model = Category
		fields = ('name',)

class PageForm(forms.ModelForm):
	max_len = 200
	title = forms.CharField(max_length=max_len, help_text="Please enter the title of the page.")
	url = forms.URLField(max_length=max_len, help_text="Please enter the URL of the page.")
	views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
	class Meta:
		# Provide an association between the ModelForm and a model
		model = Page
		# What fields do we want to include in our form?
		# This way we don't need every field in the model present.
		# Some fields may allow NULL values, so we may not want to include them.
		# Here, we are hiding the foreign key.
		# we can either exclude the category field from the form,
		exclude = ('category',)
		# or specify the fields to include (i.e. not include the category field)
		#fields = ('title', 'url', 'views')
	def clean(self):
		cleaned_data = self.cleaned_data
		url = cleaned_data.get('url')
		# If url is not empty and doesn't start with 'http://',
		# then prepend 'http://'.
		if url and not url.startswith('http://'):
			url = 'http://' + url
			cleaned_data['url'] = url
			return cleaned_data

"""
def add_page(request, category_name_slug):
	try:
		category = Category.objects.get(slug=category_name_slug)
	except Category.DoesNotExist:
		category = None
	form = PageForm()
	if request.method == 'POST':
		form = PageForm(request.POST)
		if form.is_valid():
			if category:
				page = form.save(commit=False)
				page.category = category
				page.views = 0
				page.save()
				return show_category(request, category_name_slug)
	else:
		print(form.errors)
	context_dict = {'form':form, 'category': category}
	return render(request, 'rango/add_page.html', context_dict)
"""