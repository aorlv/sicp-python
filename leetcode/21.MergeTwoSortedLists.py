def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()                  #dummy для стартовой точки списка
        cur = dummy                         #при помощи cur будем сравнивать элементы двух списком, как указателем

        while list1 and list2:              #пока не дошли до конца списков - продолжаем цикл
            if list1.val > list2.val:       #если элемент list1 больше элемента list2
                cur.next = list2            #указываем cur'ом на него, т.е. добавляем в новый смердженный список
                list2 = list2.next          #и переносим указатель на следующий элемент
            else:
                cur.next = list1
                list1 = list1.next

            cur = cur.next                  #после записи элемента в новый список - двигаем указатель на след позицию

        if list1:                           #если в конце остался элемент со списка list1 - записываем его в конец
            cur.next = list1
        else:                               #и наоборот
            cur.next = list2
        
        return dummy.next                   #возвращаем dummy, т.к. он все ещё указывает на начало списка

mergeTwoLists([1,2,4], [1,3,4])