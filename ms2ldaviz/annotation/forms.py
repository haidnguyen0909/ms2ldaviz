from django import forms

example_spectrum = "53.0384:331117.7\n57.0447:798106.4\n65.0386:633125.7\n77.0385:5916789.799999999\n81.0334:27067.0\n85.0396:740633.6\n91.0542:1251226.7000000002\n92.0492:2928042.3\n95.0493:728877.1\n103.0419:59138.40000000001\n104.0495:13185144.700000001\n105.045:1643858.5999999999\n105.0701:129215.0\n110.06:46285.0\n119.0604:12584552.9\n130.04:33153.3\n130.0652:270688.7\n131.0725:203663.6\n131.0734:45999.7\n142.0653:20711.1\n147.0555:63444.99999999999\n160.0871:61955089.8\n188.082:86709805.39999999"


class AnnotationForm(forms.Form):
    parentmass = forms.FloatField(required = True,initial = 188.0818)
    spectrum = forms.CharField(required = True,widget = forms.Textarea(attrs={'rows': 20, 'cols': 120}),initial = example_spectrum)


class BatchAnnotationForm(forms.Form):
    spectra = forms.CharField(required = True)