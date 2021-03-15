class BackPack:
    def __init__(self):
        self.max_slots = 20
        self.backpack_list = []

    def add_item(self, item):
        if len(self.backpack_list) > self.max_slots:
            return False
        else:
            self.backpack_list.append(item)
            return True

    def remove_item(self, item):
        for index, tmp_item in enumerate(self.backpack_list):
            if item is tmp_item:
                self.backpack_list.pop(index)
                return True
        return False

    def get_list_item(self):
        return self.backpack_list

    def list_items(self):
        print('=========' * 10)
        if self.backpack_list:
            for index, tmp_item in enumerate(self.backpack_list):
                print(f'Index {index}\n', tmp_item)
                print('=========' * 10)
        else:
            print(f'Index 0\n', 'Empty')
            print('=========' * 10)
