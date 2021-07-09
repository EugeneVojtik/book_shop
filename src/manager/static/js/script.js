function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

$('document').ready(function (){
    $('.like_comment').on('click', function() {
        let id=$(this).attr('id');
        let current_id = id.split('-')[1];
        console.log('added_like', id);

        $.ajax(
        {
        url:`/books/add_like2comment_ajax/${current_id}`,
        headers:{'X-CSRFToken': csrftoken},
        method: 'PUT',
        success: function (data) {
            $(`#${id}`).html("Likes: " + data['likes']);
        }
        });
});
    $('.delete_comment').on('click', function() {

        let id = $(this).attr('id');
        let comment_id = id.split('-')[1];
        $.ajax(
        {
         url: `/books/delete_comment_ajax/${comment_id}`,
         headers: {'X-CSRFToken': csrftoken},
         method: 'DELETE',
         success: function (data) {
         $(`#${id}`).remove();
         }
        });

    });


    $('span').on('click', function (){
    let id = $(this).attr('id');
    rate = id.split(' ')[1];
    book = id.split(' ')[2];
    console.log('you have tapped book rating', rate, book);
    $.ajax(
        {
         url: '/books/add_rate_ajax',
         data: {'rate': rate, 'book_slug': book},
         method: 'GET',
         success: function (data) {
         $('.book_rating').html('Rating:' + data['rating']);
         $('.block-rating').load('.block-rating');
         }
        });
    });
});

