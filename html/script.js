//* Current Time Getter
function getTime() {
    const now = new Date();
    return now.toLocaleTimeString([], {hour: '2-digit', minute:'2-digit'});
}

function updateTime() {
    document.getElementById('timeDisplay').textContent = getTime();
}

updateTime();
setInterval(updateTime, 1000);

//* Update Checker
async function callPython() {
    let result = await eel.update()();
    document.getElementById('output').innerText = result;
}

//* Menu toggle
const themeToggle = document.getElementById('switch');
const body = document.body;

// Check for saved theme preference or use system preference
const savedTheme = localStorage.getItem('theme') || 
                 (window.matchMedia('(prefers-color-scheme: light)').matches ? 'light' : 'dark');

// Apply saved theme
if (savedTheme === 'light') {
    body.classList.add('light-theme');
    themeToggle.checked = false; // Switch is off for light theme
} else {
    body.classList.remove('light-theme');
    themeToggle.checked = true; // Switch is on for dark theme
}

// Handle theme toggle
themeToggle.addEventListener('change', function() {
    if (this.checked) {
        body.classList.remove('light-theme');
        localStorage.setItem('theme', 'dark');
    } else {
        body.classList.add('light-theme');
        localStorage.setItem('theme', 'light');
    }
});

// Close menu when clicking outside
document.addEventListener('click', function(event) {
    const menuContainer = document.querySelector('.menu-container');
    const burger = document.getElementById('burger');
    
    if (!menuContainer.contains(event.target) && burger.checked) {
        burger.checked = false;
    }
});

document.getElementById('burger').addEventListener('change', function() {
    const menu = document.querySelector('.slide-out-menu');
    if (this.checked) {
        menu.style.transform = 'translateY(0)';
        menu.style.opacity = '1';
        menu.style.visibility = 'visible';
    } else {
        menu.style.transform = 'translateY(-20px)';
        menu.style.opacity = '0';
        menu.style.visibility = 'hidden';
    }
});

window.matchMedia('(prefers-color-scheme: light)').addEventListener('change', e => {
    if (!localStorage.getItem('theme')) { // Only if user hasn't set preference
        if (e.matches) {
            body.classList.add('light-theme');
            themeToggle.checked = false;
        } else {
            body.classList.remove('light-theme');
            themeToggle.checked = true;
        }
    }
});

document.addEventListener('DOMContentLoaded', function() {
    const burger = document.getElementById('burger');
    const menu = document.querySelector('.slide-out-menu');
    
    // Force close the menu
    burger.checked = false;
    menu.style.transform = 'translateY(-20px)';
    menu.style.opacity = '0';
    menu.style.visibility = 'hidden';
    
    // Then add your existing change listener
    burger.addEventListener('change', function() {
        if (this.checked) {
            menu.style.transform = 'translateY(0)';
            menu.style.opacity = '1';
            menu.style.visibility = 'visible';
        } else {
            menu.style.transform = 'translateY(-20px)';
            menu.style.opacity = '0';
            menu.style.visibility = 'hidden';
        }
    });
});