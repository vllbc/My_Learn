# 抽取式文本摘要
import nltk
import jieba
import numpy


# 分句
def sent_tokenizer(texts):
    start = 0
    i = 0  # 每个字符的位置
    sentences = []
    punt_list = ',.!?:;~，。！？：；～'  # 标点符号

    for text in texts:  # 遍历每一个字符
        if text in punt_list and token not in punt_list:  # 检查标点符号下一个字符是否还是标点
            sentences.append(texts[start:i+1])  # 当前标点符号位置
            start = i+1  # start标记到下一句的开头
            i += 1
        else:
            i += 1  # 若不是标点符号，则字符位置继续前移
            token = list(texts[start:i+2]).pop()  # 取下一个字符.pop是删除最后一个
    if start < len(texts):
        sentences.append(texts[start:])  # 这是为了处理文本末尾没有标点符号的情况
    return sentences

# 对停用词加载


def stopwordslist(filepath):
    stopwords = [line.strip() for line in open(
        filepath, 'r', encoding='utf-8').readlines()]
    return stopwords

# 对句子打分


def score_sentences(sentences, topn_words):  # 参数 sentences：文本组（分好句的文本，topn_words：高频词组
    scores = []
    sentence_idx = -1  # 初始句子索引标号-1
    # 遍历每一个分句
    for s in [list(jieba.cut(s)) for s in sentences]:
        sentence_idx += 1  # 句子索引+1。。0表示第一个句子
        # 存放关键词在分句中的索引位置.得到结果类似：[1, 2, 3, 4, 5]，[0, 1]，[0, 1, 2, 4, 5, 7]..
        word_idx = []
        for w in topn_words:  # 遍历每一个高频词
            try:
                word_idx.append(s.index(w))  # 关键词出现在该分句子中的索引位置
            except ValueError:  # w不在句子中
                pass
        word_idx.sort()
        if len(word_idx) == 0:
            continue

        # 对于两个连续的单词，利用单词位置索引，通过距离阀值计算族
        clusters = []  # 存放的是几个cluster。类似[[0, 1, 2], [4, 5], [7]]
        cluster = [word_idx[0]]  # 存放的是一个类别（簇） 类似[0, 1, 2]
        i = 1
        while i < len(word_idx):  # 遍历 当前分句中的高频词
            CLUSTER_THRESHOLD = 2  # 举例阈值我设为2
            if word_idx[i]-word_idx[i-1] < CLUSTER_THRESHOLD:  # 如果当前高频词索引 与前一个高频词索引相差小于3，
                cluster.append(word_idx[i])  # 则认为是一类
            else:
                clusters.append(cluster[:])  # 将当前类别添加进clusters=[]
                cluster = [word_idx[i]]  # 新的类别
            i += 1
        clusters.append(cluster)

        # 对每个族打分，每个族类的最大分数是对句子的打分
        max_cluster_score = 0
        for c in clusters:  # 遍历每一个簇
            significant_words_in_cluster = len(c)  # 当前簇 的高频词个数
            total_words_in_cluster = c[-1]-c[0]+1  # 当前簇里 最后一个高频词 与第一个的距离
            score = 1.0*significant_words_in_cluster * \
                significant_words_in_cluster/total_words_in_cluster
            if score > max_cluster_score:
                max_cluster_score = score
        # 存放当前分句的最大簇（说明下，一个分解可能有几个簇） 存放格式（分句索引，分解最大簇得分）
        scores.append((sentence_idx, max_cluster_score))
    return scores

# 结果输出


