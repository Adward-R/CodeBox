__author__ = 'Adward'
class Solution(object):
    def isRectangleCover(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        if len(rectangles) == 0:
            return False
        rect = [
            min(rectangles, key=lambda pt: pt[0])[0],
            min(rectangles, key=lambda pt: pt[1])[1],
            max(rectangles, key=lambda pt: pt[2])[2],
            max(rectangles, key=lambda pt: pt[3])[3],
        ]

        sum_of_area = 0
        pt_cnt = set()
        for x1, y1, x2, y2 in rectangles:
            sum_of_area += (x2 - x1) * (y2 - y1)
            for pt in [(x1, y1), (x1, y2), (x2, y1), (x2, y2)]:
                if pt in pt_cnt:
                    pt_cnt.remove(pt)
                else:
                    pt_cnt.add(pt)

        corners = [(rect[0], rect[1]), (rect[0], rect[3]), (rect[2], rect[1]), (rect[2], rect[3])]
        # print(corners, pt_cnt)
        # print([pt in pt_cnt for pt in corners])
        return len(pt_cnt) == 4 and sum([pt in pt_cnt for pt in corners]) == 4 \
               and sum_of_area == (rect[2]-rect[0])*(rect[3]-rect[1])

        # slots = [[(y_down, y_up)] for _ in range(x_right-x_left)]
        #
        # for left, down, right, up in rectangles:
        #     for i in range(left-x_left, right-x_left):
        #         if len(slots[i]) == 0:
        #             return False
        #         for j in range(len(slots[i])-1, -1, -1):
        #             bottom, top = slots[i][j]
        #             if up > top:
        #                 return False
        #             elif up == top:
        #                 if down > bottom:
        #                     slots[i][j] = (bottom, down)
        #                 elif down == bottom:
        #                     del slots[i][j]
        #                 else:
        #                     return False
        #             elif bottom < up < top:
        #                 if down > bottom:
        #                     slots[i][j] = (bottom, down)
        #                     slots[i].insert(j+1, (up, top))
        #                 elif down == bottom:
        #                     slots[i][j] = (up, top)
        #                 else:
        #                     return False
        #
        # for col in slots:
        #     if len(col):
        #         return False
        # return True


sol = Solution()
rectangles = [
    [
        [1,1,3,3],
        [3,1,4,2],
        [3,2,4,4],
        [1,3,2,4],
        [2,3,3,4]
    ],
    [
        [1,1,2,3],
        [1,3,2,4],
        [3,1,4,2],
        [3,2,4,4]
    ],
    [
        [1,1,3,3],
        [3,1,4,2],
        [1,3,2,4],
        [3,2,4,4]
    ],
    [
        [1,1,3,3],
        [3,1,4,2],
        [1,3,2,4],
        [2,2,4,4]
    ],
    [
        [0,0,2,2],
        [1,1,3,3],
        [2,0,3,1],
        [0,3,3,4]
    ],
    [
        [1,1,2,2],
        [0,1,1,2],
        [1,0,2,1],
        [0,2,3,3],
        [2,0,3,3]
    ],
    [[0,0,4,1],[0,0,4,1]],
    [[0,0,4,1],[7,0,8,2],[6,2,8,3],[5,1,6,3],[4,0,5,1],[6,0,7,2],[4,2,5,3],[2,1,4,3],[0,1,2,2],[0,2,2,3],[4,1,5,2],[5,0,6,1]]
]
for rect in rectangles:
    print(sol.isRectangleCover(rect))

# rectangles = [[0,0,5,1],[7,0,8,2],[5,1,6,3],[6,0,7,2],[4,0,5,1],[4,2,5,3],[2,1,4,3],[0,2,2,3],[0,1,2,2],[6,2,8,3],[5,0,6,1],[4,1,5,2]]
# print(sol.isRectangleCover(rectangles))