class MyCollection:
    def __init__(self, only_int=True):
        self.items = []
        self.only_int = only_int      # True = รับเฉพาะ int, False = รับได้ทุกชนิด
 
    def _check(self, value):
        if self.only_int and type(value) is not int:
            print("รับเฉพาะจำนวนเต็มเท่านั้น:", value)
            return False
        return True
 
    def _contains(self, value):
        for x in self.items:
            if x == value:
                return True
        return False
 
    def _remove_first(self, value):
        """ลบตัวแรกที่เจอ คืนค่า True ถ้าลบสำเร็จ"""
        new_items = []
        removed = False
        for x in self.items:
            if x == value and not removed:
                removed = True
            else:
                new_items.append(x)
        self.items = new_items
        return removed
 
    def show(self):
        print(self.__class__.__name__, self.items)
 
 
class MySet(MyCollection):
    def add(self, value):
        if self._check(value):
            if self._contains(value):
                print(value, "มีอยู่แล้วใน set")
            else:
                self.items.append(value)
 
    def remove(self, value):
        if not self._remove_first(value):
            print("ไม่พบ", value)
 
 
class MyBag(MyCollection):
    def add(self, value):
        if self._check(value):
            self.items.append(value)      # เก็บซ้ำได้
 
    def remove(self, value):
        if not self._remove_first(value): # ลบทีละ 1 ตัว
            print("ไม่พบ", value)
 
 
class MyQueue(MyCollection):
    def add(self, value):                 # enqueue: เข้าท้ายคิว
        if self._check(value):
            self.items.append(value)
 
    def remove(self):                     # dequeue: ออกจากหัวคิว
        if len(self.items) == 0:
            print("คิวว่าง")
            return None
        first = self.items[0]
        new_items = []
        for i in range(1, len(self.items)):
            new_items.append(self.items[i])
        self.items = new_items
        return first

st = MySet()
for n in [1, 2, 2, 3]:
    st.add(n)
st.remove(2)
st.show()

bag = MyBag()
for n in [1, 2, 2, 3]:
    bag.add(n)
bag.remove(2)
bag.show()

q = MyQueue()
for n in [10, 20, 30]:
    q.add(n)
print("ออกจากคิว:", q.remove())
q.show()

anything = MyBag(only_int=False)      # เก็บข้อมูลได้ทุกชนิด
anything.add("hello")
anything.add(3.14)
anything.add([1, 2])
anything.show()
#6901012610137
#lab09-3