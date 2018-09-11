from django.contrib import admin
import nested_admin

from .models import Subject, Course, Chapter, Step, Text, HtmlBlock, Video, Trajectory

# video
class VideoInline(nested_admin.NestedTabularInline):
    model = Video
    extra = 0

class VideoAdmin(nested_admin.NestedModelAdmin):
	pass

# html
class HtmlBlockInline(nested_admin.NestedTabularInline):
    model = HtmlBlock
    extra = 0

class HtmlBlockAdmin(nested_admin.NestedModelAdmin):
	pass

# text
class TextInline(nested_admin.NestedTabularInline):
    model = Text
    extra = 0

class TextAdmin(nested_admin.NestedModelAdmin):
	pass

# step
class StepInline(nested_admin.NestedTabularInline):#admin.StackedInline):
    model = Step
    extra = 0
    inlines = [TextInline, HtmlBlockInline, VideoInline]

class StepAdmin(nested_admin.NestedModelAdmin):
	inlines = [TextInline, HtmlBlockInline, VideoInline]

# chapter
class ChapterInline(nested_admin.NestedTabularInline):#admin.StackedInline):
    model = Chapter
    extra = 0
    inlines = [StepInline]

class ChapterAdmin(nested_admin.NestedModelAdmin):
	inlines = [StepInline]

# course 
class CourseInline(nested_admin.NestedStackedInline):
    model = Course
    extra = 0
    filter_horizontal = ('tags','students')
    inlines = [ChapterInline]

class CourseAdmin(nested_admin.NestedModelAdmin):
    model = Course
    list_display = ('name','category','degree','price','status','language')
    list_filter=['status', 'category','language', 'degree']
    search_fields=['name','content','description','students']
    filter_horizontal = ('tags','students','subjects')
    inlines = [ChapterInline]

    # fieldsets = [
    #     (None,               {'fields': ['name','author','contents','image','assigned_date',]}),
    #     ('Choices',       {'fields': ['course','degree','typeof',]}),
    #     ('Access',       {'fields': ['customers','hidden','price',]}),
    # ]

# subject 
class SubjectAdmin(nested_admin.NestedModelAdmin):
	# inlines = [CourseInline]
    pass

class TrajectoryAdmin(nested_admin.NestedModelAdmin):
    pass


admin.site.register(Video, VideoAdmin)
admin.site.register(HtmlBlock, HtmlBlockAdmin)
admin.site.register(Text, TextAdmin)
admin.site.register(Step, StepAdmin)
admin.site.register(Chapter, ChapterAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Trajectory, TrajectoryAdmin)
