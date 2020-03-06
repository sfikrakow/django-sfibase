from mozilla_django_oidc.views import OIDCAuthenticationRequestView, OIDCAuthenticationCallbackView


class OIDCAuthenticationNoPromptCallbackView(OIDCAuthenticationCallbackView):
    @property
    def failure_url(self):
        # Redirect back when in no prompt mode
        if 'oidc_prompt' in self.request.session and self.request.session['oidc_prompt'] == 'none':
            self.request.session['oidc_prompt'] = ''
            return super().success_url
        return super().failure_url


class OIDCAuthenticationNoPromptRequestView(OIDCAuthenticationRequestView):
    def get(self, request):
        request.session['oidc_prompt'] = 'none'
        return super().get(request)

    def get_extra_params(self, request):
        params = super().get_extra_params(request)
        params["prompt"] = "none"
        return params
