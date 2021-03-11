class BackPack:
    def __init__(self):
        self.max_slots = 20
        self.backpack_list = []

    def add_item(self, item):
        if len(self.backpack_list) > self.max_slots:
            print('Max Item Reached')
            return False
        else:
            self.backpack_list.append(item)

    def remove_item(self, item):
        for index, tmp_item in enumerate(self.backpack_list):
            if item is tmp_item:
                self.backpack_list.pop(index)
                return True
        return False

    def list_items(self):
        if self.backpack_list:
            for index, tmp_item in enumerate(self.backpack_list):
                print('========' * 10)
                print(f'backpack index {index}\n', tmp_item)
                print('========' * 10)
        else:
            print('========' * 10)
            print('EMPTY')
            print('========' * 10)