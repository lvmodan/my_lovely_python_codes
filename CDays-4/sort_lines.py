# -*- coding: utf-8 -*-

def is_comments(line):
    is_comment = False
    if line.startswith("#"):
        is_comment = True
    return is_comment

def is_blank_line(line):
    is_blank_line = False
    if line.strip() == "":
        is_blank_line = True
    return is_blank_line

def cmp_ignore_case(x):
    return x.upper()

def write_to_file(out_file, contents):
    with open(out_file, 'w') as f:
        f.write("\n".join(contents))


if __name__ == "__main__":
    # 读取文件 cdays−4-test.txt 内容，去除空行和注释行后，以行为单位进行排序，并将结果输出为 cdays−4-result.txt。
    file_txt = r"CDays-4\words.txt"
    out_file_txt = r"CDays-4\out_words.txt"
    import argparse
    argp = argparse.ArgumentParser(description="文件读取排序")
    argp.add_argument('-f', '--file', default=file_txt, type=str, help="需要排序的文件路径")
    argp.add_argument('-of', '--out_file', default=out_file_txt, type=str, help="需要排序的文件路径")
    args = argp.parse_args()
    file_txt = args.file
    out_file_txt = args.out_file
    wait_to_sort_list = list()
    with open(file_txt, "r") as f:
        lines = f.readlines()
        for l in lines:
            if is_blank_line(l):
                continue
            if is_comments(l):
                continue
            wait_to_sort_list.append(l.replace("\n",""))
    sorted_list = sorted(wait_to_sort_list, key=lambda x : x.upper())
    write_to_file(out_file_txt, sorted_list)
    
