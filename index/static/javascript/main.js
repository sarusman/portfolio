let currentSection=0;
const sections=document.querySelectorAll('.section');
const totalSections=sections.length;
let isScrolling=false; 

function updateSections(direction) {
  if (isScrolling) return; 
  isScrolling=true;

  currentSection +=direction;
  currentSection=Math.max(0, Math.min(currentSection, sections.length - 1));

  sections.forEach((section, index) => {
    section.style.transform=index === currentSection ? 'translateY(0)' : 'translateY(100vh)';
  });

  
  setTimeout(() => isScrolling=false, 1000); 
}

window.addEventListener('wheel', (e) => {
  if (e.deltaY > 0) updateSections(1); 
  if (e.deltaY < 0) updateSections(-1); 
});


document.querySelectorAll('.nav a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function(e) {
    const targetId = this.getAttribute('href');
    const targetElement = document.querySelector(targetId);
    console.log(targetElement)
    updateSections(1);
  });
});