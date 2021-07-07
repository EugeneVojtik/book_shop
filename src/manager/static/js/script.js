$('document').ready(function (){
    $('.like_comment').on('click', function() {
        let id=$(this).attr('id');
        console.log('added_like', id);

        $.ajax(
        {
        url:'/books/add_like2comment_ajax',
        data: {'comment_id': id.split('-')[1]},
        method: 'GET',
        success: function (data) {
            $(`#${id}`).html("Likes: " + data['likes']);
        }
        });
});
    $('.delete_comment').on('click', function() {

        let id = $(this).attr('id');

        $.ajax(
        {
         url: '/books/delete_comment_ajax',
         data: {'comment_id': id.split('-')[1]},
         method: 'GET',
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