def results(texts, topn_wordnum):  # texts 文本，topn_wordnum高频词个数,为返回几个句子
    stopwords = stopwordslist("停用词.txt")  # 加载停用词
    sentence = sent_tokenizer(texts)  # 分句
    words = [w for sentence in sentence for w in jieba.cut(sentence) if w not in stopwords if
             len(w) > 1 and w not in ['\t', '\n']]  # 词语，非单词词，同时非符号
    wordfre = nltk.FreqDist(words)  # 统计词频
    topn_words = [w[0] for w in sorted(wordfre.items(
    ), key=lambda d: d[1], reverse=True)][:topn_wordnum]  # 取出词频最高的topn_wordnum个单词

    scored_sentences = score_sentences(sentence, topn_words)  # 给分句打分

    # 1,利用均值和标准差过滤非重要句子
    avg = numpy.mean([s[1] for s in scored_sentences])  # 均值
    std = numpy.std([s[1] for s in scored_sentences])  # 标准差
    mean_scored = [(sent_idx, score) for (sent_idx, score) in scored_sentences if
                   score > (avg + 0.5 * std)]  # sent_idx 分句标号，score得分

    c = dict(mean_scoredsenteces=[sentence[idx]
             for (idx, score) in mean_scored])
    return " ".join(c["mean_scoredsenteces"])


if __name__ == '__main__':
    texts = """近期，美国国会众院通过法案，重申美国对台湾的承诺。对此，中国外交部发言人表示，有关法案严重违反一个中国原则和中美三个联合公报规定，粗暴干涉中国内政，中方对此坚决反对并已向美方提出严正交涉。\n事实上，中国高度关注美国国内打“台湾牌”、挑战一中原则的危险动向。近年来，作为“亲台”势力大本营的美国国会动作不断，先后通过“与台湾交往法”“亚洲再保证倡议法”等一系列“挺台”法案，“2019财年国防授权法案”也多处触及台湾问题。今年3月，美参院亲台议员再抛“台湾保证法”草案。众院议员继而在4月提出众院版的草案并在近期通过。上述法案的核心目标是强化美台关系，并将台作为美“印太战略”的重要伙伴。同时，“亲台”议员还有意制造事端。今年2月，5名共和党参议员致信众议院议长，促其邀请台湾地区领导人在国会上发表讲话。这一动议显然有悖于美国与台湾的非官方关系，其用心是实质性改变美台关系定位。\n上述动向出现并非偶然。在中美建交40周年之际，两国关系摩擦加剧，所谓“中国威胁论”再次沉渣泛起。美国对华认知出现严重偏差，对华政策中负面因素上升，保守人士甚至成立了“当前中国威胁委员会”。在此背景下，美国将台海关系作为战略抓手，通过打“台湾牌”在双边关系中增加筹码。特朗普就任后，国会对总统外交政策的约束力和塑造力加强。其实国会推动通过涉台法案对行政部门不具约束力，美政府在2018年并未提升美台官员互访级别，美军舰也没有“访问”台湾港口，保持着某种克制。但从美总统签署国会通过的法案可以看出，国会对外交产生了影响。立法也为政府对台政策提供更大空间。\n然而，美国需要认真衡量打“台湾牌”成本。首先是美国应对危机的代价。美方官员和学者已明确发出警告，美国卷入台湾问题得不偿失。美国学者曾在媒体发文指出，如果台海爆发危机，美国可能需要“援助”台湾，进而导致新的冷战乃至与中国大陆的冲突。但如果美国让台湾自己面对，则有损美国的信誉，影响美盟友对同盟关系的支持。其次是对中美关系的危害。历史证明，中美合则两利、斗则两伤。中美关系是当今世界最重要的双边关系之一，保持中美关系的稳定发展，不仅符合两国和两国人民的根本利益，也是国际社会的普遍期待。美国蓄意挑战台湾问题的底线，加剧中美关系的复杂性和不确定性，损害两国在重要领域合作，损人又害己。\n美国打“台湾牌”是一场危险的赌博。台湾问题是中国核心利益，中国政府和人民决不会对此坐视不理。中国敦促美方恪守一个中国原则和中美三个联合公报规定，阻止美国会审议推进有关法案，妥善处理涉台问题。美国悬崖勒马，才是明智之举。\n（作者系中国国际问题研究院国际战略研究所副所长）"""
    topn_wordnum = int(input('请输入高频词数：'))

    c = results(texts, topn_wordnum)
    print(c)
