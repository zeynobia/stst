mkdir -p model
mkdir -p results
python3 preprocess.py input/source.txt input/source.txt.pre
python3 preprocess.py input/target.txt input/target.txt.pre
python3 preprocess.py input/source_test.txt input/source_test.txt.pre
python3 preprocess.py input/target_test.txt input/target_test.txt.pre
python3 train.py input/source.txt.pre input/target.txt.pre
python3 test.py input/source_test.txt.pre results/paraphrase.txt.pre model/tm
python3 eval.py input/target_test.txt.pre results/paraphrase.txt.pre
