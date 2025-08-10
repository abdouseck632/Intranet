document.addEventListener('DOMContentLoaded', function() {
    // Animation des cartes PDF
    const pdfCards = document.querySelectorAll('.pdf-card');
    pdfCards.forEach((card, index) => {
        card.style.animationDelay = (0.1 * index) + 's';
        card.classList.add('animate-card');
    });
    
    // Initialisation du carousel
    const myCarousel = new bootstrap.Carousel(document.getElementById('labCarousel'), {
        interval: 5000,
        wrap: true
    });
    
    // Gestion de la déconnexion
    
    
    // Initialisation des tooltips
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });
});

document.addEventListener('DOMContentLoaded', function() {
    const currentPath = window.location.pathname;
    document.querySelectorAll('.nav-link').forEach(link => {
        if (link.getAttribute('href') === currentPath) {
            link.classList.add('active');
        }
    });
});