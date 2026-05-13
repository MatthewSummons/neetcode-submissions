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

class Solution {
public:
    bool hasCycle(ListNode* head) {

        ListNode* slow = head;
        ListNode* fast = head;
        
        if (slow == nullptr) {
            return false;
        } else if (slow -> next == nullptr) {
            return false;
        } else {
            fast = slow -> next -> next;
        }

        while (slow != fast) {
            slow = slow -> next;
            if (fast == nullptr) {
                return false;
            } else if (fast -> next == nullptr) {
                return false;
            } else {
                fast = fast -> next -> next;
            }
        }

        return true;
    }
};
