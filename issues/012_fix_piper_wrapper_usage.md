# Issue: Fix PiperWrapper Usage According to Piper Help

## Description
The current implementation of the `PiperWrapper` class executes Piper with incorrect attributes and command structure. The usage help for Piper indicates a different set of options and parameters that need to be followed.

### Piper Usage Help
```
usage: piper [options]

options:
   -h        --help              show this message and exit
   -m  FILE  --model       FILE  path to onnx model file
   -c  FILE  --config      FILE  path to model config file (default: model path + .json)
   -f  FILE  --output_file FILE  path to output WAV file ('-' for stdout)
   -d  DIR   --output_dir  DIR   path to output directory (default: cwd)
   --output_raw                  output raw audio to stdout as it becomes available
   -s  NUM   --speaker     NUM   id of speaker (default: 0)
   --noise_scale           NUM   generator noise (default: 0.667)
   --length_scale          NUM   phoneme length (default: 1.0)
   --noise_w               NUM   phoneme width noise (default: 0.8)
   --sentence_silence      NUM   seconds of silence after each sentence (default: 0.2)
   --espeak_data           DIR   path to espeak-ng data directory
   --tashkeel_model        FILE  path to libtashkeel onnx model (arabic)
   --json-input                  stdin input is lines of JSON instead of plain text
   --debug                       print DEBUG messages to the console
   -q       --quiet              disable logging
```

## Proposed Solution
1. **Learn Piper Usage**:
   - Study the Piper usage help to understand the correct options and parameters.

2. **Update PiperWrapper**:
   - Modify the `PiperWrapper` class to use the correct command structure and attributes.
   - Ensure compatibility with the options provided in the Piper usage help.

3. **Testing**:
   - Test the updated `PiperWrapper` implementation with various options and configurations.
   - Verify that the Piper subprocess executes correctly and produces the expected output.

## Acceptance Criteria
- The `PiperWrapper` class should execute Piper with the correct command structure and attributes.
- The implementation should be compatible with the options provided in the Piper usage help.
- The updated implementation should be thoroughly tested.

## Tasks
- Study the Piper usage help.
- Update the `PiperWrapper` class to use the correct command structure and attributes.
- Test the updated implementation.
- Update documentation to reflect the changes.

## References
- File: `backend/piper_wrapper.py`
- Current behavior: Executes Piper with incorrect attributes.
- Proposed behavior: Execute Piper with correct attributes according to the usage help.
