function copyURL() {

    const shortURL = document.querySelector(".short-link a").href;

    navigator.clipboard.writeText(shortURL)
        .then(function() {

            document.getElementById("copy-message").innerText =
                "URL copied successfully!";

        })
        .catch(function() {

            document.getElementById("copy-message").innerText =
                "Unable to copy URL.";

        });

}