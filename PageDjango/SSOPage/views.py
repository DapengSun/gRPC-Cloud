from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from SSO import SSOVerifyLogin_Client as ssologin
from Common.CommonHelper import Tool,ResponseStatus

# Create your views here.

def LoginIndex(request):
    return render_to_response(template_name='index.html')

@require_http_methods(["POST"])
@csrf_exempt
def VerifyLogin(request):
    try:
        _userName = request.POST.get('username','')
        _passWord = request.POST.get('password', '')
        # _url = request.POST.get('url', '')
        _result = ssologin.main(_userName,_passWord)

        if _result['Code'] == 0:
            return Tool.JsonResult(ResponseStatus.Ok, '验证成功', '')
        else:
            return Tool.JsonResult(ResponseStatus.Error, '验证失败', '')
    except Exception as ex:
        return Tool.JsonResult(ResponseStatus.Error, '验证失败', str(ex))


