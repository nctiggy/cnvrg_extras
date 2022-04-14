from src import get_module_logger


params_logger = get_module_logger(__name__)
params_logger.propagate = False


class Params:

    def __init__(self, **kwargs):
        try:
            self.key = kwargs['key']
            self.type = kwargs.get('type', 'categorical')
            self.min = kwargs.get('min', 0)
            self.max = kwargs.get('max', 0)
            self.scale = kwargs.get('scale', 'linear')
            self.steps = kwargs.get('steps', 0)
            self.values = kwargs['values']
        except KeyError as e:
            params_logger.error(f"Missing required field: {e}", exc_info=True)
