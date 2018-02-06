#!/usr/bin/env python3
import requests
import sys
import os

port = ":8080" # 端口修好后改为 ""
cogsUrl = "218.28.19.228"
if __name__ == '__main__':
    if "-i" in sys.argv:
        id = sys.argv[sys.argv.index("-i") + 1]
    elif len(sys.argv) == 2:
        id = sys.argv[1]
    else :
        id = input("题目id: ")
    Url = 'http://' + cogsUrl + port + '/cogs/problem/problem.php?pid={0}'.format(id)
    Page = requests.get(Url)
    html = str(Page.content)
    try:
        CanBeSolve = html.split('badge badge-success\\\'>')[1].split('<')[0]
    except IndexError:
        print("错误!! 该题不可做!!")
        exit()

    DataCnt = int(html.split('badge badge-success\\\'>')[1].split('<')[0])
    DataName = html.split('<td><code>')[1].split('.')[0]
    Time = html.split(' s)')[0].split(' ms (')[1]
    Memory = html.split(' MB')[0].split('</th>\\n<td>')[-1]
    os.system("rm -rf data")
    os.system("mkdir data")
    for i in range(1, DataCnt + 1):
        sys.stdout.write("\r下载进度 {0}%".format(int(float(i / DataCnt) * 100)))
        sys.stdout.flush()
        InputFlieName = DataName + str(i) + '.in'
        AnsFlieName = DataName + str(i) + '.ans'
        InputFlieUrl = "http://" + cogsUrl + port + "/cogs/problem/QuiXplorer/index.php\?action\=download\&dir\={0}\&item\={1}\&order\=name\&srt\=yes".format(DataName, InputFlieName)
        AnsFlieUrl = "http://" + cogsUrl + port + "/cogs/problem/QuiXplorer/index.php\?action\=download\&dir\={0}\&item\={1}\&order\=name\&srt\=yes".format(DataName, AnsFlieName)
        os.system("aria2c -q {0} -o data/{1} &> /dev/null".format(InputFlieUrl, InputFlieName))
        os.system("aria2c -q {0} -o data/{1} &> /dev/null".format(AnsFlieUrl, AnsFlieName))

    print("\n下载完成")
    FileName = input("待评测文件名:")
    print("正在生成config.json")
    with open("config.json", "w") as Config:
        Config.write('{' + "\n  \"Source\": \"{0}\",\n".format(FileName))
        Config.write("  \"Input\": \"{0}\",\n".format(DataName + '#.in'))
        Config.write("  \"Output\": \"{0}\",\n".format(DataName + '#.ans'))
        temp = "  \"#\": ["
        for i in range(1, DataCnt + 1):
            temp += str(i)
            if i != DataCnt:
                temp += ', '
        Config.write(temp + '],\n')
        Config.write("  \"Time Limit\": \"{0}\",\n".format(Time))
        Config.write("  \"Memory Limit\": \"{0}\"\n".format(Memory) + '}\n')
    print("config.json生成完成")
