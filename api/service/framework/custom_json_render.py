import contextlib
from rest_framework.renderers import JSONRenderer
from service.request_service import error_response_to_string_list, get_inactive_message


class CustomJsonRender(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):

        if not renderer_context:
            return super().render(data, accepted_media_type, renderer_context)
        response = renderer_context["response"]
        res_data = data

        if response.status_code in range(200, 299):
            return super().render(res_data, accepted_media_type, renderer_context)

        if isinstance(data, dict):
            res_data["messages"] = error_response_to_string_list(data)
            with contextlib.suppress(Exception):
                err = data["detail"]
                if (
                    err.code == "authentication_failed"
                    and str(err) == "User account is disabled."
                ):
                    res_data["messages"] = [get_inactive_message()]
        return super().render(res_data, accepted_media_type, renderer_context)
