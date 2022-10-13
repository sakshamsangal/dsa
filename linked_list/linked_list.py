# Python program for traversal of a linked list
# Node class


class Node:
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null

    def __str__(self):
        return str(self.data)


class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=' ')
            temp = temp.next
        print('')

    def seo(self):
        temp = self.head
        even_start = None
        even_end = None
        odd_start = None
        odd_end = None
        while temp:
            if temp.data & 1:
                if odd_start:
                    odd_end.next = temp
                    odd_end = temp
                    print(odd_end.data)
                else:
                    odd_start = odd_end = temp

            else:
                if even_start:
                    even_end.next = temp
                    even_end = temp
                    print(even_end.data)
                else:
                    even_start = even_end = temp
            temp = temp.next

        odd_end.next = None
        even_end.next = odd_start
        self.head = even_start

    # def print_list(self, head):
    #     if head:
    #         print(head.data, end=' ')
    #         self.print_list(head.next)
    def len_ll(self, head):
        c = 0
        temp = head
        while temp:
            temp = temp.next
            c += 1
        return c

    def intersection_point(self, h1, h2):
        l1 = self.len_ll(h1)
        l2 = self.len_ll(h2)
        diff = abs(l1 - l2)
        if l1 < l2:
            temp_h1 = h1
            temp_h2 = h2
            for _ in range(diff):
                temp_h2 = temp_h2.next
            while temp_h1 and temp_h2:
                if temp_h1 == temp_h2:
                    return temp_h1.data
                temp_h2 = temp_h2.next
                temp_h1 = temp_h1.next

            return -1


    def reverse_ll(self, prev, curr):
        if curr:
            temp = curr.next
            curr.next = prev
            return self.reverse_ll(curr, temp)
        return prev

    def add_in_end(self, item):
        if self.head:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = Node(item)
        else:
            self.head = Node(item)

    def add_in_start(self, item):
        if self.head:
            temp = Node(item)
            temp.next = self.head
            self.head = temp
        else:
            self.head = Node(item)

    def add_in_mid(self, item):
        if self.head:
            slow = self.head
            fast = self.head
            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
            temp = Node(item)
            temp.next = slow.next
            slow.next = temp

        else:
            self.head = Node(item)


def app():
    ll = LinkedList()
    ls = [1, 2, 3]
    for item in ls:
        ll.add_in_end(item)
    # ll.add_in_mid(40)
    # ll.seo()
    ll.print_list()
    ll.head = ll.reverse_ll(None, ll.head)
    ll.print_list()


# Code execution starts here
if __name__ == '__main__':
    app()
