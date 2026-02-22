const fs = require('fs');
const path = require('path');

const brainDir = 'C:\\Users\\benja\\.gemini\\antigravity\\brain\\8e4e9b1f-4c3b-435c-bda3-54aae8f30bfe';
let foundPath = null;

function searchDir(dir) {
    if (foundPath) return;
    const files = fs.readdirSync(dir);
    for (const file of files) {
        const fullPath = path.join(dir, file);
        const stat = fs.statSync(fullPath);
        if (stat.isDirectory()) {
            searchDir(fullPath);
        } else if (file.endsWith('.txt') || file.endsWith('.md')) {
            try {
                const content = fs.readFileSync(fullPath, 'utf8');
                const match = content.match(/d=\"(m 2005\.5513,2055\.454[\s\S]+?)\"/);
                if (match) {
                    foundPath = match[1];
                    console.log('Found path in', fullPath);
                    return;
                }
            } catch (e) {}
        }
    }
}

searchDir(brainDir);

if (foundPath) {
    fs.writeFileSync('heart_path_extracted.txt', foundPath, 'utf8');
    console.log('Path exported!');
} else {
    console.log('Path not found!');
}
