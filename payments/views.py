import imp
import stripe
from django.conf import settings
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt


def home(request):
    """
    Index page view
    """
    return render(request, 'payments/index.html', context=None)

def cancel(request):
    """
    Post Transaction Canceled
    """
    return render(request, 'payments/abort-payment.html', context=None)

def success(request):
    """
    Post Transaction success
    """
    return render(request, 'payments/success.html')


class StoriesView(TemplateView):
    template_name = 'payments/stories.html'

class ProjectsView(TemplateView):
    template_name = 'payments/projects.html'

@csrf_exempt
def stripe_config(request: HttpRequest):
    if request.method == 'GET':
        stripe_config = {'publicKey': settings.STRIPE_PUBLISHABLE_KEY}
        return JsonResponse(stripe_config, safe=False)
    

@csrf_exempt
def create_checkout_session(request: HttpRequest):
    if request.method == 'GET':
        domain = "http://localhost:8000/"
        stripe.api_key = settings.STRIPE_SECRET_KEY

        try:
            checkout_session = stripe.checkout.Session.create(
                success_url=domain + 'success?session_id={CHECKOUT_SESSION_ID}',
                cancel_url=domain + 'cancelled/',
                payment_method_types=['card'],
                mode='payment',
                line_items=[{
                    "price_data": {
                        "currency": "inr",
                        "product_data": {"name": "exeEscape"},
                        "unit_amount": 50000,
                    },
                    "quantity": 1,
                 }]
                )
            return JsonResponse({'sessionId': checkout_session['id']})
        except Exception as e:
            return JsonResponse({'error': str(e)})