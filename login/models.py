from django.db import models
#DB에 user라는 데이터들 생성
class User(models.Model):
    user_id = models.CharField(max_length=32, unique=True, verbose_name='유저 아이디')
    user_pw = models.CharField(max_length=128, verbose_name='유저 비밀번호')
    user_name = models.CharField(max_length=16, unique=True, verbose_name='유저 이름')
    user_email = models.EmailField(max_length=128, unique=True, verbose_name='유저 이메일')
    user_register_dttm = models.DateTimeField(auto_now_add=True, verbose_name='계정 생성시간')
    user_ticket=models.ManyToManyField('User_ticket')
    def __str__(self):
        return self.user_name
    #DB에 저장
    class Meta:
        db_table = 'user'
        verbose_name = '유저'
        verbose_name_plural = '유저'

class User_ticket(models.Model):
    seat=models.JSONField(default=list)
    date=models.DateTimeField(auto_now_add=True,editable=False)
    movie=models.CharField(max_length=200)
    cinema=models.CharField(max_length=200)
    theater=models.CharField(max_length=200)

    def __str__(self):
        return self.movie
    class Meta:
        db_table= 'user_ticket'
        verbose_name='유저 티켓'
        verbose_name='유저 티켓'
