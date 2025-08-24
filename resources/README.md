# Model Resources Directory

Place your trained model files here:

## Required Files:
- `model.json` - Keras model architecture (JSON format)
- `weights.h5` - Model weights (HDF5 format) 
- `tokenizer.pickle` - Trained tokenizer (Pickle format)

## File Descriptions:

### model.json
Contains the neural network architecture definition exported from Keras.

### weights.h5  
Contains the trained model weights in HDF5 format.

### tokenizer.pickle
Contains the fitted tokenizer that was used during training. This is crucial for preprocessing new text inputs.

## Model Compatibility:
- Supports TensorFlow/Keras models
- Compatible with both TF 1.x and 2.x formats
- Fallback to dummy model if files are missing (for demo purposes)

## Adding Your Model:
1. Export your trained Keras model:
   ```python
   # Save architecture
   model_json = model.to_json()
   with open("model.json", "w") as json_file:
       json_file.write(model_json)

   # Save weights
   model.save_weights("weights.h5")

   # Save tokenizer
   import pickle
   with open('tokenizer.pickle', 'wb') as handle:
       pickle.dump(tokenizer, handle, protocol=pickle.HIGHEST_PROTOCOL)
   ```

2. Place all three files in this directory
3. The application will automatically detect and load them

## Security Note:
These files are ignored by git (.gitignore) due to their size. 
For deployment, consider using:
- Git LFS for version control
- Cloud storage (S3, GCS, Azure Blob) for production
- Model registry services for MLOps
