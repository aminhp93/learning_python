$("#id_q").select2({
    ajax: {
        url: "/search/autocomplete",
        dataType: 'json',
        delay: 250,
        data: function(params) {
            return {
                q: params.term, // search term
                page: params.page
            };
        },
        processResults: function(data, params) {
            return {
                results: data.suggestions
            };
        },
        cache: true
    },
    placeholder: 'What are you looking for?',
    escapeMarkup: function(markup) { return markup; }, // let our custom formatter work
    minimumInputLength: 1,
    templateResult: formatRepo,
    templateSelection: formatRepoSelection
});

function formatRepo(repo) {
    if (repo.loading) {
        return repo.text;
    }

    var markup =
        '<a style="text-decoration:none" href="/posts/' + repo.slug + '">' + "<span style='font-weight:bold; color:black'>" + repo.title + "</span>" + "<br>" +
        "<span style='color:grey'>" + repo.date + "</span>" + "<br>" +
        "<span style='color:black'>" + repo.highlighted + "</span>" + '</a>' + "<hr>";

    return markup;
}

function formatRepoSelection(repo) {
    return repo.text;
}