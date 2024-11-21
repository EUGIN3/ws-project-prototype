// Navbar scroll effect
window.addEventListener('scroll', () => {
  const navbar = document.querySelector('.navbar');
  const backToTop = document.querySelector('.back-to-top');
  if (window.scrollY > 50) {
    navbar.classList.add('scrolled');
    backToTop.classList.add('visible');
  } else {
    navbar.classList.remove('scrolled');
    backToTop.classList.remove('visible');
  }
});

// Smooth scroll for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function (e) {
    e.preventDefault();
    const targetId = this.getAttribute('href').slice(1);
    const targetElement = document.getElementById(targetId);
    if (targetElement) {
      const navbarHeight = document.querySelector('.navbar').offsetHeight;
      const targetPosition = targetElement.getBoundingClientRect().top + window.pageYOffset - navbarHeight;
      window.scrollTo({
        top: targetPosition,
        behavior: 'smooth'
      });
    } else if (targetId === 'top') {
      window.scrollTo({
        top: 0,
        behavior: 'smooth'
      });
    }
  });
});

// Lazy loading images
document.addEventListener("DOMContentLoaded", function () {
  var lazyImages = [].slice.call(document.querySelectorAll("img.lazy"));

  if ("IntersectionObserver" in window) {
    let lazyImageObserver = new IntersectionObserver(function (entries, observer) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          let lazyImage = entry.target;
          lazyImage.src = lazyImage.dataset.src;
          lazyImage.classList.remove("lazy");
          lazyImageObserver.unobserve(lazyImage);
        }
      });
    });

    lazyImages.forEach(function (lazyImage) {
      lazyImageObserver.observe(lazyImage);
    });
  }
});

// Mobile menu toggle
const menuToggle = document.querySelector('.menu-toggle');
const navLinks = document.querySelector('.nav-links');

menuToggle.addEventListener('click', () => {
  navLinks.classList.toggle('active');
});

// Close menu when a link is clicked
navLinks.querySelectorAll('a').forEach(link => {
  link.addEventListener('click', () => {
    navLinks.classList.remove('active');
  });
});

// Close menu when clicking outside
document.addEventListener('click', (event) => {
  if (!event.target.closest('.navbar')) {
    navLinks.classList.remove('active');
  }
});

// Scroll animations
const animateOnScroll = () => {
  const sections = document.querySelectorAll('.content-section');
  const productCards = document.querySelectorAll('.product-card');
  const footerSections = document.querySelectorAll('.footer-section');

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
      }
    });
  }, { threshold: 0.1 });

  sections.forEach(section => observer.observe(section));
  productCards.forEach(card => observer.observe(card));
  footerSections.forEach(section => observer.observe(section));
};

// Run animations on load and scroll
window.addEventListener('load', animateOnScroll);
window.addEventListener('scroll', animateOnScroll);

// Parallax effect for hero section
window.addEventListener('scroll', () => {
  const scrollPosition = window.pageYOffset;
  document.querySelector('.hero').style.backgroundPositionY = scrollPosition * 0.7 + 'px';
});