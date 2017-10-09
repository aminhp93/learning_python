$(document).ready(function() {
    var simplemde = new SimpleMDE({
        element: document.getElementById("post_content"),
        placeholder: 'Markdown syntax is supported. Click  for Help <br>Click  or press "Ctrl + P" to toggle Preview mode Click  or press "F9" to toggle Side by Side Preview mode Click  or press "F11" to toggle Fullscreen mode',
        tabSize: 4,
        toolbar: [
        //     {
        //         name: "redText",
        //         action: function customCode(editor) {
        //             var cm = editor.codemirror;
        //             var output = '';
        //             var selectedText = cm.getSelection();
        //             var text = selectedText || 'placeholder';
        //             output = '!!' + text + '!!';
        //             cm.replaceSelection(output);
        //             cm.addClass("customized-code");
        //         },
        //         className: "fa fa-etsy",
        //         title: "Red text (Ctrl/Cmd-Alt-R)",
        //     },
            "bold", "italic", "strikethrough", "heading", "heading-smaller", "heading-bigger", "heading-1", "heading-2", "heading-3", "|", "code", "quote", "unordered-list", "ordered-list", "clean-block", "link", "image", "table", "horizontal-rule", "|", "preview", "side-by-side", "fullscreen", "guide", "redText"
        ],
        toolbarTips: true,
    });

    $("#query").autocomplete({
        source: [],
        select: function(event, ui) {
            event.preventDefault();
            $("#query").val(ui.item.label);
            window.location.href = ui.item.value;
        },
        focus: function(event, ui) {
            $("#query").val(ui.item.label);
        },
        minLength: 0,
        delay: 500,
    });

    $("input#query").keyup(function() {
        var query = $(this).val();
        if (query.length > 0) {
            dataString = 'q=' + query;
            $.ajax({
                type: "GET",
                url: "/api/posts/",
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json',
                },
                data: dataString,
                success: function(response) {
                    var availableHints = [];
                    for (var i in response.results) {
                        // console.log(response.results[i])
                        availableHints.push({
                            label: response.results[i].title.replace(/\s+/g, "-"),
                        }, {
                            label: response.results[i].content,
                        });
                    }
                    $("#query").autocomplete({
                        source: availableHints,
                    });
                }
            });
        }
    });
})