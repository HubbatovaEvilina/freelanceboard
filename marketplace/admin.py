from django.contrib import admin
from .models import Category, Order, Response, Review

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'customer', 'budget', 'status', 'created_at')
    list_filter = ('status', 'category')
    search_fields = ('title', 'description')

@admin.register(Response)
class ResponseAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'executor', 'proposed_budget', 'status', 'created_at')
    list_filter = ('status',)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'author', 'recipient', 'rating')