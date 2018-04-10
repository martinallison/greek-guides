(function(document) {
    /**
     * Reeeaaaally rough way of wiring up the speaker buttons to playing the correct
     * audio files.
     */
    var audioButtons = document.querySelectorAll("[data-play]");
    var audioElements = document.querySelectorAll("audio");

    audioElements.forEach(function(el) {
        /**
         * For each audio element, if it has a corresponding button, replace it with
         * an ear emoji while the audio plays, switching it back to the button when
         * the audio is done.
         */
        var ear = document.createElement("span");
        ear.innerText = "👂";

        var button = document.querySelector("[data-play='" + el.id + "'");

        if (!!button) {
            el.addEventListener("playing", function() {
                button.classList.add("hide");
                ear = button.parentNode.appendChild(ear);
            });
            el.addEventListener("ended", function() {
                button.classList.remove("hide");
                ear = button.parentNode.removeChild(ear);
            });
        }
    });

    audioButtons.forEach(function(el) {
        /**
         * Hook up each 'button' to play the corresponding audio.
         */
        el.addEventListener("click", function(e) {
            e.preventDefault();
            var audio = document.getElementById(el.dataset.play);

            if (!!audio) {
                audio.play();
            }
        });
    });
}(document));