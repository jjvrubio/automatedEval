#!/bin/zsh

# Script to remove unnecessary language packages from Microsoft Office apps
# Keeps only Spanish (es), Portuguese (pt), and English (en)
# Compatible with macOS

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Languages to keep (ISO codes)
KEEP_LANGUAGES=("en" "es" "pt" "en_US" "es_ES" "pt_PT")

# Microsoft Office application paths
OFFICE_APPS=(
    "/Applications/Microsoft Word.app"
    "/Applications/Microsoft Excel.app"
    "/Applications/Microsoft PowerPoint.app"
    "/Applications/Microsoft Outlook.app"
    "/Applications/Microsoft OneNote.app"
    "/Applications/Microsoft Teams.app"
)

# Function to check if a language should be kept
should_keep_language() {
    local lang="$1"
    for keep_lang in "${KEEP_LANGUAGES[@]}"; do
        # Exact match or keep_lang is a prefix followed by underscore/dash
        if [[ "$lang" == "$keep_lang" ]] || 
           [[ "$lang" == "${keep_lang}_"* ]] || 
           [[ "$lang" == "${keep_lang}-"* ]]; then
            # Special exclusions for variants we don't want to keep
            if [[ "$lang" == "es_MX" ]] || [[ "$lang" == "pt-BR" ]]; then
                return 1
            fi
            return 0
        fi
    done
    return 1
}

# Function to get confirmation from user
confirm_action() {
    local message="$1"
    echo -e "${YELLOW}$message${NC}"
    read -p "Do you want to continue? (y/N): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        print_warning "Operation cancelled by user"
        return 1
    fi
    return 0
}

# Function to calculate size of directory
get_dir_size() {
    local dir="$1"
    if [[ -d "$dir" ]]; then
        du -sh "$dir" 2>/dev/null | cut -f1
    else
        echo "0B"
    fi
}

# Main function to process Office apps
process_office_apps() {
    local total_removed_size=0
    local apps_processed=0
    
    print_status "Starting Microsoft Office language cleanup..."
    print_status "Keeping languages: ${KEEP_LANGUAGES[*]}"
    
    for app_path in "${OFFICE_APPS[@]}"; do
        if [[ ! -d "$app_path" ]]; then
            print_warning "App not found: $app_path"
            continue
        fi
        
        print_status "Processing: $(basename "$app_path")"
        apps_processed=$((apps_processed + 1))
        
        # Common language pack locations within Office apps
        local lang_dirs=(
            "$app_path/Contents/Resources"
            "$app_path/Contents/SharedSupport"
            "$app_path/Contents/Frameworks"
        )
        
        for base_dir in "${lang_dirs[@]}"; do
            if [[ ! -d "$base_dir" ]]; then
                continue
            fi
            
            # Find .lproj directories (language resource directories)
            while IFS= read -r -d '' lang_dir; do
                local lang_name=$(basename "$lang_dir" .lproj)
                
                # Skip if this language should be kept
                if should_keep_language "$lang_name"; then
                    print_status "  Keeping: $lang_name"
                    continue
                fi
                
                # Calculate size before removal
                local dir_size=$(get_dir_size "$lang_dir")
                
                print_warning "  Removing: $lang_name ($dir_size)"
                
                # Remove the language directory
                if rm -rf "$lang_dir"; then
                    print_success "  Removed: $lang_name"
                else
                    print_error "  Failed to remove: $lang_name"
                fi
                
            done < <(find "$base_dir" -name "*.lproj" -type d -print0 2>/dev/null)
        done
        
        # Also check for language-specific files in other locations
        # Some Office versions store language files differently
        local other_lang_patterns=(
            "$app_path/Contents/Resources/*/Localized"
            "$app_path/Contents/SharedSupport/*/Localized"
        )
        
        for pattern in "${other_lang_patterns[@]}"; do
            for lang_path in $pattern; do
                if [[ -d "$lang_path" ]]; then
                    local parent_dir=$(dirname "$lang_path")
                    local lang_name=$(basename "$parent_dir")
                    
                    if ! should_keep_language "$lang_name"; then
                        local dir_size=$(get_dir_size "$lang_path")
                        print_warning "  Removing localized content: $lang_name ($dir_size)"
                        rm -rf "$lang_path"
                    fi
                fi
            done
        done
        
        echo ""
    done
    
    print_success "Processed $apps_processed Office applications"
}

