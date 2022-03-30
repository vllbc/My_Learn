import numpy as np
import math

def equalNums(label_list, label):
    """
    函数说明：
        计算标记集中某个标记的数量
    Parameters：
        label_list - 标记集
        label - 某个标记
    Returns：
        num - 某个标记的数量
    """
    return np.sum(label_list == label)
    
def calcShannonEnt(label_list):
    """
    函数说明：
        计算信息熵
        对应公式 Ent(D) = -∑ Pk*log2(Pk) k=1..len(label_set)
    Parameters：
        label_list - 标记集
    Returns：
        shannonEnt - 当前标记集的信息熵
   """
    label_set = set(label_list)
    len_label_list = label_list.size
    shannonEnt = 0.0
    for label in label_set:
        prob = equalNums(label_list, label)/len_label_list
        shannonEnt -= prob * math.log2(prob)
    return shannonEnt

def conditionnalEntropy(feature_list, label_list):
    """
    函数说明：
        计算条件信息熵，对应信息增益公式中的被减项
    Parameters：
        feature_list - sample_list中某一列，表示当前属性的所有值
        label_list - 标记集
    Returns：
        entropy - 条件信息熵
   """
    feature_list = np.asarray(feature_list)
    label_list = np.asarray(label_list)
    feature_set = set(feature_list)
    entropy = 0.0

    for feat in feature_set:
        pro = equalNums(feature_list, feat)/feature_list.size
        entropy += pro * calcShannonEnt(label_list[feature_list == feat])

    return entropy

def calcInfoGain(feature_list, label_list):
    """
    函数说明：
        计算信息增益
    Parameters：
        feature_list - sample_list中某一列，表示当前属性的所有值
        label_list - 标记集
    Returns：
        当前属性的信息增益
   """
    return calcShannonEnt(label_list) - conditionnalEntropy(feature_list, label_list)

def splitDataSet(sample_list, label_list, axis, value):
    """
    函数说明：
        决策树在选好当前最优划分属性之后划分样本集
        依据value选择对应样例，并去除第axis维属性
    Parameters：
        feature_list - sample_list中某一列，表示当前属性的所有值
        label_list - 标记集
    Returns：
        return_sample_list, return_label_list
   """
    # sample_list[sample_list[...,axis] == value] 利用了numpy数组的布尔索引
    filtered_sample_list = sample_list[sample_list[...,axis] == value]
    return_label_list = label_list[sample_list[...,axis] == value]
    # np.hstack 将数组横向拼接，也就是去除第axis维属性
    return_sample_list = np.hstack((filtered_sample_list[...,:axis], filtered_sample_list[...,axis+1:]))
    return return_sample_list, return_label_list

def chooseBestFeatureToSplit(sample_list, label_list):
    """
    函数说明：
        选取最优划分属性
    Parameters：
        sample_list - 样本集
        label_list - 标记集
    Returns：
        bestFeat_index - 最优划分属性的索引值
   """
    numFeatures = sample_list.shape[1]
    bestInfoGain = 0
    bestFeat_index = -1

    for i in range(numFeatures):
        infoGain = calcInfoGain(sample_list[..., i], label_list)
        if infoGain > bestInfoGain:
            bestInfoGain = infoGain
            bestFeat_index = i
    return bestFeat_index

def createTree(sample_list, label_list, attr_list_copy):
    """
    函数说明：
        生成决策树
    Parameters：
        sample_list - 样本集
        label_list - 标记集
        attr_list_copy - 属性集（之所以加copy是为了删属性的时候是在副本上，防止递归出错）
    Returns：
        myTree - 最终的决策树
   """
    # attr_list 有del操作，不用副本的话递归会出错
    attr_list = attr_list_copy.copy()
    if len(set(label_list)) == 1:       # 如果只有一种标记，直接返回标记
        return label_list[0]
    elif sample_list.size == 0:         # 如果所有属性都被遍历，返回最多的标记
        return voteLabel(label_list)

    # bestFeat_index 最优划分属性的索引值
    # bestAttr 最优划分属性对应的名字
    bestFeat_index = chooseBestFeatureToSplit(sample_list, label_list)
    bestAttr = attr_list[bestFeat_index]
    myTree = {bestAttr: {}}
    del(attr_list[bestFeat_index])
    feat_set = set(sample_list[..., bestFeat_index])
    # 依据最优划分属性进行划分，并向下递归
    for feat in feat_set:
        return_sample_list, return_label_list = splitDataSet(sample_list, label_list, bestFeat_index, feat)
        myTree[bestAttr][feat] = createTree(return_sample_list, return_label_list, attr_list)
    return myTree

