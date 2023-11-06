import re
from datasets import load_dataset
from src.infra.exceptions import (
    DatasetNameMissingError,
    TextKeyNotFoundError,
    InvalidSegmentNumberError,
    MissingTagError,
    InvalidTagFormatError,
)


class HumanAssistantTransformer:
    def __init__(self, dataset_name=None, seed=None, range_size=None):
        if dataset_name is None:
            raise DatasetNameMissingError()

        self.dataset = load_dataset(dataset_name)["train"]

        if len(self.dataset.features) != 1 or "text" not in self.dataset.features:
            raise TextKeyNotFoundError()

        if seed is not None:
            self.dataset = self.dataset.shuffle(seed=seed)

        if range_size is not None:
            self.dataset = self.dataset.select(range(range_size))

    def transform_template_forward(self, dataset):
        conversation_text = dataset["text"]
        segments = conversation_text.split("###")

        if len(segments) < 3:
            raise InvalidSegmentNumberError()

        reformatted_segments = []

        for i in range(1, len(segments) - 1, 2):
            human_text = segments[i].strip().replace("Human:", "").strip()

            if i + 1 < len(segments):
                assistant_text = (
                    segments[i + 1].strip().replace("Assistant:", "").strip()
                )
                reformatted_segments.append(
                    f"<s>[INST] {human_text} [/INST] {assistant_text} </s>"
                )
            else:
                reformatted_segments.append(f"<s>[INST] {human_text} [/INST] </s>")

        return {"text": "".join(reformatted_segments)}

    def transform_template_backward(self, dataset):
        conversation_text = dataset["text"]
        reformatted_segments = []

        inst_start = 0
        inst_end = 0

        while True:
            inst_start = conversation_text.find("<s>[INST]", inst_end)
            inst_end = conversation_text.find("</s>", inst_start)

            if inst_start == -1:
                break

            if inst_start == -1 or inst_end == -1:
                raise MissingTagError()

            inst_segment = conversation_text[inst_start + len("<s>[INST]") : inst_end]

            inst_split = inst_segment.split(" [/INST] ")

            if len(inst_split) != 2:
                raise InvalidTagFormatError()

            human_text, assistant_text = inst_split

            if human_text and assistant_text:
                reformatted_segments.append(
                    f"### Human: {human_text.strip()} ### Assistant: {assistant_text.strip()}"
                )
            else:
                raise InvalidSegmentNumberError()

        return {
            "text": " ".join(segment for segment in reformatted_segments if segment)
        }

    def apply_forward_transformation(self):
        return self.dataset.map(self.transform_template_forward)

    def apply_backward_transformation(self):
        return self.dataset.map(self.transform_template_backward)
