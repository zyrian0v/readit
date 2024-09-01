function upvote(e) {
        console.log("upvote")
}

function downvote(e) {
        console.log("downvote")
}

var upvotes = document.getElementsByClassName("upvote");
Array.from(upvotes).forEach(v => {
        v.addEventListener("click", upvote);
});

var downvotes = document.getElementsByClassName("downvote");
Array.from(downvotes).forEach(v => {
        v.addEventListener("click", downvote);
});
