import os

BASE_PATH = '原始根目录'
LINK_PATH = '目的根目录'

def list_abs_dir(dir):
    '''
    返回 dir 路径下文件和目录的绝对路径
    '''
    return [os.path.join(dir, file) for file in os.listdir(dir)]

def link_start(dir):
    '''
    建立硬链接
    '''
    # 去掉卷标
    _, split_dir = os.path.splitdrive(dir)

    # 建立硬链接对应的目录地址 
    link_dir = os.path.join(LINK_PATH, split_dir[1:])       # 切片去掉开头的'\'
    if not os.path.exists(link_dir):
        os.makedirs(link_dir)
    
    list = list_abs_dir(dir)
    # 建立子目录列表方便遍历
    dir_list = []
    
    # 手动添加过滤表
    filer_list = ['需要过滤的文件夹名或文件名', '用逗号分隔']

    # 移除需要过滤的文件和目录
    for i in list:
        for ban in filer_list:
            if ban in i:
                list.remove(i)
                break

    for i in list:
        if os.path.isfile(i):
            file = os.path.basename(i)
            # 建立硬链接文件路径
            link_file = os.path.join(link_dir, file)
            try:
                os.link(i, link_file)
                print('{}<=====>{}'.format(file, link_file))
            except:
                # 已建立过硬链接的文件无法再次建立，直接pass
                pass
        else:
            dir_list.append(i)

    for dir in dir_list:
        # 遍历子目录
        link_start(dir)

if __name__ == '__main__':
    link_start(BASE_PATH)
