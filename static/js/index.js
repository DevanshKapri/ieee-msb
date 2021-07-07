document.addEventListener('DOMContentLoaded', function () {
    const btn = document.querySelectorAll('.toggle-btn-mobile')[0];
    const navList = document.querySelectorAll('.navbar-list')[0];

    btn.addEventListener('click', function () {
        navList.classList.toggle('show-navbar');
    });

});

document.addEventListener('DOMContentLoaded', function () {
    const navList = document.querySelectorAll('.navbar-list')[0];

    navList.addEventListener('click', function () {
        navList.classList.toggle('show-navbar');
    });

});

document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('#about-modal')[0].addEventListener('click', function() {
        document.querySelectorAll('.bg-modal')[0].style.display='flex';
        document.querySelectorAll('body')[0].style.overflow='hidden';
    });

});

document.addEventListener('DOMContentLoaded', function () {
    document.querySelector('.close').addEventListener('click', function() {
        document.querySelector('.bg-modal').style.display = 'none';
        document.querySelectorAll('body')[0].style.overflow='auto';
    });

});

document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('#view-button')[0].addEventListener('click', function() {
        document.querySelectorAll('.table-box')[0].classList.toggle('table-show');
    });

});