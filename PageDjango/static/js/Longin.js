function login(){
    var username = document.getElementById("ID").value;
    var password = document.getElementById("PASSWORD").value;
    if(username==""){
        $.jGrowl("用户名不能为空！", { header: '提醒' });
    }else if(password==""){
        $.jGrowl("密码不能为空！", { header: '提醒' });
    }else{
        AjaxFunc();
    }
}

function GetUrlParam(name) {
    var reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)"); //构造一个含有目标参数的正则表达式对象
    var r = window.location.search.substr(1).match(reg);  //匹配目标参数
    if (r != null) return unescape(r[2]); return null; //返回参数值
}

function AjaxFunc()
{
    var username = document.getElementById("ID").value;
    var password = document.getElementById("PASSWORD").value;
    var url = GetUrlParam("requesturl");

    $.ajax({
        type: 'post',
        async: false,
        url: "/sso/verifylogin",
        dataType: "json",
        data: {"username": username,"password": password},
        success: function (data) {
            if(data.Code == 200){
                window.location.href = url;
            }else{
                alert(data.Message);
            }
        },
        error: function (xhr, type) {
            console.log(xhr);
        }
    });
}