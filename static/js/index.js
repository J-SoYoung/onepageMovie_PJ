$(document).ready(function () {
    currentList();
    menuList('preMovie');
    reviewShow()
});

function currentList() {
    $.ajax({
        type: "GET",
        url: "/current",
        data: {},
        success: function (response) {
            // console.log(response["current"]);
            let current = response["current"]
            for (let i=0; i <= current.length; i++){
                let title = current[i]['title']
                let url = current[i]['url']
                let img = current[i]['img']
                let temp_html=
                    `<a class="card" href="${url}" target="_blank">
                        <img src="${img}">
                        <sapn>${title}</sapn>
                    </a>`
                $('.movie-current .cardBox').append(temp_html)
            }
        }
    })
}

function menuList(type) {
    let movieType = (type)
    // 페이지 로딩 시 영화목록 초기화
    $('.movie-rank .cardBox').empty();
    $.ajax({
        type: "GET",
        url: `/menuMovie?type=${movieType}`,
        data: {},
        success: function (response) {
           // console.log(response["menu_list"]);
           let memuMovie = (response["menu_list"]);
           for (let i=0; i <= memuMovie.length; i++ ){
               title = memuMovie[i]['title']
               img = memuMovie[i]['img']
               url = memuMovie[i]['url']
               // console.log(title, img, url)
               let temp_html =
                   `<a class="card" href="${url}" target="_blank">
                        <img src="${img}">
                        <sapn>${title}</sapn>
                    </a>`
               $('.movie-rank .cardBox').append(temp_html)
            }
        }
    })
}

function search() {
    let query = $('.searchBar').val()
    // 페이지 로딩 시 영화검색 초기화
    $('.movie-listBox').empty();
    $.ajax({
        type: "GET",
        url: `/search?query_give=${query}`,
        data: {},
        success: function (response) {
            let search = response['search_list'][0]
            // console.log(search);
            let img = search['img']
            let title = search['title']
            let url = search['url']
            // console.log(title, img, url)
            let temp_html =
               `<a class="search-link" href="${url}" target="_blank">
                   <img class="search-img" src="${img}">
                </a>
                <p class="search-tit">${title}</p>`
            $('.input-search').append(temp_html)
        }
    })
}

function reviewSave() {
    let title = $('.search-tit').text()
    let comment = $('.input-text-cont').val()
    let img = $('.search-img').attr('src')

    $.ajax({
        type: "POST",
        url: "/card",
        data: { title_give: title, comment_give: comment, img_give: img },
        success: function (response) { // 성공하면
            alert(response['success']);
            window.location.reload()
        }
    })
}

function reviewShow() {
    $('.input-text-cont').empty();
    $('.searchBar').empty();

    $.ajax({
        type: "GET",
        url: "/review",
        data: {},
        success: function (response) {
            let review = JSON.parse(response['review']);
            for (let i=0; i<=review.length; i++){
                let title = review[i]['title']
                let img= review[i]['img']
                let comment = review[i]['comment']
                // console.log(title,img, comment)
                let temp_html = `
                <div class="review-box">
                    <img class="show-img" src="${img}">
                    <div class="show-textBox">
                        <p class="show-title">${title}</p>
                        <p class="show-comment">${comment}</p>
                    </div>
                    <button class="review-del" onclick="reviewDel('${title}')">del</button>
               </div>`
                $('.review-show').append(temp_html)
            }
        }
    })
}


function reviewDel(title) {
    $.ajax({
        type: "POST",
        url: "/delete",
        data: {title_give: title},
        success: function (response) { // 성공하면
            alert(response['msg']);
            window.location.reload()

        }
    })
}