def voteLabel(label_list):
    """
    函数说明：
        这个函数是用在遍历完所有特征时，返回最多的类别
    Parameters：
        label_list: 标记列表
    Returns：
        数量最多的标记
   """

    # unique_label_list 是label_list中标记种类列表
    # label_num 是unique_label_list对应的数量列表
    unique_label_list = list(set(label_list))
    label_num_list = []

    for label in unique_label_list:
        label_num_list.append(equalNums(label_list, label))

    # label_num.index(max(label_num))是label_num数组中最大值的下标
    return unique_label_list[label_num_list.index(max(label_num_list))]

def classify(decisionTree, testVec, attr_list):
    """
    函数说明：
        对tesVec进行分类
    Parameters：
        decisionTree - 决策树
        attr_list - 属性名列表
        testVec - 测试向量
    Returns：
        label - 预测的标记
   """

    feature = list(decisionTree.keys())[0]          # feature为决策树的根节点
    feature_dict = decisionTree[feature]            # feature_dict为根节点下的子树
    feature_index = attr_list.index(feature)        # feature_index为feature对应的属性名索引
    feature_value = testVec[feature_index]          # feature_value为测试集中对应属性的值
    label = None
    if feature_value in feature_dict.keys():
        # 如果没有结果就继续向下找
        if type(feature_dict[feature_value]) == dict:
            label = classify(feature_dict[feature_value], testVec, attr_list)
        else:
            label = feature_dict[feature_value]
    return label

def testAccuracy(decisionTree, test_sample_list, test_label_list, attr_list):
    """
    函数说明：
        测试十次得到正确率均值
    Parameters：
        decisionTree - 决策树
        test_sample_list - 测试样本集
        test_label_list - 测试标记集
        attr_list - 属性集
    Returns：
        
   """
    def oneTime(decisionTree, test_sample_list, test_label_list, attr_list):
        rightNum = 0
        predict_label_list = []
        for i in range(len(test_sample_list)):
            predict_label = classify(decisionTree, test_sample_list[i], attr_list)
            predict_label_list.append(predict_label)
            if predict_label == test_label_list[i]:
                rightNum += 1
        accuracy = rightNum/len(test_sample_list)
        return accuracy
    sum = 0.0
    for i in range(10):
        sum += oneTime(decisionTree, test_sample_list, test_label_list, attr_list)
    av_accuracy = sum/10
    return av_accuracy

dataSet = np.array([[0, 0, 0, 0, 'no'],            
            [0, 0, 0, 1, 'no'],
            [0, 1, 0, 1, 'yes'],
            [0, 1, 1, 0, 'yes'],
            [0, 0, 0, 0, 'no'],
            [1, 0, 0, 0, 'no'],
            [1, 0, 0, 1, 'no'],
            [1, 1, 1, 1, 'yes'],
            [1, 0, 1, 2, 'yes'],
            [1, 0, 1, 2, 'yes'],
            [2, 0, 1, 2, 'yes'],
            [2, 0, 1, 1, 'yes'],
            [2, 1, 0, 1, 'yes'],
            [2, 1, 0, 2, 'yes'],
            [2, 0, 0, 0, 'no']])
labels = ['年龄', '有工作', '有自己的房子', '信贷情况']
print(createTree(dataSet[:, :-1], dataSet[:, -1], labels))