// script.js
document.addEventListener('DOMContentLoaded', function() {
    const productCards = document.querySelectorAll('.product-card');
    productCards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            card.style.transform = 'scale(1.05)';
        });
        card.addEventListener('mouseleave', function() {
            card.style.transform = 'scale(1)';
        });
    });
});
