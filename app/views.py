from rest_framework import generics
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import ContactListSerializer
from rest_framework.response import Response
from .models import ContactList

@api_view(['POST'])
def create_contact(request):
        # create coontact
    contact = ContactListSerializer(data=request.data)
    if contact.is_valid():
        contact.save()
        return Response(contact.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

class ContactListView(generics.ListCreateAPIView):
    # list out contacts
    queryset = ContactList.objects.all()
    serializer_class = ContactListSerializer