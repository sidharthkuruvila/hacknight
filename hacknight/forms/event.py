# -*- coding: utf-8 -*-

import flask.ext.wtf as wtf
from baseframe.forms import Form, RichTextField
#from baseframe.staticdata import timezones

__all__ = ['EventForm']

class ValidateEvent(object):
    @staticmethod
    def date(self, form, start_datetime='start_datetime', end_datetime='end_datetime'):
        if start_datetime.data >= end_datetime.data:
            wtf.ValidationError('End Date must be greater than Start Date')
        """Need to check if the datetime is past date time, obstacle is Need to have time zone detail, check accordingly.
        """
class EventForm(Form):
    title = wtf.TextField("Title", description="Name of the Event", validators=[wtf.Required()])
    description = RichTextField("Description", description="Description of the project")
    #need to datepicker here, for time being while python datetime module is used inside views
    start_datetime = wtf.DateTimeField("StartDateTime", description="Hacknight Start DateTime", validators=[wtf.Required()])
    end_datetime = wtf.DateTimeField("EndDateTime", description="Hacknight End DateTime", validators=[wtf.Required(), ValidateEvent.date])
    website = wtf.TextField("Website",description="Main Event Website", validators=[wtf.Optional()])