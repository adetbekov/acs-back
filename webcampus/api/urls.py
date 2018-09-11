from django.urls import path
from .views import SubjectView, get_course, SyllabusView, LessonView, StepView

app_name = "webcampus"

urlpatterns = [
	# url(r'^messages/(?P<pk>[0-9]+)/$', MessageListAPIView.as_view({'get': 'retrieve'}), name="messages"),
	# url(r'^tags$', TagsView.as_view(), name="tags"),
	# url(r'^categories$', CategoriesView.as_view(), name="categories"),
	# url(r'^(?P<course_slug>.+)/$', get_course, name="course"),
	# url(r'^(?P<course_slug>.+)/syllabus$', SyllabusView.as_view(), name="syllabus"),
	# url(r'^(?P<course_slug>.+)/(?P<chapter_slug>.+)$', LessonView.as_view(), name="lesson"),
	# url(r'^(?P<course_slug>.+)/(?P<chapter_slug>.+)/(?P<step_slug>.+)$', StepView.as_view(), name="step"),
	path('<slug:course_slug>/', get_course),
	path('<slug:course_slug>/syllabus', SyllabusView.as_view()),
	path('<slug:course_slug>/<slug:chapter_slug>/', LessonView.as_view()),
	path('<slug:course_slug>/<slug:chapter_slug>/<slug:step_slug>/', StepView.as_view()),
	path('subjects', SubjectView.as_view()),
	# url(r'^(?P<pk>[0-9]+)/$', get_post, name="post")
]

# from django.conf.urls import url
# from django.urls import path
# from .views import SubjectView, get_course, SyllabusView, LessonView, StepView

# urlpatterns = [
# 	# url(r'^messages/(?P<pk>[0-9]+)/$', MessageListAPIView.as_view({'get': 'retrieve'}), name="messages"),
# 	# url(r'^tags$', TagsView.as_view(), name="tags"),
# 	# url(r'^categories$', CategoriesView.as_view(), name="categories"),
# 	# url(r'^(?P<course_slug>.+)/$', get_course, name="course"),
# 	# url(r'^(?P<course_slug>.+)/syllabus$', SyllabusView.as_view(), name="syllabus"),
# 	# url(r'^(?P<course_slug>.+)/(?P<chapter_slug>.+)$', LessonView.as_view(), name="lesson"),
# 	# url(r'^(?P<course_slug>.+)/(?P<chapter_slug>.+)/(?P<step_slug>.+)$', StepView.as_view(), name="step"),
# 	path('<slug:course_slug>', get_course, name="course"),
# 	url(r'^subjects$', SubjectView.as_view(), name="subjects"),
# 	# url(r'^(?P<pk>[0-9]+)/$', get_post, name="post")
# ]