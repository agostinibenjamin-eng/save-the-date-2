# Save the Date — Flora & Benjamin · 27 Août 2026
## Version 2 — Avatars famille animés au scroll

---

## Contexte du projet

Site web "Save the Date" narratif pour le mariage de **Flora & Benjamin**, le **27 août 2026**.
La page raconte leur histoire en faisant **apparaître les personnages un par un au scroll**.
À la fin, toute la famille se **transforme en tenues de mariage** (crossfade).

Fichier de sortie : `index.html` (HTML + CSS + JS inline, zéro dépendance)

---

## Stack technique

- Un seul fichier : `index.html`
- Pure HTML5 / CSS3 / JavaScript vanilla
- Zero dépendances, zero frameworks, zero build tools
- Google Fonts via `<link>` dans `<head>`
- Assets images dans le dossier `assets/` (même dossier que index.html)

---

## Identité visuelle

| Élément | Valeur |
|---|---|
| Fond principal | `#0a0a0f` (noir profond) |
| Or champagne | `#c9a84c` |
| Ivoire | `#f5f0e8` |
| Or doux | `#e8d5a3` |
| Font titres | Cormorant Garamond (300, italic) |
| Font dates | Cinzel (400, 700) |
| Font corps | EB Garamond (400) |

---

## Assets disponibles dans `assets/`

### Personnages — tenues normales (PNG fond transparent)
| Fichier | Personnage | Rôle dans la narration |
|---|---|---|
| `isaac_famille.png` | Isaac | Fils, né 11/10/2020 — apparaît en chapitre IV |
| `flora_famille.png` | Flora | Mariée, maman — présente dès la rencontre (2005) |
| `hannah_famille.png` | Hannah | Fille aînée, née 08/05/2018 — apparaît en chapitre III |
| `benjamin_famille.png` | Benjamin | Marié, papa — présent dès la rencontre (2005) |
| `eve_famille.png` | Eve | Fille cadette, née 18/02/2023 — apparaît en chapitre V |

### Personnages — tenues de mariage (PNG fond transparent)
| Fichier | Description |
|---|---|
| `isaac_mariage.png` | Isaac en smoking noir nœud papillon |
| `flora_mariage.png` | Flora en robe de mariée blanche + voile |
| `hannah_mariage.png` | Hannah avec tiare, robe de cérémonie |
| `benjamin_mariage.png` | Benjamin en smoking noir nœud papillon, boutonnière blanche |
| `eve_mariage.png` | Eve en robe blanche, nœud blanc dans les cheveux |

### Images de groupe
| Fichier | Usage |
|---|---|
| `groupe_famille.png` | Vue complète famille (900×600px, fond transparent) |
| `groupe_mariage.png` | Vue complète famille en tenues mariage (900×600px, fond transparent) |

---

## Données personnelles

```
Mariés      : Flora & Benjamin
Date        : 27 Août 2026
Format romain : 27 · VIII · MMXXVI
Lieu        : À annoncer
Monogramme  : F & B
```

---

## Timeline narrative et apparition des personnages

| # | Date | Chapitre | Personnages présents | Nouveaux arrivants |
|---|------|----------|---------------------|--------------------|
| Hero | — | Save the Date | — | Silhouettes fantômes de tous |
| I | 9 mars 2005 | La Rencontre | Flora + Benjamin | Flora (depuis la gauche) + Benjamin (depuis la droite) |
| II | 2013 | Luxembourg | Flora + Benjamin | — (même groupe, nouveau décor) |
| III | 8 mai 2018 | Hannah | Flora + Benjamin + Hannah | Hannah descend du haut entre ses parents |
| IV | 11 oct. 2020 | Isaac | Flora + Benjamin + Hannah + Isaac | Isaac glisse depuis la gauche |
| V | 18 fév. 2023 | Eve | Toute la famille | Eve glisse depuis la droite |
| Bridge | — | Tension | Toute la famille en silhouette sombre | — |
| FINALE | 27 Août 2026 | Le Mariage | Tenues de mariage | Crossfade famille → mariage |

---

## Architecture HTML — Scène de famille centrale

La scène de famille est **positionnée en sticky** : elle reste visible pendant tout le scroll.
Les personnages sont des `<img>` absolus qui s'animent via classes CSS.

