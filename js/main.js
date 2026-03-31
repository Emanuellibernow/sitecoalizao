const revealElements = document.querySelectorAll('.reveal');
const navToggle = document.querySelector('.menu-toggle');
const mainNav = document.querySelector('.main-nav');
const navLinks = document.querySelectorAll('.main-nav a');

const observer = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
      observer.unobserve(entry.target);
    }
  });
}, {
  threshold: 0.18
});

revealElements.forEach((element) => observer.observe(element));

if (navToggle && mainNav) {
  navToggle.addEventListener('click', () => {
    const isOpen = mainNav.classList.toggle('open');
    navToggle.setAttribute('aria-expanded', String(isOpen));
  });

  navLinks.forEach((link) => {
    link.addEventListener('click', () => {
      mainNav.classList.remove('open');
      navToggle.setAttribute('aria-expanded', 'false');
    });
  });
}

// Slider Logic
const slider = document.getElementById('gallerySlider');
const slides = document.querySelectorAll('.gallery-slide');
const prevBtn = document.querySelector('.gallery-btn.prev');
const nextBtn = document.querySelector('.gallery-btn.next');
const dotsContainer = document.getElementById('galleryDots');

if (slider && slides.length > 0) {
  let currentIndex = 0;
  const totalSlides = slides.length;
  let autoplayInterval;

  // Create dots
  slides.forEach((_, index) => {
    const dot = document.createElement('button');
    dot.classList.add('gallery-dot');
    dot.setAttribute('aria-label', `Ir para slide ${index + 1}`);
    if (index === 0) dot.classList.add('active');
    dot.addEventListener('click', () => goToSlide(index));
    dotsContainer.appendChild(dot);
  });

  const dots = document.querySelectorAll('.gallery-dot');

  function updateSlider() {
    slider.style.transform = `translateX(-${currentIndex * 100}%)`;
    dots.forEach((dot, index) => {
      dot.classList.toggle('active', index === currentIndex);
    });
  }

  function goToSlide(index) {
    currentIndex = (index + totalSlides) % totalSlides;
    updateSlider();
    resetAutoplay();
  }

  function nextSlide() {
    goToSlide(currentIndex + 1);
  }

  function prevSlide() {
    goToSlide(currentIndex - 1);
  }

  function startAutoplay() {
    autoplayInterval = setInterval(nextSlide, 7000);
  }

  function resetAutoplay() {
    clearInterval(autoplayInterval);
    startAutoplay();
  }

  if (nextBtn) nextBtn.addEventListener('click', nextSlide);
  if (prevBtn) prevBtn.addEventListener('click', prevSlide);

  // Pause on hover
  slider.parentElement.addEventListener('mouseenter', () => clearInterval(autoplayInterval));
  slider.parentElement.addEventListener('mouseleave', startAutoplay);

  startAutoplay();
}

// Hero Title Carousel Logic
const heroPhrases = document.querySelectorAll('.hero-phrase');
const heroPrevBtn = document.getElementById('heroPrev');
const heroNextBtn = document.getElementById('heroNext');
if (heroPhrases.length > 1) {
  let currentPhrase = 0;
  let heroInterval;

  function switchPhrase(nextIndex) {
    heroPhrases[currentPhrase].classList.remove('phrase-active');
    heroPhrases[currentPhrase].classList.add('phrase-hidden');
    heroPhrases[currentPhrase].style.opacity = '0';
    heroPhrases[currentPhrase].style.pointerEvents = 'none';
    
    currentPhrase = (nextIndex + heroPhrases.length) % heroPhrases.length;
    
    heroPhrases[currentPhrase].classList.remove('phrase-hidden');
    heroPhrases[currentPhrase].classList.add('phrase-active');
    heroPhrases[currentPhrase].style.opacity = '1';
    heroPhrases[currentPhrase].style.pointerEvents = 'auto';
  }

  function nextPhrase() { switchPhrase(currentPhrase + 1); }
  function prevPhrase() { switchPhrase(currentPhrase - 1); }

  function startHeroAutoplay() { heroInterval = setInterval(nextPhrase, 4500); }
  function resetHeroAutoplay() { clearInterval(heroInterval); startHeroAutoplay(); }

  if (heroNextBtn) heroNextBtn.addEventListener('click', () => { nextPhrase(); resetHeroAutoplay(); });
  if (heroPrevBtn) heroPrevBtn.addEventListener('click', () => { prevPhrase(); resetHeroAutoplay(); });

  startHeroAutoplay();
}

// Testimonial Carousel Logic
const testSlider = document.getElementById('testimonialSlider');
const testSlides = document.querySelectorAll('.testimonial-slide');
const testPrevBtn = document.querySelector('.test-btn.prev');
const testNextBtn = document.querySelector('.test-btn.next');
const testDotsContainer = document.getElementById('testimonialDots');

if (testSlider && testSlides.length > 0) {
  let currentTestIndex = 0;
  const totalTestSlides = testSlides.length;
  let testAutoplay;

  testSlides.forEach((_, index) => {
    const dot = document.createElement('button');
    dot.classList.add('gallery-dot');
    dot.setAttribute('aria-label', `Ir para depoimento ${index + 1}`);
    if (index === 0) dot.classList.add('active');
    dot.addEventListener('click', () => goToTestSlide(index));
    testDotsContainer.appendChild(dot);
  });

  const testDots = testDotsContainer.querySelectorAll('.gallery-dot');

  function updateTestSlider() {
    testSlider.style.transform = `translateX(-${currentTestIndex * 100}%)`;
    testDots.forEach((dot, index) => {
      dot.classList.toggle('active', index === currentTestIndex);
    });
  }

  function goToTestSlide(index) {
    currentTestIndex = (index + totalTestSlides) % totalTestSlides;
    updateTestSlider();
    resetTestAutoplay();
  }

  if (testNextBtn) testNextBtn.addEventListener('click', () => goToTestSlide(currentTestIndex + 1));
  if (testPrevBtn) testPrevBtn.addEventListener('click', () => goToTestSlide(currentTestIndex - 1));

  function nextTestSlide() { goToTestSlide(currentTestIndex + 1); }
  
  function startTestAutoplay() {
    testAutoplay = setInterval(nextTestSlide, 6000);
  }
  function resetTestAutoplay() {
    clearInterval(testAutoplay);
    startTestAutoplay();
  }
  
  testSlider.parentElement.addEventListener('mouseenter', () => clearInterval(testAutoplay));
  testSlider.parentElement.addEventListener('mouseleave', startTestAutoplay);
  
  startTestAutoplay();
}
