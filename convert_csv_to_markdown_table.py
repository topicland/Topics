#!/usr/bin/env python3

import os

def csv_to_markdown(csv_file_path, markdown_file_path):
    markdown_table = ""

    with open(csv_file_path, 'r') as file:
        lines = file.readlines()

        for i, line in enumerate(lines):
            if i == 0:
                markdown_table += "| topic | name | alias | note | weight |\n" 
                markdown_table += "| ----- | ---- | ----- | ---- | ------ |\n"
            else:
                columns = line.strip().split(',')
                markdown_table += "| {} | {} | | {} | {} |\n".format(columns[0],columns[1],columns[3],columns[2])

    with open(markdown_file_path, 'w') as md_file:
        md_file.write(markdown_table)

def relations_csv_to_markdown(csv_file_path, markdown_file_path):
    markdown_table = ""

    with open(csv_file_path, 'r') as file:
        lines = file.readlines()

        for i, line in enumerate(lines):
            if i == 0:
                markdown_table += "| topic | source | target | relation | note |\n" 
                markdown_table += "| ----- | ------ | ------ | -------- | ---- |\n"
            else:
                columns = line.strip().split(',')
                markdown_table += '| ' + ' | '.join(columns) + ' |\n'

    with open(markdown_file_path, 'w') as md_file:
        md_file.write(markdown_table)


def groups_csv_to_markdown(csv_file_path, markdown_file_path):
    markdown_table = ""

    with open(csv_file_path, 'r') as file:
        lines = file.readlines()

        for i, line in enumerate(lines):
            if i == 0:
                markdown_table += "| topic | group_name | character_name |\n" 
                markdown_table += "| ----- | ---------- | -------------- |\n"
            else:
                columns = line.strip().split(',')
                markdown_table += '| ' + ' | '.join(columns) + ' |\n'

    with open(markdown_file_path, 'w') as md_file:
        md_file.write(markdown_table)

def mainlines_csv_to_markdown(csv_file_path, markdown_file_path):
    markdown_table = ""

    with open(csv_file_path, 'r') as file:
        lines = file.readlines()

        for i, line in enumerate(lines):
            if i == 0:
                markdown_table += "| topic | branch | event | note | previous | final |\n" 
                markdown_table += "| ----- | ------ | ------| ---- | -------- | ----- |\n"
            else:
                columns = line.strip().split(',')
                markdown_table += '| ' + ' | '.join(columns) + ' |\n'

    with open(markdown_file_path, 'w') as md_file:
        md_file.write(markdown_table)

def test():
  csv_file_path = './1Q84/characters.csv'
  markdown_file_path = './1Q84/characters.md'
  csv_to_markdown(csv_file_path, markdown_file_path)

def test_relations():
    csv_file_path = './1Q84/relations.csv'
    markdown_file_path = './1Q84/relations.md'
    relations_csv_to_markdown(csv_file_path, markdown_file_path)


def get_subdirectories(path='.'):
    return [d for d in os.listdir(path) 
            if os.path.isdir(os.path.join(path, d)) and not d.startswith('.')]

current_directory = '.'
subdirectories = get_subdirectories(current_directory)

for topic in subdirectories:
    #print(topic)
    """
    csv_file_path = './{}/characters.csv'.format(topic)
    markdown_file_path = './{}/characters.md'.format(topic)
    csv_to_markdown(csv_file_path, markdown_file_path)


    csv_file_path = './{}/relations.csv'.format(topic)
    markdown_file_path = './{}/relations.md'.format(topic)
    relations_csv_to_markdown(csv_file_path, markdown_file_path)
    

    csv_file_path = './{}/groups.csv'.format(topic)
    markdown_file_path = './{}/groups.md'.format(topic)
    groups_csv_to_markdown(csv_file_path, markdown_file_path)
    """

    """
    csv_file_path = './{}/mainlines.csv'.format(topic)
    markdown_file_path = './{}/story.md'.format(topic)
    mainlines_csv_to_markdown(csv_file_path, markdown_file_path)
    """

    #file_path = './{}/characters.csv'.format(topic)
    #file_path = './{}/relations.csv'.format(topic)
    #file_path = './{}/groups.csv'.format(topic)
    file_path = './{}/mainlines.csv'.format(topic)
    
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"The file {file_path} has been removed.")
    else:
        print(f"The file {file_path} does not exist.")


