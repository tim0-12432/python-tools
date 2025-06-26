import sys
from os import listdir, path, rename
import frontmatter
import yaml
import datetime
from typing import Union, Tuple


class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True

for first_char, resolvers in list(NoAliasDumper.yaml_implicit_resolvers.items()):
    NoAliasDumper.yaml_implicit_resolvers[first_char] = [
        (tag, regexp) for tag, regexp in resolvers
        if tag != 'tag:yaml.org,2002:timestamp'
    ]
    
class PlainString(str):
    pass

def plain_str_representer(dumper, data):
    return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='')
NoAliasDumper.add_representer(PlainString, plain_str_representer)


def replace_quotes(file_path: str) -> None:
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    content = content.replace("'", "")
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)


def update_frontmatter(file_path: str, file_name: str) -> Tuple[str, str]:
    data = frontmatter.load(path.join(file_path, file_name))
    old_date: Union[datetime.date, str] = data.get('Date', None)
    old_tags = data.get('tags', None)
    old_adds = data.get('Additional', None)
    if 'Date' in data:
        del data['Date']
    if 'tags' in data:
        del data['tags']
    if 'Additional' in data:
        del data['Additional']
    if old_date:
        if old_date == 'Invalid date':
            date = None
            time = None
        else:
            date = old_date.split('T')[0] if isinstance(old_date, str) else old_date
            time = old_date.split('T')[1] if old_date and isinstance(old_date, str) and 'T' in old_date else None
        data['date'] = date
        if time:
            data['startTime'] = PlainString(time)
            data['endTime'] = PlainString(time)
            data['allDay'] = False
        else:
            data['allDay'] = True
    else:
        data['date'] = None
    data['tags'] = old_tags if old_tags else []
    data['additional'] = old_adds if old_adds else []
    data['completed'] = None
    data['title'] = file_name.replace('.md', '')
    frontmatter.dump(data, path.join(file_path, file_name), Dumper=NoAliasDumper)

    replace_quotes(path.join(file_path, file_name))

    return data['date'], data['title']


def move_file(file_path: str, old_name: str, new_name: str) -> None:
    old_file = path.join(file_path, old_name)
    new_file = path.join(file_path, new_name)
    if path.exists(old_file):
        if not path.exists(new_file):
            rename(old_file, new_file)
        else:
            print(f"ERROR: File '{new_name}' already exists in '{file_path}'!")
    else:
        print(f"ERROR: File '{old_name}' does not exist in '{file_path}'!")


def migrate_file(file_path: str, file_name: str) -> None:
    date, title = update_frontmatter(file_path, file_name)
    new_name = f"{date} {title}.md" if date else f"{title}.md"
    move_file(file_path, file_name, new_name)


def migrate_notion_files(file_path: str) -> None:
    files = [f for f in listdir(file_path) if path.isfile(path.join(file_path, f))]
    for file_index, file in enumerate(files):
        if file.endswith(".md"):
            migrate_file(file_path, file)
            print(f"INFO {file_index + 1}/{len(files)}: Migrated '{file}' to Obsidian format...")
        else:
            print(f"WARN {file_index + 1}/{len(files)}: '{file}' is not a markdown file!")


if __name__ == '__main__':
    if (len(sys.argv) < 2):
        print("Usage: python notion-calendar-to-obsidian-migrator.py <path>")
        exit(1)
    dir = sys.argv[1]
    migrate_notion_files(dir)
