import tensorflow as tf

def save_model(model, model_path):
    """
    Save the trained model to a specified path.

    Args:
        model (tf.keras.Model): The trained model.
        model_path (str): Path where the model should be saved.
    """
    model.save(model_path)
    print(f"Model saved to {model_path}")

def load_model(model_path):
    """
    Load a trained model from a specified path.

    Args:
        model_path (str): Path to the model file.
        
    Returns:
        model (tf.keras.Model): The loaded model.
    """
    model = tf.keras.models.load_model(model_path)
    print(f"Model loaded from {model_path}")
    return model
