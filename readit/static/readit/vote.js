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

async function vote(e) {
        e.preventDefault();
        
        let url = this.getAttribute("data-url");
        let response = await fetch(url, {
                method: "POST",
                headers: {'X-CSRFToken': csrftoken},
        });
        if (!response.ok) {
                console.error("fetch failed");
                console.error(response.status);
        }
        let text = await response.text();
        console.log(text);

        let element = this.parentNode;
        let voteElement = element.getElementsByClassName("vote-count")[0];
        let voteCount = Number(voteElement.textContent);
        console.log(this);
        if (this.classList.contains("upvote")) {
                voteCount++;
        } else if (this.classList.contains("downvote")) {
                voteCount--;
        }
        voteElement.textContent = voteCount;

        let as = element.getElementsByTagName("a");
        Array.from(as).forEach(v => {
                v.classList.remove("done");
        })
        
        this.classList.add("done");
}

var upvotes = document.getElementsByClassName("upvote");
Array.from(upvotes).forEach(v => {
        v.addEventListener("click", vote);
});

var downvotes = document.getElementsByClassName("downvote");
Array.from(downvotes).forEach(v => {
        v.addEventListener("click", vote);
});
