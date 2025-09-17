document.addEventListener("DOMContentLoaded", () => {
    const texts = document.querySelectorAll('.typed-text');
    const speed = 50; // typing speed
    const delayBetweenLoops = 1500; // pause before repeating

    function typeAll() {
        let index = 0;

        function typeLine(span) {
            const text = span.getAttribute('data-text');
            span.textContent = "";
            let i = 0;

            function typeChar() {
                if (i < text.length) {
                    span.textContent += text.charAt(i);
                    i++;
                    setTimeout(typeChar, speed);
                } else {
                    index++;
                    if (index < texts.length) {
                        typeLine(texts[index]);
                    } else {
                        // After all lines typed, wait then loop
                        setTimeout(() => typeAll(), delayBetweenLoops);
                    }
                }
            }
            typeChar();
        }

        typeLine(texts[0]);
    }

    typeAll();
});