```html
<section class="family-stage-wrapper"> <!-- height: 600vh -->
  <div class="family-stage"> <!-- sticky top:0, height:100vh -->

    <!-- Fond / contexte (change par chapitre) -->
    <div class="stage-bg" id="stage-bg"></div>

    <!-- Label du chapitre courant -->
    <div class="chapter-label" id="chapter-label"></div>

    <!-- Les 5 personnages tenues normales -->
    <div class="characters-container" id="chars-famille">
      <img class="character" id="char-isaac"    src="assets/isaac_famille.png"    data-name="Isaac">
      <img class="character" id="char-flora"    src="assets/flora_famille.png"    data-name="Flora">
      <img class="character" id="char-hannah"   src="assets/hannah_famille.png"   data-name="Hannah">
      <img class="character" id="char-benjamin" src="assets/benjamin_famille.png" data-name="Benjamin">
      <img class="character" id="char-eve"      src="assets/eve_famille.png"      data-name="Eve">
    </div>

    <!-- Overlays mariage (crossfade final) -->
    <div class="characters-container wedding-overlay" id="wedding-overlay">
      <img class="character" id="wed-isaac"    src="assets/isaac_mariage.png">
      <img class="character" id="wed-flora"    src="assets/flora_mariage.png">
      <img class="character" id="wed-hannah"   src="assets/hannah_mariage.png">
      <img class="character" id="wed-benjamin" src="assets/benjamin_mariage.png">
      <img class="character" id="wed-eve"      src="assets/eve_mariage.png">
    </div>

    <!-- Texte narratif de la scène -->
    <div class="scene-text" id="scene-text"></div>

    <!-- Canvas fireworks finale -->
    <canvas id="fireworks-canvas"></canvas>

  </div>
</section>
```

---

## Positions CSS des personnages

```css
.characters-container {
  position: absolute;
  bottom: 8%;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  align-items: flex-end;
  justify-content: center;
  width: clamp(400px, 70vw, 750px);
}

.character {
  height: clamp(200px, 35vh, 380px);
  width: auto;
  object-fit: contain;
  flex-shrink: 0;
  transition: opacity 1.2s cubic-bezier(0.16,1,0.3,1),
              transform 1.2s cubic-bezier(0.16,1,0.3,1),
              filter 1s ease;
  will-change: transform, opacity;
  margin: 0 -8px; /* léger overlap comme dans l'illustration */
}

/* Ordre gauche → droite : Isaac, Flora, Hannah, Benjamin, Eve */
#char-isaac, #wed-isaac       { order: 1; }
#char-flora, #wed-flora       { order: 2; }
#char-hannah, #wed-hannah     { order: 3; }
#char-benjamin, #wed-benjamin { order: 4; }
#char-eve, #wed-eve           { order: 5; }
```

---

## États CSS des personnages

```css
/* Caché à gauche */
.char-hidden-left  { opacity: 0 !important; transform: translateX(-150px) scale(0.8) !important; }
/* Caché à droite */
.char-hidden-right { opacity: 0 !important; transform: translateX(150px) scale(0.8) !important; }
/* Caché en haut */
.char-hidden-top   { opacity: 0 !important; transform: translateY(-120px) scale(0.85) !important; }
/* Fantôme (visible mais très estompé + n/b) */
.char-ghost        { opacity: 0.07 !important; filter: grayscale(100%) !important; transform: scale(0.93) !important; }
/* Actif */
.char-visible      { opacity: 1 !important; transform: translateX(0) translateY(0) scale(1) !important; filter: none !important; }

/* Overlay mariage */
.wedding-overlay {
  position: absolute;
  bottom: 8%;
  left: 50%;
  transform: translateX(-50%);
  opacity: 0;
  transition: opacity 2.5s ease;
  pointer-events: none;
}
.wedding-overlay.crossfade-active { opacity: 1; }
```

---

## Moteur de scroll JS

