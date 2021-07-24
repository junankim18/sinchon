const toggleBtn = document.querySelector('.navbar_toggleBtn');
const menu = document.querySelector('.navbar_menu');
const icons = document.querySelector('.navbar_icons');

toggleBtn.addEventListener('click', () => {
    menu.classList.toggle('active');
    icons.classList.toggle('active');
});



const OtherBtn = document.querySelector('.others');
const big_box2 = document.querySelector('.big_box2');
const MyBtn = document.querySelector('.my');
const big_box = document.querySelector('.big_box');

OtherBtn.addEventListener('click', () => {
    big_box2.classList.toggle('active');
    big_box.classList.toggle("inactive");
    
});

MyBtn.addEventListener('click', () => {
    big_box2.classList.toggle('inactive');
    big_box.classList.toggle('active');
    
});

