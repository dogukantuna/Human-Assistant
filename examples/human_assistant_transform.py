from src.templates import HumanAssistantTransformer

def main():
    # Forward Transformation Example
    try:
        forward_transformer = HumanAssistantTransformer(
            dataset_name="timdettmers/openassistant-guanaco"
        )
        transformed_forward_dataset = forward_transformer.apply_forward_transformation()
        
        print("Forward Transformed Dataset:")
        print(transformed_forward_dataset)

    except ValueError as e:
        print(f"Forward Transformation Error: {e}")

    # Backward Transformation Example
    try:
        backward_transformer = HumanAssistantTransformer(
            dataset_name="mlabonne/guanaco-llama2-1k"
        )
        transformed_backward_dataset = backward_transformer.apply_backward_transformation()
        
        print("Backward Transformed Dataset:")
        print(transformed_backward_dataset)

    except ValueError as e:
        print(f"Backward Transformation Error: {e}")

if __name__ == "__main__":
    main()
