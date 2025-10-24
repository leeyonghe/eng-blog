#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Add meta descriptions to posts that don't have them
Extracts first 150 characters from content after <!--more--> tag
"""

import os
import re
from pathlib import Path

def extract_description(content):
    """Extract description from post content"""
    # Remove front matter
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            body = parts[2]
        else:
            body = content
    else:
        body = content
    
    # Find content after <!--more--> or use beginning
    if '<!--more-->' in body:
        body = body.split('<!--more-->', 1)[1]
    
    # Clean up the text
    body = re.sub(r'#+\s*', '', body)  # Remove markdown headers
    body = re.sub(r'\*\*([^*]+)\*\*', r'\1', body)  # Remove bold
    body = re.sub(r'\*([^*]+)\*', r'\1', body)  # Remove italic
    body = re.sub(r'`([^`]+)`', r'\1', body)  # Remove code
    body = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', body)  # Remove links
    body = re.sub(r'\n+', ' ', body)  # Replace newlines with spaces
    body = re.sub(r'\s+', ' ', body)  # Normalize spaces
    body = body.strip()
    
    # Extract first 150 characters
    if len(body) > 150:
        # Try to cut at word boundary
        desc = body[:150]
        last_space = desc.rfind(' ')
        if last_space > 100:  # If we can find a good breaking point
            desc = desc[:last_space]
        desc = desc.strip() + '...'
    else:
        desc = body
    
    return desc

def add_description_to_post(filepath):
    """Add description to post front matter if not present"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if not content.startswith('---'):
        return False
    
    parts = content.split('---', 2)
    if len(parts) < 3:
        return False
    
    front_matter = parts[1]
    body = parts[2]
    
    # Check if description already exists
    if 'description:' in front_matter:
        return False
    
    # Extract description
    description = extract_description(body)
    if not description:
        return False
    
    # Add description to front matter
    lines = front_matter.split('\n')
    new_lines = []
    
    for line in lines:
        new_lines.append(line)
        # Add description after title
        if line.startswith('title:'):
            new_lines.append(f'description: "{description}"')
    
    new_front_matter = '\n'.join(new_lines)
    new_content = f"---{new_front_matter}---{body}"
    
    # Write back to file
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    return True

def main():
    posts_dir = Path('_posts')
    if not posts_dir.exists():
        print("_posts directory not found")
        return
    
    updated_count = 0
    total_count = 0
    
    for post_file in posts_dir.glob('*.md'):
        total_count += 1
        try:
            if add_description_to_post(post_file):
                print(f"✅ Added description to: {post_file.name}")
                updated_count += 1
            else:
                print(f"⏭️  Skipped (already has description): {post_file.name}")
        except Exception as e:
            print(f"❌ Error processing {post_file.name}: {e}")
    
    print(f"\n📊 Summary:")
    print(f"Total posts: {total_count}")
    print(f"Updated posts: {updated_count}")
    print(f"Already had descriptions: {total_count - updated_count}")

if __name__ == "__main__":
    main()