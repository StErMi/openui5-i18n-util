import re
import mmap
import fnmatch
import os
import argparse

parser = argparse.ArgumentParser(
    description="Easily find all i18n strings inside your project and build translation files")
parser.add_argument("-pf", "--project-folder", dest='project_folder', required=True,
                    help="Project's root folder")
parser.add_argument("-if", "--i18n-folder", dest='i18n_folder', required=True, help="i18n root folder")
parser.add_argument("-fp", "--file-patterns", dest='file_patterns', required=False, default=['*.xml', '*.js'],
                    nargs='+', help="Array of file extension pattern patterns where to search i18n strings")
parser.add_argument("-ip", "--i18n-patterns", dest='i18n_patterns', required=False,
                    default=['{i18n>([^}]+)}'], nargs='+',
                    help="Array of i18n patterns")
parser.add_argument("-l", "--languages", dest='languages', required=False, default=['en'], nargs='+',
                    help="Array of languages supported by your project")
parser.add_argument("-ml", "--main-language", dest='main_language', required=False, default='en',
                    help="Project's main language")
args = parser.parse_args()

file_patterns = args.file_patterns
app_languages = args.languages
main_language = args.main_language
project_folder = args.project_folder
i18n_folder = args.i18n_folder
i18n_patterns = args.i18n_patterns


def __match_content(file_name, _i18n_patterns):
    local_i18n = []
    with open(file_name, 'r+') as f:
        data = mmap.mmap(f.fileno(), 0)
        groups = re.findall('|'.join(_i18n_patterns), data)
        if len(groups) > 0:
            for group in groups:
                for match in group:
                    if match and len(match) > 0:
                        local_i18n.append("{0}".format(match))

            local_i18n.sort()
            local_i18n = ["# Matches in file {0}".format(os.path.realpath(file_name))] + local_i18n
    return local_i18n


def __write_file(path, content_lines):
    old_content_lines = __read_file_per_line(path)
    diff_content = __diff_content(content_lines, old_content_lines)
    content = "\n".join(diff_content)

    target = open(path, 'w')
    target.write(content)
    target.close()


def __read_file_per_line(file_name):
    try:
        with open(file_name) as f:
            content = f.readlines()
        # you may also want to remove whitespace characters like `\n` at the end of each line
        return [x.strip() for x in content]
    except IOError:
        return []


def __diff_content(new_content_lines, old_content_lines):
    old_content_dict = {}
    if old_content_lines is not None:
        for line in old_content_lines:
            splitted = line.split("=", 1)
            old_content_dict[splitted[0]] = splitted[1]

    final_content = []
    for line in new_content_lines:
        value = old_content_dict.get(line, "")
        if line.startswith('#'):
            # We're in a comment, just append as it is
            final_content.append(line)
        else:
            final_content.append("{0}={1}".format(line, value))

    return final_content


def __walk_please(project_dir, _file_patterns, _i18n_patterns):
    i18n_list = []
    for root, subFolders, files in os.walk(project_dir):
        for filename in files:
            is_main_file = os.path.realpath(os.path.join(root, filename)) == os.path.realpath(__file__)

            if not is_main_file:
                for file_pattern in _file_patterns:
                    if fnmatch.fnmatch(filename, file_pattern):
                        i18n_list += __match_content(os.path.join(root, filename), _i18n_patterns)

    return i18n_list


def __remove_duplicates(current_list):
    new_list = []
    for i in current_list:
        if i not in new_list:
            new_list.append(i)
    return new_list


def build_i18n(_project_folder, _i18n_folder, _app_languages, _main_language, _i18n_patterns, _file_patterns):
    translations = __walk_please(_project_folder, _file_patterns, _i18n_patterns)
    content = __remove_duplicates(translations)
    i18n_filename = 'i18n.properties'
    if len(_app_languages) == 1:
        __write_file(os.path.join(_i18n_folder, i18n_filename), content)
    else:
        for lang in _app_languages:
            if not lang == _main_language:
                i18n_filename = 'i18n_{0}.properties'.format(lang)
            else:
                i18n_filename = 'i18n.properties'
            __write_file(os.path.join(_i18n_folder, i18n_filename), content)


build_i18n(project_folder, i18n_folder, app_languages, main_language, i18n_patterns, file_patterns)
