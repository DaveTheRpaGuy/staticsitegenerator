import shutil
import os
import re
import sys

from textnode import TextNode, TextType
from htmlnode import HTMLNode
from markdown_html import markdown_to_html_node

#How to start local server:
#python3 src/main.py
#cd public && python3 -m http.server 8888

def main():
    basepath = sys.argv[0]
    if not basepath:
        basepath = "/"

    static_path = "static"
    public_path = "docs"
    content_path = "content"
    
    copy_to(static_path, public_path)
    generate_pages_recursively(content_path, "template.html", public_path, basepath)
    
def copy_to(source, destination):
    if os.path.exists(source) == False:
        raise Exception("Source location does not exist")
    if os.path.exists(destination):
        shutil.rmtree(destination)
    os.mkdir(destination)
    dir_contents = os.listdir(source)
    for name in dir_contents:
        source_path = os.path.join(source, name)
        destination_path = os.path.join(destination, name)
        if os.path.isfile(source_path):
            shutil.copy(source_path, destination_path)
            continue
        copy_to(source_path, destination_path)
        
def extract_title(markdown):
    matches = re.findall(r'^#.*$', markdown, re.M)
    if len(matches) == 0:
        raise Exception("Could not find heading 1")
    heading_one_text = re.sub(r'^#', '', matches[0].strip()).strip()
    return heading_one_text

def generate_pages_recursively(dir_path_content, template_path, dest_dir_path, basepath):
    if os.path.exists(dest_dir_path) == False:
        os.mkdir(dest_dir_path)
    dir_contents = os.listdir(dir_path_content)
    for name in dir_contents:
        source_path = os.path.join(dir_path_content, name)
        destination_path = os.path.join(dest_dir_path, name)
        if os.path.isfile(source_path):
            generate_page(source_path, template_path, destination_path.replace('.md', '.html'), basepath)
            continue
        generate_pages_recursively(source_path, template_path, destination_path, basepath)

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    from_file_contents = read_file(from_path)
    template_file_contents = read_file(template_path)
    node = markdown_to_html_node(from_file_contents)
    html = node.to_html()
    title = extract_title(from_file_contents)
    full_html = template_file_contents.replace("{{ Title }}", title).replace("{{ Content }}", html)
    full_html = full_html.replace('href="/', 'href="{BASEPATH}').replace('src="/', 'src="{BASEPATH}')
    create_file(dest_path, full_html)

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        file_contents = file.read()
    return file_contents

def create_file(file_path, file_contents):
    with open(file_path, "x", encoding='utf-8') as file:
        file.write(file_contents)

main()