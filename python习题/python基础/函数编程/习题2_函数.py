# -*-coding:utf-8-*-


# 写函数，用户传入修改的文件名，与要修改的内容，执行函数，完成整个文件的批量修改操作


def FileContent(path, content):
    with open(path, "w", encoding='utf') as f:
        f.write(content)


if __name__ == '__main__':
    path = r""
    content = "数据内容"
    FileContent(path, content)
