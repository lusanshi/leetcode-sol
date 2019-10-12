#
# @lc app=leetcode.cn id=133 lang=python3
#
# [133] 克隆图
#
"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        done = {}

        def dfs(n):
            if not n: return
            if n in done: return done[n]
            clone = Node(n.val, [])
            done[n] = clone
            for neighbor in n.neighbors:
                clone.neighbors.append(dfs(neighbor))

            return clone

        def bfs(n):
            from collections import deque
            q = deque()
            clone = Node(n.val, [])
            done[n] = clone
            q.appendleft(n)
            while q:
                temp = q.pop()
                for neighbor in temp.neighbors:
                    if neighbor not in done:
                        done[neighbor] = Node(neighbor.val, [])
                        q.appendleft(neighbor)
                    done[temp].neighbors.append(done[neighbor])

            return clone

        return bfs(node)


