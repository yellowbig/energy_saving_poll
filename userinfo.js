/**
 * Created by shuo on 17-6-14.
 */
webpackJsonp([ 3 ], {
    6: function(t, o, e) {
        "use strict";
        window.user = {
            init: function() {
                return {
                    mobile: 1 * $(".mobile-text").val(),
                    companyType: 1 * $(".companyTypes input:checked").val(),
                    company: $("#provinceName").val(),
                    companyId: $("#provinceName :checked").prop("id") >> 0,
                    loginstate: 1
                };
            },
            _ajaxLoginStatus: function(t) {
                var o = function(o) {
                    if (o.loginstate) {
                        if (200 == o.code) return t && t(), !1;
                        swal({
                            title: configs.title,
                            text: o.desc,
                            confirmButtonColor: configs.color,
                            confirmButtonText: "确定"
                        });
                    } else $(".alert").show(), $(".mask").show();
                }, e = function(t) {
                    swal({
                        title: configs.title,
                        text: statusCode[500],
                        confirmButtonColor: configs.color,
                        confirmButtonText: "确定"
                    });
                };
                $.when($.ajax({
                    type: "get",
                    url: "/activity/jnxcz/user/loginStatus",
                    dataType: "json",
                    timeout: "5000"
                }).promise()).then(o, e);
            },
            _ajaxCompanylist: function() {
                var t = function(t) {
                    if (200 == t.code) {
                        var o = template("provinceName_M", t);
                        $("#provinceName").html(o);
                    } else $(".alert").hide(), $(".mask").hide(), swal({
                        title: configs.title,
                        text: t.desc,
                        confirmButtonColor: configs.color,
                        confirmButtonText: "确定"
                    });
                }, o = function(t) {
                    $(".alert").hide(), $(".mask").hide(), swal({
                        title: configs.title,
                        text: statusCode[500],
                        confirmButtonColor: configs.color,
                        confirmButtonText: "确定"
                    });
                };
                $.when($.ajax({
                    type: "post",
                    url: "/activity/jnxcz/companylist",
                    data: {
                        type: this.init().companyType
                    },
                    dataType: "json",
                    timeout: "5000"
                }).promise()).then(t, o);
            },
            _ajaxUser: function() {
                var t = this, o = function(t) {
                    $(".alert").hide(), $(".mask").hide(), 200 != t.code && swal({
                        title: configs.title,
                        text: t.desc,
                        confirmButtonColor: configs.color,
                        confirmButtonText: "确定"
                    }, function() {
                        $(".alert").show(), $(".mask").show();
                    });
                }, e = function(t) {
                    console.log(t);
                };
                $.when($.ajax({
                    type: "post",
                    url: "/activity/jnxcz/user/EconomyUser",
                    data: window.JSON.stringify(t.init()),
                    contentType: "application/json; charset=utf-8",
                    dataType: "json",
                    timeout: "5000"
                }).promise()).then(o, e);
            }
        }, $(function() {
            !userLogin && user._ajaxCompanylist(), $("span.companyTypes input").on("click", function() {
                user._ajaxCompanylist();
            }), $(".mobile-text").blur(function() {
                /^1[34578]\d{9}$/.test($(this).val()) ? $("input.startVote").removeAttr("disabled") : ($("span.error").show(),
                    $("input.startVote").attr("disabled", "disabled"));
            }).focus(function() {
                $("span.error").hide();
            }).keyup(function() {
                /^1[34578]\d{9}$/.test($(this).val()) ? $("input.startVote").removeAttr("disabled") : $("input.startVote").attr("disabled", "disabled");
            }), $(".close").click(function() {
                $(".alert").hide(), $(".mask").hide();
            }), $(".startVote").click(function() {
                user._ajaxUser();
            });
        });
    }
}, [ 6 ]);