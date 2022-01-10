$(document).ready(function () {
    showArticles();
});

function openClose() {
    if ($("#post-box").css("display") == "block") {
        $("#post-box").hide();
        $("#btn-post-box").text("포스팅 박스 열기");
    } else {
        $("#post-box").show();
        $("#btn-post-box").text("포스팅 박스 닫기");
    }
}


function postArticle() {
    $.ajax({
        type: "POST",
        url: "/memo",
        data: {sample_give: '샘플데이터'},
        success: function (response) { // 성공하면
            alert(response["msg"]);
        }
    })
}

function showArticles() {
    $.ajax({
        type: "GET",
        url: "/memo?sample_give=샘플데이터",
        data: {},
        success: function (response) {
            alert(response["msg"]);
        }
    })
}