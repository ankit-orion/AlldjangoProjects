from django import forms 
class ContactForm(forms.Form):
    name =forms.CharField(label="Your Name",max_length=30)
    email= forms.EmailField(label="Your Mail id")
    subject=forms.CharField(label="subject", max_length=100)
    bio =forms.CharField(label="Add Your Bio",widget=forms.Textarea)