# Function to backup Office apps (optional)
backup_office() {
    print_status "Creating backup of Office applications..."
    local backup_dir="/Users/$(whoami)/Desktop/Office_Backup_$(date +%Y%m%d_%H%M%S)"
    
    mkdir -p "$backup_dir"
    
    for app_path in "${OFFICE_APPS[@]}"; do
        if [[ -d "$app_path" ]]; then
            print_status "Backing up: $(basename "$app_path")"
            cp -R "$app_path" "$backup_dir/"
        fi
    done
    
    print_success "Backup created at: $backup_dir"
    return 0
}

# Function to show current language packs
show_current_languages() {
    print_status "Current language packs found:"
    echo ""
    
    for app_path in "${OFFICE_APPS[@]}"; do
        if [[ ! -d "$app_path" ]]; then
            continue
        fi
        
        echo "$(basename "$app_path"):"
        
        # Find all .lproj directories
        find "$app_path" -name "*.lproj" -type d 2>/dev/null | while read -r lang_dir; do
            local lang_name=$(basename "$lang_dir" .lproj)
            local dir_size=$(get_dir_size "$lang_dir")
            
            if should_keep_language "$lang_name"; then
                echo -e "  ${GREEN}✓${NC} $lang_name ($dir_size) - KEEP"
            else
                echo -e "  ${RED}✗${NC} $lang_name ($dir_size) - REMOVE"
            fi
        done
        echo ""
    done
}

# Main script execution
main() {
    echo "================================================"
    echo "Microsoft Office Language Pack Cleanup Script"
    echo "================================================"
    echo ""
    
    # Check if running as root (not recommended)
    if [[ $EUID -eq 0 ]]; then
        print_error "This script should not be run as root/sudo"
        exit 1
    fi
    
    # Check if any Office apps are running
    if pgrep -f "Microsoft" > /dev/null; then
        print_error "Microsoft Office applications are currently running."
        print_error "Please close all Office applications before running this script."
        exit 1
    fi
    
    case "${1:-}" in
        "--dry-run"|"-d")
            print_status "Running in dry-run mode (no changes will be made)"
            show_current_languages
            exit 0
            ;;
        "--backup"|"-b")
            if confirm_action "This will create a backup of all Office applications before cleanup."; then
                backup_office
            fi
            ;;
        "--help"|"-h")
            echo "Usage: $0 [OPTIONS]"
            echo ""
            echo "Options:"
            echo "  -d, --dry-run    Show what would be removed without making changes"
            echo "  -b, --backup     Create backup before cleanup"
            echo "  -h, --help       Show this help message"
            echo ""
            echo "Languages that will be kept: ${KEEP_LANGUAGES[*]}"
            exit 0
            ;;
    esac
    
    # Show current state
    show_current_languages
    
    # Confirm before proceeding
    if ! confirm_action "This will permanently remove the language packs marked for removal above."; then
        exit 0
    fi
    
    # Process Office applications
    process_office_apps
    
    print_success "Language cleanup completed!"
    print_status "You may need to restart Office applications for changes to take effect."
    
    echo ""
    echo "================================================"
    echo "Cleanup Summary:"
    echo "- Kept languages: ${KEEP_LANGUAGES[*]}"
    echo "- Processed Office applications"
    echo "- Restart Office apps to see changes"
    echo "================================================"
}

# Run main function with all arguments
main "$@"