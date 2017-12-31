# DEBUG设置
DEBUG = True

# 域名设置
ALLOWED_HOSTS = [
    '192.168.0.175',
    'localhost',
    '127.0.0.1'
]

# mysql 设置
DATABASES = {

    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'sspanel',
        'USER': 'root',
        'PASSWORD': 'Wuqiaini.123',
        'HOST': '47.96.154.113',
        'PORT': '3306',
        'OPTIONS': {
            'autocommit': True,
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            'charset': 'utf8mb4',
        },
    }
}

# 是否开启邮件功能
USE_SMTP = True
# 邮件服务设置：
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# 是否开启ssl/tls
EMAIL_USE_TLS = False
EMAIL_USE_SSL = False

# 我使用163邮箱作为smtp服务器
EMAIL_HOST = 'smtpdm.aliyun.com'
EMAIL_PORT = 80
EMAIL_HOST_USER = 'no-replay@nfvpn.com'
EMAIL_HOST_PASSWORD = 'WUqiaini123'
DEFAULT_FROM_EMAIL = 'no-replay@nfvpn.com'

# SS面板设置：
MB = 1024 * 1024
GB = 1024 * 1024 * 1024
DEFAULT_TRAFFIC = 0 * GB

# 默认加密混淆协议
DEFAULT_METHOD = 'none'
DEFAULT_PROTOCOL = 'auth_chain_a'
DEFAULT_OBFS = 'plain'

# 签到流量设置
MIN_CHECKIN_TRAFFIC = 0 * MB
MAX_CHECKIN_TRAFFIC = 0 * MB
START_PORT  = 5000
# 是否启用支付宝系统
USE_ALIPAY = True
# 支付订单提示信息 修改请保留 {} 用于动态生成金额
ALIPAY_TRADE_INFO = 'Yokiy的{}元充值码'

# 网站title
TITLE = 'Yokiy'
SUBTITLE = 'Yokiy的小屋'

# 用户邀请返利比例
INVITE_PERCENT = 0
# 用户能生成的邀请码数量
INVITE_NUM = 0

# 网站邀请界面提示语
INVITEINFO = '没有啦！'

# 网站域名设置（请正确填写，不然订阅功能会失效：
HOST = 'http://www.17kantv.com/'
