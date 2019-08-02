from django import forms
from .models import Apartment
from common.models import Comment, Attachments


class ApartmentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        addresses = kwargs.pop('addresses', [])
        super(ApartmentForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs = {"class": "form-control"}
        self.fields['area'].required = False
        self.fields['address'].queryset = addresses

    class Meta:
        model = Apartment
        fields = ('address', 'entrance', 'floor', 'number_of_rooms', 'area', 'status', 'number_of_business_account',
                  'apartment_number', 'balance_of_business_account')


class ApartmentCommentForm(forms.ModelForm):
    comment = forms.CharField(max_length=64, required=True)

    class Meta:
        model = Comment
        fields = ('comment', 'commented_by')


class ApartmentAttachmentForm(forms.ModelForm):
    attachment = forms.FileField(max_length=1001, required=True)

    class Meta:
        model = Attachments
        fields = ('attachment',)
