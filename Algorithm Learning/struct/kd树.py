class Node:
    def __init__(self, data, left=None, right=None):
        self.val = data
        self.left = left
        self.right = right

class KDTree:
    def __init__(self, k):
        self.k = k
    
    def create_Tree(self, dataset, depth):
        if not dataset:
            return None
        mid_index = len(dataset) // 2 # 中位数索引
        
        axis = depth % self.k # 选择的维度
        sort_dataset = sorted(dataset, key=(lambda x: x[axis])) # 按照维度排序
        mid_data = sort_dataset[mid_index] # 中位数索引对应的数据
        cur_node = Node(mid_data) # 创建节点 
        left_data = sort_dataset[:mid_index] # 左子树数据
        right_data = sort_dataset[mid_index+1:] # 右子树数据
        cur_node.left = self.create_Tree(left_data, depth+1) # 递归创建左子树
        cur_node.right = self.create_Tree(right_data, depth+1) # 递归创建右子树
        # print(cur_node.val)
        return cur_node
    def search(self, tree, new_data):  # kd树的搜索
        self.near_node = None  # 最近的节点
        self.near_val = None # 最近的节点的值
        def dfs(node, depth):
            if not node:
                return 
            axis = depth % self.k # 当前深度对应选择的维度
            if new_data[axis] < node.val[axis]: # 如果新数据的维度值小于当前节点的维度值
                dfs(node.left, depth+1) # 递归搜索左子树
            else:
                dfs(node.right, depth+1) # 递归搜索右子树
            
            # 到这就相当于到达了叶子节点 
            dist = self.distance(new_data, node.val) # 计算新数据与当前节点的距离
            if not self.near_val or dist < self.near_val: # 如果当前节点的距离小于最近的节点的距离
                self.near_val = dist # 更新最近的节点的距离
                self.near_point = node.val # 更新最近的节点的值

            #判断是否要进入兄弟节点寻找
            if abs(new_data[axis] - node.val[axis]) < self.near_val: # 如果新数据的维度值与当前节点的维度值的差值小于最近的节点的距离，说明兄弟节点区域有可能存在更接近的值。
                if new_data[axis] < node.val[axis]:  # 控制去兄弟节点而不是刚刚回溯来的节点。 
                    dfs(node.right, depth+1)
                else:
                    dfs(node.left, depth+1)
        dfs(tree, 0) 
        return self.near_point
    def distance(self, point_1, point_2):
        res = 0
        for i in range(self.k):
            res += (point_1[i] - point_2[i]) ** 2
        return res ** 0.5

if __name__ == '__main__':
    data_set = [[2,3],[5,4],[9,6],[4,7],[8,1],[7,2]]
    new_data = [1,5]
    k = len(data_set[0])
    kd_tree = KDTree(k)
    our_tree = kd_tree.create_Tree(data_set, 0)
    predict = kd_tree.search(our_tree, new_data)
    print('Nearest Point of {}: {}'.format(new_data,predict))