```javascript
const chapters = [
  {
    progress: [0, 0.15],
    id: 'hero',
    ghost: ['isaac','flora','hannah','benjamin','eve'],
    visible: [],
    text: { label: '', date: '', narrative: 'Il était une fois…' },
    bg: 'stars'
  },
  {
    progress: [0.15, 0.30],
    id: 'rencontre',
    ghost: ['hannah','isaac','eve'],
    visible: ['flora','benjamin'],
    enterFrom: { flora: 'left', benjamin: 'right' },
    text: { label: 'I · La Rencontre', date: '9 mars 2005', narrative: 'Parmi tous les chemins possibles, deux trajectoires se croisent.' },
    bg: 'stars'
  },
  {
    progress: [0.30, 0.45],
    id: 'luxembourg',
    ghost: ['hannah','isaac','eve'],
    visible: ['flora','benjamin'],
    text: { label: 'II · Une Nouvelle Vie', date: '2013', narrative: 'Une ville, un nouveau chapitre. Luxembourg devient leur monde.' },
    bg: 'city'
  },
  {
    progress: [0.45, 0.60],
    id: 'hannah',
    ghost: ['isaac','eve'],
    visible: ['flora','benjamin','hannah'],
    enterFrom: { hannah: 'top' },
    text: { label: 'III · Hannah', date: '8 mai 2018', narrative: 'Et puis il y eut de la lumière. Hannah entre dans le monde.' },
    bg: 'warm'
  },
  {
    progress: [0.60, 0.72],
    id: 'isaac',
    ghost: ['eve'],
    visible: ['flora','benjamin','hannah','isaac'],
    enterFrom: { isaac: 'left' },
    text: { label: 'IV · Isaac', date: '11 octobre 2020', narrative: 'La famille grandit. Isaac apporte sa propre lumière.' },
    bg: 'warm'
  },
  {
    progress: [0.72, 0.82],
    id: 'eve',
    ghost: [],
    visible: ['flora','benjamin','hannah','isaac','eve'],
    enterFrom: { eve: 'right' },
    text: { label: 'V · Eve', date: '18 février 2023', narrative: 'La dernière pièce du puzzle. Complète. Parfaite.' },
    bg: 'warm'
  },
  {
    progress: [0.82, 0.90],
    id: 'bridge',
    ghost: [],
    visible: ['flora','benjamin','hannah','isaac','eve'],
    dim: true,
    text: { label: '', date: '', narrative: 'Et maintenant… après 21 ans…' },
    bg: 'dark'
  },
  {
    progress: [0.90, 1.0],
    id: 'finale',
    wedding: true,
    text: { label: 'Le Mariage · Enfin', date: '27 Août 2026', narrative: 'Flora & Benjamin' },
    bg: 'gold'
  }
];

// Dans le scroll handler :
function updateScene(progress) {
  const chapter = chapters.find(c => progress >= c.progress[0] && progress < c.progress[1])
                  || chapters[chapters.length - 1];
  
  const allChars = ['isaac','flora','hannah','benjamin','eve'];
  
  allChars.forEach(name => {
    const el = document.getElementById('char-' + name);
    el.className = 'character';
    
    if (chapter.wedding) {
      el.classList.add('char-visible');
    } else if (chapter.ghost && chapter.ghost.includes(name)) {
      el.classList.add('char-ghost');
    } else if (chapter.visible && chapter.visible.includes(name)) {
      el.classList.add('char-visible');
    } else {
      // Caché hors écran (position initiale selon enterFrom)
      const enterFrom = chapter.enterFrom && chapter.enterFrom[name];
      if (enterFrom === 'left')  el.classList.add('char-hidden-left');
      else if (enterFrom === 'right') el.classList.add('char-hidden-right');
      else if (enterFrom === 'top')   el.classList.add('char-hidden-top');
      else el.classList.add('char-hidden-left'); // fallback
    }
  });
  
  // Crossfade mariage
  const weddingOverlay = document.getElementById('wedding-overlay');
  if (chapter.wedding) {
    weddingOverlay.classList.add('crossfade-active');
    triggerFireworks(); // canvas particles
  } else {
    weddingOverlay.classList.remove('crossfade-active');
  }
  
  // Mettre à jour le texte
  updateSceneText(chapter.text);
  
  // Mettre à jour le fond
  updateBackground(chapter.bg);
}
```

---

## Texte narratif de scène

```css
.scene-text {
  position: absolute;
  top: 6%;
  left: 50%;
  transform: translateX(-50%);
  text-align: center;
  z-index: 20;
  pointer-events: none;
  width: 90%;
  max-width: 600px;
}
.scene-label {
  font-family: 'Cinzel', serif;
  font-size: clamp(0.6rem, 1.2vw, 0.85rem);
  color: #c9a84c;
  letter-spacing: 0.5em;
  text-transform: uppercase;
  margin-bottom: 0.4rem;
  opacity: 0;
  transition: opacity 0.8s ease;
}
.scene-date-display {
  font-family: 'Cormorant Garamond', serif;
  font-style: italic;
  font-size: clamp(1.8rem, 4.5vw, 3.5rem);
  color: #f5f0e8;
  line-height: 1.1;
  opacity: 0;
  transform: translateY(15px);
  transition: opacity 0.9s ease, transform 0.9s cubic-bezier(0.16,1,0.3,1);
}
.scene-narrative {
  font-family: 'EB Garamond', serif;
  font-size: clamp(0.85rem, 1.6vw, 1.1rem);
  color: rgba(245,240,232,0.6);
  margin-top: 0.6rem;
  opacity: 0;
  transition: opacity 1s ease 0.3s;
}
.scene-text.active .scene-label,
.scene-text.active .scene-date-display,
.scene-text.active .scene-narrative { opacity: 1; transform: translateY(0); }
```

