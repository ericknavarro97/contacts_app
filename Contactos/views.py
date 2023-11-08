from rest_framework.generics import RetrieveAPIView, ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated

from Contactos.serializers import ContactSerializer


class CreateContact(CreateAPIView):
    """Retrieve contact by user"""
    model = Contact
    serializer_class = ContactSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        """Filter contacts by user"""
        return self.request.user.contactos.all()

    def perform_create(self, serializer):
        """Create contact"""
        serializer.save(user=self.request.user)
        return serializer.data


class RetrieveContact(RetrieveAPIView):
    """Retrieve contact by user"""

    model = Contact
    serializer_class = ContactSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = "pk"

    def get_queryset(self):
        """Filter contacts by user"""
        return self.request.user.contactos.all()


class RetrieveListContacts(ListAPIView):
    """Retrieve all contacts by user"""

    model = Contact
    serializer_class = ContactSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        """Filter contacts by user"""
        return self.request.user.contactos.all()


class UpdateContact(UpdateAPIView):
    """Retrieve all contacts by user"""

    model = Contact
    serializer_class = ContactSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = "pk"

    def get_queryset(self):
        """Filter contacts by user"""
        return self.request.user.contactos.all()


class DeleteContact(DestroyAPIView):
    """Retrieve all contacts by user"""

    serializer_class = ContactSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = "pk"

    def get_queryset(self):
        """Filter contacts by user"""
        return self.request.user.contactos.all()
