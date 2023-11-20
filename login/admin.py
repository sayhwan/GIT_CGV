from django.contrib import admin
from .models import User

# 로그인 하는 함수
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=(
        'user_id',
        'user_pw',
        'user_name',
        'user_email',
        'user_register_dttm'
    )