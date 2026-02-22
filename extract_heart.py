import os
import re

brain_dir = r'C:\Users\benja\.gemini\antigravity\brain\8e4e9b1f-4c3b-435c-bda3-54aae8f30bfe'

path_d = None
# Let's search all recent task logs
for root, dirs, files in os.walk(brain_dir):
    for f in files:
        if f.endswith('.txt') or f.endswith('.md'):
            filepath = os.path.join(root, f)
            try:
                with open(filepath, 'r', encoding='utf-8', errors='ignore') as file:
                    content = file.read()
                    # Find the specific heart svg
                    match = re.search(r'd=\"(m 2005\.5513,2055\.454.+?)\"', content, re.DOTALL)
                    if match:
                        path_d = match.group(1)
                        print('Found path!')
                        break
            except Exception as e:
                pass
    if path_d:
        break

if path_d:
    with open('heart_path_extracted.txt', 'w', encoding='utf-8') as out:
        out.write(path_d)
    print('Path written to heart_path_extracted.txt')
else:
    print('Path not found!')
