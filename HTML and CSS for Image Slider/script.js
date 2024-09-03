let currentSlide = 0;
const slides = document.querySelectorAll(".slide");
const totalSlides = slides.length;
const slideInfo = document.getElementById("slide-info");

document.getElementById("next").addEventListener("click", function() {
    changeSlide(1);
});

document.getElementById("prev").addEventListener("click", function() {
    changeSlide(-1);
});

function changeSlide(direction) {
    slides[currentSlide].classList.remove("active");
    currentSlide = (currentSlide + direction + totalSlides) % totalSlides;
    slides[currentSlide].classList.add("active");
    updateSlideInfo();
}

function updateSlideInfo() {
    slideInfo.textContent = `Изображение ${currentSlide + 1} из ${totalSlides}`;
}

updateSlideInfo();
