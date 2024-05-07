document.addEventListener('DOMContentLoaded', function() {
    const themeSwitch = document.getElementById('theme-switch');
    const body = document.body;
    const header = document.querySelector('header');
    const footer = document.querySelector('footer');
    const sections = document.querySelectorAll('section');

    themeSwitch.addEventListener('change', function() {
        if (this.checked) {
            body.classList.add('dark-mode');
            header.classList.add('dark-mode');
            footer.classList.add('dark-mode');
            sections.forEach(section => section.classList.add('dark-mode'));
        } else {
            body.classList.remove('dark-mode');
            header.classList.remove('dark-mode');
            footer.classList.remove('dark-mode');
            sections.forEach(section => section.classList.remove('dark-mode'));
        }
    });
});
