//
//  main.cpp
//  lru-cache
//
//  Created by Adward on 15/7/28.
//  Copyright (c) 2015年 Eddie. All rights reserved.
//

#include <iostream>
#include <vector>

using namespace std;

class LRUCache{
private:
    struct CacheBlock{
        int key;
        int value;
        int dist;
        CacheBlock(): key(0), value(0), dist(0) {};
        CacheBlock(int key, int value): key(key), value(value), dist(0) {};
    };
    vector<CacheBlock> *cache;
    int capacity;
public:
    LRUCache(int capacity) {
        cache = new vector<CacheBlock>;
        this->capacity = capacity;
    }
    
    ~LRUCache() {
        delete cache;
    }
    
    int get(int key) {
        vector<CacheBlock>::iterator iter = cache->begin();
        int foundValue = -1;
        for (; iter!=cache->end(); iter++) {
            iter->dist ++;
            if (key == iter->key) {
                foundValue = iter->value;
                iter->dist = 0;
            }
        }
        return foundValue;
    }
    
    void set(int key, int value) {
        vector<CacheBlock>::iterator iter = cache->begin();
        bool found = false;
        for (; iter!=cache->end(); iter++) {
            iter->dist ++;
            if (key == iter->key) {
                found = true;
                iter->dist = 0;
                iter->value = value;
            }
        }
        if (!found) { //need to insert new key
            if (capacity == cache->size()) { //full
                vector<CacheBlock>::iterator lruPtr = cache->begin();
                for (iter=cache->begin(); iter!=cache->end(); iter++) {
                    if (iter->dist > lruPtr->dist) {
                        lruPtr = iter;
                    }
                }
                cache->erase(lruPtr);
            }
            cache->push_back(*new CacheBlock(key, value));
        }
    }
    
    void display() {
        vector<CacheBlock>::iterator iter = cache->begin();
        for (; iter!=cache->end(); iter++) {
            cout << iter->key << ":" <<iter->value << endl;
        }
    }
};

int main(int argc, const char * argv[]) {
    LRUCache lruCache(4);
    //cout << lruCache.get(3);
    lruCache.set(0, 0);
    lruCache.set(1, -1);
    lruCache.set(2, -2);
    lruCache.set(3, -3);
    lruCache.set(4, -4);
    cout << "get: " << lruCache.get(1) << endl;
    lruCache.set(5, -5);
    lruCache.set(3, 3);
    lruCache.set(6,-6);
    lruCache.display();
    return 0;
}
