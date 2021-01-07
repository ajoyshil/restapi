from functools import wraps

from django.http import JsonResponse
from django.contrib.auth import logout
from utils.JWTManager import JWTManager


def login_required(function):
    @wraps(function)
    def decorator(request, *args, **kwargs):
        auth_token = request.META.get('HTTP_AUTHORIZATION')
        print(auth_token)
        if auth_token is None:
            # Check the cookie once
            auth_token = request.COOKIES.get('HTTP_AUTHORIZATION')
        if auth_token is not None:
            auth_token = auth_token.split(" ")[-1]
            token_manager = JWTManager()
            token_valid = token_manager.validate_token(auth_token)
            # check if the token is a refresh token
            is_ref_token = token_manager.is_refresh_token()
            if is_ref_token:
                return JsonResponse({"status": False, "message": "INVALID AUTHORIZATION", "code": 401}, status=401)
            user = None
            if token_valid:
                user = token_manager.get_user()
            else:
                return JsonResponse({"status": False, "message": "SESSION EXPIRED", "code": 401}, status=401)
            if user is not None:
                request.user = user
                return function(request, *args, **kwargs)
            else:
                return JsonResponse({"status": False, "message": "UNAUTHORIZED", "code": 401}, status=401)
        else:
            return JsonResponse({"status": False, "message": "AUTHORIZATION NOT AVAILABLE", "code": 401}, status=401)
    return decorator


def allow_http_cookie_authorization(function):
    @wraps(function)
    def decorator(request, *args, **kwargs):
        try:
            auth_token = request.COOKIES['HTTP_AUTHORIZATION']
            if auth_token is not None:
                request.META['HTTP_AUTHORIZATION'] = auth_token
                return function(request, *args, *kwargs)
        except Exception as e:
            pass
    return decorator


def unauthorized_user_only(function):
    @wraps(function)
    def decorator(request, *args, **kwargs):
        auth_token = request.META.get('HTTP_AUTHORIZATION')
        if auth_token is not None:
            return JsonResponse({"status": False, "message": "AUTHORIZED USERS NOT ALLOWED", "code": 405}, status=405)
        else:
            return function(request, *args, **kwargs)
    return decorator


def admin_only(function):
    @wraps(function)
    def decorator(request, *args, **kwargs):
        if request.user is not None:
            if request.user.user_type == 0:
                return function(request, *args, **kwargs)
            else:
                return JsonResponse({"status": False, "message": "INVALID ACCESS AUTHORIZATION", "code": 400}, status=400)
        else:
            return JsonResponse({"status": False, "message": "INVALID ACCESS AUTHORIZATION", "code": 400}, status=400)
    return decorator


def standard_user_only(function):
    @wraps(function)
    def decorator(request, *args, **kwargs):
        if request.user is not None:
            if request.user.user_type == 1:
                return function(request, *args, **kwargs)
            else:
                return JsonResponse({"status": False, "message": "INVALID ACCESS AUTHORIZATION", "code": 401}, status=401)
        else:
            return JsonResponse({"status": False, "message": "INVALID ACCESS AUTHORIZATION", "code": 401}, status=401)
    return decorator


def mlm_user_only(function):
    @wraps(function)
    def decorator(request, *args, **kwargs):
        if request.user is not None:
            if request.user.user_type == 2:
                return function(request, *args, **kwargs)
            else:
                return JsonResponse({"status": False, "message": "INVALID ACCESS AUTHORIZATION", "code": 400}, status=400)
        else:
            return JsonResponse({"status": False, "message": "INVALID ACCESS AUTHORIZATION", "code": 400}, status=400)
    return decorator


def franchise_owner_only(function):
    @wraps(function)
    def decorator(request, *args, **kwargs):
        if request.user is not None:
            if request.user.user_type == 2:
                return function(request, *args, **kwargs)
            else:
                return JsonResponse({"status": False, "message": "INVALID ACCESS AUTHORIZATION", "code": 400}, status=400)
        else:
            return JsonResponse({"status": False, "message": "INVALID ACCESS AUTHORIZATION", "code": 400}, status=400)
    return decorator


