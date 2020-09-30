from utils.bear_utils import BearGenerator
import pytest


@pytest.mark.functional
@pytest.mark.smoke
class TestUserCantAddValidValue:
    """
       Ensure that user can CRUD database with valid, common values.
       Smoke test
       :return:
       """
    def test_user_can_add_bears(self, alaska):
        bears = BearGenerator.generate_bears(50)
        alaska.add_bears(*bears)
        alaska.bears_should_be_in_alaska(*bears)

    def test_user_can_change_bear_name(self, alaska):
        bears = BearGenerator.generate_bears(1)
        alaska.add_bears(*bears)
        alaska.change_bear_name(bears[0], 'MISHA')
        alaska.bears_should_be_in_alaska(bears[0])

    def test_user_can_change_bear_type(self, alaska):
        bears = BearGenerator.generate_bears(1)
        bears[0].change_type('BLACK')
        alaska.add_bears(bears)
        alaska.change_bear_type(bears[0], 'POLAR')
        alaska.bears_should_be_in_alaska(bears[0])

    def test_user_can_change_bear_age(self, alaska):
        bears = BearGenerator.generate_bears(1)
        alaska.add_bears(bears)
        alaska.change_bear_age(bears[0], 23.1)
        alaska.bears_should_be_in_alaska(bears[0])

    def test_user_can_delete_bear(self, alaska):
        bears = BearGenerator.generate_bears(10)
        alaska.add_bears(*bears)
        alaska.bears_should_be_in_alaska(*bears)
        alaska.delete_bears(*bears[2:5])
        alaska.bears_should_be_absent_in_alaska(*bears[2:5])

    def test_user_can_delete_all_bears(self, alaska):
        bears = BearGenerator.generate_bears(10)
        alaska.add_bears(*bears)
        alaska.bears_should_be_in_alaska(*bears)
        alaska.delete_all_bears()
        alaska.bears_should_be_absent_in_alaska(*bears)


@pytest.mark.functional
class TestUserCantAddInvalidOrNotCommonValue:
    """
    Ensure that user can CRUD database with valid/invalid, noncommon values.
    Mat and At tests
    """
    @pytest.mark.MAT_name
    def test_user_can_add_bear_with_empty_string_name(self, alaska):
        bears = BearGenerator.generate_bears(1)
        bears[0].change_name('')
        alaska.add_bears(*bears)
        alaska.bears_should_be_in_alaska(*bears)
        alaska.delete_all_bears()

    @pytest.mark.MAT_name
    def test_user_can_add_bear_with_whitespaces_name(self, alaska):
        bears = BearGenerator.generate_bears(1)
        bears[0].change_name('  ')
        alaska.add_bears(*bears)
        alaska.bears_should_be_in_alaska(*bears)
        alaska.delete_all_bears()

    @pytest.mark.MAT_name
    def test_user_can_add_bear_with_null_name(self, alaska):
        bears = BearGenerator.generate_bears(1)
        bears[0].change_name('null')
        alaska.add_bears(*bears)
        alaska.bears_should_be_in_alaska(*bears)
        alaska.delete_all_bears()

    @pytest.mark.AT_name
    def test_user_can_not_add_bear_with_none_value_name(self, alaska):
        bears = BearGenerator.generate_bears(1)
        bears[0].change_name(None)
        alaska.add_bears(*bears)
        alaska.bears_should_be_absent_in_alaska(*bears)
        alaska.delete_all_bears()

    @pytest.mark.AT_type
    def test_user_can_not_add_bear_with_invalid_type(self, alaska):
        bears = BearGenerator.generate_bears(1)
        bears[0].change_type('WRONG_TYPE')
        alaska.add_bears(*bears)
        alaska.bears_should_be_absent_in_alaska(*bears)
        alaska.delete_all_bears()

    @pytest.mark.MAT_age
    def test_user_can_add_bear_with_zero_age(self, alaska):
        bears = BearGenerator.generate_bears(1)
        bears[0].change_age(1)
        alaska.add_bears(*bears)
        alaska.bears_should_be_in_alaska(*bears)
        alaska.delete_all_bears()

    @pytest.mark.AT_age
    def test_user_can_not_add_bear_with_negative_age(self, alaska):
        bears = BearGenerator.generate_bears(1)
        bears[0].change_age(-1)
        alaska.add_bears(*bears)
        alaska.bears_should_be_absent_in_alaska(*bears)
        alaska.delete_all_bears()

    @pytest.mark.AT_age
    def test_user_can_not_add_bear_with_positive_inf_age(self, alaska):
        bears = BearGenerator.generate_bears(1)
        bears[0].change_age(float('inf'))
        alaska.add_bears(*bears)
        alaska.bears_should_be_absent_in_alaska(*bears)
        alaska.delete_all_bears()

    @pytest.mark.AT_age
    def test_user_can_not_add_bear_with_negative_inf_age(self, alaska):
        bears = BearGenerator.generate_bears(1)
        bears[0].change_age(float('-inf'))
        alaska.add_bears(*bears)
        alaska.bears_should_be_absent_in_alaska(*bears)
        alaska.delete_all_bears()

    @pytest.mark.AT_age
    def test_user_can_not_add_bear_with_nan_age(self, alaska):
        bears = BearGenerator.generate_bears(1)
        bears[0].change_age(float('nan'))
        alaska.add_bears(*bears)
        alaska.bears_should_be_absent_in_alaska(*bears)
        alaska.delete_all_bears()

    @pytest.mark.MAT_age
    def test_user_can_not_add_bear_with_string_type_age(self, alaska):
        bears = BearGenerator.generate_bears(1)
        bears[0].change_age('string')
        alaska.add_bears(*bears)
        alaska.bears_should_be_absent_in_alaska(*bears)
        alaska.delete_all_bears()


@pytest.mark.performance
class TestPerformance:
    """
    Ensure in database durability.
    Performance test
    """
    def test_load_in_time_until_max(self, performance_alaska):
        performance_alaska.load_in_time()

    def test_load_max_and_update(self, performance_alaska):
        performance_alaska.load_max()
        performance_alaska.update_bear_multiple_times(1000)

    def test_load_max_and_delete(self, performance_alaska):
        performance_alaska.load_max()
        performance_alaska.delete_bear_multiple_times(1000)

    def test_load_max_multiple_times(self, performance_alaska):
        performance_alaska.load_spikelly()


@pytest.mark.none_function
class TestLogicStructure:
    """
    Ensure in database structure consistency.
    None function test
    """
    def test_user_can_add_two_equal_bears(self, alaska):
        bears = BearGenerator.generate_bears(1)
        bears_copy = bears
        alaska.add_bears(*bears)
        alaska.add_bears(*bears_copy)
        alaska.bears_should_be_in_alaska(*bears, *bears_copy)
