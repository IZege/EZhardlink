import os

BASE_PATH = 'E:\影视'
LINK_PATH = 'E:\link'          # 建立链接基础地址

def list_abs_dir(dir):
    '''
    返回 dir 路径下文件和目录的绝对路径
    '''
    return [os.path.join(dir, file) for file in os.listdir(dir)]

def link_start(dir):
    '''
    建立硬链接
    '''
    # 去掉 dir 卷标
    _, split_dir = os.path.splitdrive(dir)

    # 建立硬链接对应的目录地址 
    link_dir = os.path.join(LINK_PATH, split_dir[1:])       # 切片去掉开头的'\'
    if not os.path.exists(link_dir):
        os.makedirs(link_dir)
    
    list = list_abs_dir(dir)
    # 建立子目录列表方便遍历
    dir_list = []
    
    # 手动添加过滤表
    filer_list = ['[AI-Raws][劇場版 空の境界 - The Garden of sinners -][MOVIE 01-09+SP Fin][BDRip][MKV]', '[AI-Raws] ペルソナ3 PV・CM集 (BD HEVC 1920x1080 yuv444p10le FLAC)[F81577CD]', \
                  '[KTXP&philosophy-raws&VCB-Studio] Rakuen Tsuihou -Expelled From Paradise- [Hi10p_1080p]', '香港时代电影', \
                  'Ghost in the Shell 2017 TW 2D+3D+bonus 3Disc Blu-ray AVC AtmosTrueHD 7.1 -TTG', '[Magic-Raws] 宇宙战舰大和号2205 新的旅程', \
                  '爱，死亡和机器人.Love.Death.and.Robots.2022.S03.1080p.NF.WEB-DL.H265.10bit.HDR.DDP5.1.Atmos-LeagueNF', '爱，死亡和机器人S01.Love.Death.and.Robots.2019.1080p.WEB-DL.x265.AC3￡cXcY@FRDS', \
                  '爱，死亡和机器人S02.Love.Death.and.Robots.2021.1080p.WEB-DL.x265.AC3￡cXcY@FRDS']

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
    # 从当前目录下开始
    link_start(BASE_PATH)