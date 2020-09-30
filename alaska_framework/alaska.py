from alaska_framework.api import Request


class Alaska:
    def __init__(self):
        self.alaska = Request()

    def add_bears(self, *bears):
        for bear in bears:
            result = self.alaska.create_bear(bear)
            assert result == bear.id, f'The bear {bear.id} did not changed name.'

    def bears_should_be_in_alaska(self, *bears):
        for bear in bears:
            assert self.alaska.is_bear(bear),\
                f'{bear.bear_data} is out of Alaska or hides as {self.alaska.view_bear(bear)}'

    def bears_should_be_absent_in_alaska(self, *bears):
        for bear in bears:
            assert self.alaska.view_bear(bear) is None,\
                f'{bear.bear_data} is in Alaska as {self.alaska.view_bear(bear)}'

    def all_bears_should_be_in_alaska(self, bears):
        alaska_dwellers = self.alaska.view_all_bears()
        assert alaska_dwellers == bears, f'The bears are out of Alaska'

    def all_bears_should_not_be_in_alaska(self, bears):
        alaska_dwellers = self.alaska.view_all_bears()
        assert alaska_dwellers != bears, f'The bears are out of Alaska'

    def change_bear_name(self, bear, new_name):
        bear.change_name(new_name)
        result = self.alaska.update_bear(bear)
        assert result == 'OK', f'The bear {bear.id} did not changed name.'

    def change_bear_type(self, bear, new_type):
        bear.change_type(new_type)
        result = self.alaska.update_bear(bear)
        assert result == 'OK', f'The bear {bear.id} did not changed name.'

    def change_bear_age(self, bear, new_age):
        bear.change_age(new_age)
        result = self.alaska.update_bear(bear)
        assert result == 'OK', f'The bear {bear.id} did not changed name.'

    def delete_bears(self, *bears):
        for bear in bears:
            result = self.alaska.delete_bear(bear)
            assert result == 'OK', f'The bear {bear.id} was not removed from Alaska.'

    def delete_all_bears(self):
        response = self.alaska.delete_all_bears()
        assert response == 'OK', 'The bears were not removed from Alaska'

    def append_bears_id(self, *bears):
        for bear in bears:
            bear.bear_data["bear_id"] = bear.id
