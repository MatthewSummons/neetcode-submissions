/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

void p(ListNode* a) {
    if (a != nullptr) {
        cout << a -> val << endl;
    } else {
        cout << "Null" << endl;
    }
}

void pl(ListNode* hd) {
    cout << "[ ";
    while (hd != nullptr) {
        cout << hd -> val << " ";
        hd = hd -> next;
    } cout << "]" << endl;
}

class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {

        ListNode* dummy = new ListNode();
        ListNode* tail = dummy;

        while (list1 != nullptr && list2!= nullptr) {
            if (list1 -> val <= list2 -> val) {
                tail -> next = list1;
                list1 = list1 -> next;
            } else {
                tail -> next = list2;
                list2 = list2 -> next;
            }

            tail = tail -> next;
        }

        if (list1 != nullptr) {
            tail -> next = list1;
        } else if (list2 != nullptr) {
            tail -> next = list2;
        }

        return dummy -> next;
    }
};
