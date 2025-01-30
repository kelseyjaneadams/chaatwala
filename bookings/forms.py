from django import forms
from .models import Booking
from collections import OrderedDict


class CustomTimeForm(forms.ModelForm):
    """
    Custom form for the Booking model to split the booking_time field
    into dropdowns for hours and minutes.
    """
    HOUR_CHOICES = [
        (hour, f"{hour:02}:00") for hour in range(12, 22)
    ]
    MINUTE_CHOICES = [
        (minute, f"{minute:02}") for minute in [0, 15, 30, 45]
    ]

    hour = forms.ChoiceField(
        choices=HOUR_CHOICES,
        label="Hour"
    )
    minute = forms.ChoiceField(
        choices=MINUTE_CHOICES,
        label="Minute"
    )

    class Meta:
        model = Booking
        exclude = ['booking_id', 'booking_time']
        fields = [
            'user',
            'contact_name',
            'number_of_guests',
            'booking_date',
            'hour',
            'minute',
            'special_request',
            'status',
        ]

    def __init__(self, *args, **kwargs):
        """
        Initializes the form and reorders fields to place hour
        and minute dropdowns below booking_date.
        """
        super().__init__(*args, **kwargs)
        self.fields = OrderedDict([
            ('user', self.fields['user']),
            ('contact_name', self.fields['contact_name']),
            ('number_of_guests', self.fields['number_of_guests']),
            ('booking_date', self.fields['booking_date']),
            ('hour', self.fields['hour']),
            ('minute', self.fields['minute']),
            ('special_request', self.fields['special_request']),
            ('status', self.fields['status']),
        ])

    def clean(self):
        """
        Combines the hour and minute fields into the booking_time field.
        """
        cleaned_data = super().clean()
        hour = cleaned_data.get('hour')
        minute = cleaned_data.get('minute')

        if hour and minute:
            cleaned_data['booking_time'] = f"{hour}:{minute}"
        return cleaned_data

    def save(self, commit=True):
        """
        Overrides save to update the booking_time field dynamically.
        """
        instance = super().save(commit=False)
        hour = self.cleaned_data.get('hour')
        minute = self.cleaned_data.get('minute')

        if hour and minute:
            instance.booking_time = f"{hour}:{minute}"

        if commit:
            instance.save()
        return instance