from django import forms
from .models import *

class TweetForm (forms.ModelForm):
    tweet_text = forms.CharField(widget=forms.Textarea(attrs = {
                                            "rows":10,
                                            "placeholder": "tweet area",
                                            "id": "id_for_text_area"
                                             }))
    follows_count = forms.IntegerField()
    likes_count = forms.IntegerField()

    
    class Meta:
        model = Tweet
        fields = ['tweet_text', 
        'follows_count',
         'likes_count']
    
    # clean_<my_fied>
    def clean_tweet_text(self,*args, **kwargs ):
        text = self.cleaned_data.get("tweet_text")
        if "MARIA" not  in text:
            print(text)

            raise forms.ValidationError ("This is not valid")
        else: 
            return text
 

class RawTweetForm (forms.Form):
    tweet_text = forms.CharField(widget=forms.Textarea(attrs = {
                                            "rows":10,
                                            "placeholder": "tweet area",
                                            "id": "id_for_text_area"
                                             })
    )
    follows_count = forms.IntegerField()
    likes_count = forms.IntegerField()

    

        

