# Prompt — Save the Date Flora & Benjamin
## Version 2 · Avatars animés au scroll · Pour Gemini 3 Pro (Antigravity)

> **Instructions** : Copie le bloc complet ci-dessous et colle-le dans Antigravity / Gemini.
> Place ce fichier et `CLAUDE.md` à la racine du projet. Le dossier `assets/` contient déjà tous les PNG.

---

```
Lis attentivement le fichier CLAUDE.md avant de commencer. Il contient toutes les spécifications techniques, les données personnelles, et les chemins des assets.

## Mission

Crée `index.html` : un site "Save the Date" de mariage de niveau studio — un seul fichier HTML avec CSS et JavaScript inline, aucune dépendance externe sauf Google Fonts.

---

## Concept central

La page est une **scène de théâtre** : une zone centrale montre la famille Flora & Benjamin. En scrollant, les membres de la famille **apparaissent progressivement**, racontant 21 ans d'histoire commune. À la fin, toute la famille se **transforme en tenues de mariage** via un crossfade spectaculaire.

---

## Structure de la page

### 1. HERO — "Save the Date" (100vh)

Fond `#0a0a0f`. Contenu centré. Auto-animé au chargement.

**Anneau 3D CSS** (voir spec dans CLAUDE.md) — positionné en arrière-plan, centré.

**Particules flottantes** : 50 `<span class="particle">` positionnés aléatoirement via CSS custom properties `--px`, `--py`, `--pdur`, `--pdelay`. Animation : flottement vers le haut, opacity 0.1–0.3, tailles 2–5px, couleur `#c9a84c`.

**Texte central** (animations CSS staggerées, `animation-fill-mode: both`) :
- `"Save the Date"` — Cormorant Garamond italic 300, `clamp(2rem,5vw,4rem)`, ivoire `#f5f0e8`, chaque lettre dans un `<span>`, apparaît de bas en haut, stagger 50ms, débute à 0.5s
- Ligne or horizontale : `width: 0 → 60%`, height 1px, or `#c9a84c`, débute à 1.5s, durée 1.2s
- `"27 · VIII · MMXXVI"` — Cinzel 700, `clamp(2.5rem,7vw,6rem)`, or `#c9a84c`, translateY(20px)→0 + blur(6px)→0, débute à 2s

**Indicateur scroll** en bas : `"Notre Histoire ↓"`, Cinzel petit, or, pulsation scale 1↔1.2 infinite.

---

### 2. SCÈNE NARRATIVE — La Vie de Flora & Benjamin (600vh wrapper)

C'est le cœur du site. **Lire CLAUDE.md section "Architecture HTML — Scène de famille centrale"** pour le HTML exact.

**Principe :**
- Le wrapper `<section class="family-stage-wrapper">` fait `height: 600vh`
- À l'intérieur : `<div class="family-stage">` en `position: sticky; top: 0; height: 100vh`
- Pendant ces 600vh de scroll, la scène reste fixe et évolue

**JS de scroll :**
```javascript
const wrapper = document.querySelector('.family-stage-wrapper');
window.addEventListener('scroll', () => {
  const rect = wrapper.getBoundingClientRect();
  const totalScrollable = wrapper.offsetHeight - window.innerHeight;
  const scrolled = -rect.top;
  const progress = Math.max(0, Math.min(1, scrolled / totalScrollable));
  updateScene(progress);
}, { passive: true });
```

**Implémenter exactement la logique `updateScene(progress)`** décrite dans CLAUDE.md avec les 8 chapitres et leurs plages de progress.

**Transitions de personnages :**
Chaque personnage (`<img>` avec fond transparent) utilise les classes CSS d'état définies dans CLAUDE.md :
- `.char-hidden-left` / `.char-hidden-right` / `.char-hidden-top` : off-screen, opacity 0
- `.char-ghost` : opacity 0.07, filter grayscale, scale 0.93 — fantôme suggérant le futur
- `.char-visible` : opacity 1, transform none — personnage pleinement présent

**La transition entre états est fluide** grâce au `transition` CSS de 1.2s sur `.character`.

**Texte narratif** : zone `.scene-text` en haut de la scène. À chaque changement de chapitre, le contenu change avec un fade out/in (0.4s). Afficher : label du chapitre (Cinzel, or, letter-spacing), date (Cormorant italic, large, ivoire), texte narratif (EB Garamond, opacity 0.6).

**Backgrounds de scène** (CSS classes sur `#stage-bg`) :
- `bg-stars` : radial-gradient doux, or, + 30 pseudo-étoiles CSS (box-shadow technique)
- `bg-city` : skyline minimaliste CSS en bas (barres verticales or, scaleY animées)
- `bg-warm` : gradient chaud légèrement rosé-doré au centre
- `bg-dark` : fond très sombre, quasi noir
- `bg-gold` : aura radiale or depuis le centre + particules canvas fireworks

---

### 3. FINALE — L'Explosion (dans la scène, progress 0.90+)

