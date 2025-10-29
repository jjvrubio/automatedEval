
#!/bin/zsh

# Define the source and destination directories
SOURCE_DIR="/Users/juanjo/Library/Mobile Documents/iCloud~md~obsidian/Documents/METIS"
DEST_DIR="/Users/juanjo/Library/CloudStorage/OneDrive-KALEIDAGEOGRAFIAS&MERCADOSSL/The Octavius/METIS™ Framework"

# Synchronize from source to destination
# rsync -av --update "$SOURCE_DIR/" "$DEST_DIR/"

# Synchronize from destination to source
rsync -av --update "$DEST_DIR/" "$SOURCE_DIR/"
