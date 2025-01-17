document.getElementById('subBtn').addEventListener('click', (e) => {
    e.preventDefault();

    const isMovie = document.getElementById("movie").checked;
    const isYT = document.getElementById("youtube").checked;
    const isBook = document.getElementById("book").checked;
    const isOther = document.getElementById("other").checked;
    const type = document.getElementById("type").value;

    const title = document.getElementById("titel").value;
    const description = document.getElementById("desc").value;

    const reflect = document.getElementById("reflect").value;
    const love = document.getElementById("love").value;
    const hate = document.getElementById("hate").value;
    const lesson = document.getElementById("lesson").value;

    const insights = document.getElementById("insights").value;
    const change = document.getElementById("change").value;

    const data = {
        isMovie: isMovie,
        isYT: isYT,
        isBook: isBook,
        isOther: isOther,
        type: type,
        title: title,
        description: description,
        reflect: reflect,
        love: love,
        hate: hate,
        lesson: lesson,
        insights: insights,
        change: change
    };

    fetch('/sub_form', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(result => {
        console.log('Success:', result);
        alert('Content Evaluation Submitted Successfully!');
    })
    .catch(error => {
        console.error('Error:', error);
        alert('An error occurred. Please try again.');
    });

    Array.from(document.getElementsByTagName("form")).forEach((form) => {
        form.reset();
    });
});

