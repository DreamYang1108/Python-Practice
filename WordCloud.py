# _*_ coding: utf-8 _*_
# @DateTime : 2020/10/24 22:13
# @Author   : DreamYang
# @File     : WordCloud.py
# @Software : PyCharm 


import re
import numpy as np
import pandas as pd
import jieba
from PIL import Image
from matplotlib import colors
from matplotlib import pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator


def loaddata():
    data = pd.read_excel(r"./data/wordcloud/中文.xlsx", header=1, usecols=[0], names=None)
    df_li = data.values.tolist()
    result = []
    for s_li in df_li:
        result.append(s_li[0])
    return result


if __name__ == "__main__":
    result = str(loaddata())
    results = re.sub("[A-Za-z0-9\[\`\~\!\@\#\$\^\&\*\(\)\=\|\{\}\'\:\;\'\,\[\]\.\<\>\/\?\~\。\@\#\\\&\*\%]", "", result)\
        .replace("谢谢", "").replace("今天", "")
    text = ""
    for line in results:
        text += " ".join(jieba.cut(line, cut_all=False))
    background_Image = np.array(Image.open(r"./data/wordcloud/trump.jpg"))
    wc = WordCloud(scale=32, background_color="white", mask=background_Image, font_path=r"C:\Windows\Fonts\simhei.ttf",
                   max_words=1000, max_font_size=40, random_state=28, mode="RGB")
    wc.generate_from_text(text)

    process_word = WordCloud.process_text(wc, text)
    sort = sorted(process_word.items(), key=lambda e: e[1], reverse=True)
    img_colors = ImageColorGenerator(background_Image)
    wc.recolor(color_func=img_colors)
    plt.imshow(wc)
    plt.axis("off")
    wc.to_file(r"./data/wordcloud/trump_wordcloud.jpg")
    print("生成词云成功!")
