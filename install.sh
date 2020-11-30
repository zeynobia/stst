git clone https://github.com/clab/fast_align
mkdir -p fast_align/build
cd fast_align/build
cmake ..
make
cd ../../
git clone https://github.com/kpu/kenlm
mkdir -p kenlm/build
cd kenlm/build
cmake ..
make -j 4
pip3 install pyter3
pip3 install rouge
pip3 install kenlm

