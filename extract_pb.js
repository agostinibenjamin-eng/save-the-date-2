const fs = require('fs');
const filePath = 'C:\\Users\\benja\\.gemini\\antigravity\\conversations\\8e4e9b1f-4c3b-435c-bda3-54aae8f30bfe.pb';
try {
    const buffer = fs.readFileSync(filePath);
    const content = buffer.toString('utf8');
    
    const searchString = 'm 2005.5513,2055.4548';
    const index = content.indexOf(searchString);
    if (index !== -1) {
        // Assume string goes until a known ending or a quote.
        let endIdx = content.indexOf('"', index);
        if (endIdx === -1) endIdx = index + 10000;
        let sub = content.substring(index, endIdx);
        // Clean up the trailing escape characters if any
        if (sub.endsWith('\\')) sub = sub.slice(0, -1);
        fs.writeFileSync('heart_path.txt', sub, 'utf8');
        console.log('Success! Found snippet of length ' + sub.length);
    } else {
        console.log('Absolutely not found.');
    }
} catch (e) {
    console.error(e);
}
