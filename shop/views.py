from django.shortcuts import render
from .serializer import MenuSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import UserRegistrationSerializer, UserLoginSerializer, CartItemSerializer, ContactFormSerializer
from .models import Menu, CartItem, Contact
from django.http import JsonResponse
from rest_framework import viewsets
from django.template.loader import render_to_string
from django.core.mail import send_mail, EmailMessage



class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class AddToCartView(APIView):
    def post(self, request, format=None):
        serializer = CartItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteCartItemView(APIView):
    def delete(self, request, pk, format=None):
        try:
            cart_item = CartItem.objects.get(pk=pk)
            cart_item.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except CartItem.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)



class ContactFormView(APIView):
    def post(self, request, format=None):
        serializer = ContactFormSerializer(data=request.data)
        if serializer.is_valid():
            # Extract validated form data
            name = serializer.validated_data['name']
            email = serializer.validated_data['email']
            message = serializer.validated_data['message']

           # Save the contact form data to the database
            contact = Contact(name=name, email=email, message=message)
            contact.save()

           # For sending email notifications
            subject = 'Thank you for contacting Smoothie Bar'
            template_name = 'notification.html'
            context = {'name': name}
            html_message = render_to_string(template_name, context)
            sender = 'smoothiedaddi@gmail.com'  # Update with your email address
            recipients = [email]
            email = EmailMessage(subject, html_message, sender, recipients)
            email.content_subtype = 'html'
            email.send()

            # Return a success response
            return Response({'message': 'Form submitted successfully'}, status=status.HTTP_200_OK)
        else:
            # Return an error response
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User registered successfully.'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    


class UserLoginView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        # Perform any additional actions or generate a token here
        return Response({'message': 'Login successful.'}, status=status.HTTP_200_OK)

