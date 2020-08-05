import jieba
import wordcloud
f=open("关于实施乡村振兴战略的意见.txt","r",encoding="utf-8")
txt=f.read()
print("文件读取完成。")
f.close()
w=wordcloud.WordCloud(width=1000,height=750,font_path="msyh.ttc",max_words=100,\
                      background_color="white",max_font_size=180)
w.generate(" ".join(jieba.lcut(txt)))
print("分词与词云生成完成。")
w.to_file("关于实施乡村振兴战略的意见_wordcloud.png")
print("词云导出完成。")
