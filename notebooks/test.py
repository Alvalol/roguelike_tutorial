import itertools

processors = {
            'sleep': [
                'sleep',
                'sleep',
                'sleep',
            ],
            'wake_up': [
                'wake_up'
            ],
            'life': [
                'hello',
                'shake_hand,'
                'goodbye']
        }
    
    def _define_world_reference(self):
        nested_proc = [p for p in self.processors.values()]
        unique_proc = set(itertools.chain.from_iterable(nested_proc))
        for processor_instance in unique_proc:
            print(processor_instance)