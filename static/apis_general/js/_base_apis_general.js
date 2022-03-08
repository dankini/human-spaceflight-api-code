$(document).ready(function () {
    //Pagination numbers
    $('#paginationSimpleNumbers').DataTable({
        "pagingType": "simple_numbers",
        "ordering": false // false to disable sorting (or any other option)
    });
});