Quand `progress >= 0.90` :

**Étape 1 — Flash** : div `#flash-overlay` plein écran, `background: radial-gradient(circle, rgba(201,168,76,0.5), transparent)`, opacity 0→0.6→0 en 1.2s, une seule fois.

**Étape 2 — Crossfade mariage** : `#wedding-overlay` passe à `opacity: 1` via la classe `.crossfade-active` (transition CSS 2.5s). Les avatars mariage apparaissent par-dessus les avatars normaux.

**Étape 3 — Fireworks canvas** : déclencher `triggerFireworks()` (voir spec CLAUDE.md). Canvas plein écran, z-index 15, pointer-events none. 300 particules or/ivoire depuis le centre.

**Étape 4 — Texte de révélation** (remplace le texte de scène normal, z-index 25) :
```
"Flora & Benjamin"
— ligne or qui s'étend depuis le centre (deux moitiés, chacune width 0→30%, transition 1.2s)
"27 Août 2026" — Cinzel 700, clamp(3rem,9vw,8rem), #c9a84c
   Chaque caractère span, rotateY(90deg)→rotateY(0), translateZ(30px)→0, stagger 55ms
"Le Mariage · Enfin" — Cormorant italic, letter-spacing 0.5em, opacity 0→1 (délai 1.5s)
"Lieu à annoncer" + pin SVG pulsant + "L'annonce arrive bientôt…"
```

**Aura fond finale** : 5 divs `.nebula-orb` positionnés aléatoirement, `filter: blur(90px)`, couleurs or/ivoire très faibles (opacity 0.05-0.08), animation de dérive lente (30–50s loops).

---

### 4. FOOTER (50vh)

Fond `#0a0a0f`. Centré verticalement.
- Ligne or fine (40% width, centered, margin auto)
- `"Invitation formelle à suivre"` — Cormorant italic, opacity 0.65
- `"Réservez cette date · 27 · 08 · 2026"` — Cinzel, or, letter-spacing 0.3em
- Monogramme `"F & B"` dans cercle (border or, 50px, Cinzel)
- Bouton scroll-to-top `↑` : border or, hover: fond or/10, transition douce

---

## CSS Global obligatoire

```css
:root {
  --bg: #0a0a0f;
  --gold: #c9a84c;
  --ivory: #f5f0e8;
  --gold-soft: #e8d5a3;
  --ease: cubic-bezier(0.16, 1, 0.3, 1);
  --ease-spring: cubic-bezier(0.34, 1.56, 0.64, 1);
}
*, *::before, *::after { margin: 0; padding: 0; box-sizing: border-box; }
html { scroll-behavior: smooth; }
body { background: var(--bg); color: var(--ivory); overflow-x: hidden; font-family: 'EB Garamond', serif; }
```

---

## Contraintes techniques impératives

1. **Un seul fichier** `index.html` — tout CSS dans `<style>`, tout JS dans `<script>` avant `</body>`
2. **Images** : toutes dans `assets/` avec les noms exacts listés dans CLAUDE.md
3. **Animations** : uniquement `transform` et `opacity` pour les performances (GPU compositing)
4. **`will-change: transform`** sur tous les éléments animés au scroll
5. **`passive: true`** sur tous les scroll listeners
6. **Jamais de `margin-top` pour positionner** — utiliser `transform: translateY()`
7. **Toutes les tailles** en `clamp(min, vw, max)` pour le responsive
8. **Canvas fireworks** : `requestAnimationFrame`, stopper quand tous les particles sont alpha ≤ 0

---

## Responsive (mobile < 768px)

- `character` height : `clamp(140px, 26vh, 240px)`
- Fireworks : 150 particles (détecter `window.innerWidth < 768`)
- Font-sizes plus petites dans les clamp()
- Hero : réduire nombre de particles à 25

---

## Qualité attendue

Ce site doit ressembler à ce qu'un studio de création numérique haut de gamme produirait pour une campagne de luxe. Chaque transition doit être fluide, chaque typographie parfaitement espacée, chaque animation intentionnelle et élégante.

C'est l'histoire de 21 ans d'amour, de 3 enfants, et d'un mariage qui était écrit depuis le début.
Fais-le sentir.
```

---

## Checklist avant livraison

- [ ] `index.html` ouvre dans le navigateur sans serveur
- [ ] Scroll fluide à travers les 8 chapitres
- [ ] Flora et Benjamin apparaissent au chapitre I (depuis gauche/droite)
- [ ] Hannah apparaît depuis le haut au chapitre III
- [ ] Isaac apparaît depuis la gauche au chapitre IV
- [ ] Eve apparaît depuis la droite au chapitre V
- [ ] Crossfade vers tenues de mariage au chapitre FINALE
- [ ] Fireworks canvas se déclenche une seule fois
- [ ] "27 Août 2026" apparaît lettre par lettre avec rotation 3D
- [ ] Responsive mobile fonctionnel
- [ ] Aucune erreur console
