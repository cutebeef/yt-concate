from .steps.step import StepException

class Pipeline:
    def __init__(self,steps):
        self.steps = steps  #上面那個steps參數,把參數存成屬性

    def run(self, inputs):
        data = None
        for step in self.steps:
            try:
                date = step.process(data, inputs) #資料傳遞交接
            except StepException as e:
                print('Exception happened', e)
                break
