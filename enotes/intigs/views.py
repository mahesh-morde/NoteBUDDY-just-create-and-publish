from audioop import reverse
from django.shortcuts import redirect, render
import razorpay

from django.core.mail import send_mail
from django.http import HttpResponse

from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseBadRequest
 
 
# authorize razorpay client with API Keys.
razorpay_client = razorpay.Client(
    auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))
 
 
def contrib(request):
    currency = 'INR'
    amount = 20000  # Rs. 200
 
    # Create a Razorpay Order
    razorpay_order = razorpay_client.order.create(dict(amount=amount,
                                                       currency=currency,
                                                       payment_capture='0'))
 
    # order id of newly created order.
    razorpay_order_id = razorpay_order['id']
    callback_url = 'paymenthandler/'
 
    # we need to pass these details to frontend.
    context = {}
    context['razorpay_order_id'] = razorpay_order_id
    context['razorpay_merchant_key'] = settings.RAZOR_KEY_ID
    context['razorpay_amount'] = amount
    context['currency'] = currency
    context['callback_url'] = callback_url
 
    return render(request, 'contrib.html', context=context)
 
 
# we need to csrf_exempt this url as
# POST request will be made by Razorpay
# and it won't have the csrf token.
@csrf_exempt
def paymenthandler(request):
 
    # only accept POST request.
    if request.method == "POST":
        try:
           
            # get the required parameters from post request.
            payment_id = request.POST.get('razorpay_payment_id', '')
            razorpay_order_id = request.POST.get('razorpay_order_id', '')
            signature = request.POST.get('razorpay_signature', '')
            params_dict = {
                'razorpay_order_id': razorpay_order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature
            }

            
 
            # verify the payment signature.
            result = razorpay_client.utility.verify_payment_signature(
                params_dict)
            if result is not None:
                amount = 20000  # Rs. 200
                try:
 
                    # capture the payemt
                    razorpay_client.payment.capture(payment_id, amount)
 
                    # # render success page on successful caputre of payment
                    # render_result = render(request, 'paymentsuccess.html')
                
                    # Render the loader page
                    loader_page = render(request, 'loader.html')

                    # Call the submit_email view
                    sendusermail(request)
                    print("load")
                    # return loader_page
                    # Redirect to the actual success page after a delay
                    redirect_url = 'payment-success/' 
                    response = HttpResponse(loader_page)
                    response['refresh'] = f'5;url={redirect_url}'
                    return response
                except:
 
                    # if there is an error while capturing payment.
                    return render(request, 'paymentfail.html')
            else:
 
                # if signature verification fails.
                return render(request, 'paymentfail.html')
        except:
 
            # if we don't find the required parameters in POST data
            return HttpResponseBadRequest()
    else:
       # if other than POST request is made.
        return HttpResponseBadRequest()




from django.http import JsonResponse

def submit_email(request):
    if request.method == 'POST':
        user_email = request.POST.get('email', '')

        settings.USER_EMAIL = user_email
        print(settings.USER_EMAIL)

        # Do something with the user_email, such as save it to the database or process it further

        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})








def sendusermail(request):
    email= settings.USER_EMAIL
    print("e: "+ email)
    settings.USER_EMAIL = ""
    msg = """Dear User, 

Thank you for your 200 Rupee contribution to the NoteBUDDY application. Your support is invaluable and will directly contribute to the improvement and maintenance of our platform.

We appreciate your generosity and are grateful to have you as part of our community.

Best regards,
NoteBUDDY Team """
    send_mail(
        "Payment Successfull",
        msg,
        "mukeshbhute64@gmail.com",
        [email],  # You can add user's email here
        fail_silently=False,
    )
    return HttpResponse('hello')


def payment_success(request):
    return render(request, 'paymentsuccess.html')




