// // $(document).ready(function () {
// //     showMovie();
// // });
//
// function golist(type) {
//     let menuType = (type)
//     $.ajax({
//         type: "GET",
//         url: `/list?type=${menuType}`,
//         data: {},
//         success: function (response) { // 성공하면
//              console.log(response["movie_list"]);
//             let current = response["movie_list"]
//             for (let i = 0; i <= 10; i++){
//                 let title = current[i]['title']
//                 let img = current[i]['img']
//                 let kinds = current[i]['kinds']
//                 let director = current[i]['director']
//                 let temp_html =
//                     `<div class="movie-list">
//                         <a class="list-img" href="{{url_for('search')}}"><img src="${img}"></a>
//                         <div class="list-cont">
//                             <div class="movie-name">
//                                 <span class="movie-age">15</span><span class="movie-tit">${title}</span>
//                             </div>
//                             <div class="summary">
//                                 <span class="title">개요</span><span class="text">${kinds}</span>
//                             </div>
//                             <div class="director">
//                                 <span class="title">감독</span><span class="text">${director}</span>
//                             </div>
//                             <div class="actor">
//                                 <span class="title">출연</span><span class="text">
//                                 배우없는 영화있어!! 크롤링 안돼! 나이제한도!! none나와서 못했어!!! 으악ㄱㄱ</span>
//                             </div>
//                             <div class="contents">
//                                 <span class="title">줄거리</span>
//                                 <p class="text"></p>
//                             </div>
//                         </div>
//                         <button class="list-like">
//                             <i class="fas fa-heart"></i>
//                             <span>1</span>
//                         </button>
//                     </div>`
//             $('.movie-listBox').append(temp_html)
//             }
//         }
//     })
// }
//
