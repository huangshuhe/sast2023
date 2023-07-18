# sast2023 word game

## 环境配置

python
使用第三方库：streamlit

## 使用设置

### 启动

对 main_basic.py 文件，约定以下参数：

```
--file  -f  接文章的路径
```

启动 main_basic.py, 按如下在终端运行：
```
python main_basic.py -f [文章路径]
```

启动 main_GUI_textinput.py 与 main_GUI_fileuploader.py 文件，按如下在终端运行：(需有streamlit第三方库)

```
streamlit run main_GUI_textinput.py
```
或：
```
streamlit run main_GUI_textinput.py
```
### 格式

文章使用 JSON 存储的格式如下：
```
{
    "language": "zh",
    "articles": [
        {
            "title": "xxx",
            "article": "xxx{{1}}xxxxx{{2}}xxx",
            "hints": ["xx", "xx",.....]
        }
    ]
}
```
文件夹提供一个样例文章example.json
## 游戏说明

"⽂章填词"是⼀个⼗分简单的⼩游戏。具体来说，出题者事先准备好⼀篇⽂章，并将其中的⼀些单词挖去；对于
挖去的单词，出题者会给⼀定提⽰，例如该词的词性、褒贬、类型等；做题者看不到⽂章，只能根据提⽰随意选择
单词；最终将做题者给定的单词填回原⽂，往往会达成不错的喜剧效果。

## 完成功能

main_basic.py : 仅完成基础功能
main_GUI_textinput.py : 实现GUI拓展功能，通过输入文件路径打开文章文件
main_GUI_fileuploader.py : 实现GUI拓展功能，通过上传json文件打开文章文件