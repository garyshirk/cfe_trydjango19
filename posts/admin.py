from django.contrib import admin

# Register your models here.
from posts.models import Post

# Create a modeladmin so that we can show timestamp via modeladmin list_display option in admin server
class PostModelAdmin(admin.ModelAdmin):
	#list_display = ["__unicode__", "timestamp", "updated", "content"]
	list_display = ["title", "timestamp", "updated", "content"]
	list_display_links = ["updated"]
	list_filter = ["updated", "timestamp"]
	search_fields = ["title", "content"]
	list_editable = ["title"]
	class Meta:
		model = Post
		# notice you include PostAdmin as an arg in the register method below

admin.site.register(Post, PostModelAdmin)


