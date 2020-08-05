import jieba
import wordcloud
from imageio import imread
mask=imread("cloud2.png")
f=open("关于实施乡村振兴战略的意见.txt","r",encoding="utf-8")
txt=f.read()
print("文件读取完成。")
f.close()
#wordcloud常用参数:width,height,min_font_size,max_font_size,font_step,font_path,max_words,stop_words={""},mask,background_color
w=wordcloud.WordCloud(width=1000,height=750,font_path="msyh.ttc",max_words=100,\
                      background_color="white",mask=mask)
w.generate(" ".join(jieba.lcut(txt)))
print("分词与词云生成完成。")
w.to_file("wordcloud_cloud2.png")
print("词云导出完成。")