def patient_only(function):
    @wraps(function)
    def decorator(request, *args, **kwargs):
        if request.user is not None:
            if request.user.user_type == 3:
                return function(request, *args, **kwargs)
            else:
                return JsonResponse({"status": False, "message": "INVALID ACCESS AUTHORIZATION", "code": 400}, status=400)
        else:
            return JsonResponse({"status": False, "message": "INVALID ACCESS AUTHORIZATION", "code": 400}, status=400)
    return decorator


def super_admin_only(function):
    @wraps(function)
    def decorator(request, *args, **kwargs):
        if request.user is not None:
            if request.user.user_type == 4:
                return function(request, *args, **kwargs)
            else:
                return JsonResponse({"status": False, "message": "INVALID ACCESS AUTHORIZATION", "code": 400}, status=400)
        else:
            return JsonResponse({"status": False, "message": "INVALID ACCESS AUTHORIZATION", "code": 400}, status=400)
    return decorator


def admin_group_only(function):
    @wraps(function)
    def decorator(request, *args, **kwargs):
        if request.user is not None:
            if request.user.user_type in [0, 4]:
                return function(request, *args, **kwargs)
            else:
                return JsonResponse({"status": False, "message": "INVALID ACCESS AUTHORIZATION", "code": 400}, status=400)
        else:
            return JsonResponse({"status": False, "message": "INVALID ACCESS AUTHORIZATION", "code": 400}, status=400)
    return decorator


def non_admin_only(function):
    @wraps(function)
    def decorator(request, *args, **kwargs):
        if request.user is not None:
            if request.user.user_type in [1, 2]:
                return function(request, *args, **kwargs)
            else:
                return JsonResponse({"status": False, "message": "INVALID ACCESS AUTHORIZATION", "code": 400}, status=400)
        else:
            return JsonResponse({"status": False, "message": "INVALID ACCESS AUTHORIZATION", "code": 400}, status=400)
    return decorator


def admin_and_standard_user_only(function):
    @wraps(function)
    def decorator(request, *args, **kwargs):
        if request.user is not None:
            if request.user.user_type in [0, 1]:
                return function(request, *args, **kwargs)
            else:
                return JsonResponse({"status": False, "message": "INVALID ACCESS AUTHORIZATION", "code": 400},
                                    status=400)
        else:
            return JsonResponse({"status": False, "message": "INVALID ACCESS AUTHORIZATION", "code": 400}, status=400)
    return decorator


def admin_and_mlm_user_only(function):
    @wraps(function)
    def decorator(request, *args, **kwargs):
        if request.user is not None:
            if request.user.user_type in [0, 1]:
                return function(request, *args, **kwargs)
            else:
                return JsonResponse({"status": False, "message": "INVALID ACCESS AUTHORIZATION", "code": 400},
                                    status=400)
        else:
            return JsonResponse({"status": False, "message": "INVALID ACCESS AUTHORIZATION", "code": 400}, status=400)
    return decorator


def unregistered_and_admin_only(function):
    @wraps(function)
    def decorator(request, *args, **kwargs):
        if request.user is not None:
            if request.user.user_type == 0:
                return function(request, *args, **kwargs)
            else:
                return JsonResponse({"status": False, "message": "INVALID ACCESS AUTHORIZATION", "code": 400}, status=400)
        else:
            return function(request, *args, **kwargs)
    return decorator


def unregistered_and_standard_user_only(function):
    @wraps(function)
    def decorator(request, *args, **kwargs):
        if request.user is not None:
            if request.user.user_type == 1:
                return function(request, *args, **kwargs)
            else:
                return JsonResponse({"status": False, "message": "INVALID ACCESS AUTHORIZATION", "code": 400}, status=400)
        else:
            return function(request, *args, **kwargs)
    return decorator


def unregistered_and_mlm_user_only(function):
    @wraps(function)
    def decorator(request, *args, **kwargs):
        if request.user is not None:
            if request.user.user_type == 0:
                return function(request, *args, **kwargs)
            else:
                return JsonResponse({"status": False, "message": "INVALID ACCESS AUTHORIZATION", "code": 400}, status=400)
        else:
            return function(request, *args, **kwargs)
    return decorator

