alias md2docx-short='pandoc "$1" --defaults=~/pandoc/profiles/docx-short.yaml -o "${1%.md}.docx"'
alias md2docx-long='pandoc "$1" --defaults=~/pandoc/profiles/docx-long.yaml -o "${1%.md}.docx"'
alias md2pdf-long='pandoc "$1" --defaults=~/pandoc/profiles/pdf-long.yaml -o "${1%.md}.pdf"'
