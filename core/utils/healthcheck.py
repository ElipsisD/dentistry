from django.http import HttpResponse
from rest_framework.request import Request


def healthcheck(request: Request) -> HttpResponse:  # noqa: ARG001, D103
    return HttpResponse("OK", content_type="text/plain")
