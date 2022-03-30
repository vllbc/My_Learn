# 原版看着十分的繁琐

# def upload_avatar(request):
#     """用户上传新头像"""
#     try:
#         avatar_file = request.FILES['avatar']
#     except KeyError:
#         raise error_codes.AVATAR_FILE_NOT_PROVIDED

#     try:
#        resized_avatar_file = resize_avatar(avatar_file)
#     except FileTooLargeError as e:
#         raise error_codes.AVATAR_FILE_TOO_LARGE
#     except ResizeAvatarError as e:
#         raise error_codes.AVATAR_FILE_INVALID

#     try:
#         request.user.avatar = resized_avatar_file
#         request.user.save()
#     except Exception:
#         raise error_codes.INTERNAL_SERVER_ERROR
#     return HttpResponse({})

# 使用上下文管理器修改后

# class raise_api_error:
#     """captures specified exception and raise ApiErrorCode instead

#     :raises: AttributeError if code_name is not valid
#     """
#     def __init__(self, captures, code_name):
#         self.captures = captures
#         self.code = getattr(error_codes, code_name)

#     def __enter__(self):
#         该方法将在进入上下文时调用
#         return self

#     def __exit__(self, exc_type, exc_val, exc_tb):
#         该方法将在退出上下文时调用
#         exc_type, exc_val, exc_tb 分别表示该上下文内抛出的异常类型、异常值、错误栈
#         __enter__()：主要执行一些环境准备工作，同时返回一资源对象。如果上下文管理器open("test.txt")的__enter__()函数返回一个文件对象。
#         __exit__()：完整形式为__exit__(type, value, traceback),这三个参数和调用sys.exec_info()函数返回值是一样的，分别为异常类型、异常信息和堆栈。如果*执行体语句*没有引发异常，则这三个参数均被设为None。否则，它们将包含上下文的异常信息。__exit__()方法返回True或False,分别指示被引发的异常有没有被处理，如果返回False，引发的异常将会被传递出上下文。如果__exit__()函数内部引发了异常，则会覆盖掉执行体的中引发的异常。处理异常时，不需要重新抛出异常，只需要返回False，with语句会检测__exit__()返回False来处理异常。

#         if exc_type is None:
#             return False

#         if exc_type == self.captures:
#             raise self.code from exc_val
#         return False

# def upload_avatar(request):
#     """用户上传新头像"""
#     with raise_api_error(KeyError, 'AVATAR_FILE_NOT_PROVIDED'):
#         avatar_file = request.FILES['avatar']

#     with raise_api_error(ResizeAvatarError, 'AVATAR_FILE_INVALID'),\
#             raise_api_error(FileTooLargeError, 'AVATAR_FILE_TOO_LARGE'):
#         resized_avatar_file = resize_avatar(avatar_file)

#     with raise_api_error(Exception, 'INTERNAL_SERVER_ERROR'):
#         request.user.avatar = resized_avatar_file
#         request.user.save()
#     return HttpResponse({})
