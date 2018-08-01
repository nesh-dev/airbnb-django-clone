from django import forms
from django.forms.utils import ErrorList
from django.http import JsonResponse
from django.http import HttpResponse



class FormUserNeededMixin(object):

    def form_valid(self, form):
        if self.request.user.is_authenticated():
            form.instance.user = self.request.user
            return super(FormUserNeededMixin, self).form_valid(form)
        else:
            form._errors[forms.forms.NON_FIELD_ERRORS] = ErrorList(["User must be logged in to continue"])
            return self.form_invalid(form)


class UserOwnerMixin(FormUserNeededMixin, object):

    def form_valid(self, form):
        if form.instance.user == self.request.user:

            return super(UserOwnerMixin, self).form_valid(form)
        else:
            form._errors[forms.forms.NON_FIELD_ERRORS] = ErrorList(["this user is not allowed to change this data"])
        return self.form_invalid(form)


class AjaxFormMixin(object):        
    def render_to_json_response(self, context, **response_kwargs):
        """Render a json response of the context."""

        data = json.dumps(context)
        response_kwargs['content_type'] = 'application/json'
        return HttpResponse(data, **response_kwargs)
    
    def form_invalid(self, form):
        response = super(AjaxFormMixin, self).form_invalid(form)
        if self.request.is_ajax():
            return self.render_to_json_response(form.errors, status=400)

        return response

    def form_valid(self, form):
        response = super(AjaxFormMixin, self).form_valid(form)
        if self.request.is_ajax():
            # Request is ajax, send a json response
            data = {
                'pk': self.object.pk,
            }
            return self.render_to_json_response(data)

        return response  # Request isn't ajax, send normal response