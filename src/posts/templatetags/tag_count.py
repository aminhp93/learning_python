from django import template

register = template.Library()

@register.filter
def tag_count(value):
	return value