from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework import authentication, permissions
from rest_framework.permissions import AllowAny
from django.db.models import Q, Count, Exists
from rest_framework.viewsets import ModelViewSet
from itertools import chain
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

# from .serializers import MessageSerializer, UserSerializer, ChatMessageSerializer
# from messenger.models import Message
from rest_framework.response import Response
from datetime import datetime
from blog.models import Post, Category, Tag
from .serializers import ShortPostSerializer, PostSerializer, CategorySerializer, TagSerializer
from rest_framework.decorators import api_view


# class MessageListAPIView(ListAPIView):
# 	serializer_class = MessageSerializer
# 	depth = 1
# 	def get_queryset(self):
# 		user = self.request.user
# 		pk = self.kwargs['pk']
# 		return Message.objects.filter(Q(user_from__id=pk,user_to=user)|Q(user_from=user,user_to__id=pk)).order_by("-id")
	
# class MessageListAPIView(ModelViewSet):
# 	# serializer_class = MessageSerializer
# 	# depth = 1
# 	# def get_queryset(self):
# 	# 	user = self.request.user
# 	# 	pk = self.kwargs['pk']
# 	# 	return Message.objects.filter(Q(user_from__id=pk,user_to=user)|Q(user_from=user,user_to__id=pk)).order_by("-id")
# 	def retrieve(self, request, pk=None):
# 		all_users = User.objects.all()
# 		user = get_object_or_404(all_users, pk=pk)
# 		queryset = Message.objects.filter(Q(user_from__id=pk,user_to=request.user)|Q(user_from=request.user,user_to__id=pk)).order_by("id")
# 		queryset.filter(user_to=request.user, viewed__isnull=True).update(viewed=datetime.now())
# 		return Response({
# 			"user_from": UserSerializer(user).data,
# 			"results": MessageSerializer(queryset, many=True).data
# 		})
	



	# def get(self):
	# 	user = self.request.user
	# 	pk = self.kwargs['pk']
	# 	messages = Message.objects.filter(Q(user_from__id=pk,user_to=user)|Q(user_from=user,user_to__id=pk)).order_by("-id")
	# 	return Response({
	# 			user_from: UserSerializer(id=pk),
	# 			messages: messages
	# 		})
# class CurrentUserView(APIView):
#     def get(self, request):
#         serializer = UserSerializer(request.user)
#         return Response(serializer.data)

# class UserMessagesView(ListAPIView):
# 	serializer_class = ChatMessageSerializer
# 	def get_queryset(self):
# 		chats = []
# 		user = self.request.user
# 		messages = Message.objects.filter(Q(user_from=user)|Q(user_to=user)).order_by("-id")
# 		chatters = set(messages.values_list('user_from', flat=True)).union(messages.values_list('user_to', flat=True))
# 		for chatter in list(chain(chatters)):
# 			filtered = messages.filter(Q(user_from__id=chatter,user_to=user)|Q(user_from=user,user_to__id=chatter))
# 			# filtered = before_filtered.annotate(unviewed_count=5).order_by("-id")
# 			# print(filtered[1].unviewed_count)
# 			if len(filtered)>0:
# 				chats.append(filtered[0]) 
# 		return sorted(set(chats),key=lambda k: k.id,reverse=True)



# Exists(before_filtered.filter(delivered__isnull=True).count())


class PostsView(ListAPIView):
	queryset = Post.objects.filter(~Q(Q(status='O')|Q(status='D'))).order_by('-created')
	permission_classes = (AllowAny,)
	serializer_class = ShortPostSerializer


class CategoriesView(ListAPIView):
	queryset = Category.objects.all()
	permission_classes = (AllowAny,)
	serializer_class = CategorySerializer


class TagsView(ListAPIView):
	queryset = Tag.objects.all()
	permission_classes = (AllowAny,)
	serializer_class = TagSerializer


@api_view(['GET', 'PUT', 'DELETE'])
def get_post(request, post_slug):
    try:
        post = Post.objects.get(title_slug=post_slug)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)

    elif request.method == 'PUT':
        # serializer = SnippetSerializer(snippet, data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        pass

    elif request.method == 'DELETE':
        # snippet.delete()
        # return Response(status=status.HTTP_204_NO_CONTENT)
        pass

