# Human & Assistant

Human & Assistant is a simple library designed to make transformations on conversational datasets for fine-tuning chat templates, compatibility with 🤗 Datasets. Apply forward transformation to reformat the conversations to the instructions tuning format from the OpenAssistant Dataset format, or a backward transformation to revert the conversation to its original format.

## Installation

Clone this repository and install the required dependencies:

```bash
git clone https://github.com/neursim/human-assistant.git
cd human-assistant
pip install -e .
```

## Usage

### Initialization

To initialize the Human & Assistant, you'll need to pass the dataset name:

```python
from human_assistant import templates.human_assistant

# Initialize the HumanAssistantTransformer with a HuggingFace dataset name
transformer = HumanAssistantTransformer(dataset_name="timdettmers/openassistant-guanaco")
```

Optional Parameters:

- `seed`: Seed for shuffling the dataset.
- `range_size`: A range to select a portion of the dataset.

Example:

```python
transformer = HumanAssistantTransformer(dataset_name="timdettmers/openassistant-guanaco", seed=42, range_size=100)
```

### Forward Transformation

After initializing a dataset, to apply a forward transformation:

```python
transformed_dataset = transformer.apply_forward_transformation()
```

#### Output Format After Forward Transformation

After applying the forward transformation, the dataset will be transformed into a string with specially formatted tags. 

For example, the conversation text `"### Human: How are you? ### Assistant: I'm good, thank you."` will be converted into:

`<s>[INST] How are you? [/INST] I'm good, thank you. </s>` for each data.

### Backward Transformation

After initializing a dataset, to apply a backward transformation:

```python
transformed_dataset = transformer.apply_backward_transformation()
```

#### Output Format After Backward Transformation

The backward transformation will revert the dataset back to its original format:

For example, the instruction text `<s>[INST] How are you? [/INST] I'm good, thank you. </s>` will be converted into:

`"### Human: How are you? ### Assistant: I'm good, thank you."` for each data.

### Limitations

- Dataset should have a single feature named "text".
- Dataset should contain conversational data, where each entry is a string of one or more segments.
- Segment consists of dialogue turns for a human and an assistant, separated by ###.
- Each human turn starts with `### Human: {human_text} ### Assistant: {assistant_text}`
- Each instruction format should be: `<s>[INST] {human_text} [/INST] {assistant_text} </s>`
