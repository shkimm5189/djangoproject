from django.contrib import admin
from rest_api_board.models import MyBoard
from rest_api_account.models import Profiles
# 게시판 내용 관리자 페이지에서 확인
admin.site.register(MyBoard)

# 유저 등록 현황 관리자 페이지에서 확인
admin.site.register(Profiles)

