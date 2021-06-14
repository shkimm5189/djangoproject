DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # 사용할 DB
        'NAME': 'django_test',                 # database 이름
        'USER': 'django',                        # 접속 계정
        'PASSWORD': 'test',              # 접속 계정 비밀번호
        'HOST': 'localhost',                    # DB 주소
        'PORT': '3306'                         # port
    }
}