import re

def split_elements(input_string):
    result = [t[0] for t in re.findall(r'(([A-Z][a-z]*)|e)', input_string)]
    return result

def parse_input(input_string):
    result = {}
    for line in input_string.split('\n'):
        match = re.match(r'([A-Za-z]+) => ((?:[A-Z][a-z]*)+)', line)
        fr = match.group(1)
        to = match.group(2)
        result[fr] = result.get(fr, [])
        result[fr].append(to)
    return result

def generate_possible_steps(start, trans_dict):
    # generate each possible step from here (eg. each possible step for each possible char)
    elems = split_elements(start)
    for i in range(0, len(elems)):
        if elems[i] in trans_dict.keys():
            for j in range(0, len(trans_dict[elems[i]])):
                # Replace this element with each of its results
                a = elems[:i]
                b = trans_dict[elems[i]][j]
                c = elems[i+1:]
                yield ''.join(a + [b] + c)

def get_num_combinations(start, d):
    return len(set(generate_possible_steps(start, d)))

def get_path_to_molecule(path_so_far, target, trans_dict):
    if path_so_far[-1] == target:
        return path_so_far
    else:
        branches = reversed(list(generate_possible_steps(path_so_far[-1], trans_dict)))
        for branch in branches:
            result = get_path_to_molecule(path_so_far + [branch], target, trans_dict)
            if result:
                return result
        
            
    

INPUT_MOLECULE = "CRnCaCaCaSiRnBPTiMgArSiRnSiRnMgArSiRnCaFArTiTiBSiThFYCaFArCaCaSiThCaPBSiThSiThCaCaPTiRnPBSiThRnFArArCaCaSiThCaSiThSiRnMgArCaPTiBPRnFArSiThCaSiRnFArBCaSiRnCaPRnFArPMgYCaFArCaPTiTiTiBPBSiThCaPTiBPBSiRnFArBPBSiRnCaFArBPRnSiRnFArRnSiRnBFArCaFArCaCaCaSiThSiThCaCaPBPTiTiRnFArCaPTiBSiAlArPBCaCaCaCaCaSiRnMgArCaSiThFArThCaSiThCaSiRnCaFYCaSiRnFYFArFArCaSiRnFYFArCaSiRnBPMgArSiThPRnFArCaSiRnFArTiRnSiRnFYFArCaSiRnBFArCaSiRnTiMgArSiThCaSiThCaFArPRnFArSiRnFArTiTiTiTiBCaCaSiRnCaCaFYFArSiThCaPTiBPTiBCaSiThSiRnMgArCaF"

INPUT_TRANSFORMATION_STRING = """Al => ThF
Al => ThRnFAr
B => BCa
B => TiB
B => TiRnFAr
Ca => CaCa
Ca => PB
Ca => PRnFAr
Ca => SiRnFYFAr
Ca => SiRnMgAr
Ca => SiTh
F => CaF
F => PMg
F => SiAl
H => CRnAlAr
H => CRnFYFYFAr
H => CRnFYMgAr
H => CRnMgYFAr
H => HCa
H => NRnFYFAr
H => NRnMgAr
H => NTh
H => OB
H => ORnFAr
Mg => BF
Mg => TiMg
N => CRnFAr
N => HSi
O => CRnFYFAr
O => CRnMgAr
O => HP
O => NRnFAr
O => OTi
P => CaP
P => PTi
P => SiRnFAr
Si => CaSi
Th => ThCa
Ti => BP
Ti => TiTi
e => HF
e => NAl
e => OMg"""