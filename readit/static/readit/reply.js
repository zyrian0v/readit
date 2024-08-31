function reply(e) {
        e.preventDefault();
        let comment_id = this.getAttribute("data-comment");
        let form = document.getElementById("reply_"+comment_id)
        if (form.style.display == "block") {
                form.style.display = "none";
        } else {
                form.style.display = "block";
        }
}

var reply_buttons = document.getElementsByClassName("reply");
Array.from(reply_buttons).forEach(v => {
        v.addEventListener("click", reply);
});
