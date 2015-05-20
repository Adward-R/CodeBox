//
//  main.cpp
//  binary-tree-preorder-traversal
//
//  Created by Adward on 15/5/19.
//  Copyright (c) 2015年 Eddie. All rights reserved.
//

#include <iostream>
#include <vector>
#include <stack>

using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
private:
    vector<int> vec;
    
    void preorderRecursive(TreeNode* root) {
        if (root==NULL) {
            return;
        }
        else {
            vec.push_back(root->val);
            preorderRecursive(root->left);
            preorderRecursive(root->right);
        }
    }
public:
    vector<int> preorderTraversal(TreeNode* root) {
        //preorderRecursive(root);
        //return vec;
        struct FatherNode {
            TreeNode* ptr;
            bool onLeft;
            FatherNode(TreeNode* p) : ptr(p), onLeft(true) {}
        };
        
        if (root==NULL) {
            return vec;
        }
        
        stack<FatherNode*> fatherNodes;
        TreeNode* node = root;
        
        while (true) {
            vec.push_back(node->val);
            if (node->left!=NULL) {
                fatherNodes.push(new FatherNode(node));
                node = node->left;
            }
            else if (node->right!=NULL) {
                fatherNodes.push(new FatherNode(node));
                fatherNodes.top()->onLeft = false;
                node = node->right;
            }
            else { //leaf node
                while (!fatherNodes.empty()
                       && (fatherNodes.top()->onLeft == false
                       || fatherNodes.top()->ptr->right == NULL)) {
                    fatherNodes.pop();
                }
                if (fatherNodes.empty()) { //reaches the root
                    return vec;
                }
                else {
                    fatherNodes.top()->onLeft = false;
                    node = fatherNodes.top()->ptr->right;
                }
            }

        }
        return vec;
    }
    
    TreeNode* treeBuild(vector<int>& vec){
        bool onLeft = true;
        TreeNode* root = NULL;
        TreeNode* node;
        stack<TreeNode*> fatherNodes;
        if (vec[0]<0){
            return NULL;
        }
        else{
            root = new TreeNode(vec[0]);
            node = root;
        }
        for (int i=1; i<vec.size(); i++) {
            fatherNodes.push(node);
            if (vec[i]<0){
                if (onLeft) {
                    onLeft = false;
                }
                else{
                    fatherNodes.pop();
                }
            }
            else{
                node = new TreeNode(vec[i]);
                if (onLeft) {
                    fatherNodes.top()->left = node;
                }
                else{
                    fatherNodes.top()->right = node;
                    onLeft = true;
                }
            }
        }
        return root;
    }
};

int main(int argc, const char * argv[]) {
    Solution sol;
    
    
    vector<int> treeInput;
    char ch;
    int tmpVal;
    
    //Treat any integer < 0 as # or NULL for simplicity
    while ((ch=getchar())!='{') {
        cout<<"Illegal Input"<<endl;
    }
    scanf("%d",&tmpVal);
    treeInput.push_back(tmpVal);
    while ((ch=getchar())==',') {
        scanf("%d",&tmpVal);
        treeInput.push_back(tmpVal);
    }
    
    TreeNode* treeRoot = sol.treeBuild(treeInput);
    cout<<"build finished"<<endl;
    vector<int> preorderSerialized = sol.preorderTraversal(treeRoot);
    for (int j=0; j<preorderSerialized.size(); j++) {
        cout<<preorderSerialized[j]<<",";
    }
    
    
   // sol.preorderTraversal(<#TreeNode *root#>);
    return 0;
}
