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
    console.log(targetId)
    console.log(currentSection)
    if (targetElement.id=="section1" && currentSection==0 ){
      updateSections(1);
    }else if (targetElement.id=="section2" && currentSection==0 ){
      updateSections(2);
    }else if (targetElement.id=="section2" && currentSection==1 ){
      updateSections(1);
    }else if (targetElement.id=="section1" && currentSection==2 ){
      updateSections(-1);
    }else if (targetElement.id=="section3" && currentSection==0 ){
      updateSections(3);
    }else if (targetElement.id=="section3" && currentSection==1 ){
      updateSections(2);
    }else if (targetElement.id=="section3" && currentSection==2 ){
      updateSections(1);
    }else if (targetElement.id=="section1" && currentSection==3 ){
      updateSections(-3);
    }else if (targetElement.id=="section1" && currentSection==3 ){
      updateSections(-2);
    }else if (targetElement.id=="section2" && currentSection==3 ){
      updateSections(-1);
    }
  });
});






window.addEventListener('touchstart', (e) => {
  
}, { passive: true });


window.addEventListener('touchend', (e) => {
  
  

  
  if (deltaY > 0) {
    
    updateSections(1);
  } else if (deltaY < 0) {
    
    updateSections(-1);
  }
}, { passive: true });

