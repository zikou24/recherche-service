from django import forms
from django.forms import ModelForm
from .models import Createservice
from .models import Category, ReviewRating


class Serviceform(ModelForm):

    class Meta:

        model = Createservice

        fields = ['Service_name',

                  'description', 'your_sertificate', 'images', 'category']

    def __init__(self, *args, **kwargs):

        self.user = kwargs.pop('user')

        super(Serviceform, self).__init__(*args, **kwargs)

        print(self.user)

        if self.user is not None:

            self.fields['category'].queryset = Category.objects.filter(

                wilaya=self.user.wilaya)


class reviews(ModelForm):
    class Meta:
        model = ReviewRating
        
        fields = ['subject', 'review', 'rating']
