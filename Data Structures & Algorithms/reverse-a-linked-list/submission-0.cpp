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
        cout << a -> val << " ";
    } else {
        cout << "Null" << " ";
    }
}

class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode* before = nullptr;
        ListNode* curr   = head;
        ListNode* after  = nullptr;

        while (curr != nullptr) {
            after = curr -> next;
            curr -> next = before;
            before = curr;
            curr = after;
        } return before;
    }
};
