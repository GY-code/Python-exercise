import jieba
import wordcloud
txt=open("threekingdoms.txt","r",encoding="utf-8").read()
print("文件读取完成。")
w=wordcloud.WordCloud(width=1000,height=750,font_path="msyh.ttc",max_words=100,\
                      background_color="white",max_font_size=150)
w.generate(" ".join(jieba.lcut(txt)))
print("分词与词云生成完成。")
w.to_file("threekingdoms_wordcloud.png")
print("词云导出完成。")
