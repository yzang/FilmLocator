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
	print self.data
        if self.data.get('title'):
            filters['title']=self.data['title']
        if self.data.get('start_year'):
            filters['year__gte']=int(self.data['start_year'])
        if self.data.get('end_year'):
            filters['year__lte']=int(self.data['end_year'])
        if self.data.get('location'):
            filters['location']=self.data['location']
        if self.data.get('company'):
            filters['company']=self.data['company']
        if self.data.get('distributor'):
            filters['distributor']=self.data['distributor']
        if self.data.get('director'):
            filters['director']=self.data['director']
        if self.data.get('writer'):
            filters['writer']=self.data['writer']
        if self.data.get('actors'):
            filters['actors__name']=self.data['actors']
	print filters
        return filters
