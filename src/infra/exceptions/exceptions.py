class DatasetNameMissingError(ValueError):
    def __init__(
        self, message="ERROR: DatasetNameMissingError. dataset_name must be provided."
    ):
        super().__init__(message)


class TextKeyNotFoundError(ValueError):
    def __init__(
        self,
        message="ERROR: TextKeyNotFoundError. The 'text' key was not found in the provided dataset, aborting the transformation. Make sure the input dictionary contains a 'text' key with conversation data.",
    ):
        super().__init__(message)


class InvalidSegmentNumberError(ValueError):
    def __init__(
        self, message="ERROR: InvalidSegmentNumberError. Invalid number of segments"
    ):
        super().__init__(message)


class InvalidTagFormatError(ValueError):
    def __init__(
        self, message="ERROR: InvalidTagFormatError. Invalid tag format in dataset."
    ):
        super().__init__(message)


class MissingTagError(ValueError):
    def __init__(
        self, message="ERROR: MissingTagError. Missing required tags in the dataset."
    ):
        super().__init__(message)
