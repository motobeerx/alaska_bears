from configurations.performance_alaska_config import PerformanceConfig
from utils.bear_utils import BearGenerator
from utils.randome_utils import RandomUtils
from alaska_framework.alaska import Alaska
import time


class PerformanceAlaska(Alaska):
    def load(self, increment=PerformanceConfig.LOAD_INCREMENT):
        bears = BearGenerator.generate_bears(increment)
        self.add_bears(*bears)
        self.all_bears_should_be_in_alaska(bears)
        return bears

    def load_in_time(self, increment=PerformanceConfig.LOAD_INCREMENT,
                     during_time=PerformanceConfig.LOAD_DURATION_TIME,
                     cold_down=PerformanceConfig.COLD_DOWN):
        for x in range(int(during_time/cold_down)):
            self.load(increment)
            time.sleep(cold_down)

    def load_spikelly(self, amount_of_spikes=PerformanceConfig.LOAD_FREQUENCY,
                      max_stress=PerformanceConfig.MAX_STRESS,
                      cold_down=PerformanceConfig.COLD_DOWN):
        for x in range(amount_of_spikes):
            bears = self.load_max(max_stress)
            self.delete_all_bears()
            self.all_bears_should_be_absent_in_alaska(bears)
            time.sleep(cold_down)

    def load_max(self, max_stress=PerformanceConfig.MAX_STRESS):
        return self.load(max_stress)

    def update_bear_multiple_times(self, frequency=PerformanceConfig.LOAD_FREQUENCY):
        bears = BearGenerator.generate_bears(1)
        self.add_bears(*bears)
        for x in range(frequency):
            self.change_bear_name(bears[0], RandomUtils.get_random_str())
            self.bear_should_be_in_alaska(bears[0])

    def delete_bear_multiple_times(self, frequency=PerformanceConfig.LOAD_FREQUENCY):
        for x in range(frequency):
            bears = BearGenerator.generate_bears(1)
            self.add_bears(*bears)
            self.bear_should_be_in_alaska(bears[0])
            self.delete_bears(*bears)
            self.bear_should_be_absent_in_alaska(bears[0])
