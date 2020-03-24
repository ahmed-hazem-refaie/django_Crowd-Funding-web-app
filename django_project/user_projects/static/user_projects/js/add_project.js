// Add project form validation
$("#submit").prop("disabled", true);

// Validat project title input ==> Just characters a-z and A-Z
$("input[name=project_title]").focusout(function() {
    if (/^[a-z A-Z]+$/.test($(this).val()) == false) {
        $("#titleError").text("Project Title must be characters ONLY.!");
        $(this).removeClass("is-valid");
        $(this).addClass("is-invalid");
    } else {
        $(this).removeClass("is-invalid");
        $(this).addClass("is-valid");
        $("#titleError").text("");
        enableSubmit();
    }
});

$("select[name=project_category]").on("change", function() {
    if ($("select[name=project_category] :selected").val() === "Choose...") {
        $("#categoryError").text("You must select Category for your project..");
        $(this).removeClass("is-valid");
        $(this).addClass("is-invalid");
    } else {
        $(this).removeClass("is-invalid");
        $(this).addClass("is-valid");
        $("#categoryError").text("");
        enableSubmit();
    }
});

$("input[name=project_total_target]").focusout(function() {
    if (/^[0-9]+$/.test($(this).val()) == false) {
        $("#targetError").text("your target must be more than 1. only numbers");
        $(this).removeClass("is-valid");
        $(this).addClass("is-invalid");
    } else {
        $(this).removeClass("is-invalid");
        $(this).addClass("is-valid");
        $("#targetError").text("");
        enableSubmit();
    }
});

$("input[name=project_start_date]").on("change", function() {
    if (new Date($("input[name=project_start_date]").val()) < new Date()) {
        $("#startError").text("Project must be start after today");
        $(this).removeClass("is-valid");
        $(this).addClass("is-invalid");
    } else {
        $(this).removeClass("is-invalid");
        $(this).addClass("is-valid");
        $("#startError").text("");
        enableSubmit();
    }
});

$("input[name=project_end_date]").on("change", function() {
    if (
        new Date($("input[name=project_end_date]").val()) <
        new Date($("input[name=project_start_date]").val())
    ) {
        $("#endError").text("End Date must be after start date");
        $(this).removeClass("is-valid");
        $(this).addClass("is-invalid");
    } else {
        $(this).removeClass("is-invalid");
        $(this).addClass("is-valid");
        $("#endError").text("");
        enableSubmit();
    }
});

$("#tags").focusout(function() {
    if ($("#tags").val().length < 1) {
        $("#tagsError").text("add at least One tag");
        $(this).removeClass("is-valid");
        $(this).addClass("is-invalid");
    } else {
        $(this).removeClass("is-invalid");
        $(this).addClass("is-valid");
        $("#tagsError").text("");
        enableSubmit();
    }
});

$("#projectImages").focusout(function() {
    if ($("#projectImages").val().length < 1) {
        $("#imagesError").text("This field is requird*");
        $(this).removeClass("is-valid");
        $(this).addClass("is-invalid");
    } else {
        $(this).removeClass("is-invalid");
        $(this).addClass("is-valid");
        $("#imagesError").text("");
        enableSubmit();
    }
});

$("textarea[name=project_description]").focusout(function() {
    if (/^[a-z A-Z %$@!.&*,~'"()-+/0-9]+$/.test($(this).val()) == false) {
        $("#detailsError").text(
            "Please add description to your projects [just characters, numbers and (% $ @ ! . & * , ~ '\" ( ) - + / )] "
        );
        $(this).removeClass("is-valid");
        $(this).addClass("is-invalid");
    } else {
        $(this).removeClass("is-invalid");
        $(this).addClass("is-valid");
        $("#detailsError").text("");
        enableSubmit();
    }
});

function enableSubmit() {
    if (
        $("input[name=project_title]").hasClass("is-valid") &&
        $("select[name=project_category]").hasClass("is-valid") &&
        $("input[name=project_total_target]").hasClass("is-valid") &&
        $("input[name=project_start_date]").hasClass("is-valid") &&
        $("input[name=project_end_date]").hasClass("is-valid") &&
        $("#tags").val().length > 0 &&
        $("#projectImages").hasClass("is-valid") &&
        $("textarea[name=project_description]").hasClass("is-valid")
    ) {
        // check validation
        $("#submitMessage").text("Submit Now...");
        $("#submit").prop("disabled", false);
    }
}

/* Comment Ajax Call */
// $("#reply").on("click", function() {
//     $.ajax({
//         url: "http://localhost:8000/comments/reply",
//         method: "post",
//         contentType: "Application/json",
//         data: JSON.stringify($("#replyForm").serialize()),
//         dataType: "text",
//         success(data) {
//             console.log("ok");
//         },
//         error(error) {
//             console.log(error);
//         }
//     });
// });