---

## Finale — Révélation complète (progress 0.90+)

Quand le crossfade mariage est actif, afficher en overlay centré :

```
1. Flash doré (div plein écran, radial-gradient, opacity 0→0.5→0, duration 1s)
2. Canvas fireworks : 300 particules or/ivoire depuis le centre
3. Texte de révélation (remplace le texte de scène normal) :
   - "Flora & Benjamin" — Cormorant italic, clamp(2rem,5vw,4.5rem), ivoire
   - Ligne or qui se dessine depuis le centre vers les deux côtés
   - "27 Août 2026" — Cinzel 700, clamp(3rem,9vw,8rem), or champagne
     Chaque caractère fait un rotateY 90deg→0deg staggeré (60ms apart)
   - "Le Mariage · Enfin" — Cormorant italic, small, letter-spacing 0.5em
   - "Lieu à annoncer · L'annonce arrive bientôt…" — petit, italic, opacity 0.5
```

---

## Canvas Fireworks

```javascript
class Particle {
  constructor(x, y) {
    this.x = x; this.y = y;
    this.vx = (Math.random() - 0.5) * 14;
    this.vy = (Math.random() - 0.5) * 14 - 4;
    this.alpha = 1;
    this.size = Math.random() * 3.5 + 0.5;
    this.color = ['#c9a84c','#f5f0e8','#ffffff','#e8d5a3','#d4af6a'][Math.floor(Math.random()*5)];
    this.gravity = 0.18;
    this.decay = 0.012 + Math.random() * 0.012;
  }
  update() {
    this.x += this.vx; this.y += this.vy;
    this.vy += this.gravity; this.alpha -= this.decay; this.vx *= 0.99;
  }
  draw(ctx) {
    ctx.globalAlpha = Math.max(0, this.alpha);
    ctx.fillStyle = this.color;
    ctx.beginPath();
    ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
    ctx.fill();
  }
}

let particles = [];
let animFrame;
function triggerFireworks() {
  if (particles.length > 0) return; // n'activer qu'une fois
  const canvas = document.getElementById('fireworks-canvas');
  const ctx = canvas.getContext('2d');
  canvas.width = window.innerWidth;
  canvas.height = window.innerHeight;
  const cx = canvas.width / 2, cy = canvas.height * 0.45;
  for (let i = 0; i < 300; i++) particles.push(new Particle(cx, cy));
  function animate() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    particles = particles.filter(p => p.alpha > 0);
    particles.forEach(p => { p.update(); p.draw(ctx); });
    if (particles.length > 0) animFrame = requestAnimationFrame(animate);
    else { ctx.globalAlpha = 0; }
  }
  animate();
}
```

---

## Anneau 3D Hero (CSS)

```css
.ring-3d {
  width: clamp(150px, 20vw, 220px);
  height: clamp(150px, 20vw, 220px);
  border: 1.5px solid rgba(201,168,76,0.35);
  border-radius: 50%;
  transform-style: preserve-3d;
  animation: ring-spin 20s linear infinite;
  position: absolute;
  top: 50%; left: 50%;
  transform-origin: center;
}
.ring-3d::before {
  content: '';
  position: absolute;
  inset: 18px;
  border: 1px solid rgba(201,168,76,0.2);
  border-radius: 50%;
}
@keyframes ring-spin {
  from { transform: translate(-50%,-50%) rotateX(70deg) rotateZ(0deg); }
  to   { transform: translate(-50%,-50%) rotateX(70deg) rotateZ(360deg); }
}
```

---

## Responsive

```css
@media (max-width: 768px) {
  .character { height: clamp(140px, 26vh, 240px); }
  .characters-container { width: 95vw; }
}
```

- Mobile : 150 particules fireworks au lieu de 300
- Réduire margin négatif overlap à -4px sur mobile

---

## Fonts

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700&family=Cormorant+Garamond:ital,wght@0,300;1,300;1,400&family=EB+Garamond:ital@0;1&display=swap" rel="stylesheet">
```

---

## Structure des fichiers

```
save-the-date/
├── index.html              ← fichier unique à générer
├── CLAUDE.md               ← spécifications (ce fichier)
├── PROMPT.md               ← prompt de génération
└── assets/
    ├── isaac_famille.png
    ├── flora_famille.png
    ├── hannah_famille.png
    ├── benjamin_famille.png
    ├── eve_famille.png
    ├── isaac_mariage.png
    ├── flora_mariage.png
    ├── hannah_mariage.png
    ├── benjamin_mariage.png
    ├── eve_mariage.png
    ├── groupe_famille.png
    └── groupe_mariage.png
```
