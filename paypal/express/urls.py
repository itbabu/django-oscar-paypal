from django.conf.urls.defaults import *

from paypal.express import views


urlpatterns = patterns('',
    url(r'^redirect/', views.RedirectView.as_view(), name='paypal-redirect'),
    url(r'^preview/', views.SuccessResponseView.as_view(preview=True),
        name='paypal-success-response'),
    url(r'^cancel/', views.CancelResponseView.as_view(),
        name='paypal-cancel-response'),
    url(r'^place-order/', views.SuccessResponseView.as_view(),
        name='paypal-place-order'),
)
