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

        ListNode* top = list1;
        ListNode* bot = list2;

        ListNode* head = nullptr;
        if (top != nullptr && bot != nullptr) {
            if (top -> val <= bot -> val) {
                head = top;
                top = top -> next;
            } else {
                head = bot;
                bot = bot -> next;
            }
        } else if (top == nullptr) {
            return bot;
        } else {
            return top;
        }

        ListNode* curr = head;
        while (top != nullptr || bot != nullptr) {
            
            if (top == nullptr) {
                p(top); p(bot);
                curr -> next = bot;
                break;
            } else if (bot == nullptr) {
                curr -> next = top;
                break;
            } else if (top -> val <= bot -> val) {
                curr -> next = top;
                top = top -> next;
            } else {
                curr -> next = bot;
                bot = bot -> next;
            }

            curr = curr -> next;
        }

        return head;
        
    }
};
