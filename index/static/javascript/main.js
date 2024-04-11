let currentSection = 0;
const sections = document.querySelectorAll('.section');
const totalSections = sections.length;
let isScrolling = false; 

function updateSections(direction) {
  if (isScrolling) return; // Bloque le défilement si une transition est déjà en cours
  isScrolling = true;

  currentSection += direction;
  currentSection = Math.max(0, Math.min(currentSection, sections.length - 1));

  sections.forEach((section, index) => {
    section.style.transform = index === currentSection ? 'translateY(0)' : 'translateY(100vh)';
  });

  // Attend la fin de la transition avant de permettre un nouveau défilement
  setTimeout(() => isScrolling = false, 1000); // Assurez-vous que ce délai correspond à la durée de votre transition CSS
}

// Écoute les événements de défilement
window.addEventListener('wheel', (e) => {
  if (e.deltaY > 0) updateSections(1); // Défilement vers le bas
  if (e.deltaY < 0) updateSections(-1); // Défilement vers le haut
});
