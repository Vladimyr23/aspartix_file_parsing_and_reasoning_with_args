
import sys
from aspartix_parser import Apx_parser
import itertools


def conflict_free(arguments, attacks):
    confl_free_sets = []
    combs = []

    for i in range(1, len(arguments) + 1):
        els = [list(x) for x in itertools.combinations(arguments, i)]
        combs.extend(els)
    combs_sorted = [list(combs_sorted) for combs_sorted in combs][::-1]
    # print("Combs: ", combs_sorted)
    for i in combs_sorted:
        att_count = 0
        # print(i)
        for att in attacks:
            # print(att)
            if set([str(att)[2], str(att)[4]]).issubset(set(i)) or any([i in item for item in
                                                                        confl_free_sets]):  # any(x in item for item in confl_free_sets for x in i):#(True if list(filter(lambda x:i in x,confl_free_sets)) else False):#(any([set(i).issubset(set(item)) in item for item in confl_free_sets])):
                break
            else:
                att_count += 1
            #    print(att_count)
            # if ((str(att)[2] and str(att)[4]) not in i) and (not any([i in item for item in confl_free_sets])):
            #     att_count += 1
            #     print(att_count)
            if att_count == len(attacks):
                confl_free_sets.append(i)
    return confl_free_sets


def admissible(confl_free, attacks):
    admissible_sets = []

    for ext in confl_free:
        count = 0
        # print(ext)
        for att in attacks:
            if str(att)[4] not in ext:
                count += 1
                # print(att, count)
            else:
                # print(att, count)
                for atr in attacks:
                    # print(att, atr, count, str(atr)[4], str(att)[2])
                    if (str(att)[2] == str(atr)[4]) and (str(atr)[2] in ext):
                        count += 1
                        # print(count)
        if count == len(attacks):
            admissible_sets.append(ext)

    return admissible_sets


# def complete(admissible_sets, attacks):
#     complete_ext = []
#     for adm in admissible_sets:
#         for att in attacks:
#             if (str(att)[2] in adm) and
#
#     return complete_ext

def preferred(admissible_sets):
    preferred_exts = []

    for adm in admissible_sets:
        count = 0
        # print(adm, count)
        for adm_t in admissible_sets:
            if set(adm).issubset(set(adm_t)) and adm_t != adm:
                pass
            else:
                count += 1
                # print(adm, adm_t, count)
            if count == len(admissible_sets):
                preferred_exts.append(adm)

    return preferred_exts


def stable_extensions(stable_exts):
    pass


if __name__ == '__main__':
    filepath = 'example.apx'
    if sys.argv[1:]:
        filepath = sys.argv[1]

    arguments = []
    attacks = []
    parser = Apx_parser(filepath)
    arguments, attacks = parser.read_file()
    parser.close()
    print(arguments, attacks)
    print("There are ", len(arguments), " arguments and ", len(attacks), " attacks.")
    # print(str(attacks[0])[4])
    confl_free = conflict_free(arguments, attacks)
    print("Conflict free extensions: ", "[]", sorted(confl_free))
    admissible_sets = admissible(confl_free, attacks)
    print("Admissible extensions: ", "[]", sorted(admissible_sets))
    # complete_ext = complete(admissible_sets, attacks)
    preferred_exts = preferred(admissible_sets)
    print("Preferred extensions: ", sorted(preferred_exts))
    stable_exts = stable_extensions(preferred_exts)
    print("Stable extensions: ", stable_exts)
