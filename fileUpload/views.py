from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.conf import settings

def uploadFile(request):
    if request.method == 'POST' and 'document' in request.FILES:
        file = request.FILES['document']
        
        if file.name.endswith('.csv'):
            df = pd.read_csv(file)
        elif file.name.endswith(('.xls', '.xlsx')):
            df = pd.read_excel(file)
        else:
            return HttpResponse("Unsupported file type")

        combinedList = zip(df['Cust State'].tolist(), df['Cust Pin'].tolist(), df['DPD'].tolist())
        
        return render(request, 'display.html', {'combinedList': combinedList})

    return render(request, 'fileUpload.html')



def sendEmail(request):
    if request.method == 'POST':
        list1 = request.POST.getlist('list1[]')
        list2 = request.POST.getlist('list2[]')
        list3 = request.POST.getlist('list3[]')

        
        combined_list = zip(list1, list2, list3)

        
        email_body = render_to_string('mailTemplate.txt', {'combined_list': combined_list})

        
        email = EmailMessage(
            subject='Python Assignment - Md Kaif Qureshi',
            body=email_body,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=['tech@themedius.ai'],  
            cc=['yash@themedius.ai'],  
        )

        
        email.send()

        return render(request, 'display.html', {'alert_message': "email sent succesfully!"})

    return redirect('send_email')
