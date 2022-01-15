from django import forms
from .models import Topic, Entry

class TopicForm(forms.ModelForm):                                           # ModelForm uses the ifnormation from the models we define to autmatically build a form
    class Meta:                                                             # Simplest version of ModelForm consists of a nested Meta class, and this class tells Django which model to base the form on/which fields to include
        model = Topic                                                       # We build the form from the Topic model
        fields = ['text']                                                   # Only include the text field from the Topic model
        labels = {'text': ''}                                               # Generate a label for the text field        

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}              # A widget is a form element. We're overriding djangos widget by creating one of our own
                                                                            # Default widget is 40 columns, we made it 80 columns                   