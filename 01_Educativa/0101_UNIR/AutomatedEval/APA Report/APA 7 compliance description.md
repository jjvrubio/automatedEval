We have to analyse the bibliography in a thesis to check its conformace to APA 7 format. 

The idea is extract the text in chapter named "VII. REFERENCIAS BIBLIOGRAFICAS " till the end of the document, or next chapter found, and convert that into a markdown text. 

§ represents the word paragraph.

Rules for parsing and analyzing:

1. PDF files contains plenty of 'artifacts' that poses a challenge to properly convert the contents to a markdown file.
2. The PDF file is formatted in columns.
3. The language of the text is Spanish. Accentuaded or diacrital symbols have to be considered.
4. Chapters in the document are noted by starting with either:
   1.  roman or arabic numerals  and uppercase words ending in '.'. 
   2. subchapters, follow the same protocol but a re compose of two numbers separated by a '.'.
   3. Biblography chapters names uses: bibliografía, referencias, referencias bibliográficas. And are separated by blank space to the numeral.
   4. After that it goes a new paragraph.

5. § start with uppercase Proper Noun.
6. Every § has 1 and only 1 reference.
7. Many references are containing this structure: "Recuperado de"  followed by a blank, else a colon and a blank which is followed by an URL. 
8. The URL ends either on a blank space, or a dot plus a blank space. This marks the end of the currect paragraph and reference.
9. The word "Recuperado" and the subsequent URL always forming part of  the same paragraph.

Then, using the markdown format -or file-. A python program has to:

1. evaluate the compliance with APA 7 format standard the references extracted from the bibliography chapter.
2.  Once properly identified all the references, it has to check those used all are cited properly.
3. Identified those references not cited in the text. 

The thesis is written in Spanish, another challenge. 

When analysis and reasoning for improving code alwasy review the potential impacts to the rest of the code.

In the case above, the processing logic and sequence  should be mantained unless it appears sensible reasons to opt otherwise.