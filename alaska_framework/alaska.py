from alaska_framework.api import Request


class Alaska:
    def __init__(self):
        self.alaska = Request()

    def add_bears(self, *bears):
        for bear in bears:
            result = self.alaska.create_bear(bear)
            assert result == bear.id, f'The bear {bear.id} did not changed name.'

    def bear_should_be_in_alaska(self, bear):
        assert self.alaska.is_bear(bear), f'{bear.bear_data} is out of Alaska or hides as {self.alaska.view_bear(bear)}'

    def bear_should_be_absent_in_alaska(self, bear):
        assert self.alaska.view_bear(bear) is None, f'{bear.bear_data} is in Alaska as {self.alaska.view_bear(bear)}'

    def all_bears_should_be_in_alaska(self, bears):
        alaska_dwellers = self.alaska.view_all_bears()
        for bear in bears:
            assert self.alaska.view_bear(bear) in alaska_dwellers, f'The {bear.bear_data} is out of Alaska'

    def all_bears_should_be_absent_in_alaska(self, bears):
        alaska_dwellers = self.alaska.view_all_bears()
        for bear in bears:
            assert self.alaska.view_bear(bear) not in alaska_dwellers, f'The {bear.bear_data} is out of Alaska'

    def change_bear_name(self, bear, new_name):
        bear.change_name(new_name)
        result = self.alaska.update_bear(bear)
        assert result == 'OK', f'The bear {bear.id} did not changed name.'

    def change_bear_type(self, bear, new_type):
        bear.change_type(new_type)
        result = self.alaska.update_bear(bear)
        assert result == 'OK', f'The bear {bear.id} did not change name.'

    def change_bear_age(self, bear, new_age):
        bear.change_age(new_age)
        result = self.alaska.update_bear(bear)
        assert result == 'OK', f'The bear {bear.id} did not change name.'

    def delete_bears(self, *bears):
        for bear in bears:
            result = self.alaska.delete_bear(bear)
            assert result == 'OK', f'The bear {bear.id} was not removed from Alaska.'

    def delete_all_bears(self):
        response = self.alaska.delete_all_bears()
        assert response == 'OK', 'The bears were not removed from Alaska'

    def change_name_non_existed_bear(self, bear, new_name):
        bear.change_name(new_name)
        result = self.alaska.update_bear(bear)
        assert result is None, f'The NONEXISTED bear {bear.id} changed name.'

    def delete_non_existed_bear(self, bear):
        result = self.alaska.delete_bear(bear)
        assert result != 'OK' and result is None, f'The NONEXISTED bear {bear.id} was removed from Alaska.'
