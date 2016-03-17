from django import forms

from webapp.models import Film


class FilterForm(forms.ModelForm):
    class Meta:
        model=Film
        exclude={'year','actors','latitude','longitude','fact'}
    start_year=forms.IntegerField()
    end_year=forms.IntegerField()
    actors=forms.CharField(max_length=150)

    def get_filter(self):
        filters={}
        if self.cleaned_data['title']:
            filters['title']=self.cleaned_data['title']
        if self.cleaned_data['year__gte']:
            filters['year__gte']=self.cleaned_data['year__gte']
        if self.cleaned_data['year__lte']:
            filters['year__lte']=self.cleaned_data['year__lte']
        if self.cleaned_data['location']:
            filters['location']=self.cleaned_data['location']
        if self.cleaned_data['company']:
            filters['company']=self.cleaned_data['company']
        if self.cleaned_data['distributor']:
            filters['distributor']=self.cleaned_data['distributor']
        if self.cleaned_data['director']:
            filters['director']=self.cleaned_data['director']
        if self.cleaned_data['writer']:
            filters['writer']=self.cleaned_data['writer']
        if self.cleaned_data['actors__name']:
            filters['actors__name']=self.cleaned_data['actors__name']
        return filters
