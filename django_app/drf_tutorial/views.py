from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView


class ApiRoot(APIView):
    def get(self, request, format=None):
        return Response({
            'users': reverse('member:user_list', request=request, format=format),
            'snippets': reverse('snippets:snippet_list', request=request, format=format)
        })
