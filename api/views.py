from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.decorators import login_required

from.serializers import *
from blog.models import *

# Create your views here.


@api_view(['GET'])
def categoryList(request):
  categories = Category.objects.all()
  serializer = CategorySerializer(categories, many=True)
  return Response(serializer.data)


@login_required
@api_view(['GET'])
def categoryDetail(request, pk):
  category = Category.objects.get(id=pk)
  serializer = CategorySerializer(category, many=False)
  return Response(serializer.data)


@login_required
@api_view(['POST'])
def categoryCreate(request):
  serializer = CategorySerializer(data=request.data)
  if serializer.is_valid():
    serializer.save()
  return Response(serializer.data)


@login_required
@api_view(['POST'])
def categoryUpdate(request,pk):
  category = Category.objects.get(id=pk)
  serializer = CategorySerializer(instance=category, data=request.data)
  if serializer.is_valid():
    serializer.save()
  return Response(serializer.data)


@login_required
@api_view(['DELETE'])
def categoryDelete(request,pk):
  category = Category.objects.get(id=pk)
  category.delete()
  return Response('Category Successfully Deleted!')


@api_view(['GET'])
def postList(request):
  posts = Post.objects.all()
  serializer = PostSerializer(posts, many=True)
  return Response(serializer.data)


@login_required
@api_view(['GET'])
def postDetail(request, pk):
  post = Post.objects.get(id=pk)
  serializer = PostSerializer(post, many=False)
  return Response(serializer.data)


@login_required
@api_view(['POST'])
def postCreate(request):
  serializer = PostSerializer(data=request.data)
  if serializer.is_valid():
    serializer.save()
  return Response(serializer.data)


@login_required
@api_view(['POST'])
def postUpdate(request, pk):
  post = Post.objects.get(id=pk)
  serializer = PostSerializer(instance=post, data=request.data)
  if serializer.is_valid():
    serializer.save()
  return Response(serializer.data)


@login_required
@api_view(['DELETE'])
def postDelete(request, pk):
  post = Post.objects.get(id=pk)
  post.delete()
  return Response('Post Successfully Deleted!')


@api_view(['GET'])
def commentList(request):
  comments = Comment.objects.all()
  serializer = CommentSerializer(comments, many=True)
  return Response(serializer.data)


@api_view(['GET'])
def commentDetail(request, pk):
  comment = Comment.objects.get(id=pk)
  serializer = CommentSerializer(comment, many=False)
  return Response(serializer.data)


@api_view(['POST'])
def commentCreate(request):
  serializer = CommentSerializer(data=request.data)
  if serializer.is_valid():
    serializer.save()
  return Response(serializer.data)


@api_view(['POST'])
def commentUpdate(request, pk):
  comment = Comment.objects.get(id=pk)
  serializer = CommentSerializer(instance=comment, data=request.data)
  if serializer.is_valid():
    serializer.save()
  return Response(serializer.data)


@login_required
@api_view(['DELETE'])
def commentDelete(request, pk):
  comment = Comment.objects.get(id=pk)
  comment.delete()
  return Response('Comment Successfully Deleted!')


@api_view(['GET'])
def contactList(request):
  contacts = Contact.objects.all()
  serializer = ContactSerializer(contacts, many=True)
  return Response(serializer.data)


@api_view(['GET'])
def contactDetail(request, pk):
  contact = Contact.objects.get(id=pk)
  serializer = ContactSerializer(contact, many=False)
  return Response(serializer.data)


@api_view(['POST'])
def contactCreate(request):
  serializer = ContactSerializer(data=request.data)
  if serializer.is_valid():
    serializer.save()
  return Response(serializer.data)


@api_view(['POST'])
def contactUpdate(request, pk):
  contact = Contact.objects.get(id=pk)
  serializer = ContactSerializer(instance=contact, data=request.data)
  if serializer.is_valid():
    serializer.save()
  return Response(serializer.data)


@api_view(['DELETE'])
def contactDelete(request, pk):
  contact = Contact.objects.get(id=pk)
  contact.delete()
  return Response('Contact info Successfully Deleted!')


@api_view(['GET'])
def newslettertList(request):
  newsletters = Newsletter.objects.all()
  serializer = NewsletterSerializer(newsletters, many=True)
  return Response(serializer.data)


@api_view(['GET'])
def newsletterDetail(request, pk):
  newslatter = Newsletter.objects.get(id=pk)
  serializer = NewsletterSerializer(newslatter, many=False)
  return Response(serializer.data)


@api_view(['POST'])
def newsletterCreate(request):
  serializer = NewsletterSerializer(data=request.data)
  if serializer.is_valid():
    serializer.save()
  return Response(serializer.data)


@api_view(['POST'])
def newsletterUpdate(request, pk):
  newsletter = Newsletter.objects.get(id=pk)
  serializer = NewsletterSerializer(instance=newsletter, data=request.data)
  if serializer.is_valid():
    serializer.save()
  return Response(serializer.data)


@api_view(['DELETE'])
def newsletterDelete(request, pk):
  newsletter = Newsletter.objects.get(id=pk)
  newsletter.delete()
  return Response('Email Successfully Deleted!')
