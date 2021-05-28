let form = document.querySelector('.popup-container');
let container = document.querySelector('.full-container');

function openForm() {
    form.classList.add('active');
    container.classList.add('active');
}
  
function closeForm() {
    form.classList.remove('active');
    container.classList.remove('